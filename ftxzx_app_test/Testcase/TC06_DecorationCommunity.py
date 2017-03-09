# coding = utf-8
# __author__ = 'peidongxue'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationCommunity(PublicClass):
    """来交流"""

    def test44_Replies(self):
        """交流广场-发帖-回复"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        reply_content = conf.get(case_name, 'reply_content')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if reply_content == '':
            reply_content = conf.get('default', 'content')
        self.login(usr, psw)  # 登陆测试账号
        self.clickName("来交流")  # 点击首页来交流按钮
        self.assertEqual('装修社区', self.textId('tv_header'), '"装修社区"页面header错误')  # 判断header
        self.clickName("交流广场")  # 点击交流广场按钮
        self.assertEqual('交流广场', self.textId('tv_header'), '"装修社区"页面header错误')  # 判断header
        self.clickId("header")  # 点击第一条交流论坛
        self.assertEqual('论坛帖', self.textId('tv_header'), '"装修社区"页面header错误')  # 判断header
        self.clickId("btn_reply")  # 点击回复按钮
        self.inputId("et_input_answer", reply_content)  # 输入回复内容
        self.clickId("btn_send", sleep_time)  # 点击发送按钮
        self.swipeUp()  # 上滑
        self.goBack(3)  # 返回3次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test45_WellPastes(self):
        """精选好帖-回复"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        reply_content = conf.get(case_name, 'reply_content')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if reply_content == '':
            reply_content = conf.get('default', 'content')
        self.login(usr, psw)
        self.clickName("来交流")  # 点击首页来交流按钮
        self.clickName("精选好帖")  # 点击交流广场按钮
        self.assertEqual('精选好帖', self.textId('tv_header'), '"精选好贴"页面header错误')
        self.clickId("rel")  # 点击第一条交流论坛
        self.assertEqual('论坛帖', self.textId('tv_header'), '"论坛帖"页面header错误')
        self.clickId("btn_reply")  # 点击回复按钮
        self.inputId("et_input_answer", reply_content)  # 输入回复内容
        self.clickId("btn_send", sleep_time)  # 点击发送按钮
        self.swipeUp()  # 上滑
        self.goBack(3)  # 返回3次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test46_DairyPK(self):
        """日记大赛-回复"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        reply_content = conf.get(case_name, 'reply_content')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if reply_content == '':
            reply_content = conf.get('default', 'content')
        self.login(usr, psw)
        self.clickName("来交流")  # 点击首页来交流按钮
        self.clickName("日记大赛")  # 点击交流广场按钮
        self.assertEqual('日记大赛', self.textId('tv_header'), '"日记大赛"页面header错误')
        self.clickId("header")  # 点击第一条交流论坛
        self.clickId("btn_reply")  # 点击回复按钮
        self.inputId("et_input_answer", reply_content)  # 输入回复内容
        self.clickId("btn_send", sleep_time)  # 点击发送按钮
        self.swipeUp()  # 上滑
        self.goBack(3)  # 返回3次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test47_1_Hot(self):
        """你问我答-热门"""
        self.clickName("来交流",)  # 点击来交流
        self.clickName("你问我答", sleep_time)  # 点击你问我答
        self.assertEqual('你问我答', self.textId('tv_header'), '"你问我答"页面header错误')
        self.assertTrue(self.driver.find_element_by_id("rl_item"), '"你问我答"-"热门"页面加载失败"')  # 判断页面刷新是否成功
        self.swipeUp()  # 上滑
        self.goBack(2)  # 返回2次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test48_2_Newest(self):
        """你问我答-最新"""
        self.clickName("来交流")  # 点击来交流
        self.clickName("你问我答", sleep_time)  # 点击你问我答
        self.clickId("tv_new")  # 点击热门
        self.assertTrue(self.driver.find_element_by_id("rl_item"), '"你问我答"-"最新"页面加载失败')  # 判断页面刷新是否成功
        self.swipeUp()  # 上滑
        self.goBack(2)  # 返回2次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test49_3_HighPrice(self):
        """你问我答-高悬赏"""
        self.clickName("来交流")  # 点击来交流
        self.clickName("你问我答", sleep_time)  # 点击你问我答
        self.clickId("tv_high_price")  # 点击高悬赏页面
        self.assertTrue(self.driver.find_elements_by_id("rl_item"), '"你问我答"-"高悬赏"页面加载失败')  # 判断页面刷新是否成功
        self.swipeUp()  # 上滑
        self.goBack(2)  # 返回2次到首页
        self.assertHomepage()  # 返回首页是否成功

    def test50_Ask(self):
        """来交流-你问我答-我要提问"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        ask_content = conf.get(case_name, 'ask_content')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if ask_content == '':
            ask_content = conf.get('default', 'content')
        s = str(random.randint(0, 1000))
        self.login(usr, psw)
        self.clickName("来交流",)  # 点击来交流
        self.clickName("你问我答", sleep_time)  # 点击你问我答
        self.clickId("ll_btn_Ask")  # 点击我要提问按钮
        self.assertEqual('我要提问', self.textId('tv_header'), '"我要提问"页面header错误')
        self.inputId('et_myAsk', ask_content + s)  # 输入要提问的内容
        self.clickId("btn_right1")  # 点击右上角的下一步
        self.assertEqual('选择标签', self.textId('tv_header'), '"选择标签"页面header错误')
        self.clickId("bt_submit")  # 点击发布
        self.assertEqual(ask_content + s, self.textId("tv_question_des"), '"你问我答"问题提交失败')  # 断言发布后的页面，问题是否发布成功
        self.goBack(3)  # 返回首页
        self.assertHomepage()  # 返回首页是否成功


if __name__ == '__main__':
    unittest.main()
