"""Task: """
from screenplay.abilities.browse_web import BrowseTheWeb
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage

class CompleteCheckout:
    """Tarea de alto nivel: Completar el formulario de checkout"""
    def __init__(self, firstName: str, lastName: str, zipCode: str):
        self._firstName = firstName
        self._lastName = lastName
        self._zipCode = zipCode

    @classmethod
    def with_info(cls, firstName: str, lastName: str, zipCode: str) -> "CompleteCheckout":
        """Constructor expresivo: CompleteCheckout.with_info('firstName', 'lastName', 'zipCode')."""
        return cls(firstName, lastName, zipCode)
    
    def perform_as(self, actor) -> None:
        page = actor.ability_to(BrowseTheWeb).page
        InventoryPage(page).go_to_cart()
        CartPage(page).proceed_to_checkout()
        CheckoutPage(page).fill_shipping(self._firstName, self._lastName, self._zipCode)