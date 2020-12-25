from flask import Flask, render_template, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    username ='ariel'
    return render_template('CSS_CV_BoazKahlon CSS.css', name='ariel', second_name=) # רנדר טמפליט יודעת לחפש בתוך טמפלייט







# @app.route('/main')
# def main():
#     logged_in = False
#     if logged_in:
#         #  redirect is mooving to other route
#         return redirect('/ContactList')
#     else:
#         #  url_for is mooving to  function
#         return redirect(url_for('vip'))
#
#
# @app.route('/ContactList')
# def contacts():
#     return "used the redirect func"
#
#
# @app.route('/vip')
# def vip():
#     return " used the url_for func"

# @app.route('/name', get,post,)


if __name__ == '__main__':
    app.run(debug=True)