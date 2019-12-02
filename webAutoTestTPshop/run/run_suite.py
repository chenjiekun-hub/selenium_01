# 1.导包
import unittest
from utils import DriverUtils

# 2.使用TestLoader加载测试用例
suite = unittest.TestLoader().discover("../case/shopping_case/", "test*.py")

# 将关闭浏览器开关打开
DriverUtils.change_openkey(True)

# 3.实例化运行器对象
runner = unittest.TextTestRunner()
# 4.执行测试套件
runner.run(suite)

# 将关闭浏览器开关关闭
DriverUtils.change_openkey(False)
DriverUtils.quit_driver()