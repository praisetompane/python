from abc import ABC

class STwoContract(ABC):
    """
        NB: This is an alternative to explicitly setting the metaclass to ABCMeta.
            The ABC class is syntactic sugar.
    """
    def s_two_work(self):
            pass