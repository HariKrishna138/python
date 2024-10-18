class grandfather:
    nameGF="GRAND FATHER"
    def B1(self):
        print("GRAND FATHER PROPERTIES")
class father:
    nameF="FATHER"
    def B2(self):
        print("FATHER PROPERTIES")       
class son(grandfather,father):
    nameS="SON"
    def B3(self):
        print(self.nameF,"PROPERTIES BELONGS TO",self.nameS)
        print(self.nameGF,"PROPERTIES BELONG TO",self.nameS)
a=son()
a.B1()
a.B2()
a.B3()
