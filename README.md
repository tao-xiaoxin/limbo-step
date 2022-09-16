<<<<<<< HEAD
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
  [Pear Admin 预 览](http://flask.pearadmin.com)   
  [Pear Admin 官 网](http://www.pearadmin.com/)   
  [Pear Admin 社区](http://forum.pearadmin.com/)

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
```

执行 flask run 命令启动项目

#### 命令行创建视图

```bash
# 示例

flask new --type view --name test/a

# 自动注册蓝图
# 访问http://127.0.0.1:5000/test/a/
```

#### 预览项目

|  |  |
|---------------------|---------------------|
| ![](docs/assets/1.jpg)  | ![](docs/assets/2.jpg)  |
| ![](docs/assets/3.jpg)|  ![](docs/assets/4.jpg)   |
| ![](docs/assets/5.jpg) |  ![](docs/assets/6.jpg)   |
=======
# mimotion
![ 刷步数](https://github.com/xunichanghuan/mimotion/actions/workflows/run.yml/badge.svg)
![同步到Gitee](https://github.com/xunichanghuan/mimotion/actions/workflows/sync2gitee.yml/badge.svg)
[![GitHub forks](https://img.shields.io/github/forks/xunichanghuan/mimotion?style=flat-square)](https://github.com/xunichanghuan/mimotion/network)
[![GitHub stars](https://img.shields.io/github/stars/xunichanghuan/mimotion?style=flat-square)](https://github.com/xunichanghuan/mimotion/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/xunichanghuan/mimotion?style=flat-square)](https://github.com/xunichanghuan/mimotion/issues)

# 小米运动自动刷步数

> 小米运动自动刷步数

## Github Actions 部署指南

### 一、Fork 此仓库

### 二、设置账号密码
> 添加名为  **USER**、**PWD**、**SKEY**、**SCKEY**、**POSITION** 、**CORPID**、**CORPSECRET**、**AGENTID**、**TOUSER**、**TOPARTY**、**TOTAG**、**OPEN_GET_WEATHER**、**AREA**的变量: Settings-->Secrets-->New secret  

| Secrets |  格式  |
| -------- | ----- |
| USER |   小米运动登录账号,仅支持小米运动账号对应的手机号,不支持小米账号|
| PWD |   小米运动登录密码,仅支持小米运动账号对应的密码|
| SKEY |   酷推skey，如无填写**NO**|
| SCKEY |   server酱sckey，如无填写**NO**|
| POSITION |   是否开启企业微信推送**false**关闭,**true**开启|
| CORPID |   企业ID， 登陆企业微信，在我的企业-->企业信息里查看,必填，如果没有，填写**NO**|
| CORPSECRET |   自建应用，每个自建应用里都有单独的secret,必填，如果没有，填写**NO**|
| AGENTID |   填写你的应用ID，不加引号，是个整型常数,就是AgentId，如果没有，填写**NO**|
| TOUSER |   指定接收消息的成员，成员ID列表（多个接收者用”&#166;”分隔，最多支持1000个）。特殊情况：指定为”@all”，则向该企业应用的全部成员发送，如果没有，填写**NO**|
| TOPARTY |   指定接收消息的部门，部门ID列表，多个接收者用”&#166;”分隔，最多支持100个。当touser为”@all”时填写”@all”，如果没有，填写**NO**|
| TOTAG |   指定接收消息的标签，标签ID列表，多个接收者用”&#166;”分隔，最多支持100个。当touser为”@all”时填写”@all”，如果没有，填写**NO**|
| OPEN_GET_WEATHER |   开启根据地区天气情况降低步数**False**关闭,**True**开启|
| AREA |   设置获取天气的地区（上面开启后必填）如：**北京**，当**OPEN_GET_WEATHER**为**False**时填写**NO**|
| PAT |   此处**PAT**需要申请，值为github token，教程详见：https://www.jianshu.com/p/bb82b3ad1d11 ,需要repo和workflow权限,此项必填，避免git push的权限错误。 |

### 三、自定义启动时间多账户(用不上请忽略)

多账户请用 **#** 分割 然后保存到变量 **USER** 和 **PWD**

#### 例如

**13800138000#13800138001** 变量 **USER**

**abc123qwe#abcqwe2** 变量 **PWD**

### 四、自定义启动时间

编辑 **main.py**

找到 time_list项目，此数据为北京时间，默认表示为8点10点13点15点17点19点21点运行,如需修改，请修改time_list列表，如：time_list = [7, 9, 13, 15, 17, 19, 20]就表示为7点9点13点15点17点19点20点运行，Actions触发里面也要同步修改。
编辑 **random_cron.sh**
修改其中**if**语句的判断时间为UTC时间，即**北京时间-8**，如北京时间8点为UTC时间0点，需要运行的时间-8就是UTC时间



## 注意事项

1. 每天运行七次，整由time_list和random_cron.sh控制，分钟为随机值

2. 多账户的数量和密码请一定要对上 不然无法使用!!!

3. 启动时间得是UTC时间!

4. server酱注册地址 [点我](https://sct.ftqq.com/)

5. 如果支付宝没有更新步数,到小米运动->设置->账号->注销账号->清空数据,然后重新登录,重新绑定第三方

6. 小米运动不会更新步数，只有关联的会同步！！！！！

7. 请各位在使用时Fork[主分支](https://github.com/xunichanghuan/mimotion/)，防止出现不必要的bug.

8. TG推送教程 [点我](./TG_PUSH.md)

9. 请注意，账号不是 [小米账号]，而是 [小米运动] 的账号。

## 历史Star数

[![Stargazers over time](https://starchart.cc/xunichanghuan/mimotion.svg)](https://starchart.cc/xunichanghuan/mimotion)
>>>>>>> d0ed45a163010bc8ee9360eb50f85e7c072beda5
