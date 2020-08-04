# Put your app in here.
from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """Adds number through query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def sub_nums():
    """Subtracts number through query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_nums():
    """Multiplies number through query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return mult(result)

@app.route('/div')
def div_nums():
    """Divides number through query parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

@app.route("/math/<oper>")
def do_math(oper)
    """Do various math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
