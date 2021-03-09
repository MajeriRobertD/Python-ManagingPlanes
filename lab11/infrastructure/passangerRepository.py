from domain.passanger import Passanger

class PassangerRepository():
    def __init__(self):
        self.__passangers = []
         
    def __str__(self):
        p = ''
        for passanger in self.__passangers:
            p = p + str(passanger)
        return p
    def verify_pass(self, other_passanger):
        for el in self.__passangers:
            if el.get_pass_numb() ==other_passanger.get_pass_numb():
                return 1
            return -1
    
    def add_passanger(self, new_passanger):
        if self.verify_pass(new_passanger) == 1:
            raise ValueError("Passanger already in")
        self.__passangers.append(new_passanger)

    def get_all_pass(self):
        return self.__passangers
    
    def del_by_index(self,index):
        if index >= 0 and index < len(self.__passangers):
            del self.__passangers[index]
        
        else:
            raise IndexError("Index out of range")

    def update_by_index(self, index, new_passanger):
        if index >= 0 and index < len(self.__passangers):
            self.__passangers[index].set_first_name(new_passanger.get_first_name())
            self.__passangers[index].set_last_name(new_passanger.get_last_name())
            self.__passangers[index].set_pass_numb(new_passanger.get_pass_numb())
        
        else:
            raise IndexError('Index out of range')






    