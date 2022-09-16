from flask import Blueprint, render_template, request, jsonify

from applications.common import curd
from applications.common.utils import validate
from applications.common.utils.http import success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import xss_escape
from applications.extensions import db
# from applications.models import Dept, User
from applications.models import User
from applications.schemas import DeptOutSchema

# dept_bp = Blueprint('dept', __name__, url_prefix='/dept')


# def register_dept_views(app):
#     app.register_blueprint(dept_bp)


# @dept_bp.get('/')
# @authorize("admin:dept:main", log=True)
# def main():
#     return render_template('admin/dept/main.html')
#
#
# @dept_bp.post('/data')
# @authorize("admin:dept:main", log=True)
# def data():
#     dept = Dept.query.order_by(Dept.sort).all()
#     power_data = curd.model_to_dicts(schema=DeptOutSchema, data=dept)
#     res = {
#         "data": power_data
#     }
#     return jsonify(res)
#
#
# @dept_bp.get('/add')
# @authorize("admin:dept:add", log=True)
# def add():
#     return render_template('admin/dept/add.html')
#
#
# @dept_bp.get('/tree')
# @authorize("admin:dept:main", log=True)
# def tree():
#     dept = Dept.query.order_by(Dept.sort).all()
#     power_data = curd.model_to_dicts(schema=DeptOutSchema, data=dept)
#     res = {
#         "status": {"code": 200, "message": "默认"},
#         "data": power_data
#
#     }
#     return jsonify(res)
#
#
# @dept_bp.post('/save')
# @authorize("admin:dept:add", log=True)
# def save():
#     req_json = request.json
#     dept = Dept(
#         parent_id=req_json.get('parentId'),
#         dept_name=xss_escape(req_json.get('deptName')),
#         sort=xss_escape(req_json.get('sort')),
#         leader=xss_escape(req_json.get('leader')),
#         phone=xss_escape(req_json.get('phone')),
#         email=xss_escape(req_json.get('email')),
#         status=xss_escape(req_json.get('status')),
#         address=xss_escape(req_json.get('address'))
#     )
#     r = db.session.add(dept)
#     db.session.commit()
#     return success_api(msg="成功")
#
#
# @dept_bp.get('/edit')
# @authorize("admin:dept:edit", log=True)
# def edit():
#     _id = request.args.get("deptId")
#     dept = curd.get_one_by_id(model=Dept, id=_id)
#     return render_template('admin/dept/edit.html', dept=dept)
#
#
# # 启用
# @dept_bp.put('/enable')
# @authorize("admin:dept:edit", log=True)
# def enable():
#     id = request.json.get('deptId')
#     if id:
#         enable = 1
#         d = Dept.query.filter_by(id=id).update({"status": enable})
#         if d:
#             db.session.commit()
#             return success_api(msg="启用成功")
#         return fail_api(msg="出错啦")
#     return fail_api(msg="数据错误")
#
#
# # 禁用
# @dept_bp.put('/disable')
# @authorize("admin:dept:edit", log=True)
# def dis_enable():
#     id = request.json.get('deptId')
#     if id:
#         enable = 0
#         d = Dept.query.filter_by(id=id).update({"status": enable})
#         if d:
#             db.session.commit()
#             return success_api(msg="禁用成功")
#         return fail_api(msg="出错啦")
#     return fail_api(msg="数据错误")
#
#
# @dept_bp.put('/update')
# @authorize("admin:dept:edit", log=True)
# def update():
#     json = request.json
#     id = json.get("deptId"),
#     data = {
#         "dept_name": validate.xss_escape(json.get("deptName")),
#         "sort": validate.xss_escape(json.get("sort")),
#         "leader": validate.xss_escape(json.get("leader")),
#         "phone": validate.xss_escape(json.get("phone")),
#         "email": validate.xss_escape(json.get("email")),
#         "status": validate.xss_escape(json.get("status")),
#         "address": validate.xss_escape(json.get("address"))
#     }
#     d = Dept.query.filter_by(id=id).update(data)
#     if not d:
#         return fail_api(msg="更新失败")
#     db.session.commit()
#     return success_api(msg="更新成功")
#
#
# @dept_bp.delete('/remove/<int:_id>')
# @authorize("admin:dept:remove", log=True)
# def remove(_id):
#     d = Dept.query.filter_by(id=_id).delete()
#     if not d:
#         return fail_api(msg="删除失败")
#     res = User.query.filter_by(dept_id=_id).update({"dept_id": None})
#     db.session.commit()
#     if res:
#         return success_api(msg="删除成功")
#     else:
#         return fail_api(msg="删除失败")
