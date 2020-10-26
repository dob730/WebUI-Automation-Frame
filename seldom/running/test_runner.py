# coding=utf-8
import os
import time
import unittest
import inspect
from seldom.logging import log
from seldom.driver import browser as b
from seldom.running.HTMLTestRunner import HTMLTestRunner
from seldom.running.config import Seldom, BrowserConfig



seldom_str = """
            _      _                   
           | |    | |                  
 ___   ___ | |  __| |  ___   _ __ ___  
/ __| / _ \| | / _` | / _ \ | '_ ` _ \ 
\__ \|  __/| || (_| || (_) || | | | | |
|___/ \___||_| \__,_| \___/ |_| |_| |_| 
-----------------------------------------
                             @itest.info
"""

class TestRunner:
    def __init__(self):
        self.caseList = []
        self.casePath = os.path.pardir  # 取父目錄

    def set_case_list(self, path):
        """
        set case list
        :return:
        """
        path_list = path.split("&")
        for path in path_list:
            self.caseList.append(path)

    def set_case_suite(self, path):
        self.set_case_list(path)  # 通過set_case_list()拿到caselist元素組
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:  # 從caselist元素組中循環取出case
            # case_name = case.split("/")[-1]  # 通過split函數來將aaa/bbb分割字符串，-1取後面，0取前面
            # print(case_name + ".py")  # 打印出取出來的名稱
            # 批量加載用例，第一個參數為用例存放路徑，第一個參數為路徑文件名
            print(self.casePath)
            # self.casePath为case存放子目录的上级目录
            discover = unittest.defaultTestLoader.discover(case, pattern="test_*.py",  top_level_dir=self.casePath)  # 如果需要调用多次，且在不同目录下的话，那么需要手动给top_level_dir传值，将根目录的值给此参数
            suite_module.append(discover)  # 將discover存入suite_module元素組

        if len(suite_module) > 0:

            for suite in suite_module:  # 判斷suite_module元素組是否存在元素
                for test_name in suite:  # 如果存在，循環取出元素組內容，命名為suite
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite


def main(path=None,
         browser=None,
         report=None,
         title="Seldom Test Report",
         description="Test case execution",
         debug=False,
         rerun=0,
         save_last_run=False,
         driver_path=None,
         grid_url=None,
         timeout=10):
    """
    runner test case
    :param path:
    :param browser:
    :param report:
    :param title:
    :param description:
    :param debug:
    :param rerun:
    :param save_last_run:
    :param driver_path:
    :param grid_url:
    :param timeout:
    :return:
    """

    if path is None:
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_dir = os.path.dirname(os.path.abspath(ins.filename))
        file_path = ins.filename
        if "\\" in file_path:
            this_file = file_path.split("\\")[-1]
        elif "/" in file_path:
            this_file = file_path.split("/")[-1]
        else:
            this_file = file_path
        suits = unittest.defaultTestLoader.discover(file_dir, this_file)
    else:
        if len(path) > 3:
            if path[-3:] == ".py":  # 如果是py結尾的定義測試用例的前一層為當前目錄
                if "/" in path:
                    path_list = path.split("/")
                    path_dir = path.replace(path_list[-1], "")
                    suits = unittest.defaultTestLoader.discover(path_dir, pattern=path_list[-1])
                else:
                    suits = unittest.defaultTestLoader.discover(os.getcwd(), pattern=path)  # 如果指定執行程式 定義測試用例的目錄為當前目錄


            elif "&" in path:
                suits = TestRunner().set_case_suite(path)
            else:
                suits = unittest.defaultTestLoader.discover(path)
        else:
            suits = unittest.defaultTestLoader.discover(path)
    # set browser
    if browser is None:
        BrowserConfig.name = "chrome"
    else:
        BrowserConfig.name = browser
        BrowserConfig.grid_url = grid_url

    # Set browser drive path
    if driver_path is not None:
        ret = os.path.exists(driver_path)
        if ret is False:
            raise ValueError("Browser - driven path error，Please check if the file exists. => {}".format(driver_path))
        BrowserConfig.driver_path = driver_path

    # set timeout
    if isinstance(timeout, int):
        Seldom.timeout = timeout
    else:
        raise TypeError("Timeout {} is not integer.".format(timeout))

    """
    Global launch browser
    """
    Seldom.driver = b(BrowserConfig.name, BrowserConfig.driver_path, BrowserConfig.grid_url)

    if debug is False:
        for filename in os.listdir(os.getcwd()):
            if filename == "reports":
                break
        else:
            os.mkdir(os.path.join(os.getcwd(), "reports"))

        if report is None:
            now = time.strftime("%Y_%m_%d_%H_%M_%S")
            report = os.path.join(os.getcwd(), "reports", now + "_result.html")
            BrowserConfig.report_path = report

        with(open(report, 'wb')) as fp:
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            log.info(seldom_str)
            runner.run(suits, rerun=rerun, save_last_run=save_last_run)
        log.info("generated html file: file:///{}".format(report))
    else:
        runner = unittest.TextTestRunner(verbosity=2)
        log.info("A run the test in debug mode without generating HTML report!")
        log.info(seldom_str)
        runner.run(suits)

    """
    Close browser globally
    """
    # Seldom.driver.quit()


if __name__ == '__main__':
    main()
