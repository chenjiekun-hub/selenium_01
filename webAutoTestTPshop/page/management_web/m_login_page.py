# 对象库层
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler


# 专门用来管理和维护元素对象
class MLoginPage(BasePage):
    # 初始化方法
    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, 'username')
        # 密码输入框
        self.password = (By.NAME, 'password')
        # 验证码输入框
        self.verfiy_code = (By.NAME, 'vertify')
        # 登陆按钮
        self.submit_btn = (By.NAME, 'submit')

    # 后台登陆方法
    def test_m_login(self, username, pwd, code):
        self.find_elt(self.username).send_keys(username)
        self.find_elt(self.password).send_keys(pwd)
        self.find_elt(self.verfiy_code).send_keys(code)
        self.find_elt(self.submit_btn).click()
