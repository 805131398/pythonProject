""  # line:9
import push  # line:13
import utools  # line:14
import config  # line:15
import data  # line:16
import api  # line:17
import requests  # line:18
import random  # line:19
import time  # line:20


class Bilibili:  # line:23
    ""  # line:26

    def __init__(self) -> None:  # line:28
        self.log = ''  # line:29
        self.session = requests.Session()  # line:30

    @staticmethod  # line:32
    def exchange_cookie(cookie_str: str):  # line:33
        ""  # line:38
        c_cookie = dict(
            [cookie.split("=", 1) for cookie in cookie_str.split("; ")])  # line:39
        return c_cookie  # line:40

    def __session_code(self, cookie_str: str) -> int:  # line:42
        ""  # line:47
        c_cookie = Bilibili.exchange_cookie(cookie_str)  # line:48
        session = self.session.get(url=api.coin_url, cookies=c_cookie).json()  # line:49
        code = session['code']  # line:50
        if code == 0:  # line:51
            return 1  # line:53
        return 0  # line:54

    def __money(self, cookie_str: str) -> int:  # line:56
        ""  # line:62
        c_cookie = self.exchange_cookie(cookie_str)  # line:63
        cookie_json = self.session.get(url=api.coin_url, headers=data.headers,
                                       cookies=c_cookie).json()  # line:65
        money = cookie_json['data']['money']  # line:66
        if money is None:  # line:67
            return 0  # line:69
        else:  # line:70
            return money  # line:71

    @staticmethod  # line:73
    def get_csrf(cookie_str: str) -> str:  # line:74
        """获取cookie中的bili_jct"""  # line:79
        c_cookie = Bilibili.exchange_cookie(cookie_str)  # line:80
        bili_jct = c_cookie['bili_jct']  # line:81
        return bili_jct  # line:82

    def __print_log(self, log: str) -> None:  # line:84
        ""  # line:89
        log = f'{log}</br>'  # line:90
        self.log = f'{self.log}{log}'  # line:91

    def __get_user(self, cookie_str: str) -> tuple:  # line:93
        """"""  # line:98
        c_cookie = Bilibili.exchange_cookie(cookie_str)  # line:99
        session_data = self.session.get(url=api.inquire_url,
                                        cookies=c_cookie).json()  # line:101
        login = session_data['data']['login']  # line:102
        watch = session_data['data']['watch']  # line:103
        coins = session_data['data']['coins']  # line:104
        share = session_data['data']['share']  # line:105
        email = session_data['data']['email']  # line:107
        tel = session_data['data']['tel']  # line:108
        safe_question = session_data['data']['safe_question']  # line:109
        identify_card = session_data['data']['identify_card']  # line:110
        user_base = [login, watch, coins, share]  # line:112
        user_info = [email, tel, safe_question, identify_card]  # line:113
        return user_base, user_info  # line:114

    def print_user_info(self, cookie_str: str) -> None:  # line:116
        ""  # line:121
        c_cookie = Bilibili.exchange_cookie(cookie_str)  # line:122
        user_info = self.session.get(url=api.info_url,
                                     cookies=c_cookie).json()  # line:123
        uid = user_info['data']['mid']  # line:124
        user = user_info['data']['name']  # line:125
        lv = user_info['data']['level']  # line:126
        exp = user_info['data']['level_exp']['current_exp']  # line:127
        next_exp = user_info['data']['level_exp']['next_exp']  # line:128
        next_lv = next_exp - exp  # line:129
        day_num = int(next_lv / 65)  # line:130
        coin = user_info['data']['coins']  # line:131
        status = user_info['data']['vip']['status']  # line:132
        vip_expire = user_info['data']['vip']['due_date']  # line:133
        vip_expire = utools.formate_time(vip_expire)  # line:134
        if status:  # line:135
            log_info = f"用户{user},uid为{uid}您是大会员,大会员到期时间为{vip_expire},你目前的等级是{lv}级,目前的经验{exp},离下个等级还差{next_lv}经验,需要{day_num}天剩余硬币还有{coin}个"  # line:136
            self.__print_log(
                f"用户名:{user}</br>uid:{uid}</br>VIP:大会员</br>到期时间:{vip_expire}</br>目前的等级:{lv}级</br>目前的经验:{exp}</br>离下个等级:{next_lv}经验<br>距升级还差:{day_num}天</br>剩余硬币数:{coin}个")  # line:138
            utools.formate_print(log_info)  # line:139
        else:  # line:140
            log_info = f"用户{user},uid为{uid}您的大会员已过期,过期时间为{vip_expire},你目前的等级是{lv}级,目前的经验{exp},离下个等级还差{next_lv}经验,需要{day_num}天,剩余硬币还有{coin}个"  # line:141
            self.__print_log(
                f"用户名:{user}</br>uid:{uid}</br>VIP:非大会员</br>过期时间:{vip_expire}</br>目前的等级:{lv}级</br>目前的经验:{exp}</br>离下个等级:{next_lv}经验<br>距升级还差:{day_num}天</br>剩余硬币数:{coin}个")  # line:143
            utools.formate_print(log_info)  # line:144

    def get_vlist(self) -> list:  # line:146
        """"""  # line:150
        UID_LIST = config.UID_LIST  # line:152  应该是要被打赏的
        video_json = self.session.get(
            url=api.get_video_list_url.format(random.choice(UID_LIST))).json()  # line:154
        vlist = video_json['data']['list']['vlist']  # line:155
        return vlist  # line:156

    def look_video(self, O0O0OOOO000O0OO0O: str, OOO0OO0OOO0OO00O0: str) -> None:  # line:158
        ""  # line:164
        OO00OOOO000O00OOO = random.randint(30, 60)  # line:165
        data.watch_video_data['bvid'] = O0O0OOOO000O0OO0O  # line:166
        data.watch_video_data['played_time'] = str(OO00OOOO000O00OOO)  # line:167
        data.watch_video_data['csrf'] = Bilibili.get_csrf(OOO0OO0OOO0OO00O0)  # line:168
        O0OOO00O00O00OO0O = Bilibili.exchange_cookie(OOO0OO0OOO0OO00O0)  # line:169
        O00O000OO00O00O0O = self.session.post(url=api.watch_video_url, data=data.watch_video_data,
                                              cookies=O0OOO00O00O00OO0O).json()  # line:171
        O0OOO0OOOOOOO0OO0 = O00O000OO00O00O0O['code']  # line:172
        if O0OOO0OOOOOOO0OO0 == 0:  # line:174
            utools.formate_print('看视频完成')  # line:175
        else:  # line:176
            utools.formate_print('看视频失败')  # line:177

    def __O0OOO0O000O0O000O(O00O0OO00O0000O0O, OO000OO000000O000: str, O00OOO0O0OO000000: str) -> None:  # line:179
        ""  # line:185
        data.share_video_data['bvid'] = OO000OO000000O000  # line:186
        data.share_video_data['csrf'] = Bilibili.get_csrf(O00OOO0O0OO000000)  # line:187
        O00O0OO00O000O0O0 = Bilibili.exchange_cookie(O00OOO0O0OO000000)  # line:188
        O00OOOOOOOOO0OOO0 = O00O0OO00O0000O0O.session.post(url=api.share_video_url, data=data.share_video_data,
                                                           cookies=O00O0OO00O000O0O0,
                                                           headers=data.headers).json()  # line:190
        OO00000OO00000O0O = O00OOOOOOOOO0OOO0['code']  # line:191
        if OO00000OO00000O0O == 0:  # line:192
            utools.formate_print('分享视频成功')  # line:193
        else:  # line:194
            utools.formate_print('分享视频失败')  # line:195

    def __OOO0O00OOOO0OOO0O(OO0000O0OO0O0OO0O, O0O0O00OOO0OOO00O: str, OO00OOOOO0OO00O0O: str) -> int:  # line:197
        ""  # line:204
        O000O0O0OO0O0O0OO = Bilibili.exchange_cookie(OO00OOOOO0OO00O0O)  # line:205
        OO0OOO0OO00000000 = data.insert_coin_data  # line:206
        O000OOOO0000O0O00 = data.insert_coin_headers  # line:207
        OO0OOO0OO00000000['aid'] = O0O0O00OOO0OOO00O  # line:208
        OO0OOO0OO00000000['csrf'] = Bilibili.get_csrf(OO00OOOOO0OO00O0O)  # line:209
        O000OOOO0000O0O00['cookie'] = OO00OOOOO0OO00O0O  # line:210
        O0OOO0O0000000O00 = OO0000O0OO0O0OO0O.session.post(url=api.insert_coins_url, headers=data.insert_coin_headers,
                                                           data=OO0OOO0OO00000000,
                                                           cookies=O000O0O0OO0O0O0OO).json()  # line:213
        OO000000O0O00OOOO = O0OOO0O0000000O00['data']['like']  # line:214
        if OO000000O0O00OOOO:  # line:215
            utools.formate_print('投币成功')  # line:216
            return 1  # line:217
        else:  # line:218
            utools.formate_print('投币失败')  # line:219
            return 0  # line:220

    @staticmethod  # line:222
    def random_video_para(vlist: list) -> tuple:  # line:223
        ""  # line:228
        video = random.randint(0, len(vlist) - 1)  # line:229
        bvid = vlist[video]['bvid']  # line:230
        title = vlist[video]['title']  # line:231
        author = vlist[video]['author']  # line:232
        aid = vlist[video]['aid']  # line:233
        return bvid, title, author, aid  # line:234

    def coin(self, O0O00000000O0O00O: str) -> int:  # line:236
        ""  # line:241
        OO000O0O0OOOOOO00 = self.get_vlist()  # line:242
        O00000OO000000O0O, O0OO0OOOOOOOOOO00, O000OO000OO0000OO, O00000000000O0OO0 = Bilibili.random_video_para(
            OO000O0O0OOOOOO00)  # line:244
        utools.formate_print(f'开始向{O000OO000OO0000OO}的视频{O0OO0OOOOOOOOOO00}投币……')  # line:245
        OOO0OOO00OOO0O0O0 = self.__OOO0O00OOOO0OOO0O(O00000000000O0OO0, O0O00000000O0O00O)  # line:246
        return OOO0OOO00OOO0O0O0  # line:247

    def __OOO0O0000000OO00O(OOOOO000OO000O00O, OOO0OOOOO0O0O0OOO: str) -> None:  # line:249
        O000O0O00OOOOOO0O = OOOOO000OO000O00O.session.get(url=api.live_sign_url, cookies=Bilibili.exchange_cookie(
            OOO0OOOOO0O0O0OOO)).json()  # line:250
        if O000O0O00OOOOOO0O['code'] == 0:  # line:251
            OO00O00OO00O00O0O = O000O0O00OOOOOO0O['data']['text']  # line:252
            OOO00O0O0OOOOOO00 = O000O0O00OOOOOO0O['data']['hadSignDays']  # line:253
            OOOOO000OO000O00O.__print_log(
                '直播签到:签到成功,签到天数为{}'.format(OOO00O0O0OOOOOO00))  # line:254
            utools.formate_print(f'签到奖励:{OO00O00OO00O00O0O},连续签到{OOO00O0O0OOOOOO00}天')  # line:255
            OOOOO000OO000O00O.__print_log(
                f'签到奖励:{OO00O00OO00O00O0O},连续签到{OOO00O0O0OOOOOO00}天')  # line:256
        else:  # line:257
            utools.formate_print('直播签到:当天已签到~')  # line:258
            OOOOO000OO000O00O.__print_log('直播签到:当天已签到')  # line:259

    def __O0OOOOO0OO0000OO0(O000O0OO0OOOOOO0O, OO0OO0OOO00O0OO0O: str) -> bool:  # line:261
        ""  # line:266
        O00O0O0O0O00O0O00 = O000O0OO0OOOOOO0O.session.get(url=api.live_info_url, cookies=Bilibili.exchange_cookie(
            OO0OO0OOO00O0OO0O)).json()  # line:267
        O000O0OO0OOOOOO0O.__print_log(f'银瓜子数量:{O00O0O0O0O00O0O00["data"]["silver"]}')  # line:268
        utools.formate_print(f'银瓜子数量:{O00O0O0O0O00O0O00["data"]["silver"]}')  # line:269
        if O00O0O0O0O00O0O00['data']['silver'] > 700:  # line:270
            return True  # line:271
        return False  # line:272

    def __O00000OOOOOOOOOOO(OO0OO0O00OOOOO00O, OOOO0O00OO00OOO00: str) -> None:  # line:274
        O00OOO0O00OOOO0O0 = data.silver2coin_data  # line:275
        O00OOO0O00OOOO0O0['csrf'] = Bilibili.get_csrf(OOOO0O00OO00OOO00)  # line:276
        O00OOO0O00OOOO0O0['csrf_token'] = Bilibili.get_csrf(OOOO0O00OO00OOO00)  # line:277
        O0OOO00OOOOO0O000 = OO0OO0O00OOOOO00O.session.post(url=api.silver2coin_url,
                                                           cookies=Bilibili.exchange_cookie(OOOO0O00OO00OOO00),
                                                           data=O00OOO0O00OOOO0O0).json()  # line:278
        if O0OOO00OOOOO0O000['code'] == 0:  # line:279
            OO000OO0OO0O0000O = O0OOO00OOOOO0O000['data']['silver']  # line:280
            utools.formate_print('银瓜子兑换:成功!')  # line:281
            utools.formate_print(f'银瓜子剩余:{OO000OO0OO0O0000O}个')  # line:282
            OO0OO0O00OOOOO00O.__print_log('银瓜子兑换:成功!')  # line:283
            OO0OO0O00OOOOO00O.__print_log(f'银瓜子剩余:{OO000OO0OO0O0000O}个')  # line:284
        else:  # line:285
            utools.formate_print('银瓜子兑换:当天已兑换!')  # line:286
            OO0OO0O00OOOOO00O.__print_log('银瓜子兑换:当天已兑换!')  # line:287

    def __OOO00OOOO00O0000O(self, cookie_str: str) -> None:  # line:289
        ""  # line:294
        code = self.__session_code(cookie_str)  # line:295
        if code:  # line:296
            money = self.__money(cookie_str)  # line:297
            utools.formate_print('cookie有效即将开始查询任务……')  # line:298
            utools.formate_print('=========以下是任务信息=========')  # line:299
            self.__print_log('=========以下是任务信息=========')  # line:300
            user = self.__get_user(cookie_str)  # line:302
            user_base, user_info = user  # line:303
            for index, user_base_value in enumerate(user_base):  # line:306
                if index == 0:  # line:307
                    utools.formate_print('登录任务已完成') if user_base_value else utools.formate_print(
                        '登录任务未完成')  # line:309
                    self.__print_log('每日登录:已完成~获得5点经验值')  # line:310
                elif index == 1:  # line:311
                    if user_base_value:  # line:312
                        utools.formate_print('观看视频任务已完成')  # line:313
                        self.__print_log('观看视频:已完成~获得5点经验值')  # line:314
                    else:  # line:315
                        utools.formate_print('观看视频任务未完成,即将开始观看视频任务……')  # line:316
                        vlist = self.get_vlist()  # line:317
                        # bvid, title, author, aid
                        bvid, title, author, aid = Bilibili.random_video_para(vlist)  # line:319
                        utools.formate_print(f'开始观看作者{author}的视频{title}……')  # line:320
                        self.look_video(bvid, cookie_str)  # line:321
                        utools.formate_print('观看视频任务已完成，即将开始下一个任务……')  # line:322
                        self.__print_log('观看视频:完成~获得5点经验值')  # line:323
                elif index == 2:  # line:324
                    if config.COIN_OR_NOT and money >= 5:  # line:325
                        if user_base_value == 50:  # line:328
                            utools.formate_print('投币任务已完成')  # line:329
                            self.__print_log('每日投币:已完成~获得50点经验值')  # line:330
                        else:  # line:331
                            utools.formate_print('投币任务未完成,即将开始投币任务')  # line:332
                            coin_num = int((50 - user_base_value) / 10)  # line:333
                            for OO0OO0OO000000O0O in range(0, coin_num):  # line:334
                                index = 0  # line:335
                                if config.STRICT_MODE:  # line:336
                                    while 1:  # line:337
                                        OOOO0O0O0O00O0000 = self.coin(
                                            cookie_str)  # line:338
                                        index += 1  # line:339
                                        if OOOO0O0O0O00O0000 or index == 5:  # line:340
                                            break  # line:343
                                        time.sleep(2)  # line:344
                                else:  # line:345
                                    self.coin(cookie_str)  # line:346
                                    time.sleep(2)  # line:347
                                time.sleep(1)  # line:348
                            utools.formate_print('投币任务已完成，即将开始下一个任务……')  # line:349
                            self.__print_log('每日投币:完成~获得50点经验值')  # line:350
                    else:  # line:351
                        utools.formate_print('投币任务已跳过')  # line:352
                        self.__print_log('每日投币:跳过~')  # line:353
                else:  # line:354
                    if user_base_value:  # line:355
                        utools.formate_print('分享任务已完成')  # line:356
                        self.__print_log('每日分享:已完成~获得5点经验值')  # line:357
                    else:  # line:358
                        utools.formate_print('分享任务未完成,即将开始分享任务……')  # line:359
                        vlist = self.get_vlist()  # line:360
                        bvid, title, author, aid = Bilibili.random_video_para(
                            vlist)  # line:362
                        utools.formate_print(f'开始分享{author}的视频{title}……')  # line:363
                        self.__O0OOO0O000O0O000O(bvid, cookie_str)  # line:364
                        utools.formate_print('分享任务已完成,日常任务已全部完成!即将查询额外任务……')  # line:365
                        self.__print_log('每日分享:完成~获得5点经验值')  # line:366
                        time.sleep(1)  # line:367
            utools.formate_print('==========以下是额外任务==============')  # line:368
            self.__print_log('=========以下是额外任务=========')  # line:369
            for index, user_base_value in enumerate(user_info):  # line:371
                if index == 0:  # line:372
                    if user_base_value:  # line:373
                        utools.formate_print('绑定邮箱任务已完成')  # line:374
                        self.__print_log('绑定邮箱:已完成')  # line:375
                    else:  # line:376
                        utools.formate_print('绑定邮箱任务未完成,完成可以获得20点经验值~')  # line:377
                        self.__print_log('绑定邮箱:未完成~完成可获得20点经验')  # line:378
                elif index == 1:  # line:379
                    if user_base_value:  # line:380
                        utools.formate_print('绑定手机任务已完成')  # line:381
                        self.__print_log('绑定手机:已完成')  # line:382
                    else:  # line:383
                        utools.formate_print('绑定手机任务未完成,完成可以获得100点经验值~')  # line:384
                        self.__print_log('绑定手机:未完成~完成可获得20点经验')  # line:385
                elif index == 2:  # line:386
                    if user_base_value:  # line:387
                        utools.formate_print('设置密保任务已完成')  # line:388
                        self.__print_log('密保任务:已完成')  # line:389
                    else:  # line:390
                        utools.formate_print('设置密保任务未完成,完成可以获得30点经验值~')  # line:391
                        self.__print_log('密保任务:未完成~完成可获得30点经验')  # line:392
                else:  # line:393
                    if user_base_value:  # line:394
                        utools.formate_print('实名认证任务已完成')  # line:395
                        self.__print_log('实名认证:已完成')  # line:396
                    else:  # line:397
                        utools.formate_print('实名认证任务未完成,完成可以获得50点经验值~')  # line:398
                        self.__print_log('实名认证:未完成~完成可获得50点经验')  # line:399
            utools.formate_print('==========以下是直播任务==============')  # line:400
            self.__print_log('=========以下是直播任务=========')  # line:401
            self.__OOO0O0000000OO00O(cookie_str)  # line:402
            if config.SILVER2COIN_OR_NOT and self.__O0OOOOO0OO0000OO0(cookie_str):  # line:403
                self.__O00000OOOOOOOOOOO(cookie_str)  # line:405
            else:  # line:406
                self.__print_log('银瓜子转换币:跳过~')  # line:407
                utools.formate_print('银瓜子兑换:跳过~')  # line:408
            self.__print_log('=========以下是个人信息=========')  # line:409
            utools.formate_print('=========以下是个人信息=========')  # line:410
            self.print_user_info(cookie_str)  # line:411
        else:  # line:412
            utools.formate_print('cookie已失效,任务停止,请更换新的cookie!')  # line:413
            self.__print_log('cookie已失效,任务停止,请更换新的cookie!')  # line:414
        utools.formate_print('==========分割线==============')  # line:415

    def go(self) -> None:  # line:417
        ""  # line:421
        if len(config.COOKIE_LIST[0]) == 0:
            utools.formate_print('未添加cookie')
            return
        utools.formate_print(f'成功添加{len(config.COOKIE_LIST)}个cookie,开始任务……')  # line:422
        for O0OOOOO0O000OO0OO, O0OOOOO0O0OO0O00O in enumerate(config.COOKIE_LIST):  # line:423
            self.__print_log(f'=========这是第{O0OOOOO0O000OO0OO + 1}个账号=========')  # line:424
            utools.formate_print(f'正在签到第{O0OOOOO0O000OO0OO + 1}个账号……')  # line:425
            self.__OOO00OOOO00O0000O(O0OOOOO0O0OO0O00O)  # line:426
            time.sleep(1)  # line:427
        if config.PUSH_OR_NOT:  # line:428
            push.pushplus(config.TOKEN, self.log)  # line:429
