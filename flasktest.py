from flask import Flask, render_template, url_for
import neomodel
from neomodel import config

app = Flask(__name__)

#If we make git public, then these should be changed to environment variables
user = 'neo4j'
pw = 'fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A'
uri = '2e126d37.databases.neo4j.io'

db_url = 'neo4j+s://{}:{}@{}'.format(user, pw, uri)

config.DATABASE_URL = db_url


class Location(neomodel.StructuredNode):
    __primarykey__ = 'name'
    name = neomodel.StringProperty(unique_index=True)


def create_an_item():
    neomodel.db.set_connection(db_url)
    Location(name='Elevator E').save()


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    # create_an_item()
    app.run(debug=True)
