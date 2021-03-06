# Frequently Used Commands

## 1. Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Darkloid/darkloid.github.io/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## 2. PPPoE断线自动重拨(2021/3/6)
```任务计划程序```中添加任务：
```- 触发器：当特定事件被记录时
- 日志：应用程序
- 源：RasCient
- 事件ID：20226
- 操作：启动程序rasdial <PPPoE名称> <用户名> <密码>
```
