import smartpy as sp

class SimpleOpeartion(sp.Contract):
    def __init__(self):
        self.init(storedValue = 4, flag = False, doubleArray = [[0,0,0],[0,0,0],[0,0,0]])
    
    @sp.entry_point
    def set(self,params):
        self.data.storedValue = params.op

    @sp.entry_point
    def doubleIt(self):
        self.data.storedValue *= 2
    
    @sp.entry_point
    def divide(self,params):
        sp.verify(params.op > 0)
        self.data.storedValue /= params.op

    @sp.entry_point
    def factorial(self,params):
        sp.verify(params.op > 0)
        self.data.storedValue = 1
        sp.for x in sp.range(1, params.op+1):
            self.data.storedValue *= x
    
    @sp.entry_point
    def reverseFlag(self):
        self.data.flag = ~self.data.flag

    
@sp.add_test(name = "Test simple opeartions")
def testSimpleOpeartions():
    scenario = sp.test_scenario()
    sc = SimpleOpeartion()
    scenario += sc
    scenario += sc.set(op = 2)
    scenario += sc.doubleIt()
    scenario += sc.divide(op = 2).run(valid=True)
    scenario += sc.factorial(op = 5)
    scenario += sc.reverseFlag()
