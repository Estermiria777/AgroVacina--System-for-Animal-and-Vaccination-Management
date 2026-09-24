from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:1234@localhost:5433/animal_management"

engine = create_engine(DATABASE_URL)

