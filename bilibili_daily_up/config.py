'''
Author: ForMemRs
Date: 2022-06-19 17:41:19
LastEditors: ForMemRS
LastEditTime: 2022-08-15 10:06:27
FilePath: /bilibili_daily_up/config.py
Blog: https://www.52pojie.cn/?1507943
Copyright (c) 2022 by ForMemRs, All Rights Reserved.
'''

COIN_OR_NOT = False
# 是否投币
# 开启后如果硬币数量小于5默认也会跳过


SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md
# 新华网 人民日报 央视频  王冰冰 英雄联盟赛事

COOKIE_LIST = ["""buvid3=EE3A08C7-719F-6AB4-CE53-50475148CB3372047infoc; i-wanna-go-back=-1; _uuid=F43166E10-DBBB-C621-8B16-26A2E534A23572433infoc; buvid4=594C0B08-4263-9F05-DAEC-A727DDDBC10A72695-022062711-zwQE3GcpA677qYR4f9sX+A%3D%3D; blackside_state=0; CURRENT_BLACKGAP=0; rpdid=|(u)YRluY|m)0J'uYl~JluJYl; fingerprint=0ad0deadc4561c363d40169d339615b4; buvid_fp_plain=undefined; DedeUserID=310370945; DedeUserID__ckMd5=44978c147391e60e; nostalgia_conf=-1; buvid_fp=0ad0deadc4561c363d40169d339615b4; fingerprint3=5d49c2a6462f52f817890ab7b1abd26e; LIVE_BUVID=AUTO2616582843984392; b_ut=5; bp_article_offset_310370945=691888690131107800; CURRENT_QUALITY=120; is-2022-channel=1; PVID=1; bp_video_offset_310370945=697882535875575800; b_lsid=CFA10E159_182D27D3A5B; SESSDATA=af956c6f%2C1676940799%2C399b4%2A81; bili_jct=b9bec719d7f4ff037f04e506674d22e5; sid=5zo20mh0; innersign=1; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_EE3A08C7%22%3A%22182D27D3BE9%22%2C%22333.1193.fp.risk_EE3A08C7%22%3A%22182D27D3DF5%22%2C%22333.880.fp.risk_EE3A08C7%22%3A%22182D27D72B3%22%2C%22333.788.fp.risk_EE3A08C7%22%3A%22182D27DAC74%22%7D%7D; CURRENT_FNVAL=16"""]
# Bilibili的COOKIE获取的方法见README.md
# 支持多账号，需要多账号请在列表中添加多个COOKIE

PUSH_OR_NOT = False
# 是否推送消息
TOKEN = ''
# PUSH PLUS的TOKEN 官网为 https://www.pushplus.plus
