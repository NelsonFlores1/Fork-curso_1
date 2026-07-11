"""Page object de la pantalla de Checkout de Saucedemo"""

from __future__ import annotations
from playwright.sync_api import Page

class CheckoutPage:
    """Representa https://www.saucedemo.com/checkout-step-one.html"""

    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self._firstName = page.locator('[data-test="firstName"]')
        self._lastName = page.locator('[data-test="lastName"]')
        self._zipCode = page.locator('[data-test="postalCode"]')
        self._continue_btn = page.locator('[data-test="continue"]')
        self._error_msg = page.locator('[data-test="error"]')

    # ── Acciones ──────────────────────────────────────────────────────────
    def fill_shipping(self, firstName: str, lastName: str, zipCode: str) -> "CheckoutPage":
        """Rellena el formulario de checkout"""
        self._firstName.fill(firstName)
        self._lastName.fill(lastName)
        self._zipCode.fill(zipCode)
        self._continue_btn.click()
        return self
    
    # def continue_to_overview(self) -> None:
    #     self._continue_btn
    
    def has_error(self) -> bool:
        """True si hay un mensaje de error visible en pantalla."""
        return self._error_msg.is_visible()
    