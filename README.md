<div align="center">
<br/>
<br/>
  <h1 align="center">
    Limbo Microstep
  </h1>
  <h4 align="center">
    千 里 之 行 , 始 于 足 下
  </h4> 

  [预 览](http://flask.pearadmin.com)   |   [官 网](http://www.taoxiaoxin.club/)   |   [社区](http://www.taoxiaoxin.club/)


<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/Limbo%20Microstep-1.0.0-green" alt="Limbo Microstep Version">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.6+-green.svg" alt="Python Version">
    </a>
      <a href="#">
        <img src="https://img.shields.io/badge/Mysql-5.6.2+-green.svg" alt="Mysql Version">
    </a>
</p>
</div>

<div align="center">
  <img  width="92%" style="border-radius:10px;margin-top:20px;margin-bottom:20px;box-shadow: 2px 0 6px gray;" src="https://s2.loli.net/2022/09/16/GWqYclejZFTvyEm.jpg" />
</div>

#### 项目简介
本项目基于 Pear Admin Flask 快速构建后台管理系统，拥抱应用广泛的python语言

#### 项目架构
flask 2.0.1 +	flask-sqlalchemy + 权限验证 + Flask-APScheduler 定时任务 + marshmallow 序列化与数据验证

####  Pear Admin Flask 内置功能

- [x] 用户管理：用户是系统操作者，该功能主要完成系统用户配置。
- [x] 权限管理：配置系统菜单，操作权限，按钮权限标识等。
- [x] 角色管理：角色菜单权限分配。
- [x] 操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
- [x] 登录日志：系统登录日志记录查询包含登录异常。
- [x] 服务监控：监视当前系统CPU、内存、磁盘、python版本,运行时长等相关信息。
- [x] 文件上传:   图片上传示例
- [x] 定时任务:   简单的定时任务
#### Pear Admin Flask 项目地址
  + [Pear Admin 预 览 : http://flask.pearadmin.com](http://flask.pearadmin.com)
  + [Pear Admin 官 网 : http://www.pearadmin.com](http://www.pearadmin.com/)   
  + [Pear Admin 社区 : http://forum.pearadmin.com](http://forum.pearadmin.com/)

####  项目结构

```
limbo-step
├─applications  # 应用
│  ├─configs  # 配置文件
│  │  ├─ common.py  # 普通配置
│  │  └─ config.py  # 配置文件对象
│  ├─extensions  # 注册插件
│  ├─models  # 数据模型
│  ├─static  # 静态资源文件
│  ├─templates  # 静态模板文件
│  └─views  # 视图部分
│     ├─admin  # 后台管理视图模块
│     └─index  # 前台视图模块
├─docs  # 文档说明（占坑）
├─migrations  # 迁移文件记录
├─requirement  # 依赖文件
├─libs # 第三方包
├─test # 测试文件夹（占坑）
└─.env # 项目的配置文件

```
## Limbo Microstep 使用指南

<br />

#### 项目安装

```bash
# 下 载
git clone https://github.com/tao-xiaoxin/limbo-step.git

# 安 装
pip install -r requirement\requirement-dev.txt

# 配 置
cp .flaskenv .env

```

#### 修改配置

```python
.env
# MySql配置信息
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=PearAdminFlask
MYSQL_USERNAME=root
MYSQL_PASSWORD=root

# Redis 配置
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# 密钥配置
SECRET_KEY='pear-admin-flask'

# 邮箱配置
MAIL_SERVER='smtp.qq.com'
MAIL_USERNAME='123@qq.com'
MAIL_PASSWORD='XXXXX' # 生成的授权码
```

#### Venv 安装

```bash
python -m venv venv
```

#### 运行项目

```bash
# 初 始 化 数 据 库

flask init

# 数据库迁移

flask db migrate

# 同步数据库

flask db upgrade

#执行命令启动项目 

flask run 
```

#### 命令行创建视图

```bash
# 示例

flask new --type view --name test/a

# 自动注册蓝图
# 访问http://127.0.0.1:5000/test/a/
```

### Limbo Microstep 部署指南

#### 运行项目

```bash
# 运行项目
bash start.sh

# 启动定时任务
nohup python3 task.py >logs/crontab.log 2>&1 &

# 安装Nginx
yum install nginx -y

```

# 定时任务
```bash

# 切换到crontab目录下
cd crontab/
#添加并启动定时任务
python manage.py crontab add
#显示当前的定时任务
python manage.py crontab show
crontab -l
#删除所有定时任务
python manage.py crontab remove
# 查看定时任务执行状态
tail -f /var/log/cron
service crond status
```

#### 部署Nginx

打开目录文件 `limbo-step/applications/configs/nginx.conf`

> 将项目路径和域名：limbo.xxx.top 修改为你的即可

<br>

### 在线预览

[点我预览](http://101.43.119.135:65535/)

## 注意事项

1. 每天早上8点定时同步!

2. (pushplus)推送+注册地址 [点我](https://www.pushplus.plus/login.html)

3. 如果支付宝没有更新步数,到小米运动->设置->账号->注销账号->清空数据,然后重新登录,重新绑定第三方

4. 小米运动不会更新步数，只有关联的会同步！！！！！

5. 请注意，账号不是 [小米账号]，而是 [小米运动] 的账号。

6. 只有关联了[推送加]，才能推送步数到微信

### 预览项目

|                        |                        |
|------------------------|------------------------|
| ![](docs/assets/8.jpg) | ![](docs/assets/2.jpg) |
| ![](docs/assets/3.jpg) | ![](docs/assets/4.jpg) |
| ![](docs/assets/5.jpg) | ![](docs/assets/6.jpg) |
