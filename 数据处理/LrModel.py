from sklearn.model_selection import train_test_split
import pandas as pd
import sklearn
import re
from string import punctuation
import preprocessor as p
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


def getLrModel():
    df = pd.read_csv('train.csv')
    df.head()

    for i in range(0, len(df)):
        df.loc[:, 'tweet'][i] = p.clean(df.loc[:, 'tweet'][i])
        df.loc[:, 'tweet'][i] = ''.join(
            [c for c in df.loc[:, 'tweet'][i] if c not in punctuation])
        df.loc[:, 'tweet'][i] = df.loc[:, 'tweet'][i].lower()

    X_train, X_test, y_train, y_test = train_test_split(
        df.loc[:, 'tweet'], df.loc[:, 'label'], test_size=0.3, shuffle=False)

    vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    joblib.dump(lr, 'saved_model/lr.pkl')
    joblib.dump(vectorizer, 'saved_model/vec.pkl')
    return [vectorizer, lr]


def preprocess(fileName):
    nyc = pd.read_csv(fileName, encoding='ISO-8859-1')
    for i in range(0, len(nyc)):
        nyc.loc[:, 'tweet'][i] = p.clean(nyc.loc[:, 'tweet'][i])
        nyc.loc[:, 'tweet'][i] = ''.join(
            [c for c in nyc.loc[:, 'tweet'][i] if c not in punctuation])
        nyc.loc[:, 'tweet'][i] = nyc.loc[:, 'tweet'][i].lower()
    return nyc


def predict(dataFrame, vec, lrModel):
    nyc = dataFrame
    tweet = vec.transform(nyc.loc[:, 'tweet'])
    predict = lrModel.predict(tweet)
    cnt0 = 0  # negative
    cnt1 = 0  # positive
    for i in range(0, len(nyc)):
        if(predict[i] == 0):
            cnt0 += 1
        else:
            cnt1 += 1
    print("this week ", len(nyc), "tweets collected in TimeSquare")
    sad_rate = cnt0/(len(nyc)+1)
    print("Sad rate is", sad_rate)
    return [predict, cnt0, sad_rate]


def allInOne(fileName):
    nyc = preprocess(fileName)
    lrModel = joblib.load('saved_model/lr.pkl')
    vec = joblib.load('saved_model/vec.pkl')
    result = predict(nyc, vec, lrModel)

    return result


# test = preprocess("sadData.csv")
# test.head()
allInOne("数据集/TimeSquareWeek21.csv")
# print(sad)
# allInOne("test.csv")
