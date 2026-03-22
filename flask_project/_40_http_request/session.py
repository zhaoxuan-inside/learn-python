from flask import session, Flask, redirect, url_for, request

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'logger in as {session["username"]}'
    return 'you are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return """
    <form method="port">
        <p><input type=text name=username>
        <p><input type=submit value=Login
    </form>
    """

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))