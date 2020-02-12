from termcolor import cprint

class SeaPassage:

    def __init__(self, dep_port, arr_port, dist_miles):
        self.dep_port = dep_port
        self.arr_port = arr_port
        self.dist_miles = dist_miles


class Port:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} port'

# TODO: include terminals dict in Port class
    def ship_arrived(self, ship):
        ship.position = self.name + f' port'
        return self.name + f' port'




class Terminal(Port):

    def __init__(self, name, terminal_cargo, load_rate=20, disch_rate=25):
        super().__init__(name=name)
        self.terminal_cargo = terminal_cargo
        self.load_rate = load_rate
        self.disch_rate = disch_rate

    def __str__(self):
        res = super().__str__()
        return res + f', {self.terminal_cargo} terminal'

    def ship_arrived(self, ship):
        ship.position = self.name + f', {self.terminal_cargo} terminal'


class Ship:

    def __init__(self, name, deadweight):
        self.name = name
        self.deadweight = deadweight
        self.hfo = 200
        self.mgo = 100
        self.crew = 15


    def __str__(self):
        return f'\'{self.name}\' ship, '


class GeneralCargo(Ship):
    fuel_rate = 10
    cargo = 'general'

    def __init__(self, name, deadweight):
        super().__init__(name=name, deadweight=deadweight)
        self.cargo_quantity = None
        self.speed = 0
        self.position = None
        self.DTG = 0
        self.position = None

    def sail(self, route):
        self.position = 'sea'
        self.DTG = route.dist_miles

    def act(self):
        if self.hfo or self.mgo <= 10:
            self.bunker()
        elif self.position == 'sea':
            self.hfo -= self.fuel_rate
            self.speed = self.speed
            # if self.DTG > self.speed:
            #     self.DTG = self.DTG - self.speed
            # else:
            #     self.position =


        elif 'port' in self.position:
            self.mgo -= self.fuel_rate
            self.speed = 0

    def bunker(self):
        self.hfo += 200
        self.mgo += 100
        self.speed = 0


    def __str__(self):
        res = super().__str__()
        return res + f'{self.cargo} cargo type, deadweight {self.deadweight} tons, crew {self.crew} memebers, ' \
                     f'porisition: {self.position}'


class Tanker(GeneralCargo):
    fuel_rate = 15
    cargo = 'crude oil'

    def __init__(self, name, deadweight):
        super().__init__(name=name, deadweight=deadweight)
        self.inert_gas_system = True

    def __str__(self):
        return super().__str__()


class Container(GeneralCargo):
    fuel_rate = 20
    cargo = 'containers'

    def __init__(self, name, deadweight):
        super().__init__(name=name, deadweight=deadweight)
        self.self_discharging = True

    def __str__(self):
        return super().__str__()


bea_luna = GeneralCargo(name='bea_luna', deadweight=7000)
bea_luna.crew = 10
print(bea_luna)

eva_marie = Tanker(name='eva_marie', deadweight=78000)
eva_marie.crew = 18
print(eva_marie)

lara = Container(name='lara', deadweight=79000)
lara.crew = 20
print(lara)

albany = Port(name='Albany')

albany_gencargo_terminal = Terminal(name='Albany', terminal_cargo='general cargo')
print(albany_gencargo_terminal)

albany_tanker_terminal = Terminal(name='Albany', terminal_cargo='crude oil', load_rate=25, disch_rate=15)
print(albany_tanker_terminal)

albany_container_terminal = Terminal(name='Albany', terminal_cargo='containers', load_rate=40, disch_rate=45)


valvik_gencargo_terminal = Terminal(name='Valvik', terminal_cargo='general cargo', load_rate=10, disch_rate=5)
print(valvik_gencargo_terminal)

valvik_tanker_terminal = Terminal(name='Valvik', terminal_cargo='crude oil', load_rate=20, disch_rate=10)
print(valvik_tanker_terminal)

valvik_container_terminal = Terminal(name='Valvik', terminal_cargo='containers', load_rate=35, disch_rate=50)
print(valvik_container_terminal)

albany_valvik = SeaPassage(dep_port='Albany', arr_port='Valvik', dist_miles=5000)
valvik_albany = SeaPassage(dep_port='Valvik', arr_port='Albany', dist_miles=6000)

# hour = 365
# while hour:
#     hour -= 1
#     cprint('---------------- Час {} ---------------'.format(hour), color='red')

terminals = {'general' : albany_gencargo_terminal, 'crude oil' : albany_tanker_terminal, 'containers' :
    albany_container_terminal}

albany.ship_arrived(bea_luna)
for terminal in terminals.items():
    if bea_luna.cargo == terminal[0]:
        terminal[1].ship_arrived(bea_luna)

print(bea_luna.position)


print(bea_luna)
