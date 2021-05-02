from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('submit')