# 1.导包
import time
import unittest
from parameterized import parameterized
import json

from page.shopping_web.home_page import HomeProxy
from page.shopping_web.login_page import LoginProxy
from utils import DriverUtils, get_tip_msg


# 组装数据
def build_data():
    login_data = []
    with open("../data/login_data.json", encoding="utf-8") as f:
        case_data = json.load(f)
        for test_data in case_data.values():
            login_data.append(
                [test_data.get("username"), test_data.get("password"), test_data.get("code"), test_data.get("expect"),
                 test_data.get("is_success")])
        print(login_data)
    return login_data


# 2.定义测试类
class TestLogin(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        cls.login_page = LoginProxy()
        cls.home_page = HomeProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    def setUp(self):
        time.sleep(3)
        self.driver.get('http://localhost/')
        self.home_page.to_login_page()

    # 3.定义测试方法[('15800000011', '123456', '8888'),('15800000001', 'error', '8888'),('15800000001', '123456', '8888')]
    @parameterized.expand(build_data)
    def test_login(self, username, password, code, expect, is_success):
        # 调用login_page模块中业务层的test_login的业务方法
        self.login_page.test_login(username, password, code)
        if is_success:
            time.sleep(5)
            self.assertIn(expect, self.driver.title)
        else:
            msg = get_tip_msg()
            self.assertIn(expect, msg)
