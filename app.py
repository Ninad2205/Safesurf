# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# app = Flask(__name__)

# # Feature extraction functions for URLs and emails
# def extract_url_features(url):
#     features = []
#     features.append(len(url))  # Length of URL
#     features.append(int('https' in url))  # HTTPS present
#     features.append(url.count('.'))  # Number of dots
#     return features

# def extract_email_features(email):
#     features = []
#     features.append(len(email))  # Length of Email
#     features.append(email.count('@'))  # Should be 1 for valid emails
#     features.append(email.count('.'))  # Number of dots in the email
#     features.append(int(any(keyword in email.lower() for keyword in ['bank', 'login', 'secure', 'verify'])))  # Suspicious keywords
#     return features

# # Load dataset and train the model
# def train_model():
#     # Load URL dataset
#     url_data = pd.read_csv('phishing_dataset.csv')  # Change to your URL dataset
#     X_url = url_data['URL'].apply(extract_url_features).tolist()
#     X_url = pd.DataFrame(X_url)
#     y_url = url_data['Label']
    
#     X_train_url, X_test_url, y_train_url, y_test_url = train_test_split(X_url, y_url, test_size=0.3, random_state=42)
    
#     url_model = RandomForestClassifier()
#     url_model.fit(X_train_url, y_train_url)
    
#     # Save the trained URL model to a file
#     with open('url_phishing_model.pkl', 'wb') as file:
#         pickle.dump(url_model, file)
    
#     # Load Email dataset
#     email_data = pd.read_csv('large_phishing_email_dataset.csv')  # Change to your email dataset
#     X_email = email_data['Email'].apply(extract_email_features).tolist()
#     X_email = pd.DataFrame(X_email)
#     y_email = email_data['Label']
    
#     X_train_email, X_test_email, y_train_email, y_test_email = train_test_split(X_email, y_email, test_size=0.3, random_state=42)
    
#     email_model = RandomForestClassifier()
#     email_model.fit(X_train_email, y_train_email)
    
#     # Save the trained Email model to a file
#     with open('email_phishing_model.pkl', 'wb') as file:
#         pickle.dump(email_model, file)
    
#     return url_model, email_model

# # Check if models are saved; if not, train new ones
# try:
#     with open('url_phishing_model.pkl', 'rb') as file:
#         url_model = pickle.load(file)
# except FileNotFoundError:
#     url_model, email_model = train_model()

# try:
#     with open('email_phishing_model.pkl', 'rb') as file:
#         email_model = pickle.load(file)
# except FileNotFoundError:
#     if 'url_model' not in locals():  # In case URL model is also not loaded
#         url_model, email_model = train_model()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     input_text = request.form.get('input')
#     input_type = request.form.get('type')  # 'url' or 'email'
    
#     if input_type == 'url':
#         features = extract_url_features(input_text)
#         model = url_model
#     elif input_type == 'email':
#         features = extract_email_features(input_text)
#         model = email_model
#     else:
#         return jsonify(result={"error": "Invalid input type"})
    
#     probability = model.predict_proba([features])[0]  # Get probability estimates
#     secure_percentage = probability[0] * 100
#     phishing_percentage = probability[1] * 100
    
#     result = {
#         "secure": f"{secure_percentage:.2f}%",
#         "phishing": f"{phishing_percentage:.2f}%"
#     }
#     return jsonify(result=result)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Feature extraction functions for URLs
def extract_url_features(url):
    features = []
    features.append(len(url))  # Length of URL
    features.append(int('https' in url))  # HTTPS present
    features.append(url.count('.'))  # Number of dots
    return features

# Load dataset and train the model for URLs
def train_model():
    # Load URL dataset
    url_data = pd.read_csv('phishing_dataset.csv')  # Change to your URL dataset
    X_url = url_data['URL'].apply(extract_url_features).tolist()
    X_url = pd.DataFrame(X_url)
    y_url = url_data['Label']
    
    X_train_url, X_test_url, y_train_url, y_test_url = train_test_split(X_url, y_url, test_size=0.3, random_state=42)
    
    url_model = RandomForestClassifier()
    url_model.fit(X_train_url, y_train_url)
    
    # Save the trained URL model to a file
    with open('url_phishing_model.pkl', 'wb') as file:
        pickle.dump(url_model, file)
    
    return url_model

# Check if the URL model is saved; if not, train a new one
try:
    with open('url_phishing_model.pkl', 'rb') as file:
        url_model = pickle.load(file)
except FileNotFoundError:
    url_model = train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form.get('input')
    input_type = request.form.get('type')  # 'url'
    
    if input_type == 'url':
        features = extract_url_features(input_text)
        model = url_model
    else:
        return jsonify(result={"error": "Invalid input type"})
    
    # Get the probability estimates for phishing vs legitimate
    probability = model.predict_proba([features])[0]
    secure_percentage = probability[0] * 100
    phishing_percentage = probability[1] * 100
    
    result = {
        "secure": f"{secure_percentage:.2f}%",
        "phishing": f"{phishing_percentage:.2f}%"
    }
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
