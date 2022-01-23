from sqlalchemy import create_engine, Integer, String, insert, sql, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from random import randrange


# Create flask app
app = Flask(__name__)

# Create connection with postgres

engine_params = f"postgresql+psycopg2://{'postgres'}:{'1234'}@{'database'}:{5432}/{'postgres'}"
engine = create_engine(engine_params, pool_pre_ping=True)
conn = engine.raw_connection()
cur = conn.cursor()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Create table 'registros' model
class registros(Base):
    __tablename__ = 'registros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prediction = Column(String(length=20), nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=sql.func.now())

registros.metadata.create_all(engine)

# Cargar clasificador
model = joblib.load(r'model.pkl')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/predict", methods = ["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = model.predict(query_df)

    listToStr = ''.join(prediction[0])
    session.execute(insert(registros).values(id=randrange(1000), prediction=listToStr))

    session.commit()

    return jsonify({"Prediction":list(prediction)})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

