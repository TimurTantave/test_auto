
from ui.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def __init__(self, page):
        super().__init__(page)

        self.images = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".row img"),
            description="Dynamic content images",
        )

    def get_image_sources(self) -> list[str]:
        return [
            image.get_attribute("src")
            for image in self.images.all()
        ]

    def has_duplicate_images(self) -> bool:
        sources = self.get_image_sources()
        return len(sources) != len(set(sources))

    def refresh_page(self) -> None:
        self.actions.reload()
