"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	"""User account model."""

	__tablename__ = 'UsersFlask'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(100),
		nullable=False,
		unique=False
	)
	
	password = db.Column(
		db.String(200),
		primary_key=False,
		unique=False,
		nullable=False
	)
	
	def set_password(self, password):
		"""Create hashed password."""
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		"""Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)



class Prod(UserMixin, db.Model):
	

	__tablename__ = 'Productss'
	id = db.Column(
		db.Integer,
		primary_key=True,
		autoincrement=True
	)
	name = db.Column(
		db.String(30),
		nullable=False,
		unique=False,
		primary_key=True
	)
	
	price = db.Column(
		db.String(50),
		unique=False,
		nullable=False

	)
    

	amount = db.Column(
		db.String(50),
		unique=False,
		nullable=False
	)

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()








