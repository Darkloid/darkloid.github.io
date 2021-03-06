# Frequently Used Commands 常用命令整理

## 1. Windows 10使用内置照片查看器而不是照片应用
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

## 2. PPPoE断线自动重拨
(来源：https://blog.csdn.net/JackDual/article/details/110866600)

`任务计划程序`中添加任务：

```
- 触发器：当特定事件被记录时
- 日志：应用程序
- 源：RasCient
- 事件ID：20226
- 操作：启动程序rasdial <PPPoE名称> <用户名> <密码>
```

## 3. Windows 7/8.1/10 安装时跳过oobe的方法（重点项打"√"）
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
5. 启用Administrator账户（√）
```
【HKEY_USERS\SAM\SAM\Domains\Account\Users\000001F4】
修改“F”的值中的"11"为"10"（倒数第三行第一个数）
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
8. 不跳过"OOBE"（Win8/8.1/10；8/8.1/10跳过OOBE会导致输入法有问题不能使用，这一步可以使安装过程不用做任何选择，直接抵达桌面）（√）
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
12. 跳过"OOBE"（Win7）（√）
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


## 4. 隐藏库、回收站、家庭组、网络、视频、图片、文档、下载、音乐、桌面（未试验）
(来源：https://www.cnblogs.com/qbj196/p/12591745.html)

```
:================================================================(32/64位系统)================================================================
:先备份
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace C:\MyComputerNameSpace.reg
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions C:\FolderDescriptions.reg

:只隐藏导航窗格中的
:(Win7/8/8.1/10)库、回收站、家庭组、网络
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{031E4825-7B94-4dc3-B131-E946B44C8DD5} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{645FF040-5081-101B-9F08-00AA002F954E} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{A302545D-DEFF-464b-ABE8-61C8648D939B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{52528A6B-B9E3-4add-B60D-588C2DBA842D} /f

:只隐藏导航窗格中这台电脑/此电脑的：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{A0953C92-50DC-43bf-BE83-3742FED03C9C} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{374DE290-123F-4565-9164-39C4925E467B} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{1CF1260C-4DD0-4ebb-811F-33C572699FDE} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{24ad3ad4-a569-4530-98e1-ab02f9417aa8} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{d3162b92-9365-467a-956b-92703aca08af} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{088e3905-0323-4b02-9826-5d99428e115f} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\CLSID\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f

:隐藏导航窗格中这台电脑/此电脑和右侧文件夹下的：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641} /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de} /f

:显示导航窗格中收藏夹/快速访问的真实路径：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{18989B1D-99B5-455B-841C-AB7C74E4DDFC} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{33E28130-4E1E-4676-835A-98395C3BC3BB} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{FDD39AD0-238F-46AF-ADB4-6C85480369C7} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{374DE290-123F-4565-9164-39C4925E467B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{4BD8D571-6D19-48D3-BE97-422220080E43} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{754AC886-DF64-4CBA-86B5-F7FBF4FBCEF5} /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d} /f


:=======================================================================(64位系统)========================================================================
:先备份
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace C:\Wow6432NodeMyComputerNameSpace.reg
reg export HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions C:\Wow6432NodeFolderDescriptions.reg

:只隐藏导航窗格中的
:(Win7/8/8.1/10)库、回收站、家庭组、网络
reg add HKEY_CURRENT_USER\Software\Classes\Wow6432Node\CLSID\{031E4825-7B94-4dc3-B131-E946B44C8DD5} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\Wow6432Node\CLSID\{645FF040-5081-101B-9F08-00AA002F954E} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\Software\Classes\Wow6432Node\CLSID\{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\Software\Classes\Wow6432Node\CLSID\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{A302545D-DEFF-464b-ABE8-61C8648D939B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{52528A6B-B9E3-4add-B60D-588C2DBA842D} /f

:只隐藏导航窗格中这台电脑/此电脑的：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{A0953C92-50DC-43bf-BE83-3742FED03C9C} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{374DE290-123F-4565-9164-39C4925E467B} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{1CF1260C-4DD0-4ebb-811F-33C572699FDE} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{24ad3ad4-a569-4530-98e1-ab02f9417aa8} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{d3162b92-9365-467a-956b-92703aca08af} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{088e3905-0323-4b02-9826-5d99428e115f} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f
reg add HKEY_CURRENT_USER\SOFTWARE\Classes\Wow6432Node\CLSID\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de} /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0 /f

:隐藏导航窗格中这台电脑/此电脑和右侧文件夹下的：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A0953C92-50DC-43bf-BE83-3742FED03C9C} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{374DE290-123F-4565-9164-39C4925E467B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{1CF1260C-4DD0-4ebb-811F-33C572699FDE} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641} /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de} /f

:显示导航窗格中收藏夹/快速访问的真实路径：
:(Win8.1/10)视频、图片、文档、下载、音乐、桌面
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{18989B1D-99B5-455B-841C-AB7C74E4DDFC} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{33E28130-4E1E-4676-835A-98395C3BC3BB} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{FDD39AD0-238F-46AF-ADB4-6C85480369C7} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{374DE290-123F-4565-9164-39C4925E467B} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{4BD8D571-6D19-48D3-BE97-422220080E43} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{754AC886-DF64-4CBA-86B5-F7FBF4FBCEF5} /f
:(Win10)公用视频、公用图片、公用文档、公用下载、公用音乐
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4} /f
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d} /f
```
