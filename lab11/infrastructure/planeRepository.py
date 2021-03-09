from domain.plane import Plane
from utils import my_sort, my_search
class PlaneRepository():
    def __init__(self):
        self.__planes = []

    def __str__(self):
        p = ''
        for plane in self.__planes:
            p = p+ str(plane)
        return p 
    
    def verify_number(self, other_plane):
        for el in self.__planes:
            if el.get_number() == other_plane.get_number():
                return 1
            return -1

    def add_plane(self, new_plane):
        if self.verify_number(new_plane) == 1:
            raise ValueError("Plane already in")
        self.__planes.append(new_plane)

    def get_all(self):
        return self.__planes

    def get_by_index(self, index):
        return self.__planes[index]


    def del_by_index(self, index):
       if index >= 0 and index < len(self.__planes):
           del self.__planes[index]
       else:
           raise IndexError("Index out of range")

    def update_by_index(self,index, new_plane):
        if index >= 0 and index < len(self.__planes):
            self.__planes[index].set_number(new_plane.get_number())
            self.__planes[index].set_company(new_plane.get_company())
            self.__planes[index].set_seats(new_plane.get_seats())
            self.__planes[index].set_destination(new_plane.get_destination())
        else:
            raise IndexError("Index out of range")

    def sort_by_last_name(self, plane):
        def f(x,y):
            if x.get_last_name() <= y.get_last_name():
                return True
            return False
        return my_sort(plane.get_passangers(), f)

    def sort_by_number_of_passangers(self):
        def f(x,y):
            if len(x.get_passangers()) <= len(y.get_passangers()):
                return True
            return False
        return my_sort(self.__planes, f)

    def sort_by_num_substring(self, substring):

        def num_with_sub(plane, substring):
            return len([x for x in plane.get_passangers() if x.get_first_name().startswith(substring)])

        def f(x,y):
            if num_with_sub(x, substring) <= num_with_sub(y, substring):
                return True
            return False

        return my_sort(self.__planes, f)

    def sort_by_concatenation_of_number_and_destination(self, plane):
        def concatenation_string(plane):
            return str(len(plane.get_passangers()) + plane.get_destination())
        return my_sort(self.__planes, lambda x, y: concatenation_string(x) <= concatenation_string(y))

    def search_planes_passport_start_with(self, substring):
        def passport_start_with(plane, substring):
            for x in plane.get_passangers():
                if x.get_pass_numb().startswith(substring,0,2):
                    return True
                return False
        return my_search(self.__planes, passport_start_with)

    def search_pass_whose_name_contains(self, plane, substring):
        def contains_str(plane, substring):
            for x in plane.get_passangers():
                if substring in x.get_last_name() or substring in x.get_first_name():
                    return True
                return False
        return my_search(self.__planes, contains_str)

    def search_plane_with_name(self, the_name):
        def has_name(plane,the_name):
            for x in plane.get_passangers():
                if x.get_first_name() + x.get_last_name() == the_name:
                    return True
                return False
            return my_search(self.__planes, has_name)
        