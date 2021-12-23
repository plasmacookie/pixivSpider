# 说明
pixiv爬虫，爬取pixiv的插画作品  
三种爬取方式：
1. 通过输入的搜索内容和限制级别，下载收藏人数大于输入数值的插画作品
2. 输入画师的用户id，下载画师的全部插画作品
3. 输入作品id，下载该作品。（主要用于下载动图）

# 运行环境
windows10, python3.7  
已测试，可在该环境下运行

# 使用方法
1. 安装python
2. 下载本项目代码
3. 浏览器登录pixiv后复制cookie和ua粘贴到HTMLDownloader.py中
4. 双击start.bat开始运行
5. 可在SpiderMain.py文件中修改默认下载路径