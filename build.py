# -*- coding: UTF-8 -*-
# encoding: utf-8
import sys
import json
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from workflow import web, ICON_WEB, Workflow
import datetime
import os
import subprocess

s1, type = json.loads(sys.argv[1])

csrf = 'iU69WvH7fJqOYcPH03_UAWHPGBHOtaJLEVUheuW99lS5CswUqLEa6vZRq-qbD7tjCPlNQOON1nhBABgshIiSGA%3D%3D'
if type == 'nv_lei':
    # 女泪
    # https://www.czxiu.com/cz/diy-1052.html#main
    _id = 1560
    params = {
        '_csrf': csrf,
        'ZDiyForm[xpos]': int(340 / 2 - min((len(s1), 14)) * 12.7),
        'ZDiyForm[ypos]': 178,
        'ZDiyForm[image]': '/assets/7bbc7da5/material/diy/old/1052.gif',
        'ZDiyForm[text]': s1,
        'ZDiyForm[font]': 'fzse.ttf',
        'ZDiyForm[color]': '#ffffff',
        'ZDiyForm[color2]': '',
        'ZDiyForm[size]': 24,
        'ZDiyForm[size_zoom]': 0,
        'ZDiyForm[repeat_type]': 'none',
        'ZDiyForm[move_type]': 'none',
        'ZDiyForm[hideSignature]': 0
    }
elif type == 'zhong_ju_quan':
    # 众举拳
    # https://www.czxiu.com/cz/diy-690.html
    _id = 1085
    n = 0 if len(s1) % 2 == 0 else 12
    s1 = s1.center(10, ' ')
    params = {
        '_csrf': csrf,
        'ZDiyForm[xpos]': 8 + n,
        'ZDiyForm[ypos]': 11,
        'ZDiyForm[image]': '/assets/7bbc7da5/material/diy/old/690.gif',
        'ZDiyForm[text]': s1,
        'ZDiyForm[font]': 'hzgb.ttf',
        'ZDiyForm[color]': '#ff0000',
        'ZDiyForm[color2]': '',
        'ZDiyForm[size]': 30,
        'ZDiyForm[size_zoom]': 0,
        'ZDiyForm[repeat_type]': 'none',
        'ZDiyForm[move_type]': 'none',
        'ZDiyForm[hideSignature]': 0
    }
elif type == 'ke_ai_bao_bao':
    # 可爱宝宝
    # https://www.czxiu.com/cz/diy-1063.html#main
    _id = 1571
    s1 = '\r\n'.join(s1)
    params = {
        '_csrf': csrf,
        'ZDiyForm[xpos]': 192,
        'ZDiyForm[ypos]': 14,
        'ZDiyForm[image]': '/assets/7bbc7da5/material/diy/old/1063.gif',
        'ZDiyForm[text]': s1,
        'ZDiyForm[font]': 'simhei.ttf',
        'ZDiyForm[color]': '#000000',
        'ZDiyForm[color2]': '',
        'ZDiyForm[size]': 16,
        'ZDiyForm[size_zoom]': 0,
        'ZDiyForm[repeat_type]': 'shadow',
        'ZDiyForm[repeat_size]': 1,
        'ZDiyForm[repeat_color]': '#ffffff',
        'ZDiyForm[repeat_color2]': '',
        'ZDiyForm[move_type]': 'none',
        'ZDiyForm[hideSignature]': 0
    }
elif type == 'warn_board':
    # 警告牌
    # https://www.czxiu.com/cz/wworning.html#main
    _id = 1515
    params = {
        '_csrf': csrf,
        'ZMultiForm[name]': '警告',
        'ZMultiForm[name2]': s1,
        'ZMultiForm[hideSignature]': 0
    }
elif type == 'mao_mi_ju_zhua':
    # 猫咪举爪
    # https://www.czxiu.com/cz/diy-982.html#main
    _id = 1428
    params = {
        '_csrf': csrf,
        'ZDiyForm[xpos]': int(288 / 2 - min((len(s1), 13)) * 288 / 13),
        'ZDiyForm[ypos]': 214,
        'ZDiyForm[image]': '/assets/7bbc7da5/material/diy/old/982.gif',
        'ZDiyForm[text]': s1,
        'ZDiyForm[font]': 'fzse.ttf',
        'ZDiyForm[color]': '#de4721',
        'ZDiyForm[color2]': '',
        'ZDiyForm[size]': 22,
        'ZDiyForm[size_zoom]': 0,
        'ZDiyForm[repeat_type]': 'border',
        'ZDiyForm[repeat_size]': 5,
        'ZDiyForm[repeat_color]': '#ffff00',
        'ZDiyForm[repeat_color2]': '#ffff66',
        'ZDiyForm[move_type]': 'none',
        'ZDiyForm[hideSignature]': 0,
    }
