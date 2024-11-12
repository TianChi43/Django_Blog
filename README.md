# 做一个个人博客
**项目采用python3.7+django3.2+mysql编写**


主要实现的功能有：<br>
* 添加markdown编辑器实现编写文章
* 使用bootstrap4编写模板文件
* 采用前后端不分离的方式
* 使用layer组件实现弹窗
* 完成文章的增删（11.12）

<br>

### CSRF攻击:
  CSRF攻击你可以理解为：攻击者盗用了你的身份，以你的名义发送恶意请求。还是拿删除文章举例：用户登录了博客网站A，浏览器记录下这次会话，并保持了登录状态；用户在没有退出登录的情况下，又非常不小心的打开了邪恶的攻击网站B；攻击网站B在页面中植入恶意代码，悄无声息的向博客网站A发送删除文章的请求，此时浏览器误以为是用户在操作，从而顺利的执行了删除操作。
<br>
学习自杜塞老师的相关文章
https://juejin.cn/user/1591748567503079/posts
