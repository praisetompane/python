from child import Child
from mother import Mother
from father import Father

if __name__ == "__main__":
    sam = Father()
    vicky = Mother()
    paul = Child(vicky, sam)

    print(paul.skills())
    print(isinstance(paul, Father))
    print(isinstance(paul, Mother))
