Flask-Imagine-S3Adapter
============

[![Author](https://img.shields.io/badge/author-Kronas-blue.svg)](https://github.com/kronas)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kronas/Flask-Imagine/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/flask-imagine/badge/?version=latest)](http://flask-imagine.readthedocs.org/en/latest/?badge=latest)

Amazon AWS S3 adapter for [Flask-Imagine](https://github.com/FlaskGuys/Flask-Imagine) extension.

Installation
------
```
$ pip install Flask-Imagine-S3Adapter
```

Configuration example
------
```
from flask import Flask
from flask.ext.imagine import Imagine
from flask.ext.imagine_s3_adapter import FlaskImagineS3Adapter

app = Flask(__name__)

app.config['IMAGINE_ADAPTERS'] = {
    's3': FlaskImagineS3Adapter
}

app.config['IMAGINE_ADAPTER'] = {
    'name': 's3',
    'access_key': 'your_access_key',
    'secret_key': 'your_secret_key',
    'bucket_name': 'your_bucket_name',
    'domain': 'domain.tld'      # Domain name for using ASW S3 static website hosting
    'schema': 'https'
}

# ... Another configuration options

# Init extension
imagine = Imagine(app)
#  or 
imagine = Imagine()
imagine.init_app(app)
```
