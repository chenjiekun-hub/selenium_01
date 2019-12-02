"""
首页
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler

class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        # 搜索输入框
        self.search_box = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CLASS_NAME, "ecsc-search-button")
        # 登陆超链接
        self.login_link = (By.CLASS_NAME, "red")

    # 找到搜索输入框
    def find_search_box(self):
        return self.find_elt(self.search_box)

    # 找到搜索按钮
    def find_search_btn(self):
        return self.find_elt(self.search_btn)

    # 找到登陆超链接
    def find_login_link(self):
        return self.find_elt(self.login_link)


class HomeHandler(BaseHandler):

    def __init__(self):
        self.home_page = HomePage()

    # 输入搜索条件
    def input_search_box(self, key):
        self.input_text(self.home_page.find_search_box(), key)

    # 点击搜索按钮
    def click_search_btn(self):
        self.home_page.find_search_btn().click()

    # 点击登陆超链接
    def click_login_link(self):
        self.home_page.find_login_link().click()

class HomeProxy:

    def __init__(self):
        self.home_handler = HomeHandler()

    # 跳转登陆页面
    def to_login_page(self):
        self.home_handler.click_login_link()

    # 执行搜索操作
    def test_search_goods(self, key):
        # 输入搜索条件
        self.home_handler.input_search_box(key)
        # 点击搜索按钮
        self.home_handler.click_search_btn()
