from interfaces.s_one import SOneContract

class Worker(SOneContract):
    def do_work(self):
        print("I am an internal worker doing work")