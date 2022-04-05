from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length



class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    floor = IntegerField('Floor', validators=[DataRequired()])
    building = StringField('Building', validators = Length(min=2, max=20))
    submit = SubmitField('Confirm')