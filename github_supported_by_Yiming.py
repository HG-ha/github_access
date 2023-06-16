# coding : utf-8
"""
作者：Yiming
创建时间：2023/6/16 14:25
GitHub 主页：https://github.com/HG-ha
个人网站：https://api.wer.plus

一铭API是一个免费提供大量实用接口的API网站

如果您在使用程序的过程中发现了任何问题或有任何建议，请随时联系作者。
"""
import requests
import time

def run():
    while True:
        url = "http://api.wer.plus/api/getgithub"
        req = requests.get(url)
        if req.status_code == 200:
            if (dat := req.json())["code"] == 200:
                host = dat["avadd"][0]["addr"]

                # hosts 文件路径（Windows 系统下路径为 C:\Windows\System32\drivers\etc\hosts）
                hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

                # 读取 hosts 文件内容
                with open(hosts_path, 'r') as f:
                    content = f.readlines()
                
                for i in content:
                    if "github.com" in i:
                        content.pop(content.index(i))
                content.append(f"{host}    github.com")
                # 将更新后的内容写入 hosts 文件
                try:
                    with open(hosts_path, 'w') as f:
                        f.write("".join(content))
                except PermissionError:
                    print("ERROR: Please run as administrator")
                    return
                except Exception as e:
                    print(f"ERROR: {e}")
                    return
        time.sleep(10)

if __name__ == "__main__":
    print("""
    Make sure to run as an administrator
    The hosts file will be updated every 10 seconds
    This doesn't change anything else

    Welcome to the Yiming API: https://api.wer.plus
    """)
    try:
        run()
    except Exception as e:
        print(f"ERROR: {e}")