from flask import Flask, render_template, redirect, url_for, render_template

app = Flask(__name__)


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
    return render_template('assignment8.html', user={'firstName':'boaz','lastName': 'kahlon'} ,  hobbies= ['swim', 'run', 'coock'], page_name='Guest' )



if __name__ == '__main__':
    app.run(debug=True)





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










