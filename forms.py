from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from neo4j import GraphDatabase
from neo4j.graph import Relationship as Relationship


user = 'neo4j'
pw = 'fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A'
uri = "neo4j+s://2e126d37.databases.neo4j.io"


def return_location_list():
    driver = GraphDatabase.driver(uri, auth=(user, pw))
    locations = ["Select a Location"]
    with driver.session() as session:
        query = ("MATCH (l: Location)"
                    "RETURN l.name as name"
            )
        result = session.run(query)
        for r in result:
            locations.append(r['name'])
        driver.close()
        return locations
    
def startpoint():
    driver = GraphDatabase.driver(uri, auth=(user, pw))
    locations = ["Where are you?"]
    with driver.session() as session:
        query = ("MATCH (l: Location)"
                    "RETURN l.name as name"
            )
        result = session.run(query)
        for r in result:
            locations.append(r['name'])
        driver.close()
        return locations

def endpoint():
    driver = GraphDatabase.driver(uri, auth=(user, pw))
    locations = ["Where are you going?"]
    with driver.session() as session:
        query = ("MATCH (l: Location)"
                    "RETURN l.name as name"
            )
        result = session.run(query)
        for r in result:
            locations.append(r['name'])
        driver.close()
        return locations  

class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    floor = IntegerField('Floor', validators=[DataRequired()])
    building = StringField('Building', validators = [Length(min=2, max=20)])
    submit = SubmitField('Confirm')
    
class NavigationForm(FlaskForm):
    startpoint = SelectField("Where are you?", choices = startpoint())
    endpoint = SelectField("Where are you going?", choices= endpoint())
    submit = SubmitField('Go')
