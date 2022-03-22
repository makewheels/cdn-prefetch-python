import requests


# 看是否可以执行
def can_run():
    return True


def run():
    if can_run() == False:
        return
    # 先获取m3u8列表
    print('')
    content = requests.get("https://www.baidu.com").content


if __name__ == '__main__':
    run()
