# coding = utf-8
# __author__ = 'lufangfang'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationConstructionSite(PublicClass):
    """看工地"""

    @classmethod
    def Lff_swipeUp(cls, n=1):
        x = int(cls().width * 0.5)  # 起点横坐标与终点横坐标
        y1 = int(cls().height * 1 / 3)  # 起点纵坐标
        y2 = int(cls().height * 1 / 4)  # 终点纵坐标
        for i in range(n):
            cls().driver.swipe(x, y1, x, y2)  # 滑动屏幕，从(x,y1)滑动到(x,y2)

    @classmethod
    def Lff_swipeDown(cls, n=1):
        x = int(cls().width * 0.5)  # 起点横坐标与终点横坐标
        y1 = int(cls().height * 1 / 4)  # 起点纵坐标
        y2 = int(cls().height * 1 / 3)  # 终点纵坐标
        for i in range(n):
            cls().driver.swipe(x, y1, x, y2)  # 滑动屏幕，从(x,y1)滑动到(x,y2)

    def test63_siteMap(self):
        """看工地"""
        self.login(18337162151, 123456)
        self.clickName('看工地')  # 点击看工地icon
        self.swipeUp()
        self.clickName('施工状态')
        self.assertTrue(self.driver.find_elements_by_id('tv_item'), '施工状态选项未加载出来')
        self.clickName('施工中')
        self.swipeUp()
        self.clickName('户型')
        self.assertTrue(self.driver.find_elements_by_id('tv_item'), '户型选项未加载出来')
        self.clickName('二居室')
        self.swipeUp()
        self.goBack()
        self.assertHomepage()

    def test64_siteList(self):
        """工地列表"""
        self.clickName('看工地')  # 点击看工地icon
        self.assertTrue(self.driver.find_elements_by_id('worksite_tv_state'),
                        '没有找到“worksite_tv_state”id，跳转工地地图页失败')
        self.clickName('列表')
        self.assertTrue(self.driver.find_element_by_name('工地列表'), '没有找到“工地列表”字段，跳转工地列表页失败')
        self.clickName('户型')
        self.assertTrue(self.driver.find_element_by_name('户型').is_selected(), '点击后户型未变选中色')
        self.assertTrue(self.driver.find_element_by_name('不限'), '没有找到“不限”字段，户型列表加载失败')
        self.Lff_swipeUp(4)
        self.clickName('其它')
        self.swipeUp(2)
        self.swipeDown(2)
        self.clickId('iv_pictrues')  # 点击工地列表中第一个图片
        sleep(3)
        self.reFresh()
        self.swipeUp()
        self.swipeDown()
        self.clickName('预约参观')  # 点击预约参观按钮
        self.assertTrue(self.driver.find_element_by_name('预约参观工地'),
                        '没有找到“预约参观工地”字段，跳转到预约参观工地页面失败')
        self.inputId('et_name', 'lff女士')  # 在预约参观工地也输入称呼
        self.clickName('免费申请')  # 点击免费申请按钮
        self.goBack()  # 返回到预约参观页
        if self.driver.find_elements_by_id('rl_xiana_shoucang'):
            self.clickId('rl_xiana_shoucang')  # 点击右上角收藏按钮
            self.goBack()  # 返回到工地列表页
        else:
            self.goBack()  # 返回到预约参观页
            self.clickId('rl_xiana_shoucang')  # 点击右上角收藏按钮
            self.goBack()
        self.clickName('总价')
        self.assertTrue(self.driver.find_element_by_name('总价').is_selected(), '点击后总价未变为选中色')
        self.assertTrue(self.driver.find_element_by_name('不限'), '没有找到“不限”字段，总价列表加载失败')
        self.Lff_swipeUp()
        self.clickName('2万以下')
        self.clickName('装修阶段')
        self.assertTrue(self.driver.find_element_by_name('装修阶段').is_selected(), '点击后装修阶段未变为选中色')
        self.assertTrue(self.driver.find_element_by_name('不限'), '没有找到”不限“字段，装修阶段列表加载失败')
        self.Lff_swipeUp(2)
        self.Lff_swipeDown(2)
        self.clickName('不限')
        self.clickName('筛选')
        self.assertTrue(self.driver.find_element_by_name('筛选').is_selected(), '点击后筛选未变为选中色')
        self.clickName('区域')  # 点击筛选列表中“区域”按钮
        self.assertTrue(self.driver.find_element_by_name('附近'), '没有找到“附近“字段，筛选列表加载失败')
        self.Lff_swipeUp()
        self.clickName('朝阳区')  # 点击“区域列表”中“朝阳区”按钮
        self.clickName('类型')  # 点击“筛选”列表中的“类型”按钮
        self.assertTrue(self.driver.find_element_by_name('房天下自营'), '没有找到”房天下自营“字段，类型列表加载失败')
        self.clickName('房天下自营')  # 点击“类型列表”中的“不限按钮”
        self.clickName('确定')  # 点击确认按钮
        self.goBack(2)  # 返回到首页
        self.assertHomepage()

if __name__ == '__main__':
    unittest.main()
