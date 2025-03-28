from workers.worker import Worker
from thirdparty.third_party_class import ThirdPartyWorker
from interfaces.s_one import SOneContract
from interfaces.s_two import STwoContract

if __name__ == "__main__":

    """
        This is the registration of the third party to enable our system to treat it as a subclass of SOneContract".
        This makes ThirdPartyWorker a virtual subclass of SOneContract
    """
    SOneContract.register(ThirdPartyWorker)

    workers = [Worker(), ThirdPartyWorker()]

    for worker in workers:
        if(isinstance(worker, SOneContract)):
            worker.do_work()
        if(isinstance(worker, STwoContract)):
            worker.s_two_work()