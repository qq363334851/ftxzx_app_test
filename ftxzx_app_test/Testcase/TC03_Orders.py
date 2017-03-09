# coding = utf-8
# __author__ = 'linye'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationOrders(PublicClass):
    """装修订单"""

    @classmethod
    def FindOrder(cls, test_order):
        """
        订单详情页找到指定订单号
        :param test_order: 订单号，必填项
        """
        first_order = cls().textId('textview_orderid')[6:]  # 获取首次进入时的订单号
        if first_order != test_order:  # 如果首次进入的订单号不是指定订单号
            if cls().driver.find_elements_by_id('btn_right1'):  # 如果有下个订单按钮
                while True:
                    cls().clickId('btn_right1')  # 点击下个订单
                    if cls().textId('textview_orderid')[6:] == test_order:  # 如果当前订单是指定订单
                        break  # 跳出循环
                    if cls().textId('textview_orderid')[6:] == first_order:  # 如果当前订单时首次进入时的订单
                        cls().assertEqual(test_order, cls().textId('textview_orderid')[6:],
                                          '当前账号无测试指定订单')  # 当前账号所有订单均不是指定订单
            else:  # 如果首次进入的订单号是指定订单号
                cls().assertEqual(test_order, first_order, '当前账号无测试指定订单')  # 验证是否找到指定订单

    @classmethod
    def OrderRecord(cls):
        """记录订单页测试"""
        cls().clickId('headerRight_img')  # 点击订单记录
        cls().assertEqual('订单记录', cls().textId('tv_header'), '"订单记录"页面header错误')  # 判断header
        cls().assertTrue(
            cls().driver.find_elements_by_id('tv_order_time') and cls().driver.find_elements_by_id('tv_owner'),
            '"订单记录"页面信息错误')  # 判断订单记录页相应信息
        cls().goBack()  # 返回

    @classmethod
    def DecorationBill(cls):
        """装修账单页测试"""
        cls().clickId('tv_zhuangxiuzhangdan')  # 点击装修账单
        cls().assertEqual('装修账单', cls().textId('tv_header'), '"装修账单"页面header错误')  # 判断header
        cls().assertTrue(cls().driver.find_elements_by_id('rl_total_amount'), '"装修账单"页面信息错误')  # 判断装修账单页相应信息
        cls().assertTrue(cls().driver.find_elements_by_id('rl_paid_amount'), '"装修账单"页面信息错误')  # 判断装修账单页相应信息
        cls().assertTrue(cls().driver.find_elements_by_id('ll_surplus_amount'), '"装修账单"页面信息错误')  # 判断装修账单页相应信息
        if cls().driver.find_elements_by_id('img_total_amount'):  # 如果有订单总金额
            cls().clickId('img_total_amount')  # 点击订单总金额
            cls().assertEqual('订单总金额', cls().textId('tv_header'), '"装修账单"-"订单总金额"页面header错误')  # 判断header
            cls().assertTrue(cls().driver.find_elements_by_id('tv_orderstate'), '"装修账单"-"订单总金额"页面信息错误')  # 判断订单总金额页相应信息
            cls().assertTrue(cls().driver.find_elements_by_id('tv_ordermon'), '"装修账单"-"订单总金额"页面信息错误')  # 判断订单总金额页相应信息
            cls().goBack()  # 返回
        if cls().driver.find_elements_by_id('img_paid_amount'):  # 如果有已付金额页
            cls().clickId('img_paid_amount')  # 点击已付金额
            cls().assertEqual('已付金额', cls().textId('tv_header'), '"装修账单"-"已付金额"页面header错误')  # 判断header
            cls().assertTrue(cls().driver.find_elements_by_id('tv_orderstate'), '"装修账单"-"已付金额"页面信息错误')  # 判断已付金额页相应信息
            cls().assertTrue(cls().driver.find_elements_by_id('tv_paidmon'), '"装修账单"-"已付金额"页面信息错误')  # 判断已付金额页相应信息
            cls().goBack()  # 返回
        cls().goBack()  # 返回

    @classmethod
    def DecorationDiary(cls, case_name='default'):
        """装修日记测试"""
        if case_name == 'default':
            diary_content, reply_content = conf.get('default', 'content'), conf.get('default', 'content')
        else:
            diary_content, reply_content = conf.get(case_name, 'diary_content'), conf.get(case_name, 'reply_content')
            if diary_content == '':
                diary_content = conf.get('default', 'content')
            if reply_content == '':
                reply_content = conf.get('default', 'content')
        cls().clickId('iv_gv_orderserver')  # 点击装修日记
        cls().assertEqual('我的装修日记', cls().textId('tv_header'), '"装修日记"页面header错误')  # 判断header
        if not cls().driver.find_elements_by_id('personphoto'):  # 如果没有日记
            cls().assertEqual('暂无日记', cls().textId('tx_nodiary'), '"装修日记"无日记时提示错误')  # 判断无日记时文案
        cls().clickId('img_right1')  # 点击写日记
        cls().assertEqual('写日记', cls().textId('tv_header'), '"装修日记"-"写日记"页面header错误')  # 判断header
        cls().clickId('tv_state')  # 点击选择日记状态
        stage = random.choice(
            ['前期沟通', '见面到场', '收房验房', '上门量房', '初步方案', '修改方案',
             '约看工地', '出详细方案', '开工交底', '房屋拆改', '水电施工', '防水施工',
             '瓦工施工', '木工施工', '油漆施工', '尾期施工'])  # 随机选择一项状态
        cls().clickName(stage)  # 点击某个状态
        s = str(random.randint(0, 1000))  # 设置一个随机数
        cls().inputId('et_content', diary_content + s)  # 输入日记文案
        cls().clickId('btn_right1', sleep_time)  # 点击发布
        if cls().driver.find_elements_by_id('btn_right1'):  # 如果发布失败
            i = 0  # 初始化循环变量
            while i <= refresh_count:  # 循环5次
                if i == refresh_count:  # 如果第5次提交均失败
                    cls().assertTrue(False, '"装修日记"-"写日记"多次提交失败，用例失败')  # 日记提交失败，用例失败
                    break  # 跳出循环
                else:
                    cls().clickId('btn_right1', sleep_time)  # 重新点击发布
                    if cls().driver.find_elements_by_id('btn_right1'):  # 如果提交失败
                        i += 1  # 循环变量+1
                    else:  # 如果提交成功
                        break  # 跳出循环
        cls().assertEqual(diary_content + s, cls().textId('praice'), '"装修日记"-"写日记"提交失败')  # 判断日记是否发布成功
        cls().assertEqual(stage, cls().textId('stage'), '"装修日记"-"写日记"提交失败')  # 判断日记是否发布成功
        cls().clickId('repaly_tx_yezhu')  # 点击回复业主
        cls().inputId('et_comment', reply_content)  # 输入回复内容
        cls().clickId('tv_send')  # 点击发布
        cls().assertEqual(reply_content, cls().textId('diarydetails'), '"装修日记"回复日记失败')  # 判断回复是否发布成功
        cls().clickId('diarydetails')  # 点击回复的详情，去删除回复
        cls().clickId('positiveButton')  # 点击确认
        cls().assertFalse(cls().driver.find_elements_by_xpath('//android.widget.FrameLayout[1]/\
        android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/\
        android.widget.RelativeLayout[2]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/\
        android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]'),
                          '"装修日记"删除日记回复失败')  # 判断回复是否删除成功

        cls().clickId('repaly_tx_yezhu')  # 再次点击回复业主
        cls().inputId('et_comment', reply_content)  # 输入回复内容
        cls().clickId('tv_send')  # 点击发布
        cls().assertEqual(reply_content, cls().textId('diarydetails'), '"装修日记"回复日记失败')  # 判断回复是否发布成功
        cls().clickId('delete_tx')  # 点击删除日记
        cls().clickId('positiveButton')  # 点击确认
        cls().assertNotEqual(diary_content + s, cls().textId('praice'), '"装修日记"删除日记失败')  # 判断日记是否发布成功
        cls().assertNotEqual(stage, cls().textId('stage'), '"装修日记"删除日记失败')  # 判断日记是否发布成功
        cls().goBack()  # 返回

    @classmethod
    def Design(cls):
        """设计图测试（原电商订单功能）"""
        cls().clickId('iv_gv_orderserver', elements_list_value=1)  # 点击设计图
        cls().assertEqual('设计图', cls().textId('tv_header'), '"设计图"页面header错误')  # 判断header
        cls().assertEqual('您目前没有设计效果图', cls().textId('tv_no_data'), '此订单为电商订单，非渠道移动店铺和手动添加订单')  # 判断没有设计图时文案
        cls().goBack()  # 返回

    @classmethod
    def ServiceTeam(cls):
        """服务团队测试"""
        cls().clickId('iv_gv_orderserver', elements_list_value=2)  # 点击服务团队
        cls().assertEqual('服务团队', cls().textId('tv_header'), '"服务团队"页面header错误')  # 判断header
        cls().assertTrue(cls().driver.find_elements_by_id('tv_serviceteam_item_right_name'),
                         '"服务团队"页面加载失败或该业主无服务团队')  # 判断服务团队相关信息
        cls().assertTrue(cls().driver.find_elements_by_id('tv_serviceteam_item_right_text'),
                         '"服务团队"页面加载失败或该业主无服务团队')  # 判断服务团队相关信息
        cls().clickId('tv_serviceteam_item_right_name', sleep_time)  # 点击首个服务人员
        cls().assertTrue(cls().driver.find_elements_by_name('装饰公司'), '"服务团队"详情页加载失败')  # 判断服务人员详情页相关信息
        cls().goBack(2)  # 返回

    @classmethod
    def MaterialList(cls):
        """材料清单测试（原电商订单功能）"""
        cls().clickId('iv_gv_orderserver', elements_list_value=3)  # 点击材料清单
        cls().assertEqual('材料清单', cls().textId('tv_header'), '"材料清单"页面header错误')  # header判断
        cls().assertEqual('您暂时没有材料清单', cls().textId('textView1'), '"材料清单"页面加载失败')  # 判断没有材料清单时文案
        cls().goBack()  # 返回

    @classmethod
    def NodeCalendar(cls):
        """节点日历测试（原电商订单功能）"""
        cls().clickId('iv_gv_orderserver', elements_list_value=4)  # 点击节点日历
        cls().assertEqual('装修订单', cls().textId('tv_header'),
                          '此订单为电商订单，非渠道移动店铺和手动添加订单')  # 此处应有toast提示判断，但目前无法实现，判断页面无跳转即可

    @classmethod
    def ElectronicContract(cls):
        """电子合同测试"""
        # cls().clickId('iv_gv_orderserver', elements_list_value=5)  # 点击电子合同
        # if cls().driver.find_elements_by_id('textview_orderid'):  # 如果此订单无电子合同
        #     cls().assertEqual('装修订单', cls().textId('tv_header'), '点击"电子合同"后页面跳转失败')  # 此处应有toast提示判断，但目前无法实现，判断页面无跳转即可
        # else:  # 如果此订单有电子合同
        #     cls().assertEqual('电子合同', cls().textId('tv_header'), '"电子合同"页面header错误')  # header判断
        #     cls().assertTrue(
        #         cls().driver.find_elements_by_id('tv_contract_deco_price', '"电子合同"-"验收单"模块加载失败'))  # 判断电子合同页相应信息
        #     cls().assertTrue(cls().driver.find_elements_by_id('tv_contract_item','"电子合同"-"验收单"模块加载失败'))  # 判断电子合同页相应信息
        #     cls().goBack()  # 返回
        #  2017.03.02——装修保业务停止
        cls().clickId('iv_gv_orderserver', elements_list_value=5)  # 点击电子合同
        cls().assertEqual('装修订单', cls().textId('tv_header'), '点击"电子合同"后页面跳转失败')  # 此处应有toast提示判断，但目前无法实现，判断页面无跳转即可

    @classmethod
    def AfterSalesService(cls):
        """售后维修测试（功能暂未开放）"""
        cls().clickId('iv_gv_orderserver', elements_list_value=6)  # 点击售后维修
        cls().assertEqual('装修订单', cls().textId('tv_header'), '点击"售后维修"后页面跳转失败')  # 此处应有toast提示判断，但目前无法实现，判断页面无跳转即可

    @classmethod
    def ComplaintsAndSuggestions(cls, case_name='default'):
        """投诉建议测试 """
        if case_name == 'default':
            complaints_content, reply_content = conf.get('default', 'content'), conf.get('default', 'content')
        else:
            complaints_content, reply_content = conf.get(case_name, 'complaints_content'), \
                                                conf.get(case_name, 'reply_content')
            if complaints_content == '':
                complaints_content = conf.get('default', 'content')
            if reply_content == '':
                reply_content = conf.get('default', 'content')
        cls().clickId('iv_gv_orderserver', elements_list_value=7)  # 点击投诉建议
        cls().assertEqual('投诉建议', cls().textId('tv_header'), '"投诉建议"页面header错误')  # header判断
        cls().assertEqual('我要投诉', cls().textId('tab_application'), '"投诉建议"页的tab标签错误')  # tab判断
        cls().assertEqual('投诉记录', cls().textId('tab_record'), '"投诉建议"页的tab标签错误')  # tab判断
        cls().clickId('tv_chooserepairtype')  # 点击投诉类型
        cls().clickId('tv_item_choose')  # 选择工程质量类
        cls().clickId('tv_choosecompanytype')  # 点击投诉公司
        cls().clickId('tv_item_choose')  # 选择第一个
        s = str(random.randint(0, 1000))  # 投诉内容
        cls().inputId('et_content', complaints_content + s)  # 输入投诉内容
        cls().clickId('btn_submit')  # 点击提交
        cls().assertTrue('textview_orderid', '"投诉建议"页面提交申诉失败')  # 判断提交申诉是否成功
        cls().clickId('iv_gv_orderserver', elements_list_value=7)  # 重新进入投诉建议页
        cls().clickId('tab_record')  # 点击投诉记录
        list_state = cls().textId('tv_state')  # 记录列表页的投诉状态
        cls().clickId('tv_state')  # 点击进入投诉详情页
        detail_state = cls().textId('header_progress_label')  # 记录详情页的投诉状态
        cls().assertEqual('投诉详情页', cls().textId('tv_header'), '"投诉详情"页面header错误')  # header判断
        cls().assertEqual(list_state, detail_state, '列表页和详情页状态不一致')  # 判断列表页和详情页状态
        cls().assertEqual(complaints_content + s, cls().textId('header_subject_content'), '"投诉建议"的投诉内容错误')  # 判断投诉内容是否正确
        cls().assertFalse(cls().driver.find_elements_by_id('reply_list_user_name_content'),
                          '"投诉建议"该条测试数据不是本次提交的数据')  # 判断重新打开申诉和确认已解决按钮
        cls().clickId('reply')  # 点击回复
        cls().inputId('et_input_answer', reply_content + s)  # 输入回复内容
        cls().clickId('btn_answer')  # 提交回复
        cls().assertTrue(cls().driver.find_elements_by_id('reply_list_user_name_content'), '"投诉建议"回复失败')  # 判断回复是否成功
        cls().assertFalse(cls().driver.find_elements_by_id('be_reply_list_user_name_content'),
                          '"投诉建议"该条测试数据不是本次提交的数据')  # 判断回复是否成功
        cls().clickId('reply_list_user_name_content')  # 点击回复业主
        cls().inputId('et_input_answer', reply_content + s)  # 输入回复业主内容
        cls().clickId('btn_answer')  # 提交回复
        cls().assertTrue(cls().driver.find_elements_by_id('be_reply_list_user_name_content'), '"投诉建议"回复失败')  # 判断回复是否成功
        cls().clickId('view_progress')  # 点击查看进度页
        cls().assertEqual('投诉进度', cls().textId('tv_header'), '"投诉进度"页面header错误')  # header判断
        cls().assertTrue(cls().driver.find_elements_by_id('tv_repairname'), '"投诉进度"页面模块加载失败')  # 判断查看进度页相应信息
        cls().clickId('btn_confirm')  # 点击确认已解决
        cls().clickId('ok')  # 点击确定
        cls().assertFalse(cls().driver.find_elements_by_id('btn_confirm'), '"投诉建议"确认已解决失败')  # 判断点击是否成功
        cls().goBack()  # 返回
        new_detail_state = cls().textId('header_progress_label')  # 记录新的详情页状态
        cls().assertNotEqual(new_detail_state, detail_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().goBack()  # 返回
        new_list_state = cls().textId('tv_state')  # 记录新的列表页状态
        cls().assertNotEqual(new_list_state, list_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().assertEqual(new_list_state, new_detail_state, '"投诉建议列表页"和"投诉建议详情页"状态不一致')  # 判断状态变更是否成功
        cls().clickId('tv_state')  # 点击进入投诉详情页
        cls().clickId('maintenance_details_bottom_ok')  # 点击重新打开投诉
        cls().clickId('ok')  # 点击确定
        cls().assertEqual(cls().textId('header_progress_label'), detail_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().assertNotEqual(cls().textId('header_progress_label'), new_detail_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().goBack()  # 返回
        cls().assertEqual(cls().textId('tv_state'), list_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().assertNotEqual(cls().textId('tv_state'), new_list_state, '"投诉建议"状态变更失败')  # 判断状态变更是否成功
        cls().goBack()  # 返回

    def test15_QD_Orders(self):
        """渠道订单测试"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertEqual('我的订单', self.textId('tv_header'), '"我的订单"页面header错误')  # 判断header
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.OrderRecord()  # 测试订单记录页
        self.DecorationBill()  # 测试装修账单页
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test16_QD_Orders_Diary(self):
        """渠道订单装修日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.DecorationDiary(case_name)  # 测试装修日记
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test17_QD_ComplaintsAndSuggestions(self):
        """渠道订单投诉建议"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.ComplaintsAndSuggestions(case_name)  # 测试投诉建议
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test18_QD_OtherModule(self):
        """渠道订单其他订单服务"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.Design()  # 测试设计图
        self.ServiceTeam()  # 测试服务团队
        self.MaterialList()  # 测试材料清单
        self.NodeCalendar()  # 测试节点日历
        self.ElectronicContract()  # 测试电子合同
        self.AfterSalesService()  # 测试售后维修
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test19_YDDP_Orders(self):
        """移动店铺订单测试"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.OrderRecord()  # 测试订单记录页
        self.DecorationBill()  # 测试装修账单页
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test20_YDDP_Orders_Diary(self):
        """移动店铺订单装修日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.DecorationDiary(case_name)  # 测试装修日记
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test21_YDDP_ComplaintsAndSuggestions(self):
        """移动店铺订单投诉建议"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.ComplaintsAndSuggestions(case_name)  # 测试投诉建议
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test22_YDDP_OtherModule(self):
        """移动店铺订单其他订单服务"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.Design()  # 测试设计图
        self.ServiceTeam()  # 测试服务团队
        self.MaterialList()  # 测试材料清单
        self.NodeCalendar()  # 测试节点日历
        self.ElectronicContract()  # 测试电子合同
        self.AfterSalesService()  # 测试售后维修
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test23_SDTJ_Orders(self):
        """手动添加订单测试"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.OrderRecord()  # 测试订单记录页
        self.DecorationBill()  # 测试装修账单页
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test24_SDTJ_Orders_Diary(self):
        """手动添加订单装修日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.DecorationDiary(case_name)  # 测试装修日记
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test25_SDTJ_ComplaintsAndSuggestions(self):
        """手动添加订单投诉建议"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.ComplaintsAndSuggestions(case_name)  # 测试投诉建议
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功

    def test26_SDTJ_OtherModule(self):
        """手动添加订单其他订单服务"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        test_order = conf.get(case_name, 'test_order')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if test_order == '':
            self.assertTrue(False, '测试订单号不能为空')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击我的订单
        self.assertTrue(self.driver.find_elements_by_id('rl_decorationorder'), '业主无"装修订单"')  # 判断是否有装修订单
        self.clickId('rl_decorationorder')  # 点击装修订单
        self.assertEqual('装修订单', self.textId('tv_header'), '"装修订单"页面header错误')  # 判断header
        self.FindOrder(test_order)  # 找到测试订单
        self.Design()  # 测试设计图
        self.ServiceTeam()  # 测试服务团队
        self.MaterialList()  # 测试材料清单
        self.NodeCalendar()  # 测试节点日历
        self.ElectronicContract()  # 测试电子合同
        self.AfterSalesService()  # 测试售后维修
        self.goBack(2)  # 返回
        self.assertHomepage()  # 检查返回首页是否成功


class CommodityOrders(PublicClass):
    """商品订单"""

    def test27_FilterTab(self):
        """商品订单筛选栏"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击订单
        self.assertEqual('我的订单', self.textId('tv_header'), '"我的订单"页面header错误')  # 判断header
        self.assertTrue(self.driver.find_elements_by_id('rl_productorder'), '业主无"商品订单"')  # 判断是否有商品订单
        self.clickId('rl_productorder')  # 点击商品订单
        self.assertEqual('商品订单', self.textId('tv_header'), '"商品订单"页面header错误')  # 判断header
        self.assertEqual('全部', self.textId('tv_all_goods'), '"商品订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('待付款', self.textId('tv_unpay'), '"商品订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('待发货', self.textId('tv_undeliver_goods'), '"商品订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('待收货', self.textId('tv_unreceipt'), '"商品订单"筛选项错误')  # 判断4个筛选项
        self.clickId('tv_unpay')  # 点击待付款
        self.assertEqual('您还没有相关订单', self.textId('tv_no_order'), '"商品订单"订单状态错误')  # 筛选结果判断
        self.clickId('tv_undeliver_goods')  # 点击待发货
        self.assertEqual('买家已付款', self.textId('tv_state'), '"商品订单"订单状态错误')  # 筛选结果判断
        self.clickId('tv_unreceipt')  # 点击待收货
        self.assertEqual('您还没有相关订单', self.textId('tv_no_order'), '"商品订单"订单状态错误')  # 筛选结果判断
        self.goBack(2)  # 返回首页
        self.assertHomepage()  # 检查返回首页是否成功

    def test28_OrdersDetail(self):
        """商品订单详情"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_order')  # 点击订单
        self.assertTrue(self.driver.find_elements_by_id('rl_productorder'), '业主无"商品订单')  # 判断是否有商品订单
        self.clickId('rl_productorder')  # 点击商品订单
        self.assertEqual('商品订单', self.textId('tv_header'), '"商品订单"页面header错误')  # 判断header
        list_info = [self.textId('tv_name'), self.textId('tv_state'), self.textId('tv_des'), self.textId('tv_price'),
                     self.textId('tv_price_old')]  # 列表页信息
        self.clickId('iv_pic')  # 点击进入详情页
        self.assertEqual('订单详情', self.textId('tv_header'), '"商品订单详情"页面header错误')  # 判断顶部header
        detail_info = [self.textId('tv_productname'), self.driver.find_element_by_name('买家已付款').text,
                       self.textId('etv_description'), self.textId('tv_currentprice'),
                       self.textId('tv_oldprice')]  # 详情页信息
        self.assertEqual(list_info, detail_info, '"商品订单列表页"和"商品订单详情页"信息不一致')  # 判断列表页与详情页信息是否一致
        self.clickId('iv_img', sleep_time)  # 进入商品详情页
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '"商品订单详情"页面加载失败')  # 判断wap页加载成功
        self.assertEqual('商品详情', self.textId('tv_header'), '"商品订单详情"页面header错误')  # 判断顶部header
        self.goBack(4)  # 返回列表页
        self.assertHomepage()


class VoucherOrders(PublicClass):
    """代金券订单"""

    def test29_FilterTab(self):
        """代金券订单筛选栏"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)  # 登陆测试账号
        self.clickId('iv_order')  # 点击订单
        self.assertEqual('我的订单', self.textId('tv_header'), '"我的订单"页面header错误')  # 判断header
        self.assertTrue(self.driver.find_elements_by_id('rl_voucherorder'), '业主无"代金券订单')  # 判断是否有代金券订单
        self.clickId('rl_voucherorder')  # 点击进入代金券订单列表页
        self.assertEqual('代金券订单', self.textId('tv_header'), '"代金券订单"header错误')  # 判断header
        self.assertEqual('全部', self.textId('tv_all_order'), '"代金券订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('待付款', self.textId('tv_unpay'), '"代金券订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('待兑换', self.textId('tv_unexchange'), '"代金券订单"筛选项错误')  # 判断4个筛选项
        self.assertEqual('退款/售后', self.textId('tv_paid'), '"代金券订单"筛选项错误')  # 判断4个筛选项
        self.clickId('tv_unpay')  # 点击待付款
        self.assertEqual('您还没有相关订单', self.textId('tv_no_order'), '"代金券订单"订单状态错误')  # 当前账号无待付款订单
        self.clickId('tv_unexchange')  # 点击待兑换
        self.assertEqual('待兑换', self.textId('tv_state', 0), '"代金券订单"订单状态错误')  # 订单筛选错误
        self.clickId('tv_paid')  # 点击退款/售后
        self.assertEqual('您还没有相关订单', self.textId('tv_no_order'), '"代金券订单"订单状态错误')  # 当前账号无退款/售后订单
        self.goBack(2)  # 返回首页
        self.assertHomepage()  # 判断是否返回首页成功

    def test30_OrdersDetail(self):
        """代金券订单详情"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_order')  # 点击订单
        self.assertTrue(self.driver.find_elements_by_id('rl_voucherorder'), '业主无"代金券订单"')  # 判断是否有代金券订单
        self.clickId('rl_voucherorder')  # 点击进入代金券订单列表页
        self.assertEqual('代金券订单', self.textId('tv_header'), '"代金券订单"header错误')  # 判断header
        list_info = [self.textId('tv_name'), self.textId('tv_des'), self.textId('tv_price'),
                     self.textId('tv_price_old')]  # 列表页信息
        list_state = self.textId('tv_state')  # 列表页状态
        self.clickId('iv_pic')  # 点击进入详情页
        self.assertEqual('订单详情', self.textId('tv_header'), '"代金券订单详情页"header错误')  # 判断顶部header
        detail_info = [self.textId('tv_productname'), self.textId('tv_description'), self.textId('tv_currentprice'),
                       self.textId('tv_oldprice')]  # 详情页信息
        self.assertEqual(list_info, detail_info, '"代金券订单列表页"和"代金券订单详情页"信息不一致')  # 判断列表页与详情页信息是否一致
        detail_state = self.textId('tv_vo_state')  # 详情页状态
        if list_state == '交易成功':
            self.assertEqual('已完成', detail_state, '"代金券订单列表页"和"代金券订单详情页"信息不一致')
        elif list_state == '待兑换':
            self.assertEqual('待兑换', detail_state, '"代金券订单列表页"和"代金券订单详情页"信息不一致')
        else:
            self.assertEqual(list_state, detail_state, '"代金券订单列表页"和"代金券订单详情页"信息不一致')  # 判断详情页与列表页订单状态是否一致
        self.clickId('iv_img', sleep_time)  # 点击代金券进入代金券详情页
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '"代金券订单详情"页面加载失败')  # 判断wap页加载成功
        self.assertEqual('商品详情', self.textId('tv_header'), '"代金券订单详情"页面header错误')  # 判断顶部header
        self.goBack(4)  # 返回列表页
        self.assertHomepage()


if __name__ == '__main__':
    unittest.main()
