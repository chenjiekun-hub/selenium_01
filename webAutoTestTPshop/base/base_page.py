from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from utils import DriverUtils


# 封装对象库层元素定位的基类
class BasePage:

    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = DriverUtils.get_driver()

    # 元素定位的公用方法
    def find_elt(self, location):
        # location = ("指定元素的定位方式","对应改定位方式的值")
        return self.driver.find_element(*location)

    # 鼠标悬浮工具函数
    def action_move_element(self, element):
        action = ActionChains(DriverUtils.get_driver())
        action.move_to_element(element)
        action.perform()

    # 封装下拉选择框函数
    def select_action(self, element, value):
        select = Select(element)
        select.select_by_value(value)


# 封装操作层元素操作的基类
class BaseHandler:

    # 模拟元素文本输入的公共方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
