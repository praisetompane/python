from abc import ABCMeta, abstractmethod

class SOneContract(metaclass = ABCMeta):
    
    @abstractmethod
    def do_work(self):
        raise NotImplemented

    """    
        # NB: @abstractmethod only applies to subclasses created using regular inheritance.
              virtual sub classes can be instantiated without implementing it, while regular subclasses cannot.
    @abstractmethod
    def s_one_specialty(self):
        raise NotImplemented
    """

    def __issubclasshook__(cls):
        """
            NB: Alternativeltm we overload the behvaiour of `issubclass` function for SOneContract
                    and define what it means to be a SOneContract.
        """
        pass