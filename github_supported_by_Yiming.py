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
                # 这里如果报错GBK的话，应指定编码
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
                    time.sleep(2)
                    return
                except Exception as e:
                    print(f"ERROR: {e}")
                    time.sleep(2)
                    return
        time.sleep(10)

if __name__ == "__main__":
    print("""
    Make sure to run as an administrator
    The hosts file will be updated every 10 seconds
    This doesn't change anything else

    Welcome to the Yiming API: https://api.wer.plus
    Github: https://github.com/HG-ha/github_access
    """)
    try:
        run()
    except Exception as e:
        print(f"ERROR: {e}")
        time.sleep(2)
    except KeyboardInterrupt:
        print("Goodbye!")
        time.sleep(2)
