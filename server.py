# Run with "python server.py"

from bottle import route, run, template

@route('/api-v1/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
