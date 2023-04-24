from flask import Flask, render_template, request
#import jsonify
import requests
import joblib
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='C:/Users/seanr/Desktop/wine_quality/webapp/templates')   # template_folder='templates'


model = joblib.load("C:/Users/seanr/Desktop/wine_quality/saved_models/model.joblib")
    

@app.route('/')           #,methods=['GET']
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    data=[float(x) for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("index.html",prediction_text="The wine quality is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)