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

### 1.	Scraping Data for a Machine Learning Model from Tweeter

Scraping data may be a most important part for every data science project. If we scrape wrong data from source, the project will become unusable. Also, time is important for effectiveness. Traditional scraping tools like selenium, scrappy can be very slow for big amount data. In this point, application programming interfaces (api) can be solution for velocity but they have some disadvantages for example in our case, twitter api allows me to get one hundred fifty data for every fifteen minutes.
See [this](https://github.com/hasretdoguer/Tweet-Analyzer/tree/main/Scraping%20Tweets)

### 2.	Preprocessing of scraped data
First, I need to combine all csv files in one csv file for starting preprocessing phase. Then I need to decide what things are deleted or not from tweets for example emoticons are deleted or not. I decided to keep hashtags words without “#“ tags and decided to delete links and emoticons with using tweet-preprocessor and delete punctuations too.
  -Normalization
