import json,tkinter as tk
from pathlib import Path
from tkinter import messagebox

class Shell:
    def __init__(self, text=""):
        text = str(text)
        root=tk.Tk()
        root.withdraw()
    
    def read(self):
        path = Path("SetList.json")
        if path.exists():
            c = path.read_text()
            settings = json.loads(c)
        else:
            settings = {"显示DeBug": True, "显示Error": True, "使用GUI提示":True}
        try:
                path=Path("SetList.json")
                c=json.dumps(settings,indent=4)
                path.write_text(c)
        except PermissionError:
            print("Error!")
        return settings
    
    def Run(self, text):
        if text == "setlist":
            settings = self.read()
            keys = list(settings.keys())
        
            for i in range(len(settings)):
                print(f"{i+1}. {keys[i]}: {settings[keys[i]]}")
        
            try:
                a = int(input("请输入编号以修改设置："))
                a -= 1
            
                if 0 <= a < len(settings):
                    key_to_modify = keys[a]
                    settings[key_to_modify] = not(settings[key_to_modify])
                    if settings["使用GUI提示"]:
                        messagebox.showinfo("INFO",f"已将 {key_to_modify} 修改为: {settings[key_to_modify]}")
                    else:
                        print(f"已将 {key_to_modify} 修改为: {settings[key_to_modify]}")
                else:
                    print("编号无效")
                    return False
                
            except ValueError:
                print("请输入有效的数字")
                return False
            path=Path("SetList.json")
            c=json.dumps(settings,indent=4)
            try:
                path.write_text(c)
            except PermissionError:
                print("Error!")
            return False
        elif text == 'help':
            print("命令&作用\nsetlist 设置选项\nhelp 帮助\nexit 退出Shell")
        elif text == "exit":
            import sys
            sys.exit()
        else:
            print(f'"{text}"不是一个命令，请检查文本是否有错。')
            return True
    
    def Look(self, Num):
        settings = self.read()
        return settings[Num]

if __name__=='__main__':
    shell=Shell()
    print("Welcome to Shell!")
    while True:
        try:
            shell.Run(input("$ "))
        except:
            break
