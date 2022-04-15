from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from neo4j import GraphDatabase, Query
from neo4j.graph import Relationship as Relationship

def return_location_list():
    driver = GraphDatabase.driver("neo4j+s://2e126d37.databases.neo4j.io", auth=("neo4j", "fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A"))
    locations = ["Select a Location"]
    with driver.session() as session:
        query = ("MATCH (l: Location)"
                    "RETURN l.name as name"
            )
        result = session.run(query)
        driver.close()
        for r in result:
            locations.append(r['name'])
        return locations
    
class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    floor = IntegerField('Floor', validators=[DataRequired()])
    building = StringField('Building', validators = [Length(min=2, max=20)])
    submit = SubmitField('Confirm')
    
class NavigationForm(FlaskForm):
    startpoint = SelectField("Where are you?", choices = return_location_list())
    endpoint = SelectField("Where are you going?", choices= return_location_list())
    submit = SubmitField('Navigate')
