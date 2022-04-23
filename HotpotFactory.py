class HotpotStore(object):
 
    def createHotpot(self, typeName):
        pass
 
    def order(self, typeName):
        # 让火锅工厂根据类型，做一锅火锅
        self.Hotpot = self.createHotpot(typeName)
        self.Hotpot.mild()
        self.Hotpot.spicy()
        self.Hotpot.meat()
        self.Hotpot.vegetable()
 
# 定义一个SWUFE火锅店类
class SWUFEHotpotStore(HotpotStore):
 
    def createHotpot(self, typeName):
        self.HotpotFactory = HotpotFactory()
        return self.HotpotFactory.createHotpot(typeName)
 
 
# 定义鸳鸯锅类
class YuanyangHotpot(object):
 
    # 定义鸳鸯锅的方法
    def spicy(self):
        print("---加红锅部分---")

    def mild(self):
        print("---加清汤部分---")   
    
    def meat(self):
        print("---加荤菜---")
 
    def vegetable(self):
        print("---加素菜---")
 
# 定义红锅类
class SpicyHotpot(object):
 
    # 定义红锅的方法
    def meat(self):
        print("---加荤菜---")
 
    def vegetable(self):
        print("---加素菜---")
 
# 定义一个生产汽车的工厂，让其根据具体得订单生产车
class HotpotFactory(object):
 
    def createHotpot(self,typeName):
        self.typeName = typeName
        if self.typeName == "鸳鸯锅":
            self.Hotpot = YuanyangHotpot()
        elif self.typeName == "红锅":
            self.Hotpot = SpicyHotpot()
 
        return self.Hotpot
 
suonata = SWUFEHotpotStore()
suonata.order("红锅")