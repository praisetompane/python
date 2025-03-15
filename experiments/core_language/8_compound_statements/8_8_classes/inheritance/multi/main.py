from child import Child
from mother import Mother
from father import Father

if __name__ == "__main__":
    paul = Child()

    print(paul.skills())
    print(isinstance(paul, Father))
    print(isinstance(paul, Mother))

map()
