from flask import Flask, render_template, url_for
from forms import LocationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8c77bf14abe1c038b49ffb7087067fbe'

#If we make git public, then these should be changed to environment variables
user = 'neo4j'
pw = 'fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A'
uri = '2e126d37.databases.neo4j.io'



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/add_location")
def add_location():
    form = LocationForm()
    return render_template('add_location.html', title = 'Add a Location', form = form)


if __name__ == '__main__':
    # create_an_item()
    app.run(debug=True)
