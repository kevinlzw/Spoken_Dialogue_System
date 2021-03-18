import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
import pickle

if __name__ == '__main__':
    posts = nltk.corpus.nps_chat.xml_posts()

    posts_text = [post.text for post in posts]

    # divide train and test in 80 20
    train_text = posts_text[:int(len(posts_text) * 0.8)]
    test_text = posts_text[int(len(posts_text) * 0.2):]

    # Get TFIDF features
    vectorizer = TfidfVectorizer(ngram_range=(1, 3),
                                 min_df=0.001,
                                 max_df=0.7,
                                 analyzer='word')

    X_train = vectorizer.fit_transform(train_text)
    X_test = vectorizer.transform(test_text)

    y = [post.get('class') for post in posts]

    y_train = y[:int(len(posts_text) * 0.8)]
    y_test = y[int(len(posts_text) * 0.2):]

    gb = GradientBoostingClassifier(n_estimators=400, random_state=0)

    gb.fit(X_train, y_train)

    with open('vectorizer.pk', 'wb') as fin:
        pickle.dump(vectorizer, fin)

    with open('question_detection.sav', 'wb') as file:
        pickle.dump(gb, file)



    # predictions_rf = gb.predict(X_test)

    # print(classification_report(y_test, predictions_rf))