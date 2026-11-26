class SoftAssert:
    def __init__(self):
        self.errors = []

    def check(self, condition: bool, message: str):
        if not condition:
            self.errors.append(message)

    def assert_all(self):
        assert not self.errors, (
            "Soft assertion errors:\n" + "\n".join(self.errors)
        )