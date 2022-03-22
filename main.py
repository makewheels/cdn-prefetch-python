import requests


# 看是否可以执行
def can_run():
    return True


def get_base_url(url):
    return url[0:url.rfind('/') + 1]


# 下载单个m3u8文件
def download_m3u8(m3u8Url):
    print('开始下载m3u8：')
    print(m3u8Url)
    base_url = get_base_url(m3u8Url)
    m3u8 = str(requests.get(m3u8Url).content, 'utf-8')
    m3u8Arr = m3u8.split('\n')
    for line in m3u8Arr:
        if line.startswith('#') or line == '':
            continue
        url = base_url + line
        print(url)
        requests.get(url)


# 程序从这里开始
def run():
    if not can_run():
        return
    # 先获取m3u8列表
    print('获取m3u8列表')
    m3u8List = str(requests.get('https://video-2022-dev.cdn.bcebos.com/mlst.txt').content, 'utf-8')
    # 按照每行一个分割
    m3u8Arr = m3u8List.split('\n')
    print('已获取，总数：', end='')
    print(len(m3u8Arr))
    for m3u8Url in m3u8Arr:
        download_m3u8(m3u8Url)


if __name__ == '__main__':
    run()
