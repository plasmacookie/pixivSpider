# 多线程下载图片
import threading
from threading import Thread
from HTMLParser import HTMLParser
from DataOutPut import DataOutPut
import math

count = 0
glob_lock = threading.Lock()


def download(illust_ids, min_count, file_path, id_count):
    global count
    # 下载id列表中的所有图片
    h = HTMLParser()
    d = DataOutPut()
    for illust in illust_ids:
        resource = h.get_resource(illust)
        d.download_img(resource, min_count, file_path)
        glob_lock.acquire()
        count += 1
        num = round(count/id_count*100, 2)
        print('\r下载进度:'+str(num)+'/100', end="")
        glob_lock.release()



def multi_download(illust_ids, min_count, file_path):
    # 多线程下载图片
    # 默认线程总数
    t_count = 128
    # id总数
    id_count = len(illust_ids)
    # 设置线程数
    if id_count < t_count:
        thread_count = id_count
    else:
        thread_count = t_count

    # 每个线程要分配的id数量
    d = math.ceil(id_count/thread_count)
    # 声明线程列表
    threads = []
    for i in range(thread_count - 1):
        t = Thread(target=download, args=(illust_ids[i*d:(i+1)*d], min_count, file_path, id_count))
        threads.append(t)
        t.start()
    t = Thread(target=download, args=(illust_ids[(thread_count-1)*d:id_count], min_count, file_path, id_count))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
