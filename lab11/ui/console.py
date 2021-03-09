from domain.plane import Plane
from domain.passanger import Passanger

class PlaneUI():
    def __init__(self, controller):
        self.controller = controller

    @staticmethod
    def print_menu():
        s = 'Menu: \n'
        s += '\t 0.Exit \n'
        s += '\t 1.Add plane \n'
        s += '\t 2.Show all planes \n'
        s += '\t 3.Add Passanger \n'
        s += '\t 4.Show all passangers \n'
        s += '\t 5.Update plane by index \n'
        s += '\t 6.Delete plane at index \n'
        s += '\t 7.Add a passanger to a plane at given index. \n'
        s += '\t 8.Sort by last name. \n'
        print(s)

    @staticmethod
    def read_passanger():
        first_name = input("Passanger first name:")
        last_name = input('Passanger last name:')
        pass_numb = input('Passanger passport number:')
        return Passanger(first_name, last_name, pass_numb)

       



    @staticmethod
    def read_plane():
        number = int(input('Give plane identification number'))
        company = input("Give plane company")
        seats = int(input("How many seats does this plane have?"))
        destination = input("What is the destination?")
        passangers = []
        p_len = int(input("How many passengers does this plane have:"))
        for _ in range(p_len):
            passangers.append(PlaneUI.read_passanger())
        return Plane(number, company, seats, destination, passangers)

    @staticmethod
    def print_passangers(the_plane):
        for el in the_plane.get_passangers():
            print(el)


    def main_menu(self):
        while True:
            self.print_menu()
            selection = int(input('Enter choice:'))

            if selection == 1:
                p = PlaneUI.read_plane()
                self.controller.add_plane_ctrl(p)
                #for el in p.get_passangers():
                #    self.controller.add_passanger_ctrl(el)

                anykey = input('Enter any key to return to main menu')
                self.main_menu()
                break
            
            elif selection == 2:
                for el in self.controller.get_all_ctrl():
                    print(el)
                    

                anykey = input('Enter any key to return to main menu')
                self.main_menu()
                break

            elif selection == 3:
                pas = PlaneUI.read_passanger()
                self.controller.add_passanger_ctrl(pas)

                anykey = 'Enter any key to return to main menu: '
                self.main_menu()
                break
            
            elif selection == 4:
                for el in self.controller.get_all_passangers():
                    print(el)

                anykey = input('Enter any key to return to main menu: ')
                self.main_menu()
                break

            elif selection == 5:
                the_index = int(input('Enter index: '))
                new_plane = PlaneUI.read_plane()
                self.controller.update_plane_by_index_ctrl(the_index, new_plane)

                anykey = 'Enter any key to return to main menu: '
                self.main_menu()
                break
            
            elif selection == 6:
                the_index = int(input('Enter index: '))
                self.controller.delete_plane_by_index(the_index)

                anykey = 'Enter any key to return to main menu: '
                self.main_menu()
                break
            elif selection == 7:
                the_plane = self.controller.plane_get_by_index_ctrl(int(input('Enter index: ')))
                self.controller.add_passanger_to_a_plane_ctrl(the_plane, PlaneUI.read_plane())

            elif selection == 8:
                the_plane = self.controller.plane_get_by_index_ctrl(int(input('Enter index: ')))
                self.controller.sort_by_last_name_ctrl(the_plane)
                PlaneUI.print_passangers(the_plane)

            
            elif selection == 0:
                break
                
            else:
                print('Invalid choice')
            
            