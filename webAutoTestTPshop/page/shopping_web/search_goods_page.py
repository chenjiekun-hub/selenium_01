"""
搜索结果页+商品详情页面
"""
# 对象库层
import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandler

# 专门用来管理和维护元素对象
from utils import DriverUtils


class SearchGoodsPage(BasePage):
    # 初始化方法
    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 搜索结果页面加入购物车按钮
        self.search_goods_btn = (By.CSS_SELECTOR, "[onclick*='+104']")
        # 商品详情页面的加入购物车按钮
        self.add_goods_btn = (By.ID, "join_cart")
        # iframe
        self.iframe_element = (By.CSS_SELECTOR, "[id*='layui-layer-iframe']")
        # 提示信息元素
        self.output_result = (By.CSS_SELECTOR, ".conect-title span")

    def find_search_goods_btn(self):
        return self.find_elt(self.search_goods_btn)

    def find_add_goods_btn(self):
        return self.find_elt(self.add_goods_btn)

    def find_iframe_element(self):
        return self.find_elt(self.iframe_element)

    # 结果弹出框
    def find_output_result(self):
        return self.find_elt(self.output_result)


# 操作层
class SearchGoodsHandler(BaseHandler):

    def __init__(self):
        # 实例化对象库层
        self.search_goods_page = SearchGoodsPage()

    # 点击搜索结果的第一个商品
    def click_goods_link(self):
        self.search_goods_page.find_search_goods_btn().click()

    # 点击详情页面加入购物车
    def click_add_goods_btn(self):
        self.search_goods_page.find_add_goods_btn().click()

    # 获取弹出信息
    def get_result(self):
        DriverUtils.get_driver().switch_to.frame(self.search_goods_page.find_iframe_element())
        time.sleep(2)
        return self.search_goods_page.find_output_result().text


# 业务层
class SearchGoodsProxy:

    def __init__(self):
        self.search_goods_handler = SearchGoodsHandler()

    # 从搜索结果页面进入商品详情页面并加入购物车获取添加结果的业务方法
    def test_add_goods(self):
        self.search_goods_handler.click_goods_link()
        self.search_goods_handler.click_add_goods_btn()
        return self.search_goods_handler.get_result()
