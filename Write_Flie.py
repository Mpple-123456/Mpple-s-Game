from pathlib import Path
import json
try:
    menu=["乒乓球游戏","3D游戏【来自希妈阿Q】","打丧尸（有Bug）","我的世界【素材来自MineBBS论坛】","吃小鱼","火箭大战","迷宫"]
    path=Path("GameMenu.json")
    c=json.dumps(menu,indent=4)
    path.write_text(c)
    print("生成成功！")
except PermissionError:
    print("Error!")
