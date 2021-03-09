from domain.passanger import Passanger

class Controller():
    def __init__(self, repo_plane, repo_pass    ):
        self.__repo_plane = repo_plane
        self.__repo_pass = repo_pass
    
    def add_plane_ctrl(self, new_plane):
        self.__repo_plane.add_plane(new_plane)

    def get_all_ctrl(self):
        return self.__repo_plane.get_all()

    def add_passanger_ctrl(self, new_passanger):
        #import pdb; pdb.set_trace()
        self.__repo_pass.add_passanger(new_passanger)

    def get_all_passangers(self):
        return self.__repo_pass.get_all_pass()

    def plane_get_by_index_ctrl(self, the_index):
        return self.__repo_plane.get_by_index(the_index)

    def update_plane_by_index_ctrl(self, the_index, new_plane):
        self.__repo_plane.update_plane_by_index(the_index)

    def delete_plane_by_index(self, the_index):
        self.__repo_plane.del_by_index(the_index)

    def add_passanger_to_a_plane_ctrl(self, new_passanger):
        self.__repo_plane.add_passangers_to_plane(new_passanger)
    
    def sort_by_last_name_ctrl(self, plane):
        self.__repo_plane.sort_by_last_name(plane)







