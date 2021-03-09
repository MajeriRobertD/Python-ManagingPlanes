from domain.plane import Plane 
from domain.passanger import Passanger
from infrastructure.planeRepository import PlaneRepository
from infrastructure.passangerRepository import PassangerRepository
from application.controller import Controller
from ui.console import PlaneUI


repo_plane = PlaneRepository()
repo_pass = PassangerRepository
ctrl = Controller(repo_plane, repo_pass)
ui = PlaneUI(ctrl)
ui.main_menu()

