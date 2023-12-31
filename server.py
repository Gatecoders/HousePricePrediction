from flask import Flask,request,jsonify
import util
app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_prices',methods=['POST'])
def predict_home_prices():
    if request.method=='POST':
        location=request.form["location"]
        bhk=int(request.form["bhk"])
        bath=int(request.form["bath"])
        total_sqft = float(request.form["sqft"])

        response=jsonify({
            'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
        })

        response.headers.add('Access-Control-Allow-Origin','*')
        return response



if __name__=="__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_aritfacts()
    app.run(debug=True,port=8000)