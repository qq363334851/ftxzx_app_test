# coding = utf-8
# __author__ = 'linye'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class Homepage(PublicClass):
    """首页"""

    def test01_LoginAndAdvertisement(self):
        """登陆和广告"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.logout()
        if self.driver.find_elements_by_id('iv_jiaju_home_ad_close'):
            self.swipeRight(5)  # 向右滑动5次
            self.swipeLeft(5)  # 向左滑动5次
            self.clickId('iv_jiaju_home_ad_close')  # 关闭广告
            self.assertFalse(self.driver.find_elements_by_id('iv_jiaju_home_ad_close'), '首页"广告轮播图"关闭失败')  # 验证广告是否关闭

    def test02_CityAndHomeModule(self):
        """城市和首页模块"""
        self.clickId('ll_dingwei')  # 点击左上角切换城市
        self.assertEqual('北京', self.textId('tv1'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('上海', self.textId('tv2'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('广州', self.textId('tv3'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('深圳', self.textId('tv4'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('武汉', self.textId('tv5'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('宁波', self.textId('tv6'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('苏州', self.textId('tv7'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('重庆', self.textId('tv8'), '城市列表中"热门城市"错误')  # 验证热门城市
        self.assertEqual('A', self.textId('tv_switch_city_item_index'), '城市字母错误')  # 验证城市字母
        self.clickId('tv2', sleep_time)  # 点击热门城市"上海"
        self.assertEqual('上海', self.textId('tv_city_home'), '切换城市失败')  # 验证选择城市是否成功
        self.assertEqual('-买建材-', self.textId('tv_item_jiaju_category'), '首页"代金券"模块加载失败')  # 验证代金券模块
        self.assertTrue(self.driver.find_elements_by_id('tv_headline_news_1'), '首页"装修头条"模块加载失败')  # 验证装修头条模块
        self.clickId('ll_dingwei')  # 点击左上角切换城市
        self.clickId('tv1', sleep_time)  # 点击热门城市"北京"
        self.assertEqual('-建材特卖汇-', self.textId('tv_item_jiaju_category'), '首页"建材特卖汇"模块加载失败')  # 验证建材特卖汇模块
        self.assertTrue(self.driver.find_elements_by_id('tv_headline_news_1'), '首页"装修头条"模块加载失败')  # 验证装修头条模块
        self.swipeDown()

    def test03_FeedStream(self):
        """Feed流"""
        sleep(2 * sleep_time)  # 部分手机首页加载时间较长可能导致用例失败
        self.swipeUp()  # 上滑
        self.assertTrue(self.driver.find_elements_by_name('-美图-'), '首页feed流"装修美图"模块加载失败')  # 验证feed流美图
        self.swipeUp()  # 上滑
        self.assertTrue(self.driver.find_elements_by_name('-话题-'), '首页feed流"话题"模块加载失败')  # 验证feed流话题
        self.assertTrue(self.driver.find_elements_by_name('-攻略-'), '首页feed流"装修攻略"模块加载失败')  # 验证feed流攻略
        self.swipeUp()  # 上滑
        self.assertTrue(self.driver.find_elements_by_name('-装修日记-'), '首页feed流"装修日记"模块加载失败')  # 验证feed流装修日记
        self.assertTrue(self.driver.find_elements_by_name('-专题-'), '首页feed流"专题"模块加载失败')  # 验证feed流专题
        self.swipeUp()  # 上滑
        self.assertTrue(self.driver.find_elements_by_name('-美图-'), '首页feed流"装修美图"模块加载失败，循环失败')  # 验证feed流循环
        self.clickId('iv_go_to_top')  # 点击回到顶部
        self.assertHomepage()  # 验证是否返回首页顶部成功

    def test04_CustomDesign(self):
        """"定制设计"""
        self.clickId('iv_golden_eye_find_designer')  # 点击首页定制设计
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '首页"定制设计方案"页面加载失败')  # 验证定制设计模块加载
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test05_TianxiaZXB(self):
        """"天下装修保"""
        self.clickId('iv_golden_eye_insurance')  # 点击首页天下装修保
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '首页"天下装修保"页面加载失败')  # 验证天下装修保模块加载
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test06_ProfessionalInspector(self):
        """"专业验房"""
        self.clickId('iv_golden_eye_check_house')  # 点击首页专业验房
        self.assertTrue(self.driver.find_elements_by_id('btn_right1'), '首页"专业验房"页面加载失败')  # 验证专业验房模块加载
        self.goBack()  # 返回首页
        self.assertHomepage()  # 验证是否返回首页成功

    def test07_BottomIcon(self):
        """"底部icon"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_home_inspiration')  # 点击图库
        self.assertTrue(self.driver.find_element_by_id('iv_home_inspiration').is_selected(), '无图库icon')  # 验证页面跳转
        self.clickId('iv_home_diary')  # 点击日记
        self.assertTrue(self.driver.find_element_by_id('iv_home_diary').is_selected(), '无日记icon')  # 验证页面跳转
        self.clickId('iv_order')  # 点击订单
        self.assertTrue(self.driver.find_element_by_id('iv_order').is_selected(), '无订单icon')  # 验证页面跳转
        self.clickId('iv_info')  # 点击我的
        self.assertTrue(self.driver.find_element_by_id('iv_info').is_selected(), '无我的icon')  # 验证页面跳转
        self.clickId('iv_shouye')  # 点击首页
        self.assertTrue(self.driver.find_element_by_id('iv_shouye').is_selected(), '无首页icon')  # 验证页面跳转
        self.assertHomepage()  # 验证是否返回首页成功

    def test08_Seckill(self):
        """首页建材特卖汇（秒杀）"""
        self.clickId('ll_dingwei')  # 点击定位城市
        self.clickId('tv1', sleep_time)  # 选择热门城市的第一个-北京
        self.clickName('-建材特卖汇-')  # 点击首页的建材特卖会模块
        self.assertEqual(self.textId('tv_header'), '秒杀', '"建材特卖汇"页面header错误')  # 验证是否进入秒杀页面
        self.assertEqual(self.textId('tv_super_action'), '超值购', '"建材特卖汇"页面未加载成功')  # 验证秒杀页面是否加载成功
        self.swipeUp(15)  # 上滑15次
        self.clickId('icv_top_button')  # 点击回到顶部按钮
        self.assertTrue(self.driver.find_element_by_id('iv_ad1'), '"建材特卖汇"页面点击回到顶部失败')  # 验证置顶是否成功
        self.clickId('iv_super_action')  # 点击商品类别过滤按钮
        self.assertEqual(self.textId('tv_main_goods'), '全部分类', '"建材特卖汇"页面商品过滤框未成功调起')  # 验证过滤框是否调起
        self.clickName('美的')  # 点击美的
        self.assertTrue(self.driver.find_elements_by_id('iv_sub_selected'), '"建材特卖汇"页面"商品过滤框"未成功勾选品牌')  # 判断是否点击成功
        self.clickId('tv_reset')  # 重置
        self.assertFalse(self.driver.find_elements_by_id('iv_sub_selected'), '"建材特卖汇"页面"商品过滤框"点击重置失败')
        self.clickName('九阳')  # 点击九阳
        self.clickId('tv_submit')  # 勾选品牌，点击确认
        self.assertEqual(self.textId('tv_super_action'), '超值购', '"建材特卖汇"页面未加载成功')  # 验证秒杀页面是否加载成功
        self.assertIn('九阳', self.textId('tv_productDes'), '"建材特卖汇"页面"商品过滤失败')  # 验证品牌过滤是否成功
        self.goBack()  # 返回
        self.swipeDown()  # 下拉
        self.assertHomepage()  # 验证是否返回首页成功


if __name__ == '__main__':
    unittest.main()
