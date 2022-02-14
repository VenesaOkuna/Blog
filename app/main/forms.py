from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import DataRequired,Email
from ..models import User, Subscription

class CommentForm(FlaskForm):

    username=StringField('Username', validators = [DataRequired()])
    comment = TextAreaField('Blog comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class AddBlogForm(FlaskForm):
    title=StringField('Title', validators = [DataRequired()])
    content = TextAreaField ('Blog', validators = [DataRequired()])
    submit = SubmitField('SUBMIT')

class SubscriptionForm(FlaskForm):
   name=StringField('Name',validators =[DataRequired()])
   email=StringField('Email',validators =[DataRequired()])
   submit = SubmitField('Submit')
   def validate_email(self,data_field):
            if Subscription.query.filter_by(email =data_field.data).first():
                raise ValidationError('we already have an account here')

class UpdateBlogForm(FlaskForm):
   title=StringField('Title',validators = [DataRequired()])
   content=TextAreaField('Content',validators = [DataRequired()])
   submit=SubmitField('SUBMIT')