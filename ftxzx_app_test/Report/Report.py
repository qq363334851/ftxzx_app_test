# coding = utf-8
# __author__ = 'linye'

import HTMLTestRunner.HTMLTestRunner
from Testcase import *


def suite_use_make_suite():
    """TestCase下的所有测试加到TestSuite"""
    suite.addTest(unittest.makeSuite(Homepage))
    suite.addTest(unittest.makeSuite(DecorationPicture))
    suite.addTest(unittest.makeSuite(DecorationOrders))
    suite.addTest(unittest.makeSuite(CommodityOrders))
    suite.addTest(unittest.makeSuite(VoucherOrders))
    suite.addTest(unittest.makeSuite(Mine))
    suite.addTest(unittest.makeSuite(DecorationCompany))
    suite.addTest(unittest.makeSuite(DecorationCommunity))
    suite.addTest(unittest.makeSuite(Diary))
    # suite.addTest(unittest.makeSuite(DecorationStrategy))
    # suite.addTest(unittest.makeSuite(DecorationConstructionSite))
    return suite
suite = unittest.TestSuite()
suite_use_make_suite()

filename = 'C:\\Users\\user\\Desktop\\ftxzx_app_test_result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'TestReport', description=u'FTXZX_App_Test')
runner.run(suite)
fp.close()
