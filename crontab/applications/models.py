from django.db import models


class FileUser2Push(models.Model):
    app_id = models.CharField(primary_key=True, max_length=180)
    uid = models.IntegerField(unique=True, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_activate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_user2push'


class FileTaskLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    task_type = models.CharField(max_length=180, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    outcome = models.IntegerField(blank=True, null=True)
    time_stamp = models.CharField(max_length=180, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_task_log'


class AdminUserRole(models.Model):
    user = models.ForeignKey('AdminUser', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('AdminRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user_role'


class AdminUser(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AdminPower(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    open_type = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.CharField(max_length=19, blank=True, null=True)
    icon = models.CharField(max_length=128, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_power'


class AdminRolePower(models.Model):
    power = models.ForeignKey('AdminPower', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('AdminRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role_power'


class AdminDictType(models.Model):
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_dict_type'


class AdminDictData(models.Model):
    data_label = models.CharField(max_length=255, blank=True, null=True)
    data_value = models.CharField(max_length=255, blank=True, null=True)
    type_code = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_dict_data'


class AdminRole(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role'


class User2Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    phone = models.CharField(unique=True, max_length=125, blank=True, null=True)
    password = models.CharField(max_length=125, blank=True, null=True)
    user = models.ForeignKey('AdminUser', models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_activate = models.IntegerField(blank=True, null=True)
    scope = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_user2account'
