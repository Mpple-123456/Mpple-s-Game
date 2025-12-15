import os,string,time,sys
from pathlib import Path
import json
from Shell import Shell
import tkinter as tk
from tkinter import messagebox
#加入依赖库
GAME_VERSION=1.0

os.system("title Mpple's Game")
shell=Shell()

def DeBug(t):
    t=str(t)
    if shell.Look("显示DeBug"):
        print("[DeBug] "+t)

def Error(t):
    t=str(t)
    if shell.Look("显示Error"):
        if shell.Look("使用GUI提示"):
            messagebox.showerror("错误",t)
        else:
            print("[Error] "+t)

def info(t):
    t=str(t)
    if shell.Look("使用GUI提示"):
        messagebox.showinfo("INFO",t)
    else:
        print(t)
        

path=Path('GameMenu.json')

time.sleep(1)
#读取文件
def RUN_COMMAND(COMMAND):
    os.system(COMMAND)
#执行CMD命令

def START_MENU():
    while True:
        try:
            print("Welcome to Mpple's Games")
            print(f"Version:{GAME_VERSION}")
            print("--------Menu-----------")
            for i in range(len(menu)):
                print(f"{i+1}.{menu[i]}")
            if len(menu)==0:
                print("(无)")
            print('--------更多选项-------')
            print(str(len(menu)+1)+'.退出')
            print(str(len(menu)+2)+'.刷新')
            print(str(len(menu)+3)+'.重启')
            print(str(len(menu)+4)+'.睡眠')
            print(str(len(menu)+5)+'.关于')
            print(str(len(menu)+6)+'.修改列表')
            print('--------命令帮助-------')
            print('输入"help"帮助')
            print("-----------------------")
            NUMBER=input("Please Select&Input Command 请选择&输入命令：")
            try:
                NUMBER=int(NUMBER)
            except ValueError:
                shell.Run(NUMBER)
                time.sleep(2)
            else:
                INPUT_NUMBER(NUMBER)
            RUN_COMMAND("cls")
        except KeyboardInterrupt or EOFError:
            print("用户退出。")
            break
#显示&输入

def INPUT_NUMBER(NUM):
    if NUM>len(menu)+6 or NUM<1:
        Error("数字错误！")
        #提示错误

    elif NUM==len(menu)+1:
        print('3秒后退出...')
        for i in range(3):
            print(3-i)
            time.sleep(1)
        RUN_COMMAND('cls')
        sys.exit()
        #退出

    elif NUM==len(menu)+2:
        pass
        #刷新

    elif NUM==len(menu)+3:
        print('3秒后重启...')
        for i in range(3):
            print(3-i)
            time.sleep(1)
        RUN_COMMAND('cls')
        RUN_COMMAND('start Game.py')
        sys.exit()
        #重启

    elif NUM==len(menu)+4:
        print('3秒后睡眠...')
        for i in range(3):
            print(3-i)
            time.sleep(1)
        RUN_COMMAND('cls')
        print('睡眠中...按任意键唤醒。')
        RUN_COMMAND('pause >nul')
        print('启动中...')
        #睡眠

    elif NUM==len(menu)+5:
        RUN_COMMAND('cls')
        info("**Mpple's Game**\n   游戏启动器\n   来自Mpple")
        RUN_COMMAND('pause')
        #关于
    
    elif NUM==len(menu)+6:
        APPEND_OR_RM_GameMenu()
        #修改

    else:
        DeBug(f"用户选择{NUM}")
        START_GAME(NUM)
        #提示&运行

    time.sleep(0.5)
    #休息

#接受输入

def START_GAME(START_NUMBER):
    FILES="GAME_FLIES\\"+str(START_NUMBER)+'\\'+str(START_NUMBER)+'.exe'
    path=Path(FILES)
    if path.exists():
        COMMAND="start "+FILES
        RUN_COMMAND(COMMAND)
        DeBug(f"运行命令：{COMMAND}")
        print("启动游戏需要一些时间，请耐心等待。")
    else:
        Error("找不到"+FILES)
    time.sleep(3)

def Write_Menu():
    path=Path("GameMenu.json")
    c=json.dumps(menu,indent=4)
    path.write_text(c)
    info("生成成功！")

def APPEND_OR_RM_GameMenu():
    print("-----修改GameMenu-----")
    print("1.删除\n2.新增\n3.退出")
    try:
        Num=input("请选择：")
        if Num=='1':
            Name=input("请输入删除的元素名称：")
            menu.remove(Name)
            info("已删除")
        elif Num=='2':
            Name=input("请输入添加的元素名称：")
            menu.append(Name)
        Write_Menu()
    except:
        Error("Error")

root=tk.Tk()
osname=os.name
root.withdraw()

if osname!='nt':
    messagebox.showwarning("Warning!", f"你的系统为{osname}, \n软件需要在Windows中打开！")
    sys.exit()

print("读取游戏文件中...",end='')
if path.exists():
    #如果文件存在
    try:
        c=path.read_text()
        menu=json.loads(c)
        print("成功！\n")
        try:
            START_MENU()
        except Exception as Error:
            Error(f"致命错误！{Error}")
        #文件没有问题，执行主函数

    except json.decoder.JSONDecodeError:
        #文件损坏
        try:
            print("失败！\n")
            print("你好，你的游戏配置文件已损坏。（不准）")
            a=input("如果你要重新写入，请输入 1 +回车：")
            #提示&输入

            if a=='1':
                try:
                    #尝试写入
                    menu=["乒乓球游戏","3D游戏【来自希妈阿Q】","打丧尸","我的世界【素材来自MineBBS论坛】","吃小鱼","火箭大战","迷宫"]
                    Write_Menu()

                except PermissionError:
                    #如果修改失败
                    Error("Error!")
        except:
            sys.exit()
                
else:
    #否则文件不存在
    try:
        print("失败！\n")
        print("你好，你的游戏配置文件好像丢失了。如果有类似文件，请将名字修改成GameMenu。（不准）")
        a=input("如果你要重新写入，请输入 1 +回车：")
        #提示&输入

        if a=='1':
                try:
                    #尝试写入
                    menu=["乒乓球游戏","3D游戏【来自希妈阿Q】","打丧尸","我的世界【素材来自MineBBS论坛】","吃小鱼","火箭大战","迷宫"]
                    Write_Menu()

                except PermissionError:
                    #如果修改失败
                    Error("Error!")
    except:
        sys.exit()

time.sleep(3)
#显示2秒   
