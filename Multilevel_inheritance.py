class grandfather:
    nameGF="GRAND FATHER"
    def B1(self):
        print("GRAND FATHER PROPERTIES")
class father(grandfather):
    nameF="FATHER"
    def B2(self):
        print(self.nameGF,"PROPERTIES BELONG TO",self.nameF)
class son(father):
    nameS="SON"
    def B3(self):
        print(self.nameF,"PROPERTIES BELONGS TO",self.nameS)
a=son()
a.B1()
a.B2()
a.B3()
