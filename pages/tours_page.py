from pages.base_page import BasePage

class ToursPage(BasePage):

    def _verify_page(self):
        assert "Search Results" in self.driver.title