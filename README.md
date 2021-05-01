# Visara

# All links needed
- [Colab file for blindness in 70 months prediction](https://colab.research.google.com/drive/1ZYCiKwTzFD6Jwu2VyxBS42mLqRS1x0Mb?usp=sharing)
- [Colab file for Diabetic retinopathy prediction](https://colab.research.google.com/drive/1Lo_kXwBiREveQ-P584Vp4HUyXm8vBmz4?usp=sharing)
- [Blindness Deployed Code(NGROK)](https://colab.research.google.com/drive/1gNqGtGATPIklXvfptHzz2-4sDzFU-k66?usp=sharing)
- [Diabetic-Retinopathy-Prediction(NGROK)](https://colab.research.google.com/drive/19jGOLhsaLr_ERiFcE1siSdyaGQpHxg4A?usp=sharing)
- [Link to website](https://visara.herokuapp.com/)

# Inspiration ✨

Diabetes is a devastating health condition. Over 84% of patients are unaware that they have diabetes, and this is huge because there lacks an objective assessment tool for automated detection. Diabetic Retinopathy is an eye condition that can cause vision loss and blindness in people who have diabetes. Diabetic Retinopathy must be diagnosed both quickly and accurately; however, the inconsistency between clinicians exacerbates the current poor treatment of DR. Currently, detecting DR is a very time-consuming task, which requires a trained clinician to evaluate the retina. In addition to this, diagnosing patients can be extremely inconsistent amongst ophthalmologists and our severity predictor ensures an objective and quick assessment of DR. To counter the detrimental effects of diabetic retinopathy and lack of consistency from clinician diagnosis, we present to you, the Visara.

Visara is a web-app that utilizes a variety of state-of-the-art models to revolutionize the ophthalmologic field. Owing to the current pandemic, travelling to gyms/yoga centers is neither safe nor feasible which brings our project to show. The web-app would not only predict the DR and the extent of blindness but would also suggest the Yoga postures which are proven to be beneficial in the cure of Diabetic Retinopathy using a Yoga Bot which detects the posture of the user while performing the Asana. Studies have shown that concise organization of reports leads to better efficiency of treatment. Additionally, doctors can often miss key information from their patient if a medical text report is disorganized so this summarizer ensures that no information is lost in the process of communicating with a doctor. Therefore based on the diagnosis results a report is generated which can be accessed both by the doctor and the patient for the evaluation.

# What it does 🤖
Our Visara aims to bring a solution which can help people take necessary preventive measures against one of the most common problems faced by a diabetic person which is vision loss. The fundamental objective of the project is to allow patients and doctors to efficiently utilize resources and funds. The most attractive quality of this project is to try to automate almost everything from the detection of Diabetic Retinopathy (DR) severity prediction and blindness time prediction to creating a report summarizer and handing over the details to our YogaBot.

For new users, our YogaBot asks them a few generic questions regarding their medical history and recommends Yoga asanas to boost their health and immunity. For registered users, we keep a record of their previous asanas and their improvement to suggest some new routines. Our bot then acts as a personal trainer, records the body structure and notifies if the body is upheld correctly. 

# Key features 💡

Our YogaBot is a recommendation feature which analyzes the user’s health to recommend and teach Asanas to boost their health structure. It acts as a personal trainer checking the posture of the user while performing the Asanas.

Diabetic Retinopathy (DR) severity prediction, blindness time prediction, and a report summarizer are DR’s three main features. Each of these features are displayed in the form of records, where doctors can add various types of records by selecting one of the 3 features. Once they fill out the necessary information required for each record, they can retrieve an output within seconds. All records can be conveniently displayed on a single page. Additionally, our app would implement a login/logout authentication system, which enables a user to easily and securely access their data.

1. For the DR severity prediction aspect of our web app, we will predict the stage of DR based on an image of the patient’s retina image. Our model classify the retina on a scale of 0-4, with 0 being no DR and 4 being the most severe.

2. The next section in our web app predicts the chance of a patient going blind from DR over a course of 70 months. A doctor can enter demographic and treatment information about the specific patient. Using a ML Model, we intend to create a graph with the percent chance of going blind over a course of months. This is helpful for the doctor and the patient as they can easily decide how soon they need treatment, and if they need treatment, without getting their retina scanned. 

3. Lastly, we have a report summarizer for the doctor to easily view a summary of the patient’s condition write up. Similarly, patients can also view their doctor’s report in a more concise and organized format. 

# Novelty 💎
 Over 84% of patients are unaware they have diabetes, and this is large because there lacks an objective assessment tool for automated detection. Currently, detecting DR is a very time-consuming task, which requires a trained clinician to evaluate the retina. In addition to this, diagnosing patients can be extremely inconsistent amongst ophthalmologists, and our severity predictor ensures an objective and quick assessment of DR. Moreover, we cater a personalized set of yoga asanas for each individual along with a personal posture trainer which comes without the risks of Covid transmission.

# Tech Stack 📚

- HTML, CSS, JavaScript
- Python
- Tensorflow
- Flask
- OpenCV
- Natural Language Processing
- CNN

# Future scope 📈

- Connect the patient with the doctor using a messaging feature. 
- Diet Planner according to the patient stats. 
- Keeping a track of patient exercise and diet history stats using IOT devices.  
