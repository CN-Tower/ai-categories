import sys, os
import urllib
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
import json
from multiprocessing import Process
import requests

class BaiDuMusic():
    def __init__(self):
        pass

    top = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Host':'music.baidu.com'
    }
    def search(self, songName):
        firstUrl = "http://music.baidu.com/search?key=" + parse.quote(str(songName))
        userAgent = " User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 "
        headers = {'User-Agent': userAgent}
        requst = urllib.request.Request(firstUrl, headers=headers)
        result = urllib.request.urlopen(requst).read()

        # 使用BeautifulSoup快速解析html文档
        soup = BeautifulSoup(result, from_encoding="utf-8")
        res_arr = []
        try:
            tmpjson = soup.find_all("li", {"class": "bb-dotimg clearfix song-item-hook "})
            for x in tmpjson:
                tmpobj = json.loads(x['data-songitem'])
                value = (tmpobj['songItem']['oid'] + "+++" +tmpobj['songItem']['author']+ "+++" + tmpobj['songItem']['sname'])[4:-5]
                res_arr.append(value)
            return res_arr
        except Exception as e:
            print(u"抱歉没有找到相关资源".encode("utf-8"))
            return 0

    def download(self, songid, songName, savePath="down/"):
        songNewUrl = "http://music.baidu.com/data/music/file?link=&song_id=" + str(songid)
        print(songNewUrl)
        if not os.path.isdir(savePath):
            os.makedirs(savePath)
        savemp3 = savePath + songName + ".mp3"
        with open(savemp3, 'wb') as handle:
            response = requests.get(songNewUrl, stream=True, headers=self.top)
            print(response.status_code)
            # 文件流写入, 使用1024的模式提取数据
            for block in response.iter_content(1024):
                # 数据提取完成
                if not block:
                    break
                handle.write(block)  # 写入文件
    # urllib.request.urlretrieve(songNewUrl, savemp3)


if __name__ == '__main__':
    bMusic = BaiDuMusic()
    res = bMusic.search(u"冰雨")
    # for x in res:     
    # print x
    # 1128053+++刘德华+++冰雨    
    # 7327899+++李翊君+++冰雨    
    # 53535187+++张恒+++冰雨    
    Process(target=bMusic.download, args=(1128053, "刘德华-冰雨")).start()
    Process(target=bMusic.download, args=(7327899, "李翊君-冰雨")).start()
    Process(target=bMusic.download, args=(53535187, "张恒-冰雨")).start()