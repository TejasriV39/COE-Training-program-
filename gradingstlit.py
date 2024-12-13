import streamlit as st

st.title("Student Grading")

project_score = st.number_input("Enter the Student's project score", min_value=0.0, step=1.0)
internal_score = st.number_input("Enter the Student's internal score", min_value=0.0, step=1.0)
external_score = st.number_input("Enter the Student's external score", min_value=0.0, step=1.0)

if st.button("Result"):
    if project_score >= 50 and internal_score >= 50 and external_score >= 50:
        total = project_score + internal_score + external_score
        if total > 90:
            grade = "A Grade"
        elif total > 80:
            grade = "B Grade"
        else:
            grade = "C Grade"
        st.write(f"Total Score: {total}, Grade: {grade}")
    else:
        if project_score < 50:
            st.write(f"You're Failed in project with score: {project_score}")
        if internal_score < 50:
            st.write(f"You're Failed in internal with score: {internal_score}")
        if external_score < 50:
            st.write(f"You're Failed in external with score: {external_score}")

