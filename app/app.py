import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Get the current working directory
current_dir = os.getcwd()

# Load the model
model_path = os.path.join(current_dir, 'best_campus_placement_predictor.joblib')
rf = joblib.load(model_path)

def predict_placement(features):
    prediction = rf.predict([features])
    probability = rf.predict_proba([features])
    return prediction[0], probability[0]

def main():
    st.title("Campus Placement Predictor")

    st.write("""
    This app predicts the likelihood of campus placement based on various factors.
    Please fill in the following information:
    """)

    # Input fields
    mba_p = st.slider("MBA Percentage", 0.0, 100.0, 50.0)
    degree_p = st.slider("Degree Percentage", 0.0, 100.0, 50.0)
    workex = st.selectbox("Work Experience", ["No", "Yes"])
    hsc_s = st.selectbox("Higher Secondary Specialization", ["Commerce", "Science", "Arts"])
    degree_t = st.selectbox("Degree Type", ["Comm&Mgmt", "Sci&Tech", "Others"])
    hsc_p = st.slider("Higher Secondary Percentage", 0.0, 100.0, 50.0)
    ssc_p = st.slider("Secondary School Percentage", 0.0, 100.0, 50.0)
    gender = st.selectbox("Gender", ["Male", "Female"])

    # Mapping categorical variables
    workex_map = {"No": 0, "Yes": 1}
    hsc_s_map = {"Commerce": 1, "Science": 2, "Arts": 0}
    degree_t_map = {"Comm&Mgmt": 0, "Sci&Tech": 2, "Others": 1}
    gender_map = {"Male": 1, "Female": 0}

    if st.button("Predict"):
        features = [
            mba_p,
            degree_p,
            workex_map[workex],
            hsc_s_map[hsc_s],
            degree_t_map[degree_t],
            hsc_p,
            ssc_p,
            gender_map[gender]
        ]

        prediction, probability = predict_placement(features)

        if prediction == 1:
            st.success(f"Congratulations! You are likely to be placed. Probability: {probability[1]:.2%}")
        else:
            st.error(f"You might need to work harder. Probability of not being placed: {probability[0]:.2%}")

    if st.button("Show Placement Tips"):
        st.markdown("""
        ## Tips to Improve Your Chances of Placement

        1. **Improve Your Academic Performance**: Focus on maintaining high grades, especially in your MBA and degree courses.
        2. **Gain Work Experience**: Try to get internships or part-time jobs related to your field.
        3. **Develop Technical Skills**: Enhance your skills in areas relevant to your degree and desired job.
        4. **Participate in Extracurricular Activities**: This shows leadership and teamwork skills.
        5. **Prepare for Aptitude Tests**: Many companies use these as part of their recruitment process.
        6. **Enhance Your Communication Skills**: Work on both verbal and written communication.
        7. **Build a Strong Resume**: Highlight your achievements, skills, and experiences.
        8. **Network**: Attend job fairs, seminars, and industry events.
        9. **Practice Mock Interviews**: This will help you feel more confident during actual interviews.
        10. **Stay Updated with Industry Trends**: Keep yourself informed about the latest developments in your field.
        """)

if __name__ == '__main__':
    main()