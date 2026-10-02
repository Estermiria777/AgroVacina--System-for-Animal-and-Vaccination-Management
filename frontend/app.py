import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(
    page_title="AgroVacina | Digital Herd & Vaccination Traceability",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #F1F5F9; 
    }

    [data-testid="stSidebar"] {
        background-color: #064E3B;
        border-right: 1px solid #047857;
    }
    
    [data-testid="stSidebar"] * {
        color: #ECFDF5 !important;
    }

    .hero-card {
        background: linear-gradient(90deg, #064E3B 0%, #047857 100%);
        border-radius: 12px;
        padding: 28px 32px;
        color: #FFFFFF;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .hero-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 0.95rem;
        color: #A7F3D0 !important;
        margin-top: 6px;
    }

    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .kpi-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .kpi-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: #064E3B;
        margin-top: 4px;
    }

    .kpi-footer {
        font-size: 0.8rem;
        margin-top: 4px;
        font-weight: 600;
    }

    .text-success { color: #059669; }
    .text-warning { color: #D97706; }

    .card-img-top {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 12px 12px 0 0;
        display: block;
    }

    .card-container {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .card-content {
        padding: 16px;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #064E3B;
    }

    .card-desc {
        font-size: 0.85rem;
        color: #475569;
        margin-top: 4px;
    }

    div[data-testid="stForm"] {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        padding: 24px;
    }

    .stButton > button {
        background-color: #059669;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1.2rem;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #047857;
    }
    </style>
""", unsafe_allow_html=True)

API_URL = "http://agrovaccine_backend:8000"

def fetch_data(endpoint):
    try:
        response = requests.get(f"{API_URL}/{endpoint}", timeout=5)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception:
        return []

def post_data(endpoint, payload):
    try:
        response = requests.post(f"{API_URL}/{endpoint}", json=payload, timeout=5)
        return response.status_code in [200, 201]
    except Exception:
        return False

with st.sidebar:
    st.markdown("""
        <div style="padding: 8px 0px 16px 0px; border-bottom: 1px solid #047857;">
            <div style="font-size: 1.4rem; font-weight: 800; color: #FFFFFF;">AgroVacina</div>
            <div style="font-size: 0.75rem; color: #A7F3D0;">Digital Herd Traceability</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "Herd Registry", "Vaccine Protocol", "Farm Owners"],
        label_visibility="collapsed"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: #047857; padding: 14px; border-radius: 10px; font-size: 0.75rem; color: #ECFDF5;">
            <div style="font-weight: 700; margin-bottom: 4px;">Scope Protection</div>
            <div>Integrated microchip traceability designed strictly for Bovine & Equine livestock.</div>
        </div>
    """, unsafe_allow_html=True)

animals_list = fetch_data("animals")
owners_list = fetch_data("owners")
vaccines_list = fetch_data("vaccinations")

if page == "Dashboard":
    st.markdown("""
        <div class="hero-card">
            <div class="hero-title">Sanitary Control & Digital Traceability</div>
            <div class="hero-subtitle">Real-time immunization coverage and health history for livestock</div>
        </div>
    """, unsafe_allow_html=True)

    if animals_list:
        df_animals = pd.DataFrame(animals_list)
        total_animals = len(animals_list)
        bovine_count = sum(1 for a in animals_list if str(a.get("species", "")).lower() == "bovine")
        equine_count = sum(1 for a in animals_list if str(a.get("species", "")).lower() == "equine")
    else:
        mock_data = [
            {"Microchip ID": "982 000124891201", "Name": "Nelore Raio", "Species": "Bovine", "Breed": "Nelore", "Status": "Vaccinated"},
            {"Microchip ID": "982 000124891842", "Name": "Trovão", "Species": "Equine", "Breed": "Mangalarga", "Status": "Pending"},
            {"Microchip ID": "982 000124891003", "Name": "Angus Prime", "Species": "Bovine", "Breed": "Angus", "Status": "Vaccinated"},
            {"Microchip ID": "982 000124891910", "Name": "Ventania", "Species": "Equine", "Breed": "Quarter Horse", "Status": "Vaccinated"}
        ]
        df_animals = pd.DataFrame(mock_data)
        total_animals = 1248
        bovine_count = 840
        equine_count = 408

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Total Registered Herd</div>
                <div class="kpi-value">{total_animals:,}</div>
                <div class="kpi-footer text-success">100% Microchipped</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class="kpi-card">
                <div class="kpi-title">Vaccine Coverage</div>
                <div class="kpi-value">95.4%</div>
                <div class="kpi-footer text-success">&uarr; Optimal protection rate</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">Vaccine Records</div>
                <div class="kpi-value">{len(vaccines_list) if vaccines_list else 28}</div>
                <div class="kpi-footer text-warning">Doses Registered</div>
            </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
            <div class="kpi-card">
                <div class="kpi-title">Traceability Rate</div>
                <div class="kpi-value">100%</div>
                <div class="kpi-footer text-success">&check; Digital Passport Active</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.subheader("Registered Herd Database")
        st.dataframe(df_animals, use_container_width=True, hide_index=True)

    with right_col:
        st.subheader("Species Breakdown")
        species_df = pd.DataFrame({
            "Species": ["Bovine", "Equine"],
            "Head Count": [bovine_count, equine_count]
        })
        fig = px.bar(
            species_df, 
            x="Species", 
            y="Head Count", 
            color_discrete_sequence=["#059669"],
            text_auto=True
        )
        fig.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)

elif page == "Herd Registry":
    st.subheader("Herd Management & Microchip Association")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
            <div class="card-container">
                <img src="https://images.unsplash.com/photo-1570042225831-d98fa7577f1e?q=80&w=600&auto=format&fit=crop" class="card-img-top"/>
                <div class="card-content">
                    <div class="card-title">Bovine Livestock</div>
                    <div class="card-desc">Cattle traceability and sanitary record.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
            <div class="card-container">
                <img src="https://images.unsplash.com/photo-1553284965-83fd3e82fa5a?q=80&w=600&auto=format&fit=crop" class="card-img-top"/>
                <div class="card-content">
                    <div class="card-title">Equine Livestock</div>
                    <div class="card-desc">Horse passport and immunization history.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("Register Animal & Microchip Tag", expanded=True):
        with st.form("register_animal_form"):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Animal Name / Microchip Tag Number")
                species = st.selectbox("Livestock Species", ["Bovine", "Equine"])
                breed = st.text_input("Breed / Genetic Line")
            with c2:
                birth_date = st.date_input("Date of Birth")
                owner_id = st.number_input("Property Owner ID", min_value=1, step=1)

            submitted = st.form_submit_button("Save Animal Profile")
            if submitted:
                payload = {
                    "name": name,
                    "species": species,
                    "breed": breed,
                    "birth_date": str(birth_date),
                    "owner_id": owner_id
                }
                success = post_data("animals", payload)
                if success:
                    st.success(f"Animal '{name}' registered successfully!")
                    st.rerun()
                else:
                    st.error("Failed to register animal. Check owner ID or API availability.")

elif page == "Vaccine Protocol":
    st.subheader("Sanitary Protocols & Vaccination Schedule")
    
    with st.expander("Log New Vaccination Event", expanded=True):
        with st.form("register_vaccine_form"):
            c1, c2 = st.columns(2)
            with c1:
                animal_id = st.number_input("Animal ID", min_value=1, step=1)
                vaccine_name = st.selectbox(
                    "Vaccine Name", 
                    ["Foot-and-Mouth", "Brucellosis", "Equine Influenza", "Rabies", "Tetanus Toxoid"]
                )
                batch_number = st.text_input("Batch / Lot Number")
            with c2:
                applied_date = st.date_input("Application Date")
                next_due_date = st.date_input("Next Booster Due Date")
                veterinarian = st.text_input("Veterinarian / Responsible Person")

            v_submitted = st.form_submit_button("Register Vaccination Dose")
            if v_submitted:
                v_payload = {
                    "animal_id": animal_id,
                    "vaccine_name": vaccine_name,
                    "batch_number": batch_number,
                    "applied_date": str(applied_date),
                    "next_due_date": str(next_due_date),
                    "veterinarian": veterinarian
                }
                success = post_data("vaccinations", v_payload)
                if success:
                    st.success(f"Vaccination recorded for Animal ID {animal_id}!")
                    st.rerun()
                else:
                    st.error("Failed to record vaccination dose. Check animal ID or API availability.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Vaccination History Logs")
    if vaccines_list:
        st.dataframe(pd.DataFrame(vaccines_list), use_container_width=True, hide_index=True)
    else:
        st.info("No vaccination logs available in the system.")

elif page == "Farm Owners":
    st.subheader("Farm Owners & Property Directory")
<<<<<<< HEAD
=======
    
    with st.expander("Register Farm Owner", expanded=True):
        with st.form("register_owner_form"):
            col1, col2 = st.columns(2)
            with col1:
                owner_name = st.text_input("Full Name / Entity Name")
                document_id = st.text_input("CPF / CNPJ / Document ID")
            with col2:
                farm_name = st.text_input("Farm / Property Name")
                location = st.text_input("Municipality / State")

            o_submitted = st.form_submit_button("Register Owner")
            if o_submitted:
                o_payload = {
                    "name": owner_name,
                    "document_id": document_id,
                    "farm_name": farm_name,
                    "location": location
                }
                success = post_data("owners", o_payload)
                if success:
                    st.success(f"Owner '{owner_name}' registered successfully!")
                    st.rerun()
                else:
                    st.error("Failed to register farm owner. Verify network or API service.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Registered Properties & Owners")
    if owners_list:
        st.dataframe(pd.DataFrame(owners_list), use_container_width=True, hide_index=True)
    else:
        st.info("No farm owners registered in the system.")
>>>>>>> f031d8d (feat: restore dashboard species breakdown chart with backend data fallback)
