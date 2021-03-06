# Frequently Used Commands 常用命令整理

## Windows 10使用内置照片查看器而不是照片应用
注册表文件内容：
```
Windows Registry Editor Version 5.00
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.jpg] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.jpeg] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.gif] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.png] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.bmp] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.tiff] 
@="PhotoViewer.FileAssoc.Tiff" 
; Change Extension's File Type 
[HKEY_CURRENT_USER\Software\Classes\.ico] 
@="PhotoViewer.FileAssoc.Tiff"
```

## PPPoE断线自动重拨
(来源：https://blog.csdn.net/JackDual/article/details/110866600)

`任务计划程序`中添加任务：

```
- 触发器：当特定事件被记录时
- 日志：应用程序
- 源：RasCient
- 事件ID：20226
- 操作：启动程序rasdial <PPPoE名称> <用户名> <密码>
```

## Windows 7/8.1/10 安装时跳过oobe的方法
(来源：https://www.cnblogs.com/qbj196/p/12585269.html)

1. U盘引导启动，正常步骤安装，自动重启
2. 从硬盘启动，提示`正在准备设备`，自动重启
3. 【注意】U盘引导启动，按Shift + F10调出命令提示符，输入regedit打开注册表
4. 文件>加载配置单元，加载以下文件到注册表【HKEY_USERS】下，项名称同文件名

```
- (系统盘符):\Windows\System32\config\SAM
- (系统盘符):\Windows\System32\config\SOFTWARE
- (系统盘符):\Windows\System32\config\SYSTEM
- (系统盘符):\Users\Default\NTUSER.DAT（Win10，文件是隐藏的，加载的时候在文件名输入框内直接输入整个路径）
```

5. 启用Administrator账户
【HKEY_USERS\SAM\SAM\Domains\Account\Users\000001F4】修改“F”的值中的"11"为"10"（倒数第三行）
6. 
