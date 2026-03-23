# functools, 是 python 的高级库,提供高阶函数(接受函数为参数或返回函数的函数)以及函数操作工具
import functools

from flask import (
    # BluePrint,是Flask中用来模块化组织应用的工具,可以将相关的路由,视图,静态文件,模板等分组到一个可以复用的组建中,可以像插件一样将组件注册到主应用
    Blueprint, 
    # flash,用来在请求之间传递一次性消息的功能,常用于用户操作后的反馈提示
    # 消息存放在 session 中
    # 调用 flash 存储消息,下一个请求通过 get_flashed_messages() 取出并自动清除
    flash, 
    # Flask 中, g 是饮用上下文全局对象,用于在同一个请求的不同部分之间共享数据
    g, 
    # redirect 是 Flask 提供的辅助函数,用来生成 Http 重定向响应,调用 redirect , Flask 会返回一个状态码为 302 响应.
    redirect,
    # render_template 直接返回 HTML 内容,请求地址不变
    render_template, 
    # request 是全局请求对象,用来访问客户端发送的 HTTP 请求数据,由 Flask 自动管理,在视图函数或请求钩子中使用时,会动态绑定到当前请求的上下文
    # 可以从中获取到请求方法,参数,表单等
    request, 
    # session, Flask 框架内置的全局代理对象,用于在用户会话之间安全地存储数据,底层默认使用`客户端`,可以通过扩展(`Flask-Session`)改为服务端存储
    session, 
    # 根据视图函数名称和参数动态生成URL
    url_for
)

# Werkzeug 是 Flask 的 底层基础库，提供了处理 HTTP 请求/响应、路由、调试等核心功能
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db_sqlite import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/register', methods=('GET', 'POST'))  这是路由
# def register():  这是视图方法
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()

        error = None

        if not username:
            error = 'username is required.'
        elif not password:
            error = 'password is required.'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError as ex:
                error = f'user {username} is already registered.'
            else:
                return redirect(url_for("auth.login"))

        # 将 error 信息
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        ).fetchone()

        if user is None:
            error = 'incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

# 注册函数，该函数会在每一个视图函数之前执行
# 应用级钩子,在所有的url请求前都会执行
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?',
            (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 自定义装饰器方法,方法调用前判断是否已经登陆
def login_required(view):
    # @functools.warps 装饰器,将被装饰函数的元数据(如__name__,__doc__)复制到包装函数,避免调试时信息丢失;
    # FLask框架中,在自定义装饰器,可以使用@wrap保持原函数的属性
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view

