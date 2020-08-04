@app.route('/welcome')
def say_hello():
    """Return welcome at this route"""
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_hello():
    """Return welcome home"""
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def say_hello():
    """Return welcome back"""
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html