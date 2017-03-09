# coding = utf-8
# __author__  = 'linye'

import unittest  # 导入python单元测试模块
from time import sleep  # 导入sleep方法
from appium import webdriver  # 导入webdriver包
import configparser  # 导入配置文件模块
import os  # 文件、目录相关操作模块
import inspect  # 获取case_name所需方法的模块
import random  # 导入随机模块，误删，本文件没有调用，但是测试用例有调用

TestData_dir = os.path.dirname(os.path.abspath(__file__))+'\TestData'
conf = configparser.ConfigParser()
conf.read(TestData_dir)

click_time = int(conf.get('default', 'click_time'))
input_time = int(conf.get('default', 'input_time'))
sleep_time = int(conf.get('default', 'sleep_time'))
refresh_count = int(conf.get('default', 'refresh_count'))


def get_current_test_case_name():
    return inspect.stack()[1][3]


class DeviceInfo:
    """设备信息"""
    desired_caps = {'deviceName': 'CHM-TL00H', 'platformName': 'Android', 'platformVersion': '4.4.4',
                    'appPackage': 'com.soufun.decoration.app',
                    'appActivity': 'com.soufun.decoration.app.activity.MainSplashActivity', 'resetKeyboard': 'True',
                    'unicodeKeyboard': 'True'}
    # 设备信息:
    # deviceName:必填项，名称任意
    # platformName：必填项，Android
    # platformVersion：选填项，Android平台版本号
    #
    # APP信息:
    # appPackage：必填项，包名，通过重签名apk获取或和开发获取或者通过命令行自行百度获取
    # appActivity：必填项，初始Activity，通过重签名apk获取或和开发获取或者通过命令行自行百度获取
    #
    # 中文输入:
    # resetKeyboard：选填项，填写True即重置键盘
    # unicodeKeyboard：选填项，填写True即支持Unicode编码（中文）的键盘
    # 注：手机默认输入法被屏蔽，如需恢复进入设置→更多设置→语言和输入法
    #
    # 设备唯一标识:
    # udid：选填项，多设备连接时，Appium启动设备唯一标识，adb devices获取
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动App
    window_size = driver.get_window_size()  # 获取屏幕大小
    width = window_size['width']  # 获取屏幕宽度
    height = window_size['height']  # 获取屏幕高度
    sleep(2*sleep_time)
    driver.implicitly_wait(sleep_time)  # 设置全局最大等待时间


