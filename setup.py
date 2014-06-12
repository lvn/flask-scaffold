from setuptools import setup

setup(name='Flask-Project',
      version='1.0',
      description='Flask app',
      author='Elvin Yung',
      author_email='elvin@elvinyung.com',
      url='https://github.com/elvinyung/',
      install_requires=['flask', 'werkzeug', 'jinja2', 'sqlalchemy',\
       'flask-sqlalchemy', 'flask-login', 'oauth', 'flask-oauth', 'alembic', 'flask-script', 'flask-migrate'],
     )