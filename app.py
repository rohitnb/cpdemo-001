from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests
import calcfunctions

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/results', methods=['POST'])

def results():
   input1 = request.form.get('input1')
   input2 = request.form.get('input2')
   operation = request.form.get('operation')

   if input1 and input2 and operation:
        print('LOG: Input Recevied. Parameters Input1=%s, Operation=%s, Input2=%s' % (input1, operation, input2))

        if operation == "+":
            result = calcfunctions.addInputs(input1, input2)

        elif operation == "-":
            result = calcfunctions.subtractInputs(input1, input2)
        
        elif operation == "*":
            result = calcfunctions.multiplyInputs(input1, input2)

        elif operation == "/":
            result = calcfunctions.divideInputs(input1, input2)
            if result == "DIV0":
                return redirect(url_for('index'))

        elif operation == "%":
            result = calcfunctions.modInputs(input1, input2)
        
        elif operation == "^":
            result = calcfunctions.powerInputs(input1, input2)
        
        elif operation == "~":
            result = calcfunctions.squiggleInputs(input1, input2)

        print('LOG: Result = %s'% (result))
        return render_template('results.html', input1 = input1, input2 = input2, operation = operation, result = result)
   else:
       print('Request for results page received with no inputs or blank inputs -- redirecting')
       return redirect(url_for('index'))


@app.route('/singleinputs')
def singleinputs():
   print('Request for Single Inputs page received')
   return render_template('singleinputs.html')


@app.route('/siresults', methods=['POST'])

def siresults():

    input1 = request.form.get('input1')
    operation = request.form.get('operation')

    if input1 and operation:

        print('LOG: Input Recevied. Parameters Input1=%s, Operation=%s' % (input1, operation))

        if operation == "!":
            result = calcfunctions.factorialInput(input1)

        elif operation == "$":
            result = calcfunctions.dollarInput(input1)


        print('LOG: Result = %s'% (result))
        return render_template('siresults.html', input1 = input1, operation = operation, result = result)
    
if __name__ == '__main__':
   app.run()