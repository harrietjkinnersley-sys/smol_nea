from flask import Flask, render_template, request, redirect, url_for
#from flask sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def web_design():
    return render_template('web_design.html')

@app.route('/dishwasher')
def dishwasher():
    return render_template('dishwasher_tablets.html')


@app.route('/laundry')
def laundry():
    return render_template('laundry_capsules.html')

@app.route('/conditioner')
def conditioner():
    return render_template('fabric_conditioner.html')

@app.route('/handwash')
def handwash():
    return render_template('handwash.html')







if __name__ == '__main__':
    
    app.run (debug=True)