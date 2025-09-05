
def titlecase(value: str) -> str:
    """Return Title Case string."""
    return value.title()

class FilterModule(object):
    def filters(self):
        return {"titlecase": titlecase}
