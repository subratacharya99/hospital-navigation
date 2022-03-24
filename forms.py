from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length



class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    accessible = BooleanField('Accessible', validators=[DataRequired()])
    floor = IntegerField('Floor', validators=[DataRequired()])
    