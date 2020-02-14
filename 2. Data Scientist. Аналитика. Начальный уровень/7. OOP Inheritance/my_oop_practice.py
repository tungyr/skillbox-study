from termcolor import cprint

class SeaPassage:

    def __init__(self, dep_port, arr_port, dist_miles):
        self.dep_port = dep_port
        self.arr_port = arr_port
        self.dist_miles = dist_miles


class Port:

    def __init__(self, name):
        self.name = name
        self.load_rate = 2000
        self.disch_rate = 2500

    def __str__(self):
        return f'{self.name} port'

# TODO: include terminals dict in Port class
    def ship_arrived(self, ship):
        ship.position = self.name + f' port'
        print(f'Ship {ship.name} has arrived to {self.name} port')
        ship.mgo -= ship.fuel_rate
        if ship.cargo_quantity == 0:
            self.loading(ship)
        else:
            self.discharging(ship)
        # return self.name + f' port'


    def loading(self, ship):
        while ship.deadweight >= ship.cargo_quantity:
            ship.cargo_quantity = ship.cargo_quantity + self.load_rate
            # fuel consumption in port
            ship.mgo -= ship.fuel_rate
        else:
            # as soon as ship has loaded
            ship.cargo_quantity = ship.deadweight
            print(f'Ship {ship.name} has completely loaded in {self.name}!')
            ship.act()

    def discharging(self, ship):
        while 0 <= ship.cargo_quantity:
            ship.cargo_quantity = ship.cargo_quantity - self.load_rate
        else:
            ship.cargo_quantity = 0
            print(f'Ship {ship.name} discharged in {self.name}!')
            ship.mgo -= ship.fuel_rate
            return



# class Terminal(Port):
#
#     def __init__(self, name, terminal_cargo, load_rate=2000, disch_rate=2500):
#         super().__init__(name=name)
#         self.terminal_cargo = terminal_cargo
#         self.load_rate = load_rate
#         self.disch_rate = disch_rate
#
#     def __str__(self):
#         res = super().__str__()
#         return res + f', {self.terminal_cargo} terminal'
#
#     def ship_arrived(self, ship):
#         ship.destination = None
#         ship.DTG = 0
#         ship.position = self.name + f', {self.terminal_cargo} terminal'


class Ship:

    def __init__(self, name, deadweight):
        self.name = name
        self.deadweight = deadweight
        self.hfo = 60
        self.mgo = 50
        self.crew = 15
        self.route = None
        self.DTG = 0


    def __str__(self):
        return f'\'{self.name}\' ship, '


class GeneralCargo(Ship):
    fuel_rate = 10
    cargo = 'general'

    def __init__(self, name, deadweight):
        super().__init__(name=name, deadweight=deadweight)
        self.cargo_quantity = 0
        self.speed = 0
        self.position = 'port'

    def sail(self):
        # check for enough fuel quantity for passage
        hfo_for_route = round((self.route.dist_miles / 300) * self.fuel_rate)
        mgo_for_port = (self.cargo_quantity / self.route.arr_port.disch_rate) * self.fuel_rate

        if self.hfo < hfo_for_route:
            self.bunker(hfo_for_route=hfo_for_route + 10)
        if self.mgo < mgo_for_port:
            self.bunker(mgo_for_port=mgo_for_port + 10)

        self.position = 'sea'
        self.speed = 300
        self.DTG = self.route.dist_miles
        print(f'Ship sailed from {self.route.dep_port} to {self.route.arr_port}, DTG {self.DTG}')
        days = 1
        while self.DTG > self.speed:
            self.DTG = self.DTG - self.speed
            print(f'Day {days}. Ship sailing from {self.route.dep_port} to {self.route.arr_port}, DTG {self.DTG}')
            self.hfo -= self.fuel_rate
            days += 1
        else:
            self.DTG = 0
            self.route.arr_port.ship_arrived(self)



    def act(self):
        # if self.hfo <= 10 or self.mgo <= 10:
        #     self.bunker()

        if self.position == 'sea':
            self.speed = self.speed
            if self.DTG > self.speed:
                self.DTG = self.DTG - self.speed
            else:
                self.position = self.route.arr_port
                self.route.arr_port.ship_arrived(self)
        elif 'port' in self.position:
            self.speed = 0
            # if vessel loaded
            if self.cargo_quantity == self.deadweight:
                # departure after loading completion
                self.sail()
            else:
                # if vessel in ballast
                self.route.dep_port.loading(self)

    def bunker(self, hfo_for_route=0, mgo_for_port=0):
        self.position = 'bunker'
        self.hfo = self.hfo + hfo_for_route
        self.mgo = self.mgo + mgo_for_port
        print(f'Ship {self.name} bunkered with {hfo_for_route} hfo tons and {mgo_for_port} mgo tons!')



    def __str__(self):
        res = super().__str__()
        return res + f'{self.cargo} cargo type, deadweight {self.deadweight} tons, crew {self.crew} memebers, ' \
                     f'porisition: {self.position}, destination: {self.route.arr_port}, DTG: {self.DTG}, ' \
                     f'cargo: {self.cargo_quantity}'


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




# eva_marie = Tanker(name='eva_marie', deadweight=78000)
# eva_marie.crew = 18
# print(eva_marie)
#
# lara = Container(name='lara', deadweight=79000)
# lara.crew = 20
# print(lara)

albany = Port(name='Albany')
valvik = Port(name='Valvik')

# albany_gencargo_terminal = Terminal(name='Albany', terminal_cargo='general cargo')


# albany_tanker_terminal = Terminal(name='Albany', terminal_cargo='crude oil', load_rate=25, disch_rate=15)
# print(albany_tanker_terminal)
#
# albany_container_terminal = Terminal(name='Albany', terminal_cargo='containers', load_rate=40, disch_rate=45)


# valvik_gencargo_terminal = Terminal(name='Valvik', terminal_cargo='general cargo', load_rate=10, disch_rate=5)


# valvik_tanker_terminal = Terminal(name='Valvik', terminal_cargo='crude oil', load_rate=20, disch_rate=10)
# print(valvik_tanker_terminal)
#
# valvik_container_terminal = Terminal(name='Valvik', terminal_cargo='containers', load_rate=35, disch_rate=50)
# print(valvik_container_terminal)

albany_valvik = SeaPassage(dep_port=albany, arr_port=valvik, dist_miles=5000)
valvik_albany = SeaPassage(dep_port=valvik, arr_port=albany, dist_miles=6000)

# hour = 365
# while hour:
#     hour -= 1
#     cprint('---------------- Час {} ---------------'.format(hour), color='red')

# terminals = {'general' : albany_gencargo_terminal, 'crude oil' : albany_tanker_terminal, 'containers' :
#     albany_container_terminal}
#
# albany.ship_arrived(bea_luna)
# for terminal in terminals.items():
#     if bea_luna.cargo == terminal[0]:
#         terminal[1].ship_arrived(bea_luna)

bea_luna = GeneralCargo(name='Bea-Luna', deadweight=7000)
bea_luna.route = albany_valvik
print(bea_luna)
bea_luna.act()
print(bea_luna)
print(bea_luna.hfo, bea_luna.mgo)

bea_luna.route = valvik_albany
print(bea_luna)
bea_luna.act()
print(bea_luna.hfo, bea_luna.mgo)



# days = 0

# while days < 50:
#     cprint('---------------- Day {} ---------------'.format(days), color='red')