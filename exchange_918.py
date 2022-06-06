#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_918.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 20 59 19,23 * * *
new Env("极速版918券");
'''

from exchange_lib import *

body_dict = {
    'activityId': '55vXw3fpK4oYTX3ED2w1nqBWB3K',
    'scene': '1',
    'args': 'key=31FBE9916D4A339D7AEA63C0B3790FB927674283D64E52C96783F230346D89CC3F1EB6BDAD81D6B983F62B3064279C6F_bingo,roleId=5060700DC4EB9A836138A2E8D06ACB72F2F480F3675CAA5D9F6FED47F6DFE5B7E1B1E069ED74134C16E06CD499A5CA627CD8EED3D8DCA55E585D7CB53784638F67CDB49F4508E57D17838699407CC07A4157E66A802E48DACD88342E35502CE97FF842B6E3DABD2065CD89AE36E8B826C3BBB2464D2B9933D3FA878059F1FDFDB3657394ABBFDB3BF4C12BE2BA08C95920E6A9B507D1A546B162F6612684325048E0A705092BD0DBFCE1D49B37139B3C_bingo,strengthenKey=E69C4C9B08504F0E61532E94C2391A4F3C8C17E33845A8E820806A9C43EC1E9AFEF14DB1A042ADDD466454290BEDB70F_bingo'
}

waiting_delta = float(os.environ['WAITING_DELTA']) if "WAITING_DELTA" in os.environ else 0.18

# 优先前4个号，全部抢到后从后面每次执行2个号
# exchangeCouponsMayMonthV2(header="https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5&clientVersion=1.0.0", body_dict=body_dict, batch_size=5, other_batch_size=2, waiting_delta=0.25, process_number=4, coupon_type="15-8")

exchangeCouponsMayMonthV3(header="https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&client=wh5&clientVersion=1.0.0", body_dict=body_dict, batch_size=5, other_batch_size=5, waiting_delta=0.20, sleep_time=0.025, thread_number=14, coupon_type="15-8")