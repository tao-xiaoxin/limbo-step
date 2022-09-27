from flask import Blueprint, request, render_template
from applications.common.utils.http import table_api, fail_api, success_api
admin_account = Blueprint('admin_account', __name__, url_prefix='/admin/account')


@admin_account.get('/')
def main():
    return render_template('admin/account/main.html')

@admin_account.route('/add_job', methods=['GET'])
def add_task():
    return '6'

@admin_account.route('/data', methods=['GET'])
def get_task():  # 获取
    # jobs = scheduler.get_jobs()
    jobs_list = []
    # for job in jobs:
    #     jobs_list.append(job_to_dict(job))
    return table_api(data=jobs_list, count=len(jobs_list))


# 增加
@admin_account.get('/add')
def add():
    return render_template('admin/task/add.html', task_list=task_list)


@admin_account.post('/save')
def save():
    # _id = request.json.get("id")
    # name = request.json.get("id")
    # type = request.json.get("type")
    # functions = request.json.get("functions")
    # datetime = request.json.get("datetime")
    # time = request.json.get("time")
    # if not hasattr(tasks, functions):
    #     return fail_api()
    # if type == 'date':
    #     scheduler.add_job(
    #         func=getattr(tasks, functions),
    #         id=_id,
    #         name=name,
    #         args=(1, 1),
    #         trigger=type,
    #         run_date=datetime,
    #         replace_existing=True)
    # elif type == 'interval':
    #     scheduler.add_job(
    #         func=getattr(tasks, functions),
    #         id=_id,
    #         name=name,
    #         args=(1, 1),
    #         trigger=type,
    #         replace_existing=True)
    # elif type == 'cron':
    #     scheduler.add_job(
    #         func=getattr(tasks, functions),
    #         id=_id,
    #         name=name,
    #         args=(1, 1),
    #         trigger=type,
    #         replace_existing=True)

    return success_api()


# 恢复
@admin_account.put('/enable')
def enable():
    # _id = request.json.get('id')
    # # print(id)
    # if _id:
    #     scheduler.resume_job(str(_id))
    #     return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 暂停
@admin_account.put('/disable')
def dis_enable():
    # _id = request.json.get('id')
    # if _id:
        # scheduler.pause_job(str(_id))
        # return success_api(msg="暂停成功")
    return fail_api(msg="数据错误")


@admin_account.delete('/remove/<int:_id>')
def remove_job(_id):  # 移除
    # scheduler.remove_job(str(_id))
    return success_api(msg="删除成功")