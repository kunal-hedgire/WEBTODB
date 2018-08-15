from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///User.db'#Specify the dtabase name
db = SQLAlchemy(app)



class User(db.Model):#class name is equavalent to the table name
    id = db.Column('id', db.Integer,primary_key=True)#table attributes which is create in databse User
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    address = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    yearofexp = db.Column(db.Integer)
    skill = db.Column(db.String(10))

    def __init__(self,fname,lname,age,addr,gen,yrexpr,skill):#A constructor for assigning values
        self.firstname=fname
        self.lastname=lname
        self.age=age
        self.address=addr
        self.gender=gen
        self.yearofexp=yrexpr
        self.skill=skill

    def __str__(self):
        return '''
                \n\n###########User-Details################\n
                FIRSTNAME : {} \n
                LASTNAME : {}  \n
                AGE : {}  \n
                ADDRESS : {}  \n
                GENDER : {}  \n
                YEAROFEXP : {}  \n
                SKILLS : {}  \n
                '''.format(self.firstname,self.lastname,self.age,self.address,self.gender,self.yearofexp,self.skill)



@app.route('/')
def show_login_page():
    return render_template('login.html')

@app.route('/register')
def show_register_page():
    print('inside register page')
    return render_template('signup.html')

@app.route('/saveuser', methods=['GET','POST'])
def get_register_pagedata():
    print(request.form)
    user = User(request.form['firstname'],
                request.form['lastname'],
                request.form['age'],
                request.form['address'],
                request.form['gender'],
                request.form['yearofexp'],
                request.form['java'])

    db.session.add(user)
    db.session.commit()
    list = User.query.filter_by(firstname='kunal').all()

    return render_template('regsuccess.html',records= list,msg="User saved Succefully...!")

@app.route('/welcome', methods=['GET','POST'])
def welcome_page():

    return render_template('Welcome.html')




if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)