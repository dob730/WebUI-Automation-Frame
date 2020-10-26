import seldom
from seldom import Seldom
from seldom import data
from poium import PageWait
from pyautoTest.page.DonationPage import DonationPage
import os
from seldom.testdata.conversion import excel_to_list
from selenium import webdriver


file_path = os.path.dirname(os.path.abspath(__file__))


class DonationScan(seldom.TestCase):
    """掃碼捐款固定金額碼/新增/下載/刪除"""

    @classmethod
    def setUpClass(cls):
        page = DonationPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.button.click()
        page.services.click()
        PageWait(page.donation)
        page.donation.click()
        page.donation_scan.click()
        page.donation_scan_money.click()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="donation_scan", line=1))
    def test_donation_scan(self, qrcodename, amount):
        """
        A simple test
        """
        print(Seldom.driver.get_window_size())
        self.max_window()
        self.sleep(0.5)
        # xpathCount = Seldom.driver.find_elements(By.xpath("//"))


        # 先刪掉最新的
        self.click(xpath="(//button[@type='button'])[4]")
        self.sleep(0.5)
        # 確定刪除
        self.click(id_="updateScanDonationStatus_btn")
        self.clear(id_="qrcodename")
        self.click(id_="qrcodename")
        self.type(id_="qrcodename", text=qrcodename)
        self.clear(id_="amount")
        self.click(id_="amount")
        self.type(id_="amount", text=amount)
        self.click(id_="addScanDonation_btn")
        self.sleep(0.5)
        # 按右上下載鍵
        self.click(id_="download_qrcode")

        # 建立了Chrome Options 物件之後就是新增引數
        options = webdriver.ChromeOptions()
        # 文件默認內容設置彈出窗口，0:不彈窗，下載預設路徑：d:\
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
        # 設置開發者模式啓動，該模式下webdriver屬性為正常值
        options.add_experimental_option('prefs', prefs)
        # 瀏覽器不提供可視化頁面. linux下如果系統不支持可視化不加這條會啓動失敗
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path='D:\\drivers\chromedriver.exe', chrome_options=options)
        self.sleep(0.5)
        # Set browser window wide and high.
        self.set_window(945, 1020)



if __name__ == '__main__':
    seldom.main()
