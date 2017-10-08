class users:
    def __init__(self,username,pw,role,score):
       self.username=username
       self.password=pw
       self.role=role
       if(role == "I"):
           if score:
               print"Score not allowed"

           else:
               score=None


    def checkInstructor(self):
        if (role == "I"):
            return True
        else:
            return False
    def checkStudent(self):
        if (role == "S"):
            return True
        else:
            return False

