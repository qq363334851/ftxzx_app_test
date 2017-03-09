# coding = utf-8
# __author__ = 'linye'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationPicture(PublicClass):
    """装修美图"""

    def test09_ThreeTab(self):
        """装修美图顶部Tab"""
        self.clickId('iv_home_inspiration')  # 点击图库
        self.assertTrue(self.driver.find_element_by_id('iv_home_inspiration').is_selected(), '装修美图"页面跳转失败')  # 验证页面跳转
        self.clickId('tv_header_middle')  # 点击套图
        self.assertTrue(self.driver.find_element_by_id('tv_header_middle').is_selected(),
                        '"装修美图"页面"套图icon"点击后未变亮')  # 点击套图跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_left').is_selected(),
                         '"装修美图"页面"精选icon"在点击"套图"后未变暗')  # 点击套图跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_right').is_selected(),
                         '"装修美图"页面"单图icon"在点击"套图"后未变暗')  # 点击套图跳转验证
        self.assertEqual(self.textId('filter_tv_1'), '风格', '"装修美图"页面"套图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_2'), '居室', '"装修美图"页面"套图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_3'), '面积', '"装修美图"页面"套图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_4'), '总价', '"装修美图"页面"套图"的筛选栏加载失败')  # 验证页面跳转
        self.clickId('tv_header_right')  # 点击单图
        self.assertTrue(self.driver.find_element_by_id('tv_header_right').is_selected(),
                        '"装修美图"页面"单图icon"点击后未变亮')  # 点击单图跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_left').is_selected(),
                         '"装修美图"页面"精选icon"在点击"单图"后未变暗')  # 点击单图选跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_middle').is_selected(),
                         '"装修美图"页面"套图icon"在点击"单图"后未变暗')  # 点击单图跳转验证
        self.assertEqual(self.textId('filter_tv_1'), '风格', '"装修美图"页面"单图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_2'), '功能间', '"装修美图"页面"单图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_3'), '局部', '"装修美图"页面"单图"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('filter_tv_4'), '颜色', '"装修美图"页面"单图"的筛选栏加载失败')  # 验证页面跳转
        self.clickId('tv_header_left')  # 点击精选
        self.assertTrue(self.driver.find_element_by_id('tv_header_left').is_selected(),
                        '"装修美图"页面"精选icon"点击后未变亮')  # 点击精选跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_right').is_selected(),
                         '"装修美图"页面"套图icon"在点击"精选"后未变暗')  # 点击精选跳转验证
        self.assertFalse(self.driver.find_element_by_id('tv_header_middle').is_selected(),
                         '"装修美图"页面"单图icon"在点击"精选"后未变暗')  # 点击精选跳转验证
        self.assertEqual(self.textId('tv_choosestyle'), '风格', '"装修美图"页面"精选"的筛选栏加载失败')  # 验证页面跳转
        self.assertEqual(self.textId('tv_choosespace'), '户型', '"装修美图"页面"精选"的筛选栏加载失败')  # 验证页面跳转
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test10_PictureFilter(self):
        """美图筛选"""
        self.clickId('tv_home_inspiration')  # 点击图库
        jx_before_name = self.textId('tv_inspiration_name')  # 筛选前案例名
        self.clickId('tv_choosestyle')  # 点击筛选风格
        self.clickName('美式')  # 选择"美式"
        self.clickId('tv_choosespace')  # 点及筛选户型
        self.clickName('公寓')  # 选择"公寓"
        jx_after_name = self.textId('tv_inspiration_name')  # 筛选后案例名
        self.assertNotEqual(jx_before_name, jx_after_name, '筛选失败')  # 验证是否相同，相同则筛选失败

        self.clickId('tv_header_middle')  # 点击套图
        tt_before_name = self.textId('tv_left_two')  # 筛选前案例名
        self.clickId('filter_tv_1')  # 点击筛选风格
        self.clickName('混搭')  # 选择"混搭"
        self.clickId('filter_tv_2')  # 点及筛选居
        self.clickName('一居室')  # 选择"一居室"
        self.clickId('filter_tv_3')  # 点及筛选面积
        self.clickName('40以下')  # 选择"40以下"
        self.clickId('filter_tv_4')  # 点及筛选总价
        self.clickName('2万以下')  # 选择"2万以下"
        tt_after_name = self.textId('tv_left_two')  # 筛选后案例名
        self.assertNotEqual(tt_before_name, tt_after_name, '筛选失败')  # 验证是否相同，相同则筛选失败

        self.clickId('tv_header_right')  # 点击单图
        dt_before_name = self.textId('tv_left_two')  # 筛选前案例名
        self.clickId('filter_tv_1')  # 点击筛选风格
        self.clickName('现代')  # 选择"现代"
        self.clickId('filter_tv_2')  # 点及筛选功能键
        self.clickName('客厅')  # 选择"客厅"
        self.clickId('filter_tv_3')  # 点及筛选局部
        self.clickName('背景墙')  # 选择"背景墙"
        self.clickId('filter_tv_4')  # 点及筛选颜色
        self.clickName('白色')  # 选择"白色"
        dt_after_name = self.textId('tv_left_two')  # 筛选后案例名
        self.assertNotEqual(dt_before_name, dt_after_name, '筛选失败')  # 验证是否相同，相同则筛选失败
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test11_PictureDetail(self):
        """装修美图-精选详情页"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        comment_content = conf.get(case_name, 'comment_content')
        name = conf.get(case_name, 'name')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        if comment_content == '':
            comment_content = conf.get('default', 'content')
        if name == '':
            name = conf.get('default', 'content')
        self.login(usr, psw)  # 由于需要测试报名，此处需要登陆账号
        self.clickId('tv_home_inspiration')  # 点击图库
        self.clickId('tv_header_left')  # 点击精选
        self.clickId('tv_inspiration_name', sleep_time)  # 点击案例进入详情页
        self.assertTrue(self.driver.find_elements_by_id('img_right2'), '"装修美图"-"精选"详情页加载失败')  # 验证详情页加载是否成功
        self.swipeUp(30)  # 向上滑动30次
        self.clickId('tv_comment')  # 点击"有话说"
        self.clickId('btn_right1')  # 点击"我要评论"
        self.inputId('et_content', comment_content)  # 输入评论内容
        self.clickId('btn_right1')  # 发布评论
        self.assertEqual(comment_content, self.textId('tv_content'), '"装修美图"-"精选"评论（有话说）失败')  # 验证评论是否发布成功
        self.goBack()  # 返回
        self.clickId('tv_apply')  # 点击申请免费设计
        self.inputId('et_name', name)  # 输入业主姓名
        self.clickId('tv_appoitment')  # 点击免费申请
        self.assertEqual('申请成功', self.textId('tv_success'), '"装修美图"-"精选""申请免费设计"失败')  # 验证是否报名成功
        self.goBack()  # 返回
        self.clickId('iv_inspirationPic')  # 点击详情页图片
        self.assertTrue(self.driver.find_elements_by_id('iv_inspiration'), '大图页加载失败')  # 跳转至大图页
        before_header = self.textId('tv_header')  # 获取当前页码
        #  保存图片测试目前无法实现
        self.swipeRight(3)  # 右滑3次
        after_header = self.textId('tv_header')  # 获取当前页码
        self.assertNotEqual(before_header, after_header, '翻页失败')  # 验证翻页是否成功
        self.swipeLeft(4)  # 左滑4次
        self.assertTrue(self.driver.find_elements_by_id('guesslike_tv'), '"装修美图"-"精选"-"猜你喜欢"加载失败')  # 验证猜你喜欢加载是否成功
        before_title = self.textId('youlike_tv').replace(' ', '')  # 猜你喜欢标题
        self.clickId('youlike_tv', sleep_time)  # 点击第一个猜你喜欢
        after_title = self.textId('tv_title')  # 猜你喜欢标题
        self.assertEqual(before_title, after_title, '"装修美图"-"精选"-"猜你喜欢"，点击后跳转失败')  # 验证猜你喜欢跳转是否成功
        self.goBack(2)  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test12_MultiGraphDetail(self):
        """装修美图-套图详情页"""
        self.clickId('tv_home_inspiration')  # 点击图库
        self.clickId('tv_header_middle')  # 点击套图
        self.clickId('tv_left_two', sleep_time)  # 点击第一个套图
        self.assertTrue(self.driver.find_elements_by_id('pic_share_iv'), '"装修美图"-"套图详情页"加载失败')  # 验证套图详情页加载是否成功
        before_header = self.textId('tv_currentpic')  # 获取当前页码
        self.swipeLeft()  # 左滑1次
        after_header = self.textId('tv_currentpic')  # 获取当前页码
        self.assertNotEqual(before_header, after_header, '"装修美图"-"套图详情页"翻页失败')  # 验证翻页是否成功
        self.swipeLeft(20)  # 左滑20次
        self.assertEqual(self.textId('tv_currentpic'), self.textId('tv_totalpic'),
                         '"装修美图"-"套图详情页"翻页不是最后一页')  # 验证滑动后是否为最后一页
        if self.driver.find_elements_by_name('点击查看'):
            self.clickName('点击查看')  # 点击"点击查看"
            self.assertTrue(self.driver.find_elements_by_id('btn_right1'),
                            '"装修美图"-"套图详情页"-"点击查看"跳转wap页失败')  # 验证跳转wap页是否成功
            self.goBack()  # 返回套图详情页
        self.goBack(2)  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test13_SingleGraphDetail(self):
        """装修美图-单图详情页"""
        self.clickId('tv_home_inspiration')  # 点击图库
        self.clickId('tv_header_right')  # 点击单图
        before_title = self.textId('tv_left_two')  # 获取当前页面第一个单图标题
        self.clickId('tv_left_two', sleep_time)  # 点击单图，进入详情页
        self.assertTrue(self.driver.find_elements_by_id('pic_share_iv'), '"装修美图"-"单图详情页"加载失败')  # 验证详情页是否跳转成功
        self.assertTrue(self.driver.find_elements_by_id('tv_freedesign'), '"装修美图"-"单图详情页"加载失败')  # 验证详情页是否跳转成功
        self.swipeLeft(10)  # 向左滑动10次
        self.goBack()  # 返回单图列表页
        after_title = self.textId('tv_left_two')  # 获取当前页面第一个单图标题
        self.assertNotEqual(before_title, after_title, '"装修美图"-"单图列表页跳转失败')  # 验证单图详情页滑动后，返回列表页定位位置是否正确
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test14_PictureSearch(self):
        """美图搜索"""
        self.clickId('tv_home_inspiration')  # 点击图库
        self.clickId('tv_header_left')  # 点击精选
        self.clickId('img_right')  # 点击搜索
        self.assertEqual('搜索美图', self.textId('et_nav_search'), '"装修美图"搜索栏沉底文字错误')  # 判断搜索栏沉底文字
        self.inputId('et_nav_search', '美')  # 输入搜索关键词
        self.clickId('tv_deco_ask_search_item')  # 点击联想词进行搜索
        self.assertEqual('美式', self.textId('et_search'), '"装修美图"搜索结果错误')  # 判断搜索结果
        self.assertTrue(self.driver.find_elements_by_id('iv_inspirationPic'), '"装修美图"搜索结果错误')  # 判断搜索结果
        self.clickId('tv_cancel')  # 点击取消
        self.assertTrue(self.driver.find_elements_by_id('img_right'), '"装修美图"-"搜索结果页"点击取消，返回失败')  # 判断返回是否成功
        self.clickId('img_right')  # 点击搜索
        self.clickId('butt_clean_search_history')  # 点击清除历史记录
        self.clickId('btn_ok')  # 点击确定
        self.assertFalse(self.driver.find_elements_by_id('rel1'), '装修美图"-"搜索结果页"清空历史搜索失败')  # 判断清除历史记录是否成功
        self.clickId('tv_nav_search_cancel')  # 点击取消
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功


if __name__ == '__main__':
    unittest.main()
