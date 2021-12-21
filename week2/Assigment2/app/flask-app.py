from simpleinterest import simple_interest
from flask import Flask, jsonify, request

#instantiate flask objects
app = Flask('__name__')

@app.route('/', methods=['GET','POST'])
def get_input():

    """
    A function to get request using flask, evalete and return result
    """
    packet= request.get_json(force=True)
    principal =packet["principal"]
    rate = packet["rate"]
    period = packet["period"]

    interest = simple_interest(principal, rate, period)

    return jsonify(packet,interest)

# driver function
if __name__ == '_main_':
    app.run()