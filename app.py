import serverless_wsgi
from flask import Flask
from handlers import feature1, feature2

app = Flask(__name__)

app.register_blueprint(feature1.bp)
app.register_blueprint(feature2.bp)

def handler(event, context):
	return serverless_wsgi.handle_request(app, event, context)