from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

app.secret_key = '123'


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
    users = [{"name": "boaz", "lastname": "kahlon", "email": "boaz@gmail.com"},
             {"name": "guy", "lastname": "amitai", "email": "guy@gmail.com"},
             {"name": "shahar", "lastname": "lev", "email": "shahar@gmail.com"}]
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

    return render_template('assignment9.html', flag=True)


if __name__ == '__main__':
    app.run(debug=True)

# request_method=request.method

# @app.route('/contactME')
# def contact_func():
#     return render_template('contactM_HTML.html',
#                                                 user={'firstName':'boaz', 'lastName': 'kahlon'}, # נקרא dictionary
#                                                 gender = {'gender1':'boy' , 'gender2':'girl'},
#                                                 hobbies= ['swim', 'run', 'eat'] ,  # רשימה ניתן לשנות אחרי שיצרנו אותה
#                                                 degree= ('B.Sc', 'M.Sc')            # ככה לא ניתן לשנות אחרי שניצור
#                                                 )
# degree הוא taple

# render_template('assignment8.html')
# , user={'firstName':'boaz', 'lastName': 'kahlon'}
