from flask import Flask, Blueprint, redirect, url_for, render_template, request, session
from flask import jsonify

from utilities.db_manager import DBManager

app = Flask(__name__)
app.secret_key = '123'

from assignment10.assignment10app import assignment10
app.register_blueprint(assignment10)


@app.route('/')
def home():
    return render_template('CV_Page_html.html')
    # רנדר טמפליט יודעת לחפש בתוך טמפלייט

    # יש עוד פילטרים באתר. גם עבור רשימות ודברים נוספים


@app.route('/contactM_HTML.html')
def contactMe_func():
    return render_template('contactM_HTML.html')


@app.route('/assignment8.html')
def assignment():
    return render_template('assignment8.html', user={'firstName': 'boaz', 'lastName': 'kahlon'},
                           hobbies=['swim', 'run', 'coock'], page_name='Guest')


@app.route('/assignment9.html', methods=['GET', 'POST'])
def assignment9():
    users = [{"id": 7, "email": "michael.lawson@reqres.in", "name": "Michael", "lastname": "Lawson"},
             {"id": 8, "email": "lindsay.ferguson@reqres.in", "name": "Lindsay", "lastname": "Ferguson"},
             {"id": 9, "email": "tobias.funke@reqres.in", "name": "Tobias", "lastname": "Funke"},
             {"id": 10, "email": "byron.fields@reqres.in", "name": "Byron", "lastname": "Fields"},
             {"id": 11, "email": "george.edwards@reqres.in", "name": "George", "lastname": "Edwards"},
             {"id": 12, "email": "rachel.howell@reqres.in", "name": "Rachel", "lastname": "Howell"}]

    if request.method == 'GET':
        if 'name' and 'lastname' in request.args:
            name = request.args['name']
            lastname = request.args['lastname']
            users = users
            return render_template('assignment9.html', name=name, lastname=lastname, users=users, flag=True)

    if request.method == 'POST':
        if 'username' and 'post_lastname' in request.form:
            username = request.form['username']
            post_lastname = request.form['post_lastname']
            session['username'] = username
            session['loggedin'] = True
            return render_template('assignment9.html', username=username, post_lastname=post_lastname, flag=False)

    if request.method == 'POST':
        if 'username' and 'post_lastname' not in request.form:
            session['loggedin'] = False
            return render_template('assignment9.html', flag=True)
    return render_template('assignment9.html', flag=True, users=users)

@app.route('/assignment10')
def assignment10():
    return render_template('assignment10.html')

@app.route('/assignment11/users')
def Assignment11():
        query_users = "select * from ex10"
        dbManager = DBManager()
        query_result = dbManager.fetch(query_users)
        return f'users: {query_result}'


@app.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 1})

@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def getUser(SOME_USER_ID):
        query_users = "select * from ex10 WHERE id = '%s';" % SOME_USER_ID
        dbManager = DBManager()
        query_result = dbManager.fetch(query_users)
        if len(query_result) == 0:
            return 'No user'
        else:
            return jsonify({
                'success': 'True',
                'Data': query_result
            })


if __name__ == '__main__':
    app.run(debug=True)
