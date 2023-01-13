import time

import pytest

from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)  # Создаём экземпляр страницы Product Page
    product_page.open()  # Открываем в браузере
    product_page.should_be_product_page()  # Проверка ссылки и наличия кнопки добавления в корзину, клик по кнопке
    product_page.solve_quiz_and_get_code()  # Проведение вычислений с алерта и вывод результата
    time.sleep(5)
    product_page.product_name()
    product_page.product_price()
