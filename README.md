# NHS-Auto-Referral
The scope of this project is an automated system which takes queries from patients and schedule their appointment to the right primary care network under the GP services. The aim is to develop an automated system to support the existing manual review process and potentially automated the whole referral process in the future.

Step 1: Run the support_vector_model.py - The code trains the data using support vector machine algorithm

Step 2: Run the NHS_auto_referral.py
Note: Install streamlit packgage and run streamlit using the code "streamlit run NHS_autoreferral.py" in the terminal to open up a new local host browsing site

## 1. Problem
GP appoinments in the NHS UK is facing a major problem dealing with high volume of patient quieries for scheduling an appoinment with the doctor or other primary care services. Usually the patient interaction is done by admin staffs or receptionists which causes delay in appoinments as it is a manual review process. Due to this reason, patients tend to choose secondary services, which are accident and emergency care. These services are expensive for  the NHS and deal with an already high volume of important emergency cases.

## 2. Solution
Create an automated patient interactive system which automates the process of manual interaction with patients. Artificial intelligence using Natural Language processing is employed to solve the above mentioned problem.

## 3. Data
A dummy data set is created with diseases, symptoms and departments under the GP and primary care networks. Dependent variable is the departments and independent variables are diseases and various symptoms.

## 4. Evaluation 
* Accuracy - The accuracy of different models are taken and compared with eachother. Accuracy is determined by comparing the actual output of the test data set with the predicted value.
* F1 Score - F1 score determines how well each classes perfomed. As the count of "General Practisioner" class is higher compared to other classes, it is important to have the F1 scores of other classes high.
* Recall - Recall value of the class "General Practisioner" should be high as the important patients must be directed to the general practisioner instead of other primary care departments

##Distribution of the target feature

