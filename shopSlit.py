import streamlit as st
st.title("Bill Calculator")
salary =st.number_input("Enter the employee salary")
Shopping_bill1 =st.number_input("Enter the bill amount of Shop1")
Shopping_bill2 =st.number_input("Enter the bill amount of Shop2")
Shopping_bill3 =st.number_input("Enter the bill amount of Shop3")
if st.button("Calculate Gross Salary"):
    total=Shopping_bill1+Shopping_bill2+Shopping_bill3
    st.write(f"The total bill amount is: {total}")
    percentage=(total/salary)*100
    st.write(f"The percentage of amount spent on shopping is: {percentage}%")


