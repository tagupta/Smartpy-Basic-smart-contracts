import smartpy as sp

class Registry(sp.Contract):
    def __init__(self, _admin):
        self.init(admin = _admin, registry = sp.map(tkey = sp.TAddress, tvalue = sp.TInt))
    
    @sp.entry_point
    def addRecord(self, params):
        self.data.registry[sp.sender] = params.amount
    
    @sp.entry_point
    def addRecordAdmin(self, params):
        sp.verify(sp.sender == self.data.admin)
        self.data.registry[params.account] = params.amount

@sp.add_test(name = "Testing Registry Contract")
def testingRegistry():
    scenario = sp.test_scenario()
    sc = Registry(sp.address('tz1NZs63YHaxYWdgoHhqZPZFTn58GRgjxGmr'))
    scenario += sc
    scenario += sc.addRecord(amount = 53352).run(sender = sp.address('tz1-address-1'))
    scenario += sc.addRecord(amount = 29893).run(sender = sp.address('tz1-address-2'))
    scenario += sc.addRecord(amount = 34344).run(sender = sp.address('tz1-address-3'))
    scenario += sc.addRecordAdmin(account = sp.address('tz1-address-4'), amount = 5656).run(sender = sp.address('tz1NZs63YHaxYWdgoHhqZPZFTn58GRgjxGmr'))
