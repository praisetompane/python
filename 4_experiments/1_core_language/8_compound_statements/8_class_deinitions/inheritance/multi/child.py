from father import Father
from mother import Mother


class Child(Mother, Father):
    def skills(self):
        return ["Sports"] + Mother.skills(self) + Father.skills(self)
