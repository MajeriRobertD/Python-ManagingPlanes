class Passanger(object):
    def __init__(self, first_name = '', last_name = '', pass_numb = ''):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pass_numb = pass_numb
    
    def get_first_name(self):
        return self.__first_name
         
    def get_last_name(self):
        return self.__last_name

    def get_pass_numb(self):
        return self.__pass_numb

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
         
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_pass_numb(self, new_pass_numb):
        self.__pass_numb = new_pass_numb

    def __eq__(self, other):
        if self.__pass_numb == other.get_pass_numb():
            return True
        return False

    def __str__(self):
        return self.__first_name.title() + ' ' + self.__last_name.title() + ' ' + str(self.__pass_numb)

    def __repr__(self):
        return str(self)