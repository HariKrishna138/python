class father:
    nameF="FATHER"
    def B1(self):
        print("FATHER PROPERTIES")
class son(father):
    nameS="SON"
    def B2(self):
        print(self.nameF,"PROPERTIES BELONG TO",self.nameS)
a=son()
a.B1()
a.B2()
