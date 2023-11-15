from flask import Flask, request, render_template

app = Flask(__name__)

def km_to_miles(km):
    return km * 0.621371

def oz_to_lbs(oz):
    return oz * 0.0625

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    unit_type = request.form['unit_type']
    value = float(request.form['value'])
    
    if unit_type == 'km':
        converted = km_to_miles(value)
        return f"{value} kilometers is {converted} miles"
    elif unit_type == 'oz':
        converted = oz_to_lbs(value)
        return f"{value} ounces is {converted} pounds"
    else:
        return "Invalid unit type"

if __name__ == '__main__':
    app.run(debug=True)
