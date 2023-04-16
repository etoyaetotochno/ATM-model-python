def clear(func):
    def wrapper(self, *args, **kwargs):
        for element in self.elements:
            element.grid_remove()
        self.entry_visible = False
        self.grid(sticky="sew")
        func(self, *args, **kwargs)
    return wrapper

def entry(func):
    def wrapper(self, *args, **kwargs):
        self.entry_visible = True
        func(self, *args, **kwargs)
    return wrapper