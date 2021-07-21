# 验证程序制作器

## 介绍

该程序基于Python，可以将一个给定的程序“加密”，输入密码后才能运行（见程序界面）

## 程序界面

![开始运行时](https://i.bmp.ovh/imgs/2021/07/b4b931b970daecb6.png)

![第一阶段结束](https://i.bmp.ovh/imgs/2021/07/1f5143128d97c552.png)

## 使用方法

### 准备：

python3运行环境（必需）

pyinstaller（必需，若没有，请到终端中输入以下命令）：

```powershell
pip install pyinstaller
```

PySimpleGui（运行Py文件时要用到，非必需，若没有，请到终端中输入以下命令）：

```powershell
pip install PySimpleGui
```

### 开始：

从本仓库下载所有文件，并将它们复制到需要上锁的程序的根目录中

运行`setup.exe` (或`setup.py`)，你将会看到：

![第一阶段开始](https://i.bmp.ovh/imgs/2021/07/b4b931b970daecb6.png)

在第一个输入框中输入即将被上锁的程序名（包括.后缀名）（例：making.exe）

在第二个输入框输入你想要设置的密码（目前仅支持纯数字）（例：123456）

点击提交按钮，这时候程序会弹出一个窗口：

![第一阶段结束](https://i.bmp.ovh/imgs/2021/07/1f5143128d97c552.png)

这时候`start.py`已经创建完毕，并且存放在程序的根目录中，运行`execreat.bat`来将其打包成exe文件：

（因为由程序自动运行的pyinstaller打包后的程序存在问题，只能由用户手动运行bat文件）

![第二部分开始](https://i.bmp.ovh/imgs/2021/07/f41e07a2ef9a6e29.png)

打包完成后，cmd会自动删除临时文件，并且会在根目录存放start.exe（大小为10MB左右），运行start.exe，可以看到：

![](https://i.bmp.ovh/imgs/2021/07/df825e28ae48d8aa.png)

输入密码并按下提交按钮后，若你的密码正确，则该程序会将被上锁的程序开启（原被上锁的程序没有被删除，仍可用，请手动将被上锁的程序的属性设置为隐藏或改个名）

### 使用例：

#### 背景：

沐沐不想要她的家长，同学等点击桌面上的一个名为“`与你相恋的恋爱Recette`”的Galgame并发现她是一个xx的人，于是沐沐就下载此程序来不让她的家长，同学点击此程序

#### 过程：

沐沐已经提前准备好了运行环境，她从本页面下载程序包后，沐沐右键桌面上的“与你相恋的恋爱Recette”的快捷方式，点击“打开文件所在的位置”，将程序包复制到这里，双击`setup.exe`，在第一个输入框中输入“与你相恋的恋爱Recette”主程序名（汉化版本）：`recette_chs.exe` 在第二个输入框中输入自己容易想得到的密码：`2873464090`.点击提交，等待start.py导出完成

start.py导出完成后，沐沐运行`execreat.bat`来将`start.py`打包成`start.exe`，cmd自动关闭后，她右键桌面上的“与你相恋的恋爱Recette”的快捷方式。点击属性，将目标改成了...\start.exe。她有强迫症，也一并将这个快捷方式的图标改了，改成了原来的样子

沐沐担心游戏会被卸载，于是也将uninstall.exe用同样的方法上了锁，并将原uninstall.exe改名为uninstallbak.exe，上锁中的start.exe改名为uninstall.exe，这样只有输入密码后或者找到真正的卸载程序才能卸载此程序了。

注：你也可以改快捷方式的图标和名字改成计算器等，这样你的父母也不容易发现

## 后话：

本程序遵守Apache License 2.0协议。未经允许不可转载。