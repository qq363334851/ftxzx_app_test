# coding = utf-8
# __author__ = 'peidongxue'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class Diary(PublicClass):
    """装修日记"""

    @classmethod
    def clickRewriteDiary(cls):
        """点击续写日记"""
        cls().clickId("rl_home_diary")  # 点击日记按钮
        cls().clickId("iv_write")  # 点击右上角的编辑按钮
        cls().clickId("ll_writing_diary")  # 点击续写日记

    @classmethod
    def editDiary(cls, case_name='default'):
        """编辑日记"""
        if case_name == 'default':
            diary_content = conf.get('default', 'content')
        else:
            diary_content = conf.get(case_name, 'diary_content')
            if diary_content == '':
                diary_content = conf.get('default', 'content')
        cls().inputId("et_diarycontent", diary_content)  # 输入日记内容
        cls().clickId("rl_decoration_stage")  # 选择装修阶段
        stage = random.choice(
            ['开工交底', '房屋拆改', '水电施工', '防水施工', '瓦工施工', '木工施工', '油漆施工', '尾期施工', '软装', '入住'])
        cls().clickName(stage)
        cls().clickId("btn_right1")
        cls().clickId("rl_decoration_label")  # 选择装修标签
        cls().clickId('tv_tag',
                      elements_list_value=random.randint(0, len(cls().driver.find_elements_by_id('tv_tag')) - 1))
        cls().clickId("btn_right1")
        cls().clickId("btn_right1")  # 保存日记
        if cls().driver.find_elements_by_name("取消"):
            cls().clickName("取消")  # 将分享窗口关闭
        cls().assertTrue(cls().driver.find_elements_by_id("header"), '"编辑日记"成功后未跳转到"日记发布"页面')  # 验证日记发布后，是否成功跳转到日记发布页面

    @classmethod
    def like(cls):
        """点赞"""
        while not cls().driver.find_elements_by_id("list_center_point_like_interaction_number"):
            # 如果没有找到点赞按钮，上滑1次，没有找到继续上滑
            cls().swipeUp()  # 上滑1次
        before_like = cls().textId("list_center_point_like_interaction_number")  # 获取当前点赞数
        cls().clickId("list_center_point_like_interaction")  # 点赞
        after_like = cls().textId("list_center_point_like_interaction_number")  # 获取点赞后的点赞数
        # 如果点赞或者取消点赞之后，点赞数量不一样，证明成功，如果点赞数量还是一样的，证明点赞失败
        cls().assertNotEqual(before_like, after_like, '对日记"点赞"或"取消点赞"失败')

    def test51_TwoTab(self):
        """日记顶部Tab"""
        self.clickId("rl_home_diary", sleep_time)  # 点击日记按钮
        self.assertTrue(self.driver.find_elements_by_id("iv_write"), '"日记"页面跳转失败')  # 验证日记页面跳转成功
        self.clickId("tv_selection_diary", sleep_time)  # 点击精选
        self.assertTrue(self.driver.find_element_by_id('tv_selection_diary').is_selected(),
                        '点击"精选"后icon未变亮')  # 点击精选跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_new_diary').is_selected(), '点击"最新"后icon未变暗')  # 点击精选跳转验证
        self.assertTrue(self.driver.find_element_by_id("imageView_tupian"), '"精选"页面跳转失败')  # 验证精选页面跳转
        self.swipeUp(2)  # 屏幕向上滑动两次
        self.clickId("tv_new_diary")  # 点击最新
        self.assertFalse(self.driver.find_element_by_id('tv_selection_diary').is_selected(),
                         '点击"精选"后icon未变暗')  # 点击最新跳转验证
        self.assertTrue(self.driver.find_element_by_id('tv_new_diary').is_selected(), '点击"最新"后icon未变亮')  # 点击最新跳转验证
        self.assertTrue(self.driver.find_element_by_id("imageView_tupian"), '"精选"页面跳转失败')  # 验证精选页面跳转
        self.swipeUp(2)  # 屏幕向上滑动两次
        self.goBack()  # 返回首页
        self.assertHomepage()  # 返回首页是否成功

    def test52_CheckNewDiary(self):
        """最新日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId("rl_home_diary", sleep_time)  # 点击日记
        self.clickId("imageView_tupian", sleep_time)  # 点击最新的第一条日记
        self.assertTrue(self.driver.find_elements_by_id("header"), '"最新日记"页面跳转失败')  # 验证最新日记页面跳转
        self.like()  # 调用点赞方法
        self.goBack(2)  # 返回2次到首页
        self.assertHomepage()  # 验证返回首页是否成功

    def test53_CheckSelectionDiary(self):
        """精选日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId("rl_home_diary", sleep_time)  # 点击日记
        self.clickId("tv_selection_diary", sleep_time)  # 点击精选
        self.clickId("imageView_tupian", sleep_time)  # 点击精选的第一条日记
        self.assertTrue(self.driver.find_elements_by_id("header"), '"精选日记"页面跳转失败')  # 验证精选日记页面跳转
        """
        self.clickId("navigation_bar_button")  # 点击左下角的红色按钮，出现装修节点
        self.assertTrue(self.driver.find_elements_by_id("title_layout"), "装修节点未显示")  # 验证装修节点是否显示
        self.clickId("title_layout")  # 点击装修节点（这里应该写一个循环，后面再优化）
        self.assertEqual(self.textId("stickylist_header"), "开工交底", "装修节点断言失败")  # 点击装修节点，查看跳转是否正确
        """
        self.like()  # 调用点赞方法
        self.goBack(2)  # 返回2次到首页
        self.assertHomepage()  # 验证返回首页是否成功

    def test54_WriteDiary(self):
        """新建日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        diary_title = conf.get(case_name, 'diary_title')
        diary_estate = conf.get(case_name, 'diary_estate')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if diary_title == '':
            diary_title = conf.get('default', 'content')
        if diary_estate == '':
            diary_estate = conf.get('default', 'content')
        self.login(usr, psw)
        self.clickId("rl_home_diary")  # 点击日记按钮
        self.clickId("iv_write")  # 点击右上角的编辑按钮
        self.clickId("ll_new_diary")  # 点击新建日记
        self.assertEqual(self.textId("tv_header"), "编辑日记信息", '"编辑日记信息"页面header错误')  # 验证是否成功跳转到编辑日记信息页面
        self.inputId("et_title", diary_title)  # 输入日记标题
        self.inputId("et_area", str(random.randint(10, 1000)))  # 输入面积
        self.clickId("rlyt_house_size")  # 选择户型
        huxing = random.choice(
            ['小户型', '一居室', '二居室', '三居室', '四居室', '复式', '跃层', '别墅'])
        self.clickName(huxing)  # 选择户型
        self.clickId("btn_right1")  # 点击保存
        self.clickId("rlyt_decoration_style")  # 选择装修风格
        fengge = random.choice(
            ['地中海风格', '东南亚风格', '混搭风格', '简欧风格', '日韩风格', '田园风格', '现代风格', '简约风格', '中式风格'])
        self.clickName(fengge)  # 选择户型
        self.clickId("btn_right1")  # 点击保存
        yusuan = str(random.randint(1, 30))
        self.inputId("et_budget", yusuan)  # 输入预算
        self.inputId("et_estate_name", diary_estate)  # 输入小区名称
        self.clickId("btn_right1")  # 点击下一步
        self.assertEqual(self.textId("tv_header"), "创建日记", '"创建日记"页面header错误')  # 验证是否正常跳转到创建日记页面
        self.editDiary(case_name)  # 调用编辑日记方法
        self.assertIn(yusuan, self.textId("header_decoration_price"), "装修预算发布未成功")
        self.assertIn(huxing, self.textId("header_room_type"), "户型发布未成功")
        self.assertIn(fengge, self.textId("header_design_style"), "装修风格发布未成功")
        self.goBack(2)
        self.assertHomepage()
        # 日记详情页的操作不用写，在续写日记用例里面覆盖了，开发调用的是一个类

    def test55_ContinueWriteDiaryInList(self):
        """日记列表页-续写日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickRewriteDiary()  # 调用点击续写日记按钮的方法
        self.assertEqual(self.textId("tv_header"), "我的日记", '"我的日记"页面header错误')  # 验证点击续写日记，是否成功跳转
        self.clickId("tv_continue_towrite")  # 点击日记列表页的续写日记
        self.assertEqual(self.textId("tv_header"), "续写日记", '"续写日记"页面header错误')
        self.editDiary()  # 调用编辑日记方法
        self.goBack(3)
        self.assertHomepage()

    def test56_ContinueWriteDiaryInDetails(self):
        """日记详情页-续写日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickRewriteDiary()  # 调用点击续写日记按钮方法
        self.assertEqual(self.textId("tv_header"), "我的日记", '"我的日记"页面header错误')  # 验证点击续写日记，是否成功跳转
        self.clickId("iv_content_img")  # 点击我的日记列表第一条日记
        self.clickId("iv_mydiary_modification")  # 点击右上角的三个点
        self.clickId("tv_writing_diary")  # 点击续写日记
        self.editDiary(case_name)  # 调用编辑日记方法
        self.goBack(3)
        self.assertHomepage()

    def test57_Edit(self):
        """编辑日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickRewriteDiary()  # 调用点击续写日记按钮方法
        self.assertEqual(self.textId("tv_header"), "我的日记", '"我的日记"页面header错误')  # 验证点击续写日记，是否成功跳转
        self.clickId("iv_content_img")  # 点击我的日记列表第一条日记
        self.assertTrue(self.driver.find_elements_by_id("header_user_title"), '"日记详情页"跳转失败')  # 判断点击日记列表后，是否成功跳转到日记详情页
        # 日记详情页中间的编辑功能，如果页面中间有编辑按钮，则点击编辑按钮，调用编辑方法；如果页面中间没有编辑按钮，则点击撰写日记按钮
        if self.driver.find_elements_by_id("tv_my_edit"):
            self.clickId("tv_my_edit")
            self.editDiary(case_name)
        else:
            self.clickId("tv_btn_diary")  # 如果页面没有编辑按钮，点击撰写日记按钮
            self.assertEqual(self.textId("tv_header"), "续写日记", '"续写日记"页面header错误')
            self.editDiary(case_name)  # 调用编辑日记方法
        # 日记详情页右上角的编辑日记功能
        self.clickId("iv_mydiary_modification")  # 点击右上角的三个点
        self.clickId("tv_modify_housing_information")  # 点击编辑日记信息按钮
        self.assertTrue(self.driver.find_elements_by_name("编辑日记"), '"编辑日记"页面跳转失败')
        self.editDiary(case_name)  # 调用编辑日记方法
        self.goBack(3)
        self.assertHomepage()

    def test58_DeleteDiary(self):
        """删除日记"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickRewriteDiary()  # 调用点击续写日记按钮方法
        self.assertEqual(self.textId("tv_header"), "我的日记", '没有找到"我的日记"字段，未成功跳转到我的日记页')  # 验证点击续写日记，是否成功跳转
        self.clickId("iv_content_img", sleep_time)  # 点击我的日记列表第一条日记
        self.assertTrue(self.driver.find_elements_by_id("header_user_title"), "未成功跳转到日记详情页")  # 判断点击日记列表后，是否成功跳转到日记详情页
        if self.driver.find_elements_by_id("tv_my_delete"):
            self.clickId("tv_my_delete")  # 删除明细，这里应该写分支
            self.clickId("tv_cancel")  # 点击取消，仍然保留在当前页面
            self.assertTrue(self.driver.find_elements_by_id("tv_my_delete"), "保留日记明细页未成功")  # 点击取消后，验证是否取消成功，保留在当前明细页面
            self.clickId("tv_my_delete")
            self.clickId("tv_ok_delete")  # 确认删除
            self.assertFalse(self.driver.find_elements_by_id("tv_my_delete"), "删除日记未成功")
            self.clickId("iv_mydiary_modification")
            self.clickId("tv_delete_diary")  # 删除整条日记
            self.clickId("tv_ok_delete")
            self.assertEqual(self.textId("tv_header"), "我的日记", "未成功跳转到我的日记列表页")  # 删除成功，跳转到我的日记页面
        else:
            self.clickId("iv_mydiary_modification")
            self.clickId("tv_delete_diary")  # 删除整条日记
            self.clickId("tv_ok_delete", sleep_time)
            self.assertEqual(self.textId("tv_header"), "我的日记", "未成功跳转到我的日记列表页")  # 删除成功，跳转到我的日记页面
        self.goBack(2)
        self.assertHomepage()

    def test59_SlideTab(self):
        """最新-精选滑动切换"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId("rl_home_diary",)
        self.swipeLeft()  # 在最新页面，向左滑动屏幕，然后验证精选按钮是否还可以再次点击
        self.assertTrue(self.driver.find_element_by_id('tv_selection_diary').is_selected(), '滑动后"精选icon"未变亮')
        self.swipeRight()
        self.assertTrue(self.driver.find_element_by_id('tv_new_diary').is_selected(), '滑动后"最新icon"未变亮')
        self.goBack()
        self.assertHomepage()

    def test60_CancelEdit(self):
        """取消编辑"""
        # 在新建日记页面取消编辑
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId("rl_home_diary")  # 点击日记按钮
        self.clickId("iv_write")  # 点击右上角的编辑按钮
        self.clickId("ll_new_diary")  # 点击新建日记
        self.assertEqual(self.textId("tv_header"), "编辑日记信息", '没有找到"编辑日记信息"字段，跳转编辑日记信息页面失败')  # 验证是否成功跳转到编辑日记信息页面
        self.clickId("btn_back")  # 点击取消按钮
        self.assertTrue(self.driver.find_elements_by_id("tv_cancel_content"), "未弹出取消编辑确认窗体")  # 验证是否弹出取消编辑确认窗体
        self.clickId("cancel")
        self.assertEqual(self.textId("tv_header"), "编辑日记信息", "跳转到编辑日记信息页面未成功")  # 验证是否成功跳转到编辑日记信息页面
        self.clickId("btn_back")  # 点击取消按钮
        self.clickId("ok")
        self.assertTrue(self.driver.find_elements_by_id("tv_new_diary"), "取消编辑未成功，没有跳转回日记页面")


if __name__ == '__main__':
    unittest.main()
