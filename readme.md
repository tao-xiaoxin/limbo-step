# Limbo-step-app 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-flask&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-flask" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-flask&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-flask" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-flask&type=packageDownload">
  </a>
</p>

<description>

该项目使用Flask作为 Web 应用框架。拥抱应用广泛的python语言 。

项目部署采用阿里云`serverless`部署。

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |
| --- |  --- |
| 权限/策略 | AliyunFCFullAccess |

</table>

<codepre id="codepre">

# 代码 & 预览

- [ :smiley_cat:  源代码](https://github.com/tao-xiaoxin/limbo-step/tree/mini)

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-flask) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-flask)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-flask -d start-flask`   
    - 进入项目，并进行项目部署：`cd start-flask && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情


本项目是将 Python Web 框架中，非常受欢迎的 Flask 框架，部署到阿里云 Serverless 平台（函数计算 FC）。

> Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug ，模板引擎则使用 Jinja2 。Flask使用 BSD 授权。

通过 Serverless Devs 开发者工具，您只需要几步，就可以体验 Serverless 架构，带来的降本提效的技术红利。

本案例应用是一个非常简单的 Hello World 案例，部署完成之后，您可以看到系统返回给您的案例地址，例如：

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1644567788251_20220211082308412077.png)

此时，打开案例地址，就可以看到测试的应用详情：

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1644567807662_20220211082327817140.png)



</appdetail>

<devgroup>