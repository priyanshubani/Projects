from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_mail = [request.form['text']]

    raw_mail_data = pd.read_csv('mail_data.csv')
    mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

    mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
    mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

    X = mail_data['Message']
    Y = mail_data['Category']

    feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    X_features = feature_extraction.fit_transform(X)

    Y = Y.astype('int')

    model = LogisticRegression()
    model.fit(X_features, Y)

    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)

    if prediction[0] == 1:
        result = 'Ham mail'
    else:
        result = 'Spam mail'

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
