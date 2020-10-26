from poium import Page, NewPageElement


class DgtPaymentPage(Page):
    """DgtPayment page"""
    dgtPayment = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()-1]")  # 數位產品收款
    product_name = NewPageElement(name="productname")