elif type == 'forest_backboard':
    # 森林黑板
    # https://www.czxiu.com/cz/diy-696.html#main
    _id = 1091
    s2 = ''
    for i in range(0, len(s1), 5):
        s2 += s1[i:i + 5] + '\r\n'
    params = {
        '_csrf': csrf,
        'ZDiyForm[xpos]': 82,
        'ZDiyForm[ypos]': 30,
        'ZDiyForm[image]': '/assets/7bbc7da5/material/diy/old/696.gif',
        'ZDiyForm[text]': s2,
        'ZDiyForm[font]': 'fzyt.ttf',
        'ZDiyForm[color]': '#ffffff',
        'ZDiyForm[color2]': '',
        'ZDiyForm[size]': 26,
        'ZDiyForm[size_zoom]': 0,
        'ZDiyForm[repeat_type]': 'none',
        'ZDiyForm[move_type]': 'none',
        'ZDiyForm[hideSignature]': 0,
    }
else:
    type = 'ju_pai_xiao_ren'
    _id = 1700
    # 举牌小人
    # https://www.czxiu.com/cz/2017jupai.html
    s1 = s1.replace('，', '\r\n')
    s1 = s1.replace('。', '\r\n')
    s1 = s1.replace('、', '\r\n')
    s1 = s1.replace('；', '\r\n')
    s1 = s1.replace('？', '\r\n')
    s1 = s1.replace('！', '\r\n')
    s1 = s1.replace(' ', '\r\n')
    params = {
        '_csrf': csrf,
        'ZMultiForm[text]': s1,
        'ZMultiForm[bg_color]': '#ffffff',
        'ZMultiForm[hideSignature]': 0
    }

query = dict(id=_id)
payload = urllib.urlencode(params)
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'origin': "https://www.czxiu.com",
    'x-csrf-token': "1C1bvwruvKNpqmbPRYd2fqFy3mSiVp3guvSHIzsmM5_kaSrxU6Ta0xGaDuIN9xkcyESLNY9u6dPqob51WhNX0w==",
    'x-requested-with': "XMLHttpRequest",
    'cookie': 'PHPSESSID=ecc0772d3a96121a4684937e8265c16d; '
              '_csrf=ec8e32502613fb75035020b1923bd71c9613a486d1d885ca73c3962d16d6822da%3A2%3A%7Bi%3A0%3Bs%3A5%3A'
              '%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%220DqNYJfpx0h-Hpobi6UQ-8t3PU9Va5dL%22%3B%7D; '
              'UM_distinctid=169f4459f7247b-096f4e124b4ef8-6b36017b-fa000-169f4459f732; '
              'CNZZDATA404313=cnzz_eid%3D2134223424-1554578820-%26ntime%3D1554578820; '
              'czxiu_used_styles=c246cb6bd2ae7e703cb0223ece638f297ce93cd967dd59f86e55d57b456cee51a%3A2%3A%7Bi%3A0%3Bs'
              '%3A17%3A%22czxiu_used_styles%22%3Bi%3A1%3Bs%3A10%3A%22%2C1700%2C1460%22%3B%7D',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3729.6 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded"
}
# raise Exception('', _id)
response = web.post('https://www.czxiu.com/style/make', data=payload, headers=headers, params=query)
if response.status_code != 200:
    sys.stdout.write('网络不畅或者服务不可用')
data = response.json()
if 'url' in data:
    img = 'https://www.czxiu.com/' + data['url']
    file_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S.gif')
    file_path = os.path.join('/tmp', file_name)
    web.get(img).save_to_path(file_path)
    subprocess.call(['./clipfile', file_name])
else:
    sys.stdout.write(response.text)
sys.stdout.write('生成的表情到剪切板了')
