from flask import Flask
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from routes.search_routes import search_bp
app.register_blueprint(search_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
