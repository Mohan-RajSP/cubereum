"""This is manage.py file"""
from app.main import create_app
from flask_script import Manager
from waitress import serve
app = create_app()
manager = Manager(app=app)

@manager.command
def run():
    serve(app,host='0.0.0.0', port=8080)

@manager.command
def dev_run():
    app.run(host='0.0.0.0', port=8080, debug=False)

if __name__ == '__main__':
    manager.run()
