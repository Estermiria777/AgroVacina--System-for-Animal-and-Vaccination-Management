# 🐄 AgroVacina: Animal & Vaccination Management System

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC292B?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-6BA43A?style=for-the-badge&logo=python&logoColor=white)](https://alembic.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

An enterprise-grade digital platform designed for livestock health tracking, digital vaccination cards, and individual traceability for cattle, horses, and small ruminants.

---

## 💻 Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Language-Python_3.14-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.14" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/ORM-SQLAlchemy-D00000?style=flat-square&logo=python&logoColor=white" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/Migrations-Alembic-228B22?style=flat-square&logo=python&logoColor=white" alt="Alembic" />
  <img src="https://img.shields.io/badge/Containerization-Docker_Compose-0DB7ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  <img src="https://img.shields.io/badge/Validation-Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
</p>

---

## ✨ Features

- 🏷️ **Owner Management**: Complete CRUD functionality for farm owners and properties.
- 🐂 **Animal Traceability**: Individual animal profile registration with species, breed, and birth records.
- 💉 **Vaccination Records**: Digital immunization tracking with batch, dosage, and next-dose schedules.
- ⚡ **Database Versioning**: Alembic migrations synced with PostgreSQL.

---

## 🛠️ Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AgroVacina--System-for-Animal-and-Vaccination-Management.git
cd AgroVacina--System-for-Animal-and-Vaccination-Management
```

### 2. Launch Infrastructure with Docker

```bash
docker compose up -d --build
```

### 3. Apply Database Migrations

```bash
docker compose exec web alembic upgrade head
```

---

## 📑 Interactive Documentation

Once the Docker containers are running, explore the interactive API documentation at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌿 Git Branch Workflow

- `main` / `master`: Production-ready releases.
- `development`: Active feature integration branch.
