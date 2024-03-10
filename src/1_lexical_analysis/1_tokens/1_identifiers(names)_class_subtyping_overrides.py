class Parent:
    def __init__(self, values):
        self.items = []
        """ notice this uses the __update(...) copy
            if it used update(...) instead
                the subclass instantiation would fail, because  
                    "update(self, values)" would overridden to "update(self, values, some_modifier)"

        """
        self.__update(values)

    def update(self, values):
        for v in values:
            self.items.append(v)

    """
        - copy the update definition to allow subclasses overriding the update method
            without breaking __init__ method.
        - would be mangled to _Parent__update.
    """
    __update = update


class Child(Parent):
    # ∴ does not break Parent.__init__ which requires this "def update(self, values):"
    # because parent is using __update which has the definition prior to the override.
    def update(self, values, some_modifier):
        for i in range(0, len(self.items)):
            self.items[i] = self.items[i] + some_modifier
        for v in values:
            self.items.append(v + some_modifier)

    """ 
        the Child can define an __update value
            without breaking the parent.
        it would be mangled to _Child__update
    """
    __update = update


class GrandChild(Child):

    """
    If we use a private value (i.e. _update in Parent) to enable overriding update(self, values)
        this only solves it for one generation.

        If a grand child wants to use the _update name/identiifer
            it would override the Parent class one.
            thus breaking Parent.__init__
    """

    # _update = None # This breaks Parent.__init__ is private used.

    # This works because this value is mangled to _GrandChild__update and does not override _Parent.__update
    __update = None


if __name__ == "__main__":
    natural_numbers = range(1, 11)
    parent = Parent(natural_numbers)
    print(parent.items)
    more_natural_numbers = range(11, 21)
    parent.update(more_natural_numbers)
    print(parent.items)

    child = Child(natural_numbers)
    print(child.items)
    child.update(more_natural_numbers, 2)
    print(child.items)

    grandChild = GrandChild(natural_numbers)
