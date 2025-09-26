
from selenium import webdriver


from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_checkout():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

        cart = CartPage(driver)
        items = cart.get_cart_items()
        assert "Sauce Labs Backpack" in items
        assert "Sauce Labs Bolt T-Shirt" in items
        assert "Sauce Labs Onesie" in items
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Ivan", "Petrov", "12345")
        total = checkout.get_total()

        assert total == "Total: $58.29"

    finally:
        driver.quit()
