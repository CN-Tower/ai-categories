# -*- coding: utf-8 -*-
import urllib
import os
import re
import requests
import json
from bs4 import BeautifulSoup
URL = 'http://music.163.com'
NUM = 5
def download(url, user_agent='wswp', num_try=2):

    headers = {'User_agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Download error', e.reason)
        html = None
        if num_try > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_try - 1)
    return html.decode('utf-8')


#获取标签分类
def get_tag_list(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(name='a', attrs={'class': 'tag-item '})
    list = []
    for each in results:
        ee = each.get('href')
        list.append('http://music.baidu.com'+ee)
    return list

# 访问列表详细信息
def get_song_list(url):
    html = download(url)
    soup = BeautifulSoup(html, "html.parser")
    span_list = soup.find_all(name='span', attrs={'class': 'song-title'})
    for item in span_list:
        a_item= item.find(name='a').get('href')
        print(a_item)



#得到歌手
def get_song_singer(url):
    html = download(url)
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(name='a', attrs={'class': 'tag-item '})
    mess = str(results[0])
    tt = len('<textarea style="display:none;">')
    result = mess[tt:]
    tt = len('</textarea>)')-1
    resu = result[:-tt]
    list = json.loads(resu, encoding="utf-8")
    singer_list = []
    for each in list:
        singer_list.append(each["artists"][0]["name"])
    return singer_list

#下载音乐
def download_music(url, song_name,format_type):
    print("Downloading song_name:" + song_name)
    path = "songs"
    if not os.path.isdir(path):
        os.mkdir(path)
    music_file=path + '/' + song_name + '.'+format_type
    f = open(music_file, 'wb')
    f.write(download(url))
    f.close()
    return music_file
#下载歌曲
def download_song(song_name,singer):
    url = "http://sug.music.baidu.com/info/suggestion"
    #百度音乐搜索获得songid
    mess = song_name + singer
    payload = {'word': mess, 'version': '2.1.1', 'from': '0'}
    r = requests.get(url, params=payload)
    contents = r.text
    d = json.loads(contents, encoding="utf-8")
    #print d
    if ('data' not in d):
        print("do not have flac")
        return 0
    if ('song' not in d["data"]):
        print("do not have flac")
        return 0
    song_id = d["data"]["song"][0]["songid"]

    print("song_id:"+song_id)

    url = "http://music.baidu.com/data/music/fmlink" #百度音乐免费api接口
    '''
        http://music.baidu.com/data/music/fmlink?rate=320&songIds=242078437&type=&callback=cb_download&_t=1468380564513&format=json
    '''
    payload = {'songIds': song_id, 'type': 'mp3'}
    r = requests.get(url, params=payload)
    contents = r.text
    try:
        d = json.loads(contents, encoding="utf-8")
    except:
        return 0
    if d is not None and 'data' not in d or d['data'] == '':
        return 0
    f=open('json_files/'+song_id+'.json','w')
    f.write(d)
    f.close()
    songlink = d["data"]["songList"][0]["songLink"]
    if (len(songlink) < 10):
        print("do not have flac")
        return 0
    print("Song Source: " + songlink)
    format_type= d["data"]["songList"][0]["format"]
    return download_music(songlink,mess,format_type)



if __name__ == '__main__':
    #获取网页源代码
    html = download("http://music.baidu.com/tag")
    # 标签页列表链接
    list = get_tag_list(html)
    # 遍历链接
    num=0
    for song_list_url in list:
        # 访问列表详细信息
        singer_list = get_song_list(song_list_url)
        #下载音乐，传入歌曲名和歌手名
        # for singer_info in singer_list:
        #     music_path=download_song(singer_info['song_name'], singer_info['singer_name'])
        #     num+=1
    print("Download " + str(num) + " music\n")