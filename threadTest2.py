import threading, requests, time

def getHtml(url):
    resp = request.get(url)
    time.sleep(1)
    print(url, len(resp, text), ' chars')

t = threading.Thread(target=getHtml, args=())