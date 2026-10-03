from database import engine
  

try:
    connection = engine.connect()

    print("Connected to PostgreSQL successfully!")

    connection.close()

except Exception as error:
    print("Error connecting to database:")
    print(error)
