from flask import Blueprint, render_template, request, redirect
from utilities.db_manager import DBManager

assignment10 = Blueprint('assignment10', __name__, static_folder='assignment10', static_url_path='/assignment10', template_folder='templates')


@assignment10.route('/insert', methods= ['GET','POST'])
def insert_user():
    if request.method == 'POST':
        ID= request.form['id']
        firstname= request.form['firstname']
        lastname= request.form['lastname']
        email= request.form['email']
        query= "INSERT INTO ex10(ID, firstname, lastname, email ) Values ('%s', '%s','%s','%s')" % (ID, firstname, lastname, email)
        dbManager = DBManager()
        dbManager.commit(query=query)
    return redirect('/assignment10')


@assignment10.route ('/update',methods= ['GET', 'POST'])
def update_user():
    if request.method== 'POST':
        ID = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        query_email= "UPDATE ex10 set email=('%s') where ID=('%s')" %(email, ID)
        query_firstname = "UPDATE ex10 set firstname=('%s') where ID=('%s')" % (firstname, ID)
        query_lastname = "UPDATE ex10 set lastname=('%s') where ID=('%s')" % (lastname, ID)

        dbManager = DBManager()
        dbManager.commit(query=query_email)
        dbManager.commit(query=query_firstname)
        dbManager.commit(query=query_lastname)
    return redirect('/assignment10')

@assignment10.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
       ID = request.form['id']
       query = "DELETE from ex10 where ID=('%s')" % ID
       dbManager = DBManager()
       dbManager.commit(query=query)
    return redirect('/assignment10')

@assignment10.route('/assignment10')
def userlist():
    query = "select * from ex10"
    dbManager = DBManager()
    query_result = dbManager.fetch(query)
    return render_template('assignment10.html',ex10=query_result)
