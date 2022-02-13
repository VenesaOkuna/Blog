from . import db

class Random_Quote:
    '''
    Random Qoute class to define random quotes Objects
    '''

    def __init__(self,id,quote,author):
        self.id =id
        self.quote = quote
        self.author = author
 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    blog = db.relationship('Blog', backref = 'user', lazy='dynamic')
    all_comments = db.relationship('Comment',backref = 'user',lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id')) 

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'