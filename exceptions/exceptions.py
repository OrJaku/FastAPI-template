
class SomeException(Exception):
    def __init__(self, value: str | int | float) -> None:
        self.msg = f"Exception message: '{value}'."
        super().__init__(self.msg)
