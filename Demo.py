from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def Demo():
    return render_template('login.html')


database = {'teja': '504', 'akhil': '521', 'akash': '513', 'sravan': '505'}


@app.route('/form_login', methods=['GET', 'POST'])
def home():
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
