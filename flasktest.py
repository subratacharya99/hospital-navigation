from flask import Flask, render_template, url_for

app = Flask(__name__)

#If we make git public, then these should be changed to environment variables
user = 'neo4j'
pw = 'fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A'
uri = '2e126d37.databases.neo4j.io'



@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    # create_an_item()
    app.run(debug=True)
