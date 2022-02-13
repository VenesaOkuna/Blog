from os import abort
from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_random_quote
from flask_login import login_required
from ..models import Comment,Blog,User, PhotoProfile, Random_Quote, Subscription
from .forms import UpdateProfile,CommentForm,UpdateProfile,AddBlogForm,SubscriptionForm,UpdateBlogForm
from ..import db, photos

# Views


@main.route('/', methods = ['GET','POST'] )
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    #making api call
    quote=get_random_quote()
    # blog= get_blogs()
    title = 'Home - diary of a whimpy junior developer'

    return render_template('index.html',title=title,quote=quote)




@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    title='Update Your  Biograph'
    return render_template('profile/update.html',form =form, title= title)



