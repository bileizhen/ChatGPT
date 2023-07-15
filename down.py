import os
import sys
import time
import requests
from tqdm import tqdm

print("=======================================")
print("   _     _     _                     ")
print("  | |__ (_) __| | _____      ___ __  ")
print("  | '_ \| |/ _` |/ _ \ \ /\ / / '_ \ ")
print("  | |_) | | (_| | (_) \ V  V /| | | |")
print("  |_.__/|_|\__,_|\___/ \_/\_/ |_| |_|")
print("")
print("=======================================")
print("  bidown  v2.6           by bileizhen")
print("请选择功能")
print(" [1]  下载")
print(" [2]  作者")
print(" [3]  更新")
print(" [4]  退出")
print("══════════")
print("┌─[bidown]─[作者：bileizhen]")
choice = input("└──╼ ❯❯❯选择功能：")

if choice == "1":
    print("▣━━━━下载━━━━▣")
    print("┌─[bidown]─[作者：bileizhen]")
    url = input("└──╼ ❯❯❯下载链接：")
    filename = os.path.basename(url)
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open('/storage/emulated/0/' + filename, 'wb') as file:  # 指定完整的文件路径
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print("下载失败！")
    else:
        print("下载成功！")
        print("文件保存至：", '/storage/emulated/0/' + filename)  # 显示完整的文件路径

elif choice == "2":
    print("▣━━━━作者━━━━▣")
    print("作者：bileizhen")
    print("QQ：3140014249")
    print("版本：v0.1")
    print("Q群：698699383")

elif choice == "3":
        print("▣━━━━更新━━━━▣")
        url = "https://raw.githubusercontent.com/bileizhen/bidown/main/down.py"
        response = requests.get(url)
        new_script = response.text

        with open(__file__, 'w') as file:
            file.write(new_script)

        print("脚本已更新，重启脚本以更新！")
        time.sleep(1)
        sys.exit()

elif choice == "4":
        sys.exit()
    
else:
    print("无效的选择！")
    time.sleep(1)
