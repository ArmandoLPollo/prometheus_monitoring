
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
from prometheus_client import start_http_server, Summary, Counter, Info
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

i = Info('app_info', 'Application info', version='1.0.3')
c = Counter('http_requests_total', 'HTTP Requests total', labels=['method', 'endpoint'])

##########################################################################
## Routes
##########################################################################

@app.route('/')
def hello():    
    c.inc()    
    return 'Hello, World!'

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()