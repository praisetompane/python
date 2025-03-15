from father import Father
from mother import Mother


class Child:

    def __init__(self, mother: Mother, father: Father):
        self.mother = mother
        self.father = father

    def skills(self):
        return ["Sports"] + self.mother.skills() + self.father.skills()
