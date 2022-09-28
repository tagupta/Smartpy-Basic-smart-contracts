import smartpy as sp

class MyContract(sp.Contract):
    def __init__(self, _param1, _param2, _admin):
        self.init(param1 = _param1, param2 = _param2, admin = _admin)
    
    @sp.entry_point
    def entry1(self, params):
        sp.verify(self.data.param1 + params <= 100)
        self.data.param1 += params

    @sp.entry_point
    def entry2(self, params):
        sp.verify(self.data.param2 - params >= 0)
        self.data.param2 -= params
    
    @sp.entry_point
    def reset(self):
        sp.verify(self.data.admin == sp.sender)
        self.data.param1 = 50
        self.data.param2 = 50

@sp.add_test(name = "Testing my contract")
def tester():
    admin = sp.test_account("Administration")
    alice = sp.test_account("Alice")

    scenario = sp.test_scenario()
    scenario.h1("Displaying contract")
    c1 = MyContract(50,50,admin.address)
    scenario += c1

    scenario.h2("Running transactions")
    scenario += c1.entry1(12)
    scenario += c1.entry1(40).run(valid = False)
    scenario += c1.entry2(12)
    scenario += c1.entry2(40).run(valid = False)
    
    scenario.h4("Verifying some parameters")
    scenario.verify(c1.data.param1 == 62)
    scenario.show(c1.data.param1)
    scenario.verify(c1.data.param2 == 38)
    scenario.show(c1.data.param2)

    scenario.h4("Resetting some parameters")
    scenario += c1.reset().run(sender = alice, amount = sp.mutez(10000), valid = False)

    scenario.show((c1.data.param1 - 2) * 2)
    x = scenario.compute((c1.data.param1 - 2) * 2)
    scenario.verify(x == 120)
    scenario.simulation(c1)
