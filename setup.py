# -*- coding:utf-8 -*-
#By WhitemuTeam(github)
#若要使用此程序，请预先构建好Python环境，PySimpleGUI, Pyinstaller库

#导入库
import PySimpleGUI as sg
import os

print('请不要关闭此窗口')

#构建setup窗口
layout = [[sg.Text('请将此程序放在即将被上锁的程序的根目录中，然后输入该程序的名字（+.后缀名[通常是‘.exe’]）')],
          [sg.Input()],
          [sg.Text('请输入你想要设置的密码')],
          [sg.Input()],
          [sg.Button('提交',key='submit')]]

window = sg.Window('验证程序生成器', layout, icon=r'LOGO.ico') #设置窗口
event, value = window.Read() #读取输入值

#获取exe, keyword值
exe = value[0]
keyword = value[1]

#创建start.py
print('开始打印start.py')
py=open('start.py','w', encoding='utf-8')

#打印start.py
print('# -*- coding : utf-8-*-',file=py)
print('import PySimpleGUI as sg', file=py)
print('import os', file=py)
print('', file=py)
print('exe="',exe,'"', file=py)
print('keyword=',keyword, file=py)
print('', file=py)
print('layout = [[sg.Text("输入密码来继续使用此程序")],', file=py)
print('          [sg.Input(password_char="*")],', file=py)
print('          [sg.Button("提交", key="submit")]]', file=py)
print('', file=py)
print('window = sg.Window("安全验证", layout, icon=r"LOGO.ico")', file=py)
print('event, value = window.Read()', file=py)
print('', file=py)
print('if event == "submit":', file=py)
print('		s = value[0]', file=py)
print('		if str(s)==str(',keyword,"):", file=py)
print('			sg.popup("密码正确，将打开此程序", icon=r"LOGO.ico")', file=py)
print('			os.system(exe)', file=py)
print('		else:', file=py)
print('			sg.popup("密码错误，程序不会开启")', file=py)
print('', file=py)
print('window.close()', file=py)

#start.py文件打印结束
py.close()
print('start.py打印成功')

#弹出窗口
sg.Popup('制作完成，请运行execreat.bat来创建exe文件')

#-End-