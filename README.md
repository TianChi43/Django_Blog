# 做一个个人博客
**项目采用python3.7+django3.2+mysql编写**


主要实现的功能有：<br>
* 添加markdown编辑器实现编写文章
* 使用bootstrap4编写模板文件
* 采用前后端不分离的方式
* 使用layer组件实现弹窗
* 添加了防csrf攻击的相关代码
* 完成文章的增删（11.12）
* 完成文章的改查（11.13）
* 完成用户的登录与登出（11.14）
* 完成用户的注册和删除（11.16）
* 未完成用户的重置密码（https://juejin.cn/post/6844903704181604359）

<br>

### CSRF攻击:
  CSRF攻击你可以理解为：攻击者盗用了你的身份，以你的名义发送恶意请求。还是拿删除文章举例：用户登录了博客网站A，浏览器记录下这次会话，并保持了登录状态；用户在没有退出登录的情况下，又非常不小心的打开了邪恶的攻击网站B；攻击网站B在页面中植入恶意代码，悄无声息的向博客网站A发送删除文章的请求，此时浏览器误以为是用户在操作，从而顺利的执行了删除操作。
<br>

![{86A887F5-3D09-48EF-8494-566B41DF49B2}](https://github.com/user-attachments/assets/fede6b84-dce0-43ff-9a13-d0cb086f8706)



学习自杜塞老师的相关文章
https://juejin.cn/user/1591748567503079/posts<br>
看到了一篇较好的博客入门合集也是用django写的https://www.zmrenwu.com/tutorials/hellodjango-blog-tutorial/
