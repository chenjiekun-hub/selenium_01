# 对象库层
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler


# 专门用来管理和维护元素对象
class LoginPage(BasePage):
    # 初始化方法
    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 用户名输入框
        self.username = (By.ID, 'username')
        # 密码输入框
        self.password = (By.ID, 'password')
        # 验证码输入框
        self.verfiy_code = (By.ID, 'verify_code')
        # 登陆按钮
        self.submit_btn = (By.NAME, 'sbtbutton')
        # 忘记密码
        self.forget_link = (By.CSS_SELECTOR, "[href*='forget']")

    # 找到用户名输入框
    def find_username_box(self):
        return self.find_elt(self.username)

    # 找到密码输入框
    def find_password_box(self):
        return self.find_elt(self.password)

    # 找到验证码输入框
    def find_verfiy_code_box(self):
        return self.find_elt(self.verfiy_code)

    # 找到登陆按钮
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)

    # 找到忘记密码的超链接
    def find_forget_link(self):
        return self.find_elt(self.forget_link)


# 操作层,专门管理所有元素对象的操作方法
class LoginHandler(BaseHandler):

    def __init__(self):
        # 实例化对象库层
        self.login_page = LoginPage()

    # 用户名信息输入
    def input_username(self, username):
        self.input_text(self.login_page.find_username_box(), username)

    # 密码输入
    def input_password(self, pwd):
        self.input_text(self.login_page.find_password_box(), pwd)

    # 验证码输入
    def input_code(self, code):
        self.input_text(self.login_page.find_verfiy_code_box(), code)

    # 登陆按钮点击
    def click_submit_btn(self):
        self.login_page.find_submit_btn().click()

    # 点击忘记密码
    def click_forget_link(self):
        self.login_page.find_forget_link().click()


# 业务层,将多个操作连接到一起形成的一个具体业务操作
class LoginProxy:

    def __init__(self):
        # 实例化操作层
        self.login_hanlder = LoginHandler()

    # 登陆的业务操作方法
    def test_login(self, username, pwd, code):
        # 输入用户名
        self.login_hanlder.input_username(username)
        # 输入密码
        self.login_hanlder.input_password(pwd)
        # 输入验证码
        self.login_hanlder.input_code(code)
        # 点击登陆按钮
        self.login_hanlder.click_submit_btn()

    # 忘记密码的业务操作
    # def test_forget(self):
    # pass
