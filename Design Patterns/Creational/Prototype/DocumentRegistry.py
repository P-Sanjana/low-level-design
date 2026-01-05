class DocumentRegistry:
    def __init__(self):
        self.prototypes = {}

    def register(self, key, value):
        self.prototypes[key] = value

    def get(self, key):
        prototype = self.prototypes[key]
        if prototype is not None:
            return prototype.clone()
        raise ValueError(f"No prototype found for key {key} in the registry")