class PublicClass(unittest.TestCase, DeviceInfo):
    """公共类"""
    def setUp(self):
        """每次执行用例前执行该方法，当前页面是首页则不进行处理，否则重新启动App"""
        if not self.driver.find_elements_by_id('iv_home_item'):  # 首页学装修图标
            self.driver.close_app()  # 关闭App
            self.driver.launch_app()  # 启动App
            sleep(1.5*sleep_time)

    def assertHomepage(self):
        """验证是否返回首页成功"""
        self.assertTrue(self.driver.find_elements_by_id('iv_home_item'), '用例返回首页失败（未找到首页"学装修"icon）')  # 验证是否返回首页成功

    def login(self, usr, psw):
        """登陆账号"""
        self.clickId('tv_info')  # 点击我的
        if self.driver.find_elements_by_id('tv_welcome'):
            self.clickId('iv_touxiang')  # 点击头像
            if self.driver.find_elements_by_id('deleteUser'):
                self.clickId('deleteUser')  # 清空历史登陆数据
            self.inputId('userName', usr)  # 输入用户名或手机号
            self.inputId('password', psw)  # 输入密码
            self.clickId('login')  # 点击登录
            self.assertTrue(self.driver.find_elements_by_id('tv_mycount_phonenum'), '点击"登陆"后页面未跳转，登陆业主账号失败')  # 验证登陆状态
            self.goBack()  # 返回首页
            self.assertHomepage()  # 验证是否返回首页成功
        else:
            if self.textId('tv_mycount_phonenum') == usr:  # 判断已登录账号是否与将登陆账号一致
                self.goBack()  # 返回首页
                self.assertHomepage()  # 验证是否返回首页成功
            else:
                self.logout()  # 退出账号
                self.login(usr, psw)  # 登陆账号

    def logout(self):
        """登出账号"""
        self.clickId('tv_info')  # 点击我的
        if self.driver.find_elements_by_id('tv_welcome'):
            self.goBack()  # 返回首页
            self.assertHomepage()  # 验证是否返回首页成功
        else:
            self.clickId('tv_mycount_phonenum')  # 点击登陆的手机号
            self.swipeUp()  # 上滑
            self.clickId('rl_return')  # 点击退出
            self.clickId('button1', sleep_time)  # 点击确定
            self.assertTrue(self.driver.find_elements_by_id('iv_touxiang'), '点击"退出登陆"后页面未跳转，退出业主账号失败')  # 验证登出状态
            self.goBack()  # 返回首页
            self.assertHomepage()  # 验证是否返回首页成功

    def swipeRight(self, n=1):
        """
        由左向右滑动屏幕，滑动屏幕上方1/4处，如需滑动其他位置，需重新封装
        :param n: 次数，执行该操作次数，默认1次
        在appium1.5版本以下，swipe的方法中的end_x和end_y是实际要滑动的目的地坐标
        但是在1.5版本以上的，end_x和end_y是相对于前面start_x和start_y坐标的偏移量。
        """
        x1 = int(self.width * 0.05)  # 起点横坐标
        y = int(self.height * 0.25)  # 起点纵坐标、终点纵坐标
        x2 = int(self.width * 0.75)  # 终点横坐标
        for i in range(n):
            self.driver.swipe(x1, y, x2, y)  # 滑动屏幕，从(x1,y)滑动到(x2,y)

    def swipeLeft(self, n=1):  # 屏幕向左滑动
        """
        由右向左滑动屏幕，滑动屏幕上方1/4处，如需滑动其他位置，需重新封装
        :param n: 次数，执行该操作次数，默认1次
        在appium1.5版本以下，swipe的方法中的end_x和end_y是实际要滑动的目的地坐标
        但是在1.5版本以上的，end_x和end_y是相对于前面start_x和start_y坐标的偏移量。
        """
        x1 = int(self.width * 0.75)  # 起点横坐标
        y = int(self.height * 0.25)  # 起点纵坐标、终点纵坐标
        x2 = int(self.width * 0.05)  # 终点横坐标
        for i in range(n):
            self.driver.swipe(x1, y, x2, y)  # 滑动屏幕，从(x1,y)滑动到(x2,y)

    def swipeUp(self, n=1):  # 屏幕向上滑动
        """
        由下向上滑动屏幕
        :param n: 次数，执行该操作次数，默认1次
        在appium1.5版本以下，swipe的方法中的end_x和end_y是实际要滑动的目的地坐标
        但是在1.5版本以上的，end_x和end_y是相对于前面start_x和start_y坐标的偏移量。
        """
        x = int(self.width * 0.5)  # 起点横坐标、终点横坐标
        y1 = int(self.height * 0.75)  # 起点纵坐标
        y2 = int(self.height * 0.25)  # 终点纵坐标
        for i in range(n):
            self.driver.swipe(x, y1, x, y2)  # 滑动屏幕，从(x,y1)滑动到(x,y2)

    def swipeDown(self, n=1):  # 屏幕向上滑动
        """
        由上向下滑动屏幕
        :param n: 次数，执行该操作次数，默认1次
        在appium1.5版本以下，swipe的方法中的end_x和end_y是实际要滑动的目的地坐标
        但是在1.5版本以上的，end_x和end_y是相对于前面start_x和start_y坐标的偏移量。
        """
        x = int(self.width * 0.5)  # 起点横坐标、终点横坐标
        y1 = int(self.height * 0.25)  # 起点纵坐标
        y2 = int(self.height * 0.75)  # 终点纵坐标
        for i in range(n):
            self.driver.swipe(x, y1, x, y2)  # 滑动屏幕，从(x,y1)滑动到(x,y2)

    def clickId(self, elements_id, t=click_time, elements_list_value=0):
        """
        通过id找到控件并点击
        :param elements_id:控件的id
        :param t:点击后等待t秒
        :param elements_list_value:默认点击第一个控件
        """
        elements_list = self.driver.find_elements_by_id(elements_id)  # 将找到的elements赋值到列表中
        if not elements_list:
            self.assertTrue(False, '未找到id为"%s"的控件' % elements_id)  # 未找到控件，用例失败
        else:
            elements_list[elements_list_value].click()  # 找到控件并点击
            sleep(t)

    def clickName(self, elements_name, t=click_time, elements_list_value=0):
        """
        通过id找到控件并点击
        :param elements_name:控件的name
        :param t:点击后等待t秒
        :param elements_list_value:默认点击第一个控件
        """
        elements_list = self.driver.find_elements_by_name(elements_name)  # 将找到的elements赋值到列表中
        if not elements_list:
            self.assertTrue(False, '未找到name为"%s"的控件' % elements_name)  # 未找到控件，用例失败
        else:
            elements_list[elements_list_value].click()  # 找到控件并点击
            sleep(t)

    def clickXpath(self, elements_xpath, t=sleep_time, elements_list_value=0):
        """
        通过xpath找到控件并点击
        :param elements_xpath: 控件的xpath，用uiautomatorviewer获取fullIndexXpath
        :param t:点击后等待t秒
        :param elements_list_value:默认点击第一个控件
        """
        elements_list = self.driver.find_elements_by_xpath(elements_xpath)  # 将找到的elements赋值到列表中
        if not elements_list:
            self.assertTrue(False, '未找到xpath为"%s"的控件' % elements_xpath)  # 未找到控件，用例失败
        else:
            elements_list[elements_list_value].click()  # 找到控件并点击
            sleep(t)

    def textId(self, elements_id, elements_list_value=0):
        """
        通过id找到控件并获取其文本
        :param elements_id:控件的id
        :param elements_list_value:默认获取第一个控件文本
        :return:返回获取文本或空字符串
        """
        elements_list = self.driver.find_elements_by_id(elements_id)  # 将找到的elements赋值到列表中
        if not elements_list:
            return ''  # return 空字符串
        else:
            return elements_list[elements_list_value].text  # return element的文本

    def inputId(self, element_id, input_content):
        """
        找到控件清除其数据并输入新的文本内容
        :param element_id: 控件id
        :param input_content: 输入的文本内容
        """
        # self.driver.find_element_by_id(element_id).clear()  # 清除控件内的数据
        # sleep(click_time)
        self.driver.find_element_by_id(element_id).send_keys(input_content)  # 输入文字
        sleep(click_time)

    def goBack(self, n=1):
        """
        返回上一级页面
        :param n: 点击返回次数，默认1次
        """
        for i in range(n):
            self.driver.back()  # 返回上一级页面

    def reFresh(self, t=sleep_time, n=refresh_count):
        """
        页面遇到加载失败时重新刷新n次，仅限原生页，执行效率较低，勿过度使用影响效率
        :param t:点击刷新后等待t秒
        :param n:重新刷新次数
        """
        if self.driver.find_elements_by_id('btn_refresh'):
            i = 0  # 初始化循环变量
            while i <= n:
                if i == n:
                    self.assertTrue(False, '当前页面多次加载失败，用例失败')  # 点击刷新n次后页面依然未加载成功
                    break  # 跳出循环
                else:
                    self.clickId('btn_refresh')  # 点击重新加载
                    sleep(t)
                    if self.driver.find_elements_by_id('btn_refresh'):
                        i += 1  # 循环变量+1
                    else:
                        break  # 跳出循环
        else:
            pass


if __name__ == '__main__':
    unittest.main()
