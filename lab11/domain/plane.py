class Plane(object):
    def __init__(self, number = 0, company = '', seats = 0, destination = '', passangers =[]):
        self.__number = number
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passangers = passangers
    
    def get_number(self):
        return self.__number
    
    def get_company(self):
        return self.__company
        
    def get_seats(self):
        return self.__seats
    
    def get_destination(self):
         return self.__destination

    def get_passangers(self):
        return self.__passangers

    def set_number(self, new_number):
        self.__number = new_number

    def set_company(self, new_company):
        self.__company = new_company

    def set_seats(self, new_seats):
        self.__seats = new_seats

    def set_destination(self, new_destination):
        self.__destination = new_destination

    def add_passanger_to_plane(self,new_passanger):
        self.__passangers.append(new_passanger)

    def __eq__(self, other):
        if self.__number == other.get_number():
            return True
        return False

    def __str__(self):
        return 'Plane nr: ' + str(self.__number) + self.__company + ' Seats: ' + str(self.__seats) + ' ' + self.__destination + str(self.__passangers)

    def __repr__(self):
        return str(self)
        

    