import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)


@app.route('/')
def Demo():
    return render_template('start.html')


# database = {'teja': '504', 'akhil': '521', 'akash': '513', 'sravan': '505'}


@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            new_user = request.form["username"]
            new_pwd = request.form["password"]
            email = request.form["email"]
            phone = request.form["phone"]
            with sqlite3.connect("project_db.db") as con:
                cur = con.cursor()

                # con.execute('CREATE TABLE students (username TEXT, password TEXT, Email TEXT, phone TEXT)')
                # print("Table created successfully")
                # con.close()
                cur.execute("INSERT into student_data (username,password,email,phone) values (?,?,?,?)",
                            (new_user, new_pwd, email, phone))
                con.commit()
                msg = "Student successfully Added now you can login with your credentials"
        except:
            con.rollback()
            msg = "Student already exist"
        finally:
            return render_template("pass.html", a=msg)
            con.close()


@app.route('/valid_login', methods=['POST', 'GET'])
def valid_login():

    msg1 = ""
    r = ""
    if request.method == "POST":
        username = request.form['username']

        pwd = request.form['password']

        con = sqlite3.connect("project_db.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM student_data WHERE username ='" +
                    username+"' and password ='"+pwd+"'")
        r = cur.fetchall()
        print(r)

        # return render_template('pass.html', n=r, c=username, d=pwd)
        # print(r)
        try:
            if (username == r[0][0] and pwd == r[0][1]):
                session['valid_login'] = True
                # msg1 = "Logged in successfully"
                return redirect(url_for('home'))
        except:
            msg1 = "Wrong username or password "
            return render_template('login.html', info=msg1)

        # for i in r:
        #     if (username == i[0] and pwd == i[1]):
        #         session["logedin"] = True
        #         return redirect(url_for('/home'))
        #     else:
        #         msg1 = "wrong username or password"
        #         return render_template('login.html', info=msg1)

        # if username not in database:
        #     return render_template('login.html', info='invalid')
        # else:
        #     if database[username] != pwd:
        #         return render_template('login.html', info='invalid')
        #     else:
        #         # return render_template('login.html', info='You Have Successfully Logged In')
        #         return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


if __name__ == '__main__':

    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = 'key'

    app.run(port=5050, debug=True)
