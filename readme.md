# 说明
pixiv爬虫，爬取pixiv的插画作品  
三种爬取方式：
1. 通过输入的搜索内容和限制级别，下载收藏人数大于输入数值的插画作品
2. 输入画师的用户id，下载画师的全部插画作品
3. 输入插画作品id，下载该作品。（主要用于下载动图）

# 运行环境
已测试:  
windows10, python3.7  
ubuntu, python3.10  
termux, python3.10

# 使用方法
1. 安装python
2. 安装 bs4, requests, imageio 三个python库
3. 下载本项目代码
4. 浏览器登录pixiv后复制cookie和ua粘贴到HTMLDownloader.py中
5. 在SpiderMain.py中修改下载图片的默认路径
6. python SpiderMain.py 运行程序
7. 若遇到下载问题，请尝试将pixiv账号的r18与r18g开关打开

# bug修复
## 22.1.23
修复因网络问题出现的下载图片残缺问题