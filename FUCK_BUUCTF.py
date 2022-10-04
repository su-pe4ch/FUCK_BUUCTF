import time
import requests


def fuck_buu(session: requests.Session, method, url, **kwargs): #kwargs代表其他参数
    if method == 'GET':
        resp = session.get(url, **kwargs)
    elif method == 'POST':
        resp = session.post(url, **kwargs)

    # 如果 429 了会等待几秒，然后继续调用 fuck_buu 返回 resp
    if resp.status_code == 429:
        time.sleep(3)
        resp = fuck_buu(session, method, url, **kwargs)
    return resp


# 使用方法
url = ''
session = requests.Session()
fuck_buu(session, method=, url)
