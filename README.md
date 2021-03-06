# Frequently Used Commands 常用命令整理

## Windows 10使用内置照片查看器而不是照片应用
注册表文件如下：
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

```任务计划程序```中添加任务：
```- 触发器：当特定事件被记录时
- 日志：应用程序
- 源：RasCient
- 事件ID：20226
- 操作：启动程序rasdial <PPPoE名称> <用户名> <密码>
```
