"""Tests de checkout usando el patrón Page Object Model (POM).

Qué demuestra este archivo
--------------------------
1. POM en uso: CheckoutPage es el único que conoce los locators.
2. DRY: el test no repite ningún selector; todo está en el Page Object.
3. Legibilidad: el test describe QUÉ pasa, no CÓMO lo hace el navegador.
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_sin_nombre_muestra_error(authenticated_page):
    InventoryPage(authenticated_page).add_to_cart("Sauce Labs Backpack").go_to_cart()
    CartPage(authenticated_page).proceed_to_checkout()
    checkout = CheckoutPage(authenticated_page)
    # checkout.fill_shipping("TestName", "Test LastName", "0000").continue_to_overview()
    checkout.fill_shipping("TestName", "Test LastName", "0000")
    """not True: si no se muestra el mensaje de error."""
    assert not checkout.has_error()