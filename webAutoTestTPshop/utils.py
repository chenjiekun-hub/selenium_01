import time

from selenium import webdriver


# 1.定义工具类
class DriverUtils:
    # 私有变量，用来存储浏览器驱动对象
    __driver = None

    __openkey = False

    # 2.1定义获取浏览器驱动对象的方法
    # a、实现基本获取浏览器驱动的方法
    # b、为了方便其它地方调用，不想每次都实例化，则将方法定义为类级别的方法
    # c、为了保障整个测试用例执行过程中所操作的浏览器对象的唯一性，添加判断条件

    # 容易出错的地方
    # 1.在if中的代码不要写成cls.driver
    # 2.if中的代码和return的对齐方式
    # 3.忘记写return
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.implicitly_wait(10)
            cls.__driver.maximize_window()
        return cls.__driver

    # 2.2定义关闭浏览器驱动对象的方法
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__openkey is False:
            time.sleep(3)
            cls.__driver.quit()
            cls.__driver = None

    @classmethod
    def change_openkey(cls, key):
        cls.__openkey = key


# 封装获取弹出框信息方法
def get_tip_msg():
    msg = DriverUtils.get_driver().find_element_by_css_selector('.layui-layer-content').text
    print("结果信息为：", msg)
    return msg
