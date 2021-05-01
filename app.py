from flask import Flask,request, url_for, redirect, render_template
import pyrebase
app = Flask(__name__)


firebaseConfig = {
    'apiKey': "AIzaSyDubGncgvqCMzWktTMOChPntjfgMITmTcc",
    'authDomain': "visara-5a513.firebaseapp.com",
    'projectId': "visara-5a513",
    'storageBucket': "visara-5a513.appspot.com",
    'messagingSenderId': "582687989459",
    'appId': "1:582687989459:web:7e005b599c09faa8a93e26",
    'measurementId': "G-0NY6VG8PBT",
    "databaseURL" : "https://visara-5a513-default-rtdb.asia-southeast1.firebasedatabase.app/"
    }
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login/patient',methods=['POST','GET'])
def login_patient():
    int_features=[x for x in request.form.values()]
    print(int_features)
    email=int_features[0]
    password=int_features[1]
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Patient Succesfully SignedIn")
    except:
        print("Invalid User Or Password")
    return render_template('login.html')

@app.route('/login/doctor',methods=['POST','GET'])
def login_doctor():
    int_features=[x for x in request.form.values()]
    print(int_features)
    email=int_features[0]
    password=int_features[1]
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Doctor Succesfully SignedIn") 
    except:
        print("Invalid User Or Password")
    return render_template('login.html')

@app.route('/signup/doctor',methods=['POST','GET'])
def signup_doctor():
    int_features=[x for x in request.form.values()]
    print(int_features)
    email=int_features[0]
    password=int_features[1]
    confirmpasswd=int_features[2]
    try:
        auth.create_user_with_email_and_password(email,password)
        print("Doctor Created")
    except:
        print("Email already Exists")
    return render_template('signup.html')

@app.route('/signup/patient',methods=['POST','GET'])
def signup_patient():
    int_features=[x for x in request.form.values()]
    print(int_features)
    email=int_features[0]
    password=int_features[1]
    try:
        auth.create_user_with_email_and_password(email,password)
        print("Patient Created")
    except:
        print("Email already Exists")
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


