import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from applications.extensions import db
from applications.configs import configs

class User(db.Model, UserMixin):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), nullable=True, comment='用户名')
    email = db.Column(db.String(20), nullable=True, comment='邮箱')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    remark = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), nullable=True, comment='哈希密码')
    enable = db.Column(db.Integer, default=1, comment='启用')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')
    openid = db.Column(db.String(255), nullable=True, comment="微信登录openid")
    role = db.relationship('Role', secondary="admin_user_role", backref=db.backref('user'), lazy='dynamic')
    account = db.relationship("User2Account", backref="user")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.username


class User2Card(db.Model):
    __tablename__ = 'file_card'
    card_id = db.Column(db.String(180), primary_key=True, comment='卡密ID', )
    enable = db.Column(db.Boolean, comment='是否启用', default=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    expiry_time = db.Column(db.DateTime,
                            default=(datetime.datetime.now() + datetime.timedelta(days=configs.CARD_DURATION)),
                            comment="失效时间")
    user_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), comment="用户绑定的卡密")
    user = db.relationship('User', backref='card', uselist=False, )


class User2Account(db.Model):
    __tablename__ = 'file_user2account'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    phone = db.Column(db.String(125), comment='小米登录手机号',unique=True)
    password = db.Column(db.String(125),comment='小米登录密码')
    user_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), comment="操作用户id")
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    is_activate = db.Column(db.Boolean,default=True,comment='是否在线')
    scope =db.Column(db.String(125),comment='步数范围')

class User2Push(db.Model):
    __tablename__ = 'file_user2push'
    app_id = db.Column(db.String(180), primary_key=True, comment='推送+token',)
    uid = db.Column((db.Integer), comment='绑定用户id', )
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    is_activate = db.Column(db.Boolean,default=True,comment='是否有效')
    