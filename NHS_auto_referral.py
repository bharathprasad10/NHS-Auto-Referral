import streamlit as st
import pickle
from datetime import datetime
import csv
import smtplib


def write_patient_record(filename, patient_record_list):
    with open(filename, 'a', newline="") as patient_record:
        field_names = ['Full name', 'NHS number', 'DOB', 'Scheduled']
        patient_write = csv.DictWriter(patient_record, fieldnames=field_names)
        # patient_write.writeheader()
        patient_write.writerow(patient_record_list)


def quest_filter(sym_1):
    input = st.empty()
    list1 = ["Wrist", "Hand", "Finger", "Back", "Neck", "Foot", "Leg", "Ankle"]
    if (sym_1 in list1):
        sym_2 = st.empty().selectbox("How long have you had your current symptoms?",
                                     ("", "less than 24 hrs", "longer than 24 hrs", "long term or intermittent"))
        sym_3 = st.empty().selectbox("Have you tried any of these medications?", (
        "", "Paracetamol", "Any other aspirins or medications", "Any creams or gels", "not tried"))
        sym_4 = st.empty().selectbox("Have you been diagnosed with any long term medical problems?",
                                     ("", "Yes", "None"))
        sym_5 = st.empty().selectbox("Do you have any change in appearance?", (
        "", "Redness or Swelling or loss of sensation or painfull lump", "Change of shape or loss of movement", "None"))
        sym_6 = st.empty().selectbox("Do you feel any of these difficulties accompanied with the pain?",
                                     ("", "fever lasting more than 5 days", "Lack of energy", "None"))
        sym_7 = st.empty().selectbox("When do you feel difficult in affected area??",
                                     ("", "Doing regular activities", "Unable to move affected area"))
        sym_8 = st.empty().selectbox("Do you have any of these symptoms?",
                                     ("", "intense pain in bluish discolouration", "None"))

    elif (sym_1 == "Head"):
        sym_2 = st.empty().selectbox("How long have you had your current symptoms?",
                                     ("", "less than 24 hrs", "longer than 24 hrs", "long term or intermittent"))
        sym_3 = st.empty().selectbox("Have you tried any of these medications?", (
        "", "Paracetamol", "Any other aspirins or medications", "Any creams or gels", "not tried"))
        sym_4 = st.empty().selectbox("Have you been diagnosed with any long term medical problems?",
                                     ("", "Migrane or cluster or sinus headache", "Yes", "None"))
        sym_5 = st.empty().selectbox("Do you have any change in appearance?", (
        "", "Redness or Swelling or loss of sensation or painfull lump", "Change of shape or loss of movement", "None"))
        sym_6 = st.empty().selectbox("Do you feel any of these difficulties accompanied with the pain?", (
        "", "fever lasting more than 5 days", "Excessive sleepiness or change in concious level", "Lack of energy",
        "Jaw pain", "Worsening headache", "None"))
        sym_7 = st.empty().selectbox("When do you feel difficult in affected area??",
                                     ("", "Doing regular activities", "Unable to move affected area", "nil"))
        sym_8 = st.empty().selectbox("Do you have any of these symptoms?", (
        "", "Squint or eyes affected", "Dizzy or associated with ataxia or unsteadiness",
        "intense pain in bluish discolouration", "persistent vomiting", "stress", "anxiety or depression", "None"))
    else:
        st.write("Please select any option")
        sym_2, sym_3, sym_4, sym_5, sym_6, sym_7, sym_8 = "", "", "", "", "", "", ""
    combined_string_2 = sym_2 + " " + sym_3 + " " + sym_4 + " " + sym_5 + " " + sym_6 + " " + sym_7 + " " + sym_8

    if sym_2 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_3 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_4 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_5 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_6 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_7 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")
    elif sym_8 == "":
        try:
            raise ValueError('Fill the options')
        except ValueError:
            st.error("Fill the options")

    combined_string = sym_1 + " " + sym_2 + " " + sym_3 + " " + sym_4 + " " + sym_5 + " " + sym_6 + " " + sym_7 + " " + sym_8
    return combined_string


def email_sending(patient_email, string1, patient_name):
    if string1 == 'gp':
        gp_service = "General Practitioner"
    else:
        gp_service = string1
    email_to = patient_email
    subject = "You have been given an appoinment to the GP services"
    Text = "Hi {},\n\nYou have been appointed to the {}\n\nThank you,\nGP appoinments".format(patient_name, gp_service)
    message = 'Subject: {}\n\n{}'.format(subject, Text)


    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("nhs.gp.appoinments@gmail.com", "vmteojvhtccqeguw")
    server.sendmail("nhs.gp.appoinments@gmail.com",
                    email_to,
                    message)
    server.quit()


def main():
    st.title("Primary Health Center")
    st.write("""
    ## Welcome to GP appointments
    Please answer the below questions
    """)
    patient_name = st.text_input("Full name")
    print(patient_name)
    nhs_no = st.text_input("NHS number")
    print(nhs_no)
    dob_str = st.text_input("Enter your date of birth(DD/MM/YYYY)")
    print(dob_str)
    global dob
    if not dob_str == "":
        try:
            dob = datetime.strptime(dob_str, '%d/%m/%Y').date()
        except ValueError:
            st.error('Please enter in the valid format')

    patient_email = st.text_input("Enter your email address")
    print(patient_email)
    a_n_e = st.selectbox("Are you currently experiencing any of the following?",
                         ("None","Pain like a very tight band","Heavy weight or squeezing in the centre of your chest",
                          "Any pain that moves into your jaw or neck","Face drooping on one side","Cannot hold both arms up",
                          "Difficulty speaking","Numbness or weakness on one side of the body","Gasping or not being able to get words out",
                          "Choking or lips turning blue","Uncontrollable bleeding from any part of your body"))

    input = st.empty()
    sym_1 = input.selectbox("Which part of your body causing a problem or pain?",
                            ("", "Wrist", "Hand", "Finger", "Back", "Neck", "Foot", "Leg", "Ankle", "Head"))

    combined_string = quest_filter(sym_1)


    button = st.button("Submit")
    print(button)

    if (button == True):
        if(a_n_e == "None"):
            # combined_string = sym_1 + " " + sym_2 + " " + sym_3 + " " + sym_4  + " " + sym_5 + " " + sym_6 + " " + sym_7 + " " + sym_8
            print(combined_string)
            st.write("Your response is submitted for review. Please wait a few minutes to know more about the appoinment")

            with open('support_vector_model_pkl', 'rb') as f:
                lr = pickle.load(f)
            selected_department = lr.predict([combined_string])
            string1 = str(selected_department)
            disallowed_characters = "[]'"
            for character in disallowed_characters:
                string1 = string1.replace(character, "")
            print(string1)
            if string1 == 'gp':
                gp_service = "General Practitioner"
            else:
                gp_service = string1
            st.write(" You have been scheduled to the " + gp_service)
            patient_dict = {'Full name': patient_name,
                            'NHS number': nhs_no,
                            'DOB': dob,
                            'Scheduled': string1}
            print(patient_dict)
            write_patient_record('patient_record2.csv', patient_dict)
            email_sending(patient_email, string1, patient_name)

        else:
            st.write("You are showing signs of an Emergency. Please call 999 immediately")


if __name__ == '__main__':
    main()