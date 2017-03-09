# coding = utf-8
# __author__ = 'peidongxue'

from Publicclass.Publicclass import *  # Publicclass所有模块 包含该模块已经导入的模块


class DecorationCompany(PublicClass):
    """找公司"""

    def test43_CompanyList(self):
        """装饰公司列表"""
        self.clickId("ll_dingwei")  # 点击定位城市
        self.clickId("tv1")  # 选择热门城市的第一个-北京
        self.assertHomepage()  # 验证返回首页是否成功
        self.clickName("找公司")  # 点击找公司按钮
        self.assertEqual(self.textId("tv_header"), '装饰公司', '"找装饰公司"页面header错误')  # 验证找公司列表加载
        self.goBack()  # 返回首页
        self.assertHomepage()  # 返回首页是否成功


if __name__ == '__main__':
    unittest.main()
