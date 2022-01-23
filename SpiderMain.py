from HTMLParser import HTMLParser
from DataOutPut import DataOutPut
from Search import User
from Search import Tags
import MultiThreadDownload
# 默认下载路径，可修改
file_path = 'E:/img_download/'
print('1.输入搜索内容，下载收藏人数大于输入值的所有图片')
print('2.输入画师id，下载画师的所有插画作品')
print('3.输入作品id，下载作品')
print('选择您的下载方式')
i = input()
if i == '1':
    # 通过数据构造目录
    tag = input('输入搜索内容: ')
    mode = input('输入要搜索的限制级 r18 safe all: ')
    min_count = input('输入您觉得合适的收藏数: ')
    d = DataOutPut()
    path = file_path+'t_'+tag+'_'+mode+'/'
    d.mkdir(path)
    # 下载
    print('正在搜索ing...')
    tags = Tags(tag, mode)
    illust_ids = list(tags.get_illust_ids())
    print('正在下载ing...')
    MultiThreadDownload.multi_download(illust_ids, min_count, path)
    print('下载结束啦')
elif i == '2':
    # 通过输入构造目录
    user_id = input('输入画师id: ')
    d = DataOutPut()
    path = file_path+'u_'+user_id+'/'
    d.mkdir(path)
    # 下载
    print('正在搜索ing...')
    user = User(user_id)
    illust_ids = list(user.get_illust_ids())
    print('正在下载ing...')
    MultiThreadDownload.multi_download(illust_ids, 0, path)
    print('下载结束啦')
elif i == '3':
    # 通过输入构造目录
    illust = input('输入作品id: ')
    d = DataOutPut()
    path = file_path+'i_'+illust+'/'
    d.mkdir(path)
    # 下载
    print('正在搜索ing...')
    h = HTMLParser()
    resource = h.get_resource(illust)
    print('正在下载ing...')
    d.download_img(resource, 0, path)
    print('下载结束啦')
