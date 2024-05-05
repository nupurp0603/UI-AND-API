from flask import Flask, render_template, send_from_directory,request, jsonify,request
import pickle
import numpy as np

app = Flask(__name__)

d_air=0
d_temp=0
d_pres=0

# Load the trained model
with open('model/ML Model/air_flow_model.pkl', 'rb') as file:
    air_flow = pickle.load(file)

with open('model/ML Model/outlet_pressure_model.pkl', 'rb') as file:
    out_pres = pickle.load(file)

with open('model/ML Model/outlet_temp_model.pkl', 'rb') as file:
    out_temp = pickle.load(file)

# app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model/<path:path>')
def send_model(path):
    return send_from_directory('model', path)


@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get the input data from the request
    global d_air, d_temp, d_pres
    print("entered")
    d_air = request.form.get('airFlow')
    d_temp = request.form.get('outletTemp')
    d_pres = request.form.get('outletPressure')
    # print(data1," ",data3)
    return jsonify({'message': 'Data received successfully'})    

@app.route('/air_flow', methods=['POST','GET'])
def predict_air():
   global d_air, d_temp, d_pres
   print("air_flow",d_air)
   return jsonify({'message': '123'})

@app.route('/out_temp', methods=['POST','GET'])
def predict_temp():
   global d_air, d_temp, d_pres
   print("temp",d_temp)
   return jsonify({'message': '123'})

@app.route('/out_pres', methods=['POST','GET'])
def predict_pres():
   global d_air, d_temp, d_pres
   print("pres",d_pres)
   return jsonify({'message': '123'})


# @app.route('/predict/out_temp', methods=['POST'])
# def predict():
#     # Get the input data from the request
#     data = request.json
    
#     # Transform the input data into a numpy array
#     features = np.array(data['features']).reshape(1, -1)
    
#     # Make prediction
#     prediction = model.predict(features)
    
#     # Return the prediction as JSON
#     return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)



