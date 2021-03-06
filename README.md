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
4. `文件>加载配置单元`，加载以下文件到注册表【HKEY_USERS】下，项名称同文件名

```
- (系统盘符):\Windows\System32\config\SAM
- (系统盘符):\Windows\System32\config\SOFTWARE
- (系统盘符):\Windows\System32\config\SYSTEM
- (系统盘符):\Users\Default\NTUSER.DAT（Win10，文件是隐藏的，加载的时候在文件名输入框内直接输入整个路径）
```

5. **启用Administrator账户**

```
【HKEY_USERS\SAM\SAM\Domains\Account\Users\000001F4】修改“F”的值中的"11"为"10"（倒数第三行第一个数）
```

6. 不安装系统内置Metro应用，但可以使用应用商店和更改电脑设置（Win8/8.1/10）

```
【HKEY_USERS\SOFTWARE\Microsoft\Windows\CurrentVersion\Appx\AppxAllUserStore\】
删除Applications\，Config\，InboxApplications\，Staged\下的一些子项，只留下图所示的项，不要应用商店的可以把WindowsStore删除：
```
![image](https://user-images.githubusercontent.com/21973955/110205226-d99a2080-7eb1-11eb-9152-ff995b241ab7.png)

7. 禁用操作中心通知（Win7/8/8.1）

```
【HKEY_USERS\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjects\{F56F6FDD-AA9D-4618-A949-C1B91AF43B1A}\】
删除“AutoStart”
```

8. **不跳过"OOBE"（Win8/8.1/10；8/8.1/10跳过OOBE会导致输入法有问题不能使用，这一步可以使安装过程不用做任何选择，直接抵达桌面）**

```
【HKEY_USERS\SOFTWARE\Microsoft\Windows\CurrentVersion\OOBE\Components\】
删除Sections\下的Account子项（Win8/8.1）
删除Plugins\下的所有子项，切勿直接删除Plugins（Win10）
删除Wizard\下的所有子项，切勿直接删除Wizard（Win10）
```

9. 跳过“你好”动画（Win8/8.1/10）

```
【HKEY_USERS\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\】
EnableFirstLogonAnimation = 0
```

10. 修改计算机名

```
【HKEY_USERS\SYSTEM\ControlSet001\Control\ComputerName\ComputerName\】
ComputerName = X
【HKEY_USERS\SYSTEM\ControlSet001\Services\Tcpip\Parameters\】
Hostname = X
NV Hostname = X
```

11. 禁用某些服务启动

```
【HKEY_USERS\SYSTEM\ControlSet001\Services\】
BITS\，CscService\，DPS\，iphlpsvc\，PcaSvc\，Spooler\，SysMain\，WerSvc\，WinDefend\，wscsvc\，WSearch\，wuauserv\（Win7/8/8.1/10）
DiagTrack\，dmwappushservice\，MapsBroker\（Win10）
Start = 4
```

12. **跳过"OOBE"（Win7）**

```
【HKEY_USERS\SYSTEM\Setup\】
CmdLine =
OOBEInProgress = 0
SetupPhase = 0
SetupType = 0
```

13. 防止OneDrive自动安装（Win10）

```
【HKEY_USERS\NTUSER.DAT\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\】
删除“OneDriveSetup”
```

14. `文件>卸载配置单元`，重启后就能直接进入桌面或开始屏幕
