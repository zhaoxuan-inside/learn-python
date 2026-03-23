import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db_sqlite import init_db, get_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():

    # 创建并打开一个临时文件，返回文件描述符和指向它的路径
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

# client 固件使用 app 固件创建的应用对象调用 app.test_client()。测试将使用这个客户端来发送请求到应用，不用运行服务器。
@pytest.fixture
def client(app):
    return app.test_client()

# runner 固件和 client 类似。app.test_cli_runner() 创建一个运行器，它可以用来调用注册到应用的 Click 命令。
@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )
    
    def logout(self):
        return self._client.get('/auth/logout')
    
@pytest.fixture
def auth(client):
    return AuthActions(client)

