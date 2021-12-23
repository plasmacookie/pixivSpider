from HTMLDownloader import HTMLDownloader
from bs4 import BeautifulSoup
import json


class HTMLParser(object):

    def get_html(self, id):
        # 构造作品链接
        url = 'https://www.pixiv.net/artworks/'+str(id)
        # 获取链接源码
        h = HTMLDownloader.get_html(url)
        return h

    def is_ugoira(self, h):
        # 判断是否是动图，是返回True，否则返回False
        if 'ugoira' in h:
            return True
        else:
            return False

    def get_resource(self, id):
        # 获取是否是动图、收藏数、总页数和原图
        # 通过作品id获取页面源码
        h = self.get_html(id)
        # 使用BeautifulSoup获取页面元素
        soup = BeautifulSoup(h, 'html.parser')
        metas = soup.find_all('meta')
        for meta in metas:
            if meta.get('name') == 'preload-data':
                s = meta.get('content')
        j = json.loads(s)
        data = j['illust'][str(id)]
        return id, self.is_ugoira(h), data['bookmarkCount'], data['pageCount'], data['urls']['original']

    def get_ugoira_resource(self, id):
        # 获取动图的压缩包链接和帧延迟时间
        url = 'https://www.pixiv.net/ajax/illust/' + str(id) + '/ugoira_meta?lang=zh'
        h = HTMLDownloader.get_html(url)
        j = json.loads(h)
        body = j['body']
        return body['originalSrc'], body['frames']
