import random
import json

from spider import TiktokSpider
from flask import Flask, render_template


app = Flask(__name__)

aos_effect = ['fade-up', 'fade-down', 'fade-right', 'fade-left'] # html中aos滚动效果

tk = TiktokSpider()


@app.route('/')
def index():
    video_result = tk.parse_video()
    if video_result is None:
        return '获取视频列表失败.'
    return render_template('index.html',
                           video_result=video_result,
                           aos_effect=aos_effect,
                           random=random)


@app.route('/more')
def load_more():
    video_result = tk.parse_video()
    if video_result is None:
        return 0
    return json.dumps(video_result)
