from flask import Flask,request,render_template
from pycaret.classification import *
import pandas as pd
import numpy as np

app = Flask(__name__)

model = load_model('Credit_Score_Model')
cols = ['Customer_ID','Month','Age','Occupation','Annual_Income','Num_Bank_Accounts','Num_Credit_Card','Interest_Rate','Num_of_Loan','Delay_from_due_date','Num_of_Delayed_Payment','Changed_Credit_Limit','Credit_Mix','Outstanding_Debt','Credit_Utilization_Ratio','Payment_of_Min_Amount','Total_EMI_per_month','Amount_invested_monthly','Payment_Behaviour','Monthly_Balance']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    """
        Este método devuelve el resultado de la predicción del Score Crediticio del cliente.
        El formato es una tabla con los resultados de la predicción, donde la columna prediction_label predice si el score es Standard, Poor o Good.
        La columna prediction_score indica la probabilidad de la predicción
        
        Los parámetros del modelo están establecidos en la lista cols, con un total de 20 columnas
    """
    features = [x for x in request.form.values()]
    final = np.array(features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen)
    prediction_label = prediction['prediction_label'][0]
    prediction_score = float(prediction['prediction_score'][0])
    return render_template('home.html', pred='El Score Crediticio del cliente es: {0} con un score de: {1}'.format(prediction_label, prediction_score))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
