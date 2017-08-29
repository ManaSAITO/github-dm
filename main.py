 #!/usr/local/bin/python
 # -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/')
def main():
    html = '<html><title>github_dm</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/matter', methods=['POST'])
def post():
    body = json.loads(dict(request.form.lists())["payload"][0])["comment"]["body"]

# メンション付きか判定
    if "@" in body:
        
        issue_num = json.loads(dict(request.form.lists())["payload"][0])["issue"]["number"]
        issue_url = json.loads(dict(request.form.lists())["payload"][0])["issue"]["html_url"]
        title = json.loads(dict(request.form.lists())["payload"][0])["issue"]["title"]
        text =  ' new comments to you on' + '#' + str(issue_num) + title + '\n' + body + '\n' + issue_url 
        
        token = "xoxp-217894464821-218653516966-233050992274-006783d63ab4aef9657c0fd6afa7332b"
         # 宛先を特定
        if "@ManaSAITO" in body:
            user = "@mana.test"
        elif "@test" in body:
            user = "@test"
        else:
            pass

        # chat.postMessageのURL
        url = 'https://slack.com/api/chat.postMessage'
        # パラメータ
        params = {'token' : token,
                  'channel' : user,
                  'text' : text
                  }
        # クエリ文字列に変換
        params = urllib.parse.urlencode(params)
        params = params.encode('utf-8')
        # リクエスト生成
        req = urllib.request.Request(url, params)
        # ヘッダ追加
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        # URLを開く
        res = urllib.request.urlopen(req)
        # レスポンス取得
        body = res.read()
        # レスポンスを表示
        print (body.decode('utf-8'))
    else:
        pass


if __name__ == '__main__':
    app.debug = True
    app.run()

