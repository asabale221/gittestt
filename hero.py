class SuperHero:
    people='people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name=name
        self.health_points=health_points
        self.superpower=superpower
        self.nickname=nickname
        self.catchphrase=catchphrase


    def pritt(self):
        print(self.name, 'is runn')

            

Piter=SuperHero('Piter')
Piter.pritt()
spyderman=SuperHero('Piter')
print(spyderman.name)


     
