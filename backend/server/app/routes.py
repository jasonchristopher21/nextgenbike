from app import applications

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"