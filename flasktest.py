from flask import Flask, message_flashed, render_template, url_for, flash, redirect, request
from forms import LocationForm, NavigationForm
from neo4j import GraphDatabase

app = Flask(__name__)
app.config['SECRET_KEY'] = '8c77bf14abe1c038b49ffb7087067fbe'

#If we make git public, then these should be changed to environment variables
user = 'neo4j'
pw = 'fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A'
uri = '2e126d37.databases.neo4j.io'



@app.route("/")
def home():
    return render_template('newtemplates/home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('newtemplates/404.html'), 404

@app.route("/add_location", methods=['GET', 'POST'])
def add_location():
    form = LocationForm()
    if request.method == "POST":
        if form.is_submitted():
            print ("Successfully Submitted")
        if form.validate_on_submit():
            print('Success')

    return render_template('add_location.html', title = 'Add a Location', form = form)

@app.route("/contact", methods=["GET"])
def contact():
    return render_template('newtemplates/contact.html', title="Contact")


@app.route("/navigate", methods=["GET", "POST"])
def navigate():
    form = NavigationForm()
    if form.validate_on_submit():
        req = request.form
        startpoint = req['startpoint']
        endpoint = req['endpoint']
        if startpoint == "Where are you?" or endpoint == "Where are you going?" or startpoint == endpoint:
            return render_template('newtemplates/navigate.html', title = "Navigate", form=form)
        driver = GraphDatabase.driver("neo4j+s://2e126d37.databases.neo4j.io", auth=("neo4j", "fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A"))
        session = driver.session()
        startelevator, directiontoelevator = getDirectionToNearestElevator(session, startpoint)
        endelevator, directionfromelevator = getDirectionFromNearestElevator(session, endpoint)
        driver.close()
        firststep = f"From {startpoint}, head {directiontoelevator} towards Elevator {startelevator}"
        if startelevator < endelevator:
            secondstep = f"Once at Elevator {startelevator}, follow signs and head south towards Elevator {endelevator}"
        else:
            secondstep = f"Once at Elevator {startelevator}, follow signs and head north towards Elevator {endelevator}"
        thirdstep = f"After arriving at Elevator {endelevator} head {directionfromelevator} towards {endpoint}"
        finalstep = f"You have now arrived at {endpoint}"
        steps = [firststep, secondstep, thirdstep, finalstep]
        
        return render_template('results.html', directions = steps, start = startpoint, end = endpoint, title = "Directions")
    return render_template('newtemplates/navigate.html', title = 'Navigate', form = form)

@app.route("/settings")
def settings():
    return render_template('newtemplates/settings.html')

@app.route("/closures")
def closures():
    return render_template('newtemplates/closures.html')

@app.route("/team")
def team():
    return render_template('newtemplates/team.html')
    
#static methods
def getDirectionToNearestElevator(session, location):
        with session:
            query = (
                f"MATCH (: Location {{name: '{location}'}})-[r:CONNECTS]-(e: Elevator)"
                "RETURN r.name as name, e.name as ename"
               
            )
            result = session.run(query)
            for r in result:
                #print(f"The direction from {location} to Elevator {r['ename']} is {r['name']}")
                closeste = r['ename']
                directiontoe = r['name']
            return closeste, directiontoe

def getDirectionFromNearestElevator(session, location):
        with session:
            query = (
                f"MATCH (: Location {{name: '{location}'}})-[r:CONNECTS]-(e: Elevator)"
                "RETURN r.name as name, e.name as ename"
               
            )
            result = session.run(query)
            # if statement to return opposite
            
            for r in result:
                if r['name'] == "west":
                    r1 = "east"
                else:
                    r1 = "west"
            closeste = r['ename']
            return closeste, r1

if __name__ == '__main__':
    # create_an_item()
    app.run(debug=True)
