class Hero:

    people ='people'

    def __init__(self,name,nickname,superpower,health_points):
        self.name = name
        self.nicname = nickname
        self.superpower = superpower
        self.health_points = health_points


    def __mul__(self):
        return Hero(self.health_points * 2) 

      


    def __str__(self):
        return f'{self.name}\n' \
               f'{self.nicname}\n' \
               f'{self.superpower}\n' \
               f'{self.health_points}'

a = Hero('Tony Stark','stark','iron man',100)
print(a)

def printt(name):
    print(f'{name} its his name')
printt('Tony Stark')   
   



def __len__(self):
        return len(self) 
print(len(a.name)) 


     
