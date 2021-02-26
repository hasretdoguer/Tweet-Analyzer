import pandas as pd 
from flask import Flask, request, jsonify, render_template
import joblib
import tweepy
import pickle
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


app = Flask(__name__)


def preprocessing(df):
    import pandas as pd
    import regex as re
    import nltk
    import preprocessor as p
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    from nltk.stem.snowball import SnowballStemmer
    from sklearn.feature_extraction.text import TfidfVectorizer
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    df = pd.DataFrame(df, columns=["tweet_text"])
    for i in range(len(df["tweet_text"])):
        df["tweet_text"][i] = re.sub(r'(?is)#', '', (df["tweet_text"][i]))
        df["tweet_text"][i] = p.clean(df["tweet_text"][i])
        df["tweet_text"][i] = re.sub(r'[^\w\s]','',df["tweet_text"][i])
    df.dropna(inplace=True)
    stop_words = set(stopwords.words('english'))
    stop_words.update(('new','year', 'happy', 'first', 'one', 'lets', 'best', 'via', 'two', 'three', 'amp'))
    for i in range(len(df["tweet_text"])):
        word_tokens = word_tokenize(df["tweet_text"][i].lower())
        filtered_sentence = ""
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence += w
                filtered_sentence += " "
    filtered_sentence = filtered_sentence.strip()
    df["tweet_text"][i] = filtered_sentence
    df.dropna(inplace=True)
    for i in range(len(df["tweet_text"])):
        sentence = ""
        tweet = df["tweet_text"][i].lower().split()
        porter = nltk.SnowballStemmer('english')
        WNlemma = WordNetLemmatizer()
        for k in tweet:
            stemming = porter.stem(k)
            lem = WNlemma.lemmatize(stemming)
            sentence += lem
            sentence += " "
        sentence = sentence.strip()
        df["tweet_text"][i] = sentence
    return df


def vectorization(df):
    vectorizer = pickle.load(open("vector.pickel", "rb"))
    x_test = vectorizer.transform(df)
    return x_test


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',  methods=['POST'])
def username():
    user_name = request.form["username"]
    #use your own keys
    consumer_key = "******************"
    consumer_secret = "***********************"
    access_token = "****************************"
    access_token_secret = "*****************************"

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    userID = user_name
    user = api.get_user(userID)

    new_tweets = api.user_timeline(screen_name = userID,count=200, tweet_mode="extended")
    tweets = [[tweet.full_text] for tweet in new_tweets]


    df = preprocessing(tweets)

    for i in range(len(df["tweet_text"])):
        if df["tweet_text"][i] == '':
            df.drop([i], inplace=True)
    df = df.reset_index(drop=True)
    

    models = []
    with open("models2.pckl", "rb") as f:
        while True:
            try:
                models.append(pickle.load(f))
            except EOFError:
                break
    

    categories = ['art', 'game', 'movie', 'music', 'politic', 'science', 'sport', 'technology', 'travel', 'TV']
    total = []
    for i in range(len(df["tweet_text"])):
        test = [df["tweet_text"][i]]
        test = vectorization(test)
        result = []
        final = []
        for model in models:
            result.append(model.predict_proba(test))
        for k in range(len(result)):
            final.append(result[k][0][1])
        index = final.index(max(final))
        total.append(categories[index])

    data = {}
    data.setdefault("result_name", [])
    data.setdefault("result_percentage", [])

    for category in categories:
        percentage = int(total.count(category) * 100 / len(total))
        data["result_name"].append(category)
        data["result_percentage"].append(percentage)
        
    return render_template("analyzer.html", userName = user_name, 
    art = data["result_percentage"][0], game = data["result_percentage"][1],
    movie = data["result_percentage"][2], music = data["result_percentage"][3],
    politic = data["result_percentage"][4], science = data["result_percentage"][5],
    sport = data["result_percentage"][6], technology = data["result_percentage"][7],
    travel = data["result_percentage"][8], tv = data["result_percentage"][9])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader = False)


