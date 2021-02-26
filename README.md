# Tweet-Analyzer

The main objective of the project is prediction of user’s tweets so, the project is based on a multi label text classification model for prediction. In this project, I will classify tweets for ten categories which are art, game, movie, music, politic, science, sport, technology, travel, and tv. I scraped data for these categories and trained a machine learning model for these categories. Also, the project has many phases to getting prediction.   

**Requirements:**
-	Pandas
-	NumPy
-	Scikit-learn
-	Pickle
-	Joblib
-	Regex
-	Tweet-preprocessor
-	Tweepy
-	Nltk
-	Flask

### 1.Scraping Data for a Machine Learning Model from Tweeter

Scraping data may be a most important part for every data science project. If we scrape wrong data from source, the project will become unusable. Also, time is important for effectiveness. Traditional scraping tools like selenium, scrappy can be very slow for big amount data. In this point, application programming interfaces (api) can be solution for velocity but they have some disadvantages for example in our case, twitter api allows me to get one hundred fifty data for every fifteen minutes.
See [this](https://github.com/hasretdoguer/Tweet-Analyzer/tree/main/Scraping%20Tweets)

### 2.Preprocessing of scraped data
First, I need to combine all csv files in one csv file for starting preprocessing phase. Then I need to decide what things are deleted or not from tweets for example emoticons are deleted or not. I decided to keep hashtags words without “#“ tags and decided to delete links and emoticons with using tweet-preprocessor and delete punctuations too.
See [this](https://github.com/hasretdoguer/Tweet-Analyzer/tree/main/Preprocessing)

#### 2.1 Normalization
In order to carry out processing on natural language text, we need to perform normalization that mainly involves eliminating punctuation, converting the entire text into lowercase or uppercase, converting numbers into words, expanding abbreviations, canonicalization of text, and so on. In this phase, word tokenization and stop words are important. According to Stanford, tokenization is that “a token is an instance of a sequence of characters in some particular document that are grouped together as a useful semantic unit for processing.”. Next, stop words are words of a language that do not have any particular meaning. I alsodelete some words like “happy”, “new”, “year” because of the new year celebrations.

####   2.2 Stemming and Lemmatization
Stemming and lemmatization are both techniques to normalize tokens. In English and most languages a single word can have multiple forms depending on the context it is used. For example, the verb “to swear” can be take the form “swears”, “swore”, “sworn”. When we tokenize a text each of these forms are considered different but as the language user, we know that all the forms refer to only one concept or idea. 

####    2.3 TF-IDF
TF-IDF is a statistical measure that evaluates how relevant a word is to a document in a collection of documents. This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents. Also, this is an important phase to train our model. After convert data with TF-IDF, data can ready to train our model.

### 3. Multi-Label Classification
I trained my model three different multi-label classification model algorithms that are logistic regression, multinomial naïve bayes, and linear support vector. Linear support vector has the best accuracy, but I did not use somehow on AWS EC2 server. So, I decided to use multinomial naïve bayes for prediction
 
######This is the opening screen of the website. Here, users should type an English based account name. Then they should click the submit button for analysis.
![This is the opening screen of the website. Here, users should type an English based account name. Then they should click the submit button for analysis.](https://github.com/hasretdoguer/Tweet-Analyzer/tree/main/Tweet%20Analyzer/templates/index.png?raw=true)
