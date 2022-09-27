from flask import Blueprint, request, render_template

admin_account = Blueprint('admin_account', __name__, url_prefix='/admin/account')


@admin_account.get('/')
def main():
    return render_template('admin/account/main.html')