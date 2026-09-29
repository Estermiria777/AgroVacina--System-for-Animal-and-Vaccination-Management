import streamlit as st
import requests

st.set_page_config(
    page_title="AgroVaccine - Animal & Vaccination Management",
    page_icon="🐄",
    layout="wide"
)

API_BASE_URL = "http://localhost:8000/api/v1"

st.title("🐄 AgroVaccine System")

option = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Digital Vaccination Card", "Register Vaccine"]
)

if option == "Dashboard":
    st.header("📊 Dashboard")
    st.info("Herd statistics module under development.")

elif option == "Digital Vaccination Card":
    st.header("📜 Digital Vaccination Card")
    animal_id = st.number_input("Animal ID", min_value=1, step=1)
    
    if st.button("Search Records"):
        try:
            response = requests.get(f"{API_BASE_URL}/animals/{animal_id}/vaccines/")
            if response.status_code == 200:
                vaccines = response.json()
                if vaccines:
                    st.success(f"Found {len(vaccines)} vaccine records.")
                    st.dataframe(vaccines)
                else:
                    st.warning("No vaccine records found for this animal.")
            elif response.status_code == 404:
                st.error("Animal not found.")
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to connect to backend API: {e}")

elif option == "Register Vaccine":
    st.header("💉 Register New Vaccine")
    
    with st.form("vaccine_form"):
        animal_id = st.number_input("Animal ID", min_value=1, step=1)
        name = st.text_input("Vaccine Name")
        batch = st.text_input("Batch")
        application_date = st.date_input("Application Date")
        next_due_date = st.date_input("Next Due Date")
        
        submitted = st.form_submit_button("Save Vaccine")
        
        if submitted:
            payload = {
                "name": name,
                "batch": batch,
                "application_date": str(application_date),
                "next_due_date": str(next_due_date)
            }
            try:
                response = requests.post(f"{API_BASE_URL}/animals/{animal_id}/vaccines/", json=payload)
                if response.status_code in [200, 201]:
                    st.success("Vaccine registered successfully!")
                else:
                    st.error(f"Registration failed: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Failed to connect to backend API: {e}")