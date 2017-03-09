# coding=utf-8
# __author__ = 'lufangfang'
from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationStrategy(PublicClass):
    """学装修"""

    @classmethod
    def free_design(cls, case_name='default'):
        """申请免费设计"""
        if case_name == 'default':
            name = conf.get('default', 'content')
        else:
            name = conf.get(case_name, 'diary_content')
            if name == '':
                name = conf.get('default', 'content')
        cls().clickId('useful_tv')
        cls().assertTrue(cls().driver.find_element_by_id('useful_tv').is_selected(), '点击后，有用未变选中色')
        cls().clickId('ll_shenqing')
        cls().inputId('et_name', name)
        # self.assertEqual('申请成功', self.textId('tv_success'), '报名失败')  # 验证是否报名成功
        cls().clickId('tv_appoitment')
        if cls().driver.find_elements_by_id('tv_success'):  # 判断是否申请成功
            cls().goBack(3)
            cls().assertHomepage()
            cls().clickName('学装修')
        else:
            cls().goBack(4)
            cls().assertHomepage()
            cls().clickName('学装修')

    def test61_Decoration_Raiders(self):
        """学装修轮播、精彩专题、搜索"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickId('iv_home_item')
        self.assertTrue(self.driver.find_elements_by_id('title1'), '没有找到“装修攻略”字段，装修攻略页面加载失败')
        if self.driver.find_elements_by_id("headerimg"):  # 判断是否找到轮播图
            self.swipeLeft(5)
            self.swipeRight(5)
            self.swipeUp(10)
            self.clickId('footItmeImg4')  # 精彩专题
            self.swipeUp(4)
            self.goBack(1)
            self.clickId('img_right1')  # 搜索按钮
            if self.driver.find_elements_by_id('tv_hestory_item'):  # 判断是否找到历史搜索内容
                self.clickId('tv_hestory_item')
                self.clickId("auto_ListView")  # 点击cell
                self.swipeUp(3)
                self.swipeDown(3)
                self.goBack()
                self.clickId('tv_cancel_search')  # 点击取消按钮
                self.goBack()
                self.assertHomepage()
            else:
                self.goBack(2)
                self.assertHomepage()

    def test62_Strategys(self):
        """学装修"""
        case_name = get_current_test_case_name()
        usr, psw = conf.get(case_name, 'usr'), conf.get(case_name, 'psw')
        if usr == '' or psw == '':
            usr, psw = conf.get('default', 'usr'), conf.get('default', 'psw')
        self.login(usr, psw)
        self.clickName('学装修')
        self.clickId('title1')  # 新手攻略
        self.swipeUp(7)
        self.goBack()
        self.clickId('title2')  # 施工攻略
        self.swipeLeft(8)
        self.swipeRight(8)
        self.clickId('workflow_Listview')  # 点击cell
        self.swipeUp(15)
        self.free_design(case_name)
        self.clickId('title3')  # 选材攻略
        self.clickId('workflow_Listview')
        self.swipeUp(10)
        self.free_design(case_name)
        self.clickId('title4')  # 风水攻略
        self.clickId('workflow_Listview')
        self.swipeUp(15)
        self.free_design(case_name)
        self.goBack()
        self.assertHomepage()


if __name__ == '__main__':
    unittest.main()
