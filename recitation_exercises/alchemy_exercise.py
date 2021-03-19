from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# feature we don't need that is being deprecated upstream by sqlaclchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



'''
Consider the following schema:
	Forest(forest_no, forest_name, area)
	State(state_name, area)
	Coverage(entry_no, forest_no, state_name, area)

Notice how a forest can span two states
'''

'''
(1) create the tables/models, make sure you set the primary and 
    foreign keys. Look at the 'db.txt' file to find out
    what the types of each column should be. I only used either
    an integer and a string
'''
class Forest(db.Model):
	__tablename__ = "forest"
	forest_no = db.Column(db.Integer, primary_key = True)
	forest_name = db.Column(db.String)
	area = db.Column(db.Integer)

	def __init__(self, forest_no, forest_name, area):
	 self.forest_no = forest_no
	 self.forest_name = forest_name
	 self.area = area

class State(db.Model):
	__tablename__ = "state"
	state_name = db.Column(db.String(2), primary_key = True)
	area = db.Column(db.Integer)

	def __init__(self, state_name, area):
		self.state_name = state_name
		self.area = area

class Coverage(db.Model):
	__tablename__ = "coverage"
	entry_no = db.Column(db.Integer, primary_key = True)
	forest_no = db.Column(db.Integer, db.ForeignKey("forest.forest.no"))
	state_name = db.Column(db.String(2), db.ForeignKey("state.stae_name"))
	area = db.Column(db.Integer)

	def __init__(self, entry_no, forest_no, state_name, area):
		self.entry_no = entry_no
		self.forest_no = forest_no
		self.state_name = state_name
		self.area = area
		

'''
(2) populate the tables you created above, you can find the data for 
	the tables in the 'db.txt' file. The delimiter for an entry/record 
	is ',' and for the tables it is an empty line ('\n'). Remeber to 
	drop all any previosuly created tables to avoid nay problems
'''
db.drop_all()
# db.create_all()
with open('/Users/zstat/Documents/Pitt/Spring2021/WebApps/cs1520_examples/recitation_exercises/db.txt', 'r') as file:
	forest = True
	state = False



'''
(3) find and print the forest name(s) with the largest area (hint: use the func.max)
'''


'''
(4) find and print names of all forests that are located in PA (hint: might have to join 2 tables)
'''


'''
(5) find and print the number of forests for each state in descending order (hint: use func.count)
'''


'''
(6) find and print the percentage of area covered by forests in all states (hint: use func.sum)
'''





