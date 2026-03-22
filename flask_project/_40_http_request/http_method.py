from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    
    error = None

    key = request.args.get('key', '')
    print(f'path param, key: {key}')

    method = request.method
    if method == 'GET':
        return f'Get method'
    elif method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f'{username} login by {password}')
        return f'Post method'
    elif method == 'PUT':
        return f'Put method'
    elif method == 'DELETE':
        return f'Delete method'
    else:
        return f'invalid method'


@app.route('/cookie/dispaly')
def display_cookie():
    username = request.cookies.get('username')
    return f'get from cookie. {username}'

@app.route('/cookie/save/<username>')
def save_cookie(username):
    resp = make_response(render_template('cookie.html', username=username))
    resp.set_cookie('username', username)
    return resp