# coding = utf-8
# __author__ = 'linye'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class Mine(PublicClass):
    """我的"""

    def test31_MyAccount(self):
        """我的账号"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        name = conf.get(case_name, 'name')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if name == '':
            name = conf.get('default', 'content')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_info')  # 点击我的
        self.clickId('tv_mycount_phonenum')  # 点击手机号
        self.assertEqual('我的账号', self.textId('tv_header'), '"我的账号"页面header错误')  # 判断header
        before_information = [self.textId('tv_name'),
                              self.textId('tv_arear_detail'),
                              self.textId('tv_name_huxing'),
                              self.textId('tv_name_yusuan'),
                              self.textId('tv_name_fengge')[1:].rstrip(),
                              self.textId('tv_name_decoration_stage'),
                              self.textId('tv_sex_detail'),
                              self.textId('tv_age_detail')]
        self.clickId('nickname_right')
        self.assertEqual('昵称修改', self.textId('tv_header'), '"昵称修改"页面header错误')
        self.inputId('et_nick', name + str(random.randint(0, 1000)))
        self.clickId('btn_right1')
        self.clickId('iv_right_arear')
        while True:
            area = random.choice(['40平米以下', '41-60平米', '61-90平米', '91-120平米'])
            if area != before_information[1]:
                break
        self.clickName(area)
        self.clickId('huxing_right')
        while True:
            huxing = random.choice(['一居室', '二居室', '三居室', '四居室'])
            if huxing != before_information[2]:
                break
        self.clickName(huxing)
        self.clickId('yusuan_right')
        while True:
            yusuan = random.choice(['2万以下', '2-4万', '4-6万', '6-10万'])
            if yusuan != before_information[3]:
                break
        self.clickName(yusuan)
        self.clickId('fengge_right')
        while True:
            fengge = random.choice(['简约', '欧式', '混搭', '田园', '中式', '简欧', '古典', '地中海', '东南亚', '美式', '日韩', '宜家'])
            if fengge != before_information[4]:
                break
        self.clickName(fengge)
        self.clickId('confirm')
        self.clickId('right_arrow_decoration_stage')
        while True:
            decoration_stage = random.choice(['准备', '拆改', '水电', '泥木', '油漆', '验收', '竣工', '软装', '入驻'])
            if decoration_stage != before_information[5]:
                break
        self.clickName(decoration_stage)
        self.clickId('iv_right_sex')
        while True:
            sex = random.choice(['男', '女'])
            if sex != before_information[6]:
                break
        self.clickName(sex)
        self.clickId('iv_right_age')
        while True:
            age = random.choice(['25以下', '25-30', '30-35', '35-40'])
            if age != before_information[7]:
                break
        self.clickName(age)
        self.clickId('btn_right1')
        self.assertTrue(self.driver.find_elements_by_id('tv_mycount_phonenum'), '"我的"页面保存信息失败')
        self.clickId('tv_mycount_phonenum')
        self.assertNotEqual(before_information[0], self.textId('tv_name'), '"我的"页面昵称更新失败')
        self.assertNotEqual(before_information[1], self.textId('tv_arear_detail'), '"我的"页面建筑面积更新失败')
        self.assertNotEqual(before_information[2], self.textId('tv_name_huxing'), '"我的"页面户型更新失败')
        self.assertNotEqual(before_information[3], self.textId('tv_name_yusuan'), '"我的"页面预算更新失败')
        self.assertNotEqual(before_information[4], self.textId('tv_name_fengge')[1:].rstrip(), '"我的"页面喜欢风格更新失败')
        self.assertNotEqual(before_information[5], self.textId('tv_name_decoration_stage'), '"我的"页面装修阶段更新失败')
        self.assertNotEqual(before_information[6], self.textId('tv_sex_detail'), '"我的"页面性别更新失败')
        self.assertNotEqual(before_information[7], self.textId('tv_age_detail'), '"我的"页面年龄更新失败')
        self.goBack(2)
        self.assertHomepage()

    def test32_IM(self):
        """IM"""
        self.clickId('iv_info')  # 点击我的
        self.clickId('iv_my_message')
        self.assertEqual('通知', self.textId('tv_header'), '"通知"页面header错误')
        if self.driver.find_elements_by_id('iv_agent'):
            self.clickId('tv_name')
            self.assertNotEqual('通知', self.textId('tv_header'), '"通知"页面跳转失败')
            self.goBack(3)
            self.assertHomepage()
        else:
            self.assertEqual('暂无信息', self.textId('tv_load_error'), '"通知"页面提示错误')
            self.goBack(2)
            self.assertHomepage()

    def test33_Coupon(self):
        """优惠券"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')  # 点击我的
        self.clickId('tv_mycount_voucher', sleep_time)
        self.assertEqual('优惠券', self.textId('tv_header'), '"优惠券"页面header错误')
        self.goBack(2)
        self.assertHomepage()

    def test34_MyMoney(self):
        """我的钱"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')  # 点击我的
        self.clickId('tv_mycount_myoney')
        self.assertEqual('我的钱', self.textId('tv_header'), '"我的钱"页面header错误')
        self.clickId('ll_pay_activity')
        self.assertEqual('设置支付密码', self.textId('tv_header'), '点击"充值"后"支付密码"页面header错误')
        self.goBack()
        self.clickId('ll_tixian_activity')
        self.assertEqual('提现', self.textId('tv_header'), '"提现"页面header错误')
        self.goBack()
        self.clickId('ll_mingxi_activity')
        self.assertEqual('收支明细', self.textId('tv_header'), '"收支明细"页面header错误')
        self.assertEqual('收入', self.textId('rb1'), '"收支明细"页面tab错误')
        self.assertEqual('支出', self.textId('rb2'), '"收支明细"页面tab错误')
        self.goBack(3)
        self.assertHomepage()

    def test35_IntegralMall(self):
        """积分商城"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')
        self.clickId('tv_mypoint_key')
        self.assertEqual('积分商城', self.textId('tv_header'), '"积分商城"页面header错误')
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '"积分商城"页面加载失败')
        self.goBack(2)
        self.assertHomepage()

    def test36_DecorationQuotation(self):
        """装修报价"""
        self.clickId('tv_info')  # 点击我的
        self.clickId('ll_jiaju_my_price')  # 点击装修报价
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '装修报价页面加载失败')  # 验证装修报价模块加载
        self.goBack(2)  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test37_CrazyDiscount(self):
        """疯狂优惠"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('tv_info')  # 点击我的
        self.clickId('ll_jiaju_crazy_discount')
        self.assertEqual('疯狂优惠券', self.textId('tv_header'), '"疯狂优惠券"页面header错误')
        self.goBack(2)
        self.assertHomepage()

    def test38_MyCollect(self):
        """我的收藏"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('tv_info')  # 点击我的
        self.clickId('ll_jiaju_attention', sleep_time)
        self.assertEqual('我的收藏', self.textId('tv_header'), '"我的收藏"页面header错误')
        before_picture = int(self.textId('tv_picnum'))
        before_knowledge = int(self.textId('tv_knowledgenum'))
        before_diary = int(self.textId('tv_recordnum'))
        before_gongdi = int(self.textId('tv_gongdinum'))
        self.goBack()
        self.clickId('iv_home_inspiration', sleep_time)
        self.clickId('iv_inspirationPic', sleep_time)
        self.clickId('img_right1')
        self.goBack()
        self.clickId('tv_header_middle', sleep_time)
        self.clickId('iv_left_two', sleep_time)
        self.clickId('pic_save_iv')
        self.goBack()
        self.clickId('tv_header_right', sleep_time)
        self.clickId('iv_left_two', sleep_time)
        self.clickId('pic_save_iv')
        self.goBack(2)
        self.clickName('学装修')
        self.clickId('title2')
        self.clickId('imag')
        self.clickId('img_right1')
        self.goBack(3)
        self.clickId('iv_home_diary')
        self.clickId('imageView_tupian')
        self.clickId('img_right')
        self.goBack(2)
        self.clickName('看工地')
        self.clickId('worksite_btn_list')
        self.clickId('iv_pictrues', sleep_time)
        self.clickId('rl_xiana_shoucang')
        self.goBack(3)
        self.clickId('iv_info')
        self.clickId('ll_jiaju_attention', sleep_time)
        self.assertEqual(before_picture + 3, int(self.textId('tv_picnum')), '"装修美图"收藏失败')
        self.assertEqual(before_knowledge + 1, int(self.textId('tv_knowledgenum')), '"装修攻略"收藏失败')
        self.assertEqual(before_diary + 1, int(self.textId('tv_recordnum')), '"装修日记"收藏失败')
        self.assertEqual(before_gongdi + 1, int(self.textId('tv_gongdinum')), '"工地"收藏失败')
        self.clickId('tv_picnum')
        self.assertEqual('收藏的美图', self.textId('tv_header'), '"收藏的美图"页面header错误')
        self.assertTrue(self.driver.find_elements_by_id('iv_pic_meiri'), '"装修美图"收藏失败')
        self.clickId('iv_pic_meiri', sleep_time)
        self.clickId('img_right1')
        self.goBack()
        self.assertEqual('您还没有收藏的精选图集', self.textId('tv_nodata9'), '取消收藏"美图精选"失败')
        self.clickId('tv_my_case9')
        self.assertTrue(self.driver.find_elements_by_id('iv_pic_meiri'), '"套图"收藏失败')
        self.clickId('iv_pic_meiri', sleep_time)
        self.clickId('pic_save_iv')
        self.goBack()
        self.assertEqual('你还没有收藏的套图', self.textId('tv_nodata9'), '取消收藏"套图"失败')
        self.clickId('tv_my_foreman9')
        self.assertTrue(self.driver.find_elements_by_id('iv_pic_meiri'), '"单图"收藏失败')
        self.clickId('iv_pic_meiri', sleep_time)
        self.clickId('pic_save_iv')
        self.goBack()
        self.assertEqual('你还没有收藏的单图', self.textId('tv_nodata9'), '取消收藏"单图"失败')
        self.goBack()
        self.clickId('tv_knowledgenum')
        self.assertEqual('装修攻略', self.textId('tv_header'), '"装修攻略"页面header错误')
        self.assertTrue(self.driver.find_elements_by_id('imag'), '"装修攻略"收藏失败')
        self.clickId('imag')
        self.clickId('img_right1')
        self.goBack()
        self.assertEqual('你还没有收藏的装修攻略', self.textId('tv_noknowlege'), '取消收藏"装修攻略"失败')
        self.goBack()
        self.clickId('tv_recordnum')
        self.assertEqual('收藏的日记', self.textId('tv_header'), '"装修日记"页面header错误')
        self.clickId('iv_tupian')
        self.clickId('img_right')
        self.goBack()
        self.assertEqual('此处依然空空如也', self.textId('tv_no_up'), '取消收藏"装修日记"失败')
        self.goBack()
        self.clickId('tv_gongdinum')
        self.assertEqual('收藏的工地', self.textId('tv_header'), '"工地"页面header错误')
        self.assertTrue(self.driver.find_elements_by_id('iv_gongdi'), '"工地"收藏失败')
        self.clickId('iv_gongdi')
        self.reFresh()
        self.clickId('rl_xiana_shoucang')
        self.goBack()
        self.assertEqual('您还没有收藏的工地', self.textId('tv_text'), '取消收藏"工地"失败')
        self.goBack()
        self.assertEqual(before_picture, int(self.textId('tv_picnum')), '"装修美图"取消收藏失败')
        self.assertEqual(before_knowledge, int(self.textId('tv_knowledgenum')), '"装修攻略"取消收藏失败')
        self.assertEqual(before_diary, int(self.textId('tv_recordnum')), '"装修日记"取消收藏失败')
        self.assertEqual(before_gongdi, int(self.textId('tv_gongdinum')), '"工地"取消收藏失败')
        self.goBack(2)
        self.assertHomepage()

    def test39_MyReply(self):
        """我的回复"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')
        self.clickId('tv_my_documentary')
        self.assertEqual('我的回复', self.textId('tv_header'), '"我的回复"页面header错误')
        self.clickId('iv_img')
        self.assertEqual('社区', self.textId('tv_header'), '"装修社区"页面header错误')
        self.clickName('我的发帖')
        self.assertEqual('我的发帖', self.textId('tv_header'), '"我的发帖"页面header错误')
        self.goBack()
        self.clickName('收到的回复')
        self.assertEqual('收到的回复', self.textId('tv_header'), '"收到的回复"页面header错误')
        self.goBack()
        self.clickName('我的提问')
        self.assertEqual('我的提问', self.textId('tv_header'), '"我的提问"页面header错误')
        self.goBack()
        self.clickName('收到的回答')
        self.assertEqual('我的问答', self.textId('tv_header'), '"收到的回答"页面header错误')
        self.goBack(2)
        self.clickId('iv_img2')
        self.assertEqual('@我的', self.textId('tv_header'), '"@我的"页面header错误')
        self.goBack(3)
        self.assertHomepage()

    def test40_MyDiary(self):
        """我的日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')
        self.swipeUp()
        self.clickId('ll_jiaju_my_diary')
        self.assertEqual('我的日记', self.textId('tv_header'), '"我的日记"页面header错误')
        if self.driver.find_elements_by_id('iv_content_img'):
            self.clickId('iv_content_img')
            self.assertTrue(self.driver.find_elements_by_id('navigation_bar_button'), '"我的日记"页面跳转详情页失败')
            self.goBack()
        else:
            self.assertEqual('您还没有日记，去日记列表页，点击右上角的＋号，去创建日记吧！', self.textId('tv_nodata'), '无"日记"时文案错误')
        self.goBack()
        self.swipeDown()
        self.goBack()
        self.assertHomepage()

    def test41_MyReservation(self):
        """我的预约"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_info')
        self.swipeUp()
        self.clickId('ll_jiaju_myyuyue')
        self.assertEqual('我的预约', self.textId('tv_header'), '"我的预约"页面header错误')
        if self.driver.find_elements_by_id('iv_icon'):
            self.clickId('iv_icon')
            self.assertTrue(self.driver.find_elements_by_id('rl_xiana_shoucang'), '"我的预约"页面跳转详情页失败')
            self.goBack()
        else:
            self.assertEqual('目前您还没有预约的工地!', self.textId('no_worksite_appointment'), '无"预约工地"文案错误')
        self.goBack()
        self.swipeDown()
        self.goBack()
        self.assertHomepage()

    def test42_MoreSettings(self):
        """更多设置"""
        version = conf.get('default', 'version')
        self.clickId('iv_info')
        self.swipeUp()
        self.clickId('ll_jiaju_my_moresetting')
        self.assertEqual('更多设置', self.textId('tv_header'), '"更多设置"页面header错误')
        self.clickId('ll_jiaju_help_and_feedback')
        self.assertEqual('帮助与反馈', self.textId('tv_header'), '"帮助与反馈"页面header错误')
        self.goBack()
        self.clickName('清除缓存')
        self.assertEqual('确定要清除缓存吗?', self.textId('tv_message'), '清除缓存失败')
        self.clickId('positiveButton')
        self.assertEqual('更多设置', self.textId('tv_header'), '"清除缓存"失败')
        self.assertEqual('V' + version, self.textId('tv_versioncode'), '"关于我们"中"版本号"错误')
        self.clickId('tv_versioncode')
        self.assertEqual('关于我们', self.textId('tv_header'), '"关于我们"页面header错误')
        self.goBack()
        self.clickName('更多推荐应用')
        self.assertEqual('推荐应用', self.textId('tv_header'), '"更多推荐应用"页面header错误')
        self.swipeUp()
        self.clickId('more_app_item_icon')
        self.assertEqual('更多应用', self.textId('tv_header'), '"更多应用"页面header错误')
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '"更多应用"页面加载失败')
        self.goBack(4)
        self.assertHomepage()


if __name__ == '__main__':
    unittest.main()
