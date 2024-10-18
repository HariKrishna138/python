class father:
    nameF="FATHER"
    def B1(self):
        print("FATHER PROPERTIES")
class son1(father):
    nameS1="SON1"
    def B2(self):
        print(self.nameF,"PROPERTIES BELONG TO",self.nameS1)
class son2(father):
    nameS2="SON2"
    def B3(self):
        print(self.nameF,"PROPERTIES BELONGS TO",self.nameS2)
a=son1()
a.B1()
a.B2()
b=son2()
b.B1()
b.B3()
