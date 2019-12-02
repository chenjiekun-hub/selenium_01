# 1.导包
import unittest

from page.management_web.m_login_page import MLoginPage
from utils import DriverUtils


# 2.定义测试类
class TestLogin(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        cls.m_login_page = MLoginPage()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    def setUp(self):
        self.driver.get('http://localhost/Admin/Admin/login')

    # 3.定义测试方法
    def test_login(self):
        # 调用login_page模块中业务层的test_login的业务方法
        self.m_login_page.test_m_login('admin', 'admin123', '8888')
