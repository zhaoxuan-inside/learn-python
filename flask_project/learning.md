# Flash
> **Web 开发的两种常见模式**
> 1. 请求-响应模式
> 2. Post/Redirect/Get(PRG)模式

- 请求-响应模式
> 后端直接将结果返回给前端;但是这样会在一些情况下有问题,用户正常登陆后,刷新页面,会重新提交Post请求,重复提交表单;

- Post/Redirect/Get模式
> 前端 `POST` 请求后端,后端重定向到另一个 `GET` 请求,这样即使用户刷新也页面也不会有重复提交表单的问题;

> 💫 重定向会启动一个全新的请求,原来的请求上下文全部会丢失.

`flash` 将消息临时存放在 `session` 中,重定向后新的请求可以从 `session` 获取到消息,然后自动清除,这样既能通过 `PRG` 避免重复提交问题,又能优雅的传递一次性反馈.

# Session, Cookie与JWT
- Session,会话数据,分为客户端和服务端
  - 客户端Session存储在Cookie或者LocalStorage
  - 服务端Session存储在Redis或者数据库中
- Cookie,是载体用来承载数据
- JWT,数据编码方式