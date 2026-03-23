import sqlite3
from datetime import datetime

import click
# current_app 是一个特殊的对象，指向处理请求的 Flask 应用，
from flask import current_app
# g 是一个特殊的对象，对每一个请求都是唯一的，用来存储在处理请求时可能会被多个函数访问的数据；
# 例如：get_db 方法在同一个请求中被多次调用，g确保每次调用获取到的都是同一个对象，也就是同一个连接，这个连接会被存储和服用；
from flask import g

# 注册自定义转换器，将 SQLite 的 timestamp 类型转为 datetime 对象
def _convert_timestamp(ts):
    # SQLite 存储的时间格式: "2024-03-23 12:34:56"
    return datetime.strptime(ts.decode(), "%Y-%m-%d %H:%M:%S")

sqlite3.register_converter("timestamp", _convert_timestamp)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            # 用来处理 TIMESTAMP 类型的字段
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # 将 SQLite 数据库连接的默认行工厂设置为 sqlite3.Row，使查询返回的行不再是普通元组，而是支持通过列名访问的类似字典的对象。
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """
    创建 python 命令
    """
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # 注册 close_db 到 Flask 应用
    # 每次请求结束后释放资源（数据库连接、文件句柄、网络连接等）
    # 是 Flask 提供的一个优雅的资源清理机制，它让开发者可以集中管理应用上下文的生命周期，避免资源泄漏。
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)