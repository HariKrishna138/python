class A:
    company_name="SKAI"
    def __init__(self,eid,ename,edept,esal):
        self.greet="GOOD MORNING"
        self.eid=eid
        self.ename=ename
        self.edept=edept
        self.esal=esal
    def display(self):
        print(self.company_name,"\n",self.greet,"\nEmployee: \nID = ",self.eid,"\nName = ",self.ename,"\nDepartment = ",self.edept,"\nSalary = ",self.esal,"\n -----------------")
    def __del__(self):
        print("OBJECT DESTROYED \n -------------")
z=A(101,'ramu',"clerk",20000)
z.display()
del z
w=A(102,"raju","manager",55000)
w.display()
del w
e=A(103,'ravi','general manager',47000)
e.display()
del e
