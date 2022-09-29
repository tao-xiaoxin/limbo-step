from flask import Blueprint, request, render_template
from flask_login import current_user
from applications.models.admin_user import User2Push
from applications.extensions import db
from applications.libs.pushplus import send_push
from applications.common.utils.http import table_api, fail_api, success_api
from applications.configs.config import configs
push_plus = Blueprint('push_plus', __name__, url_prefix='/push/plus')


@push_plus.route('/')
def index():
    return render_template('push/main.html')


# 获取数据列表
@push_plus.route("/data", methods=["GET"])
def get_account():
    account_list = list()
    query_condition = dict()
    row_id = [i.id for i in current_user.role][0]
    if row_id != 1:
        query_condition["uid"] = current_user.id
    o_user2account = User2Push.query.filter_by(**query_condition).all()
    n = 0
    for qs in o_user2account:
        if qs.is_activate:
            is_activate = "有效"
        else:
            is_activate = "无效"
        n = n + 1
        account_list.append(
            {
                "id": n,
                "app_id": qs.app_id,
                "create_time": qs.create_time,
                "is_activate": is_activate,
            }
        )
    return table_api(data=account_list, count=len(account_list))


# 增加
@push_plus.get("/add")
def add():
    return render_template("push/add.html")


# 删除
@push_plus.delete("/remove/<int:_app_id>")
def remove_account(_app_id):  # 移除
    o_user2account=User2Push.query.get(_app_id)
    try:
        db.session.delete(o_user2account)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return success_api(msg="删除成功")


@push_plus.post("/save")
def save():
    app_id = request.json.get("app_id")
    if not app_id:
        return fail_api(msg="不可以为空!")
    uid=current_user.id
    o_user2push=User2Push.query.filter_by(uid=uid).first()
    if o_user2push:
        return fail_api(msg="令牌绑定超出限制,每个用户只可以仅限绑定一个!")
    title = "{}消息推送".format(configs.SYSTEM_NAME)
    send_result=send_push(token=app_id,title=title,content="账号绑定成功!",template="markdown")
    if str(send_result["code"]) ==str(200):
        user2account = User2Push(
            app_id=app_id,
            uid=uid,
        )
        db.session.add(user2account)
        db.session.commit()
        return success_api(msg="操作成功!")
    else:
        return fail_api(msg=send_result['msg'])
