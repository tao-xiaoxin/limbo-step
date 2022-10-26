from flask import Blueprint, request, render_template
from flask_login import current_user
from applications.models.admin_user import User2Account
from applications.libs import mi_login,zepp_life
from applications.libs.mi.other_mi import pig_step,phone_step,email_step
from applications.extensions import db
from applications.common.utils.http import table_api, fail_api, success_api
admin_account = Blueprint("admin_account", __name__, url_prefix="/admin/account")


@admin_account.get("/")
def main():
    return render_template("admin/account/main.html")


@admin_account.route("/data", methods=["GET"])
def get_account():
    account_list = list()
    query_condition = dict()
    row_id = [i.id for i in current_user.role][0]
    if row_id != 1:
        query_condition["user_id"] = current_user.id
    o_user2account = User2Account.query.filter_by(**query_condition).all()
    n = 0
    for qs in o_user2account:
        if qs.is_activate:
            is_activate = "在线"
        else:
            is_activate = "掉线"
        n = n + 1
        account_list.append(
            {
                "id": n,
                "account_id": qs.account_id,
                "phone": qs.phone,
                "password": qs.password,
                "create_time": qs.create_time,
                "is_activate": is_activate,
                "scope": qs.scope,
            }
        )
    return table_api(data=account_list, count=len(account_list))


@admin_account.post("/save")
def save():
    code_list =list()
    phone = request.json.get("phone")
    password = request.json.get("password")
    gte_scope = request.json.get("gte_scope")
    lte_scope = request.json.get("lte_scope")
    
    if not phone or not password or not gte_scope or not lte_scope:
        return fail_api(msg="不可以为空!")
    try:
        if int(gte_scope) < 9999:
            return fail_api(msg="最低步数不小于9999!")
        if int(lte_scope) > 98000:
            return fail_api(msg="最高步数不大于98000!")
        if int(lte_scope) < int(gte_scope):
            return fail_api(msg="最高步数不能大于最低步数!")
    except Exception as e:
        return fail_api(msg="输入有误,请清空重试!")
    # login_token, mi_uid = mi_login.login(phone, password)
    # if not login_token or not mi_uid:
        # return fail_api(msg="小米运动账号登录失败!")
    try:
        login_token, mi_uid = mi_login.login(phone, password)
        step, zeep_result=zepp_life.zepp_step(login_token,mi_uid,int(gte_scope),int(lte_scope))
        code_list.append(str(zeep_result['code']))
    except Exception as e:
        pass
    try:
        pig_result =pig_step(phone, password,int(gte_scope),int(lte_scope)) 
        code_list.append(str(pig_result['code']))
    except Exception as e:pass
    try:
        phone_result = phone_step(phone, password,int(gte_scope),int(lte_scope))
        code_list.append(str(phone_result['code']))
    except Exception as e:pass
    try:
        email_result = email_step(phone, password,int(gte_scope),int(lte_scope))
        code_list.append(str(email_result['code']))
    except Exception as e:pass
    if "200" not in code_list:
        return fail_api(msg="小米运动账号登录失败!")
    user2account = User2Account(
        phone=phone,
        password=password,
        user_id=current_user.id,
        scope=str("{}~{}".format(gte_scope, lte_scope)),
    )
    db.session.add(user2account)
    db.session.commit()
    return success_api(msg="操作成功!")


# 增加
@admin_account.get("/add")
def add():
    return render_template("admin/account/add.html")


# 修改
@admin_account.get("/edit/<int:_account_id>")
def edit(_account_id):
    o_user2account = User2Account.query.filter_by(account_id=_account_id).first()
    scope = str(o_user2account.scope).split("~")
    return render_template(
        "admin/account/edit.html",
        data={
            "account_id": _account_id,
            "phone": o_user2account.phone,
            "password": o_user2account.password,
            "gte": scope[0],
            "lte": scope[1],
        },
    )


# 恢复
@admin_account.put("/enable")
def enable():
    return fail_api(msg="数据错误")


# 暂停
@admin_account.put("/disable")
def dis_enable():
    return fail_api(msg="数据错误")


@admin_account.delete("/remove/<int:_account_id>")
def remove_account(_account_id):  # 移除
    o_user2account=User2Account.query.get(_account_id)
    try:
        db.session.delete(o_user2account)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return success_api(msg="删除成功")
