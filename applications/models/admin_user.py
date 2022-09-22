import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from applications.extensions import db
from sqlalchemy.orm import relationship
from applications.configs import configs


class Card(db.Model):
    __tablename__ = 'file_card'
    card_id = db.Column(db.String(180), primary_key=True, comment='卡密ID', )
    enable = db.Column(db.Boolean, comment='是否启用', default=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    expiry_time = db.Column(db.DateTime,
                            default=(datetime.datetime.now() + datetime.timedelta(days=configs.CARD_DURATION)),
                            comment="失效时间")
    user_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), comment="用户绑定的卡密")
    user = db.relationship('User', backref='card', uselist=False, )
    is_delete = db.Column(db.Boolean, default=False, )  # 假删除
    # user_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), comment="用户绑定的卡密", unique=True)


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
    is_superuser = db.Column(db.Boolean, default=False, comment="是否超级用户")
    openid = db.Column(db.String(255), nullable=True, comment="微信登录openid")

    # card = db.relationship('Card', uselist=False, backref="user")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.username
