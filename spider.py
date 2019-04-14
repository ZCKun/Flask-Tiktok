import sys
import requests


from config import *


class TiktokSpider:

    def __init__(self):
        self.url = 'https://api-h2.tiktokv.com/aweme/v1/feed'
        self.headers = {
            "User-Agent": "okhttp/3.10.0.1",
            "Accpet-Encoding": "gzip"
        }

    def get_aweme_list(self):
        """
        获取视频列表
        :return:
        """
        resp = requests.get(self.url, headers=self.headers, params=PARAMS)
        if resp.status_code != requests.codes.OK:
            print("获取视频列表失败.")
            return None
        try:
            return resp.json()['aweme_list']
        except KeyError:
            print(resp.text)

    def parse_video(self):
        """
        解析json格式小视频列表数据
        :return:
        """
        aweme_list = self.get_aweme_list()
        if aweme_list is None:
            return aweme_list
        video_result = []
        for aweme in aweme_list:
            play_addr = aweme['video']['play_addr']
            author = aweme['author']
            result = {
                'video_infos': {
                    'url': play_addr['url_list'],
                    'width': play_addr['width'],
                    'height': play_addr['height'],
                    'description': aweme['desc'],
                    'create_time': str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(aweme['create_time']))),
                    },
                'aweme_id': aweme['aweme_id'],
                'avatar_infos': {
                    'url': author['avatar_thumb']['url_list'],
                    'height': author['avatar_larger']['height'],
                    'width': author['avatar_larger']['width']
                    },
                'author_infos': {
                    'nickname': author['nickname'],
                    'uid': author['uid'],
                    'short_id': author['short_id'],
                    'signature': author['signature'],
                }

            }
            video_result.append(result)
        return video_result
