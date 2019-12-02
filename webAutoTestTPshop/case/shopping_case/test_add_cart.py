# 导包
import time
import unittest

from page.shopping_web.home_page import HomeProxy
from page.shopping_web.login_page import LoginProxy
from page.shopping_web.search_goods_page import SearchGoodsProxy
from utils import DriverUtils


# 定义测试类
class TestAddCart(unittest.TestCase):

    # 类级别的fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtils.get_driver()
        cls.driver.get('http://localhost/')
        cls.home_proxy = HomeProxy()
        # cls.home_proxy.to_login_page()
        # cls.login_proxy = LoginProxy()
        # cls.login_proxy.test_login('15800000001', '123456', '8888')
        cls.search_proxy = SearchGoodsProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtils.quit_driver()

    # def setUp(self):
    #     time.sleep(5)
    #     self.driver.get('http://localhost/')

    # 定义测试方法
    def test_add_cart(self):
        self.home_proxy.test_search_goods('小米')
        msg = self.search_proxy.test_add_goods()
        print(msg)
        self.assertIn('成功', msg)
