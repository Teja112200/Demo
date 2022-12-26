import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def Demo():
    return render_template('login.html')


database = {'teja': '504', 'akhil': '521', 'akash': '513', 'sravan': '505'}


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

                cur.execute("INSERT into student_data (username, password , email , phone) values (?,?,?,?)",
                            (new_user, new_pwd, email, phone))
                con.commit()
                msg = "Student successfully Added"
        except:
            con.rollback()
            msg = "We can not add the student to the list"
        finally:
            return render_template("pass.html", a=msg, n=new_user, c=new_pwd, d=email, q=phone)
            con.close()


@app.route('/valid_login', methods=['POST', 'GET'])
def valid_login():

    username = request.form['username']

    pwd = request.form['password']

    if username not in database:
        return render_template('login.html', info='invalid')
    else:
        if database[username] != pwd:
            return render_template('login.html', info='invalid')
        else:
            # return render_template('login.html', info='You Have Successfully Logged In')
            return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5050)
