from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


# print("os.getenv: ", os.getenv('DATABASE_URL'))
# Your connection string
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:password@localhost:5432/ToDo"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/test_db_connection')
def test_db_connection():
    try:
        # Execute a simple query to test the connection
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
        db_version = result.fetchone()
        return f"Connected to the database. PostgreSQL version: {db_version[0]}"
    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
