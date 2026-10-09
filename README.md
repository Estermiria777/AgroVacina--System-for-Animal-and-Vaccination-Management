# 🛡️ AgroVacina — Digital Herd & Vaccination Traceability

> **Full-Stack Platform for Livestock Sanitary Traceability, Vaccination Control, and Herd Management (Bovine & Equine).** 

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 📌 About The Project

**AgroVacina** is a comprehensive AgTech solution designed to streamline livestock sanitary tracking, microchip identification, and immunization history for cattle and horses (Bovine and Equine livestock).

The application solves the challenge of fragmented sanitary records by integrating a high-performance **RESTful API** with an **interactive analytical dashboard**. It enables farmers, livestock managers, and veterinarians to securely record vaccination doses, batch numbers, booster due dates, and farm ownership data.

---

## 🚀 Key Features

- 📊 **Executive Dashboard**: Real-time KPI metrics for immunization coverage, total registered livestock, microchip traceability rate, and an interactive species breakdown (*Bovine vs. Equine*).
- 🐂 **Herd Registry**: Register animals with unique RFID/Microchip Tag IDs, species classification, genetic line/breed, and owner association.
- 💉 **Vaccination Protocols**: Log immunization events (Foot-and-Mouth, Brucellosis, Equine Influenza, Rabies, Tetanus Toxoid), including batch numbers, attending veterinarians, and next booster due dates.
- 🏡 **Farm Owners Directory**: Manage rural properties and track farm owner profiles across regional jurisdictions.
- 🔄 **Resilience & Smart Fallback**: The client dashboard features an automatic data fallback strategy to maintain metric visualization and user experience even during temporary API connection loss.

---

## 🏗️ System Architecture

The project is structured as a containerized microservices architecture managed via **Docker Compose**:

```text
       ┌─────────────────────────────────────────────────────────┐
       │                      User / Web Browser                 │
       └────────────────────────────┬────────────────────────────┘
                                    │ (HTTP / Port 8501)
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │             Frontend Service (Streamlit)                │
       │   - Interactive Dashboards & Entry Forms                │
       │   - Data Visualization (Plotly)                         │
       │   - Client-Side Fallback & Resilience Logic             │
       └────────────────────────────┬────────────────────────────┘
                                    │ REST API (JSON / Port 8000)
                                    ▼
       ┌─────────────────────────────────────────────────────────┐
       │              Backend Service (FastAPI)                  │
       │   - RESTful Endpoints (/animals, /vaccinations, /owners)│
       │   - Data Validation using Pydantic Schemas             │
       │   - Auto-generated OpenAPI / Swagger Documentation      │
       └────────────────────────────┴────────────────────────────┘
```

---

## 🛠️ Tech Stack

### **Frontend**
- **Streamlit**: Reactive web framework for Data & AI applications.
- **Plotly Express**: Interactive charts and visual analytics.
- **Pandas**: In-memory data manipulation and tabular transformations.
- **Requests**: HTTP client for API consumption.

### **Backend**
- **FastAPI**: Modern, high-performance Python web framework.
- **Pydantic**: Data validation and setting management using Python type annotations.
- **Uvicorn**: Lightning-fast ASGI server implementation.

### **DevOps & Infrastructure**
- **Docker & Docker Compose**: Containerization and multi-container orchestration.

---

## 💻 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/) installed.

### Installation & Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Estermiria777/AgroVacina--System-for-Animal-and-Vaccination-Management.git
   cd AgroVacina--System-for-Animal-and-Vaccination-Management
   ```

2. **Launch Application with Docker Compose:**
   ```bash
   docker compose up -d --build
   ```

3. **Access Services:**
   - 🎨 **Frontend Application:** [http://localhost:8501](http://localhost:8501)
   - ⚙️ **Interactive API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/animals` | Retrieve all registered animals |
| `POST` | `/animals` | Register a new animal & microchip tag |
| `GET` | `/vaccinations` | Fetch complete vaccination log history |
| `POST` | `/vaccinations` | Record a new vaccination entry |
| `GET` | `/owners` | Retrieve registered farm owners |
| `POST` | `/owners` | Register a new property owner |

---

  Developed with ❤️ by <b>Ester Freire</b>
</p>
