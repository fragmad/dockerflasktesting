# environment.py
import os, sys, tempfile
from FlaskHello import hello

pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
full_path = os.path.join(new_path, 'hello')

def before_feature(context, feature):
    hello.app.config['TESTING'] = True
    context.client = hello.app.test_client()


def after_feature(context, feature):
    pass
