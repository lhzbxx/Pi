# -*- coding: utf-8 -*-
# 
# RESTful-API
# 
# 

#########
#
# 模块导入&初始化
# 
#########
from flask import *
import sqlite3
import os
import time

app = Flask(__name__)
#
#
#
#########

# 子系统：
# 
# 1. 签到。
# --- 场景：公司内部上下班、活动清点人数。
# --- 步骤：1. 公司建立群组。
# 			2. 每个用户都对应着一张明确的照片。
# 			3. 当需要签到的时候，组织人亮出一个二维码。
# 			4. 当签到的人扫描二维码时，组织人收到推送。
# 			5. 确定推送的图片与本人相符，点击确认，完成签到。
# 2. 任务。
# --- 场景：群组内部分配任务完成。
# --- 步骤：1. 领头人创建任务，分配成员（可能多个）。
# 			2. 用户可以查看自己的任务。
# 			3. 完成后发送请求确认。
# 			4. 领头人确认完毕。
# 3. 朋友圈。
# --- 场景：朋友圈。
# --- 步骤：1. 发送状态。
# 			2. 好友收到推送。
# 			3. 评论。
# 			4. 点赞。
# 4. 话题。
# --- 场景：群组人员发布讨论、同兴趣（音乐、电影、书籍、艺人、物品）人群讨论。
# --- 步骤：1. 用户选择标签（热门标签）。
# 			2. 系统向用户推送话题通知。
# 			3. 用户参与讨论，评价、投票。
# 			4. 标签推荐。
# 			5. 评论赞同。
# 5. 吐槽。
# --- 场景：
# --- 步骤：
# 6. 微活动。
# --- 场景：
# --- 步骤：
# 7. 多人创作。
# --- 场景：
# --- 步骤：
# 8. 电竞赛事文字直播。
# --- 场景：
# --- 步骤：
# 9. 日报。
# --- 场景：
# --- 步骤：
# 10. 公众号。
# --- 场景：
# --- 步骤：
# 11. 卡券发放系统。
# --- 场景：
# --- 步骤：
# 12. 微博平台。
# --- 场景：
# --- 步骤：

#########
#
# 0. 测试
# 
#########
@app.route('/test/api/hello')
def test_hello():
	r = {'status': 100, "msg": "Hello!"}
	return jsonify(r)
@app.route('/test/api/post', methods=['POST'])
def test_post():
	if not request.args:
		r = {'status': 200, "msg": "缺少参数"}
	else:
		r = {'status': 100, "msg": request.args.get('param', '')}
	return jsonify(r)
@app.route('/test/WorkWatcher/listen_work', methods=['POST'])
def WW_listen():
	return "success"
@app.route('/test/WorkWatcher/upload_image', methods=['GET', 'POST'])
def WW_upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("img", file.filename))
        return "success"
@app.route('/test/WorkWatcher/get_clock', methods=['GET', 'POST'])
def WW_clock():
	return "1"
#
#
#
#########
#
#########
#
# 1. 签到系统
# 
#########
@app.route('/checkin/api/buildgroup')
def checkin_buildgroup():
	return "Hello, World!"
#
#
#
#########

#########
#
# 基础组件&函数
# 
#########
if __name__ == '__main__':
	app.run(debug = True)
#
#
#
#########