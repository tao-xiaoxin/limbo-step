# 渲染配置
from flask import jsonify
from flask_login import login_required

from . import rights_bp
from ...common import admin


# 管理员配置
@rights_bp.get('/configs')
@login_required
def configs():
    return admin.get_render_config()


# 管理员菜单
@rights_bp.get('/menu')
@login_required
def menu():
    menu_tree = admin.make_menu_tree()
    return jsonify(menu_tree)



