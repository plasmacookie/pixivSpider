# 用于获取页面资源
from requests.adapters import HTTPAdapter
import requests

cookie = '从控制台复制的cookie'
user_agent = '从控制台复制的user-agent'


class HTMLDownloader():

    def get_resource(url, headers):
        if url == '' or url is None:
            return
        s = requests.Session()
        s.keep_alive = False
        s.mount('http://', HTTPAdapter(max_retries=5))
        s.mount('https://', HTTPAdapter(max_retries=5))
        resource = s.get(url=url, headers=headers)
        return resource

    def get_html(url):
        # 获取html源码
        headers = {
            'user-agent': user_agent,
            'cookie': cookie
        }
        resource = HTMLDownloader.get_resource(url, headers)
        return resource.text

    def get_content(id, url):
        # 获取二进制数据
        headers = {
            'referer': 'https://www.pixiv.net/artworks/'+id,
            'user-agent': user_agent,
            'cookie': cookie
        }
        resource = HTMLDownloader.get_resource(url, headers)
        return resource.content
