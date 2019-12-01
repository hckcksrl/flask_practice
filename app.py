from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


class Home(MethodView):

    def get(self):
        return "Classed-View"

    def post(self):
        return "Classed-View"


app.add_url_rule('/home', view_func=Home.as_view('home'))

