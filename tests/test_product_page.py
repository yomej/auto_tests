import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)  # Создаём экземпляр страницы Product Page
    product_page.open()  # Открываем в браузере
    product_page.should_be_product_page()  # Проверка ссылки и наличия кнопки добавления в корзину, клик по кнопке
    product_page.solve_quiz_and_get_code()# Проведение вычислений с алерта и вывод результата
    time.sleep(7)
    product_page.product_name()
    product_page.product_price()
