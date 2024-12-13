import streamlit as st
st.title("Gross Salary Calculator")
salary=st.number_input("Enter your Salary amount: ",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
    hra=0
    da=0
    if salary<10000:
        hra=0.67*salary
        da=0.73*salary
    elif salary<=20000:
        hra=0.69*salary
        da=0.76*salary
    else:
        hra=0.73*salary
        da=0.89*salary
    gross_sal= hra+ da+ salary
    st.write(f"Gross Salary: {gross_sal}")
