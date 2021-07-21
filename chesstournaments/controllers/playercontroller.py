from ..utils.menu import Menu
from ..utils.utilsanddata import PlayerData
from ..views.playerview import PlayerView, PlayerOptionView
from ..models.player import Player
from .import appcontroller


class PlayerMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = PlayerView(self.menu)

    def __call__(self, store):
        self.menu.add("auto", "Créer un nouveau joueur", CreatePlayerController())
        self.menu.add("auto", "Supprimer un joueur", DeletePlayer())
        self.menu.add("auto", "Retour à l'écran d'accueil", appcontroller.BackHomeMenuController())

        user_choice = self.view.get_user_choice()

        return user_choice.handler


class CreatePlayerController:
    def __init__(self):
        self.save = PlayerData()

    def __call__(self, store):
        data = PlayerOptionView.create_player()
        player = Player(**data)
        store["players"].append(player)
        self.save.save_player_data(player)

        return PlayerMenuController()


class DeletePlayer:
    def __init__(self):
        self.delete = PlayerData()

    def __call__(self, store):
        PlayerOptionView.display_players_list(store["players"])
        player_id = PlayerOptionView.delete_player()
        store["players"] = [p for p in store["players"] if p.identity != player_id]
        self.delete.delete_player(player_id)

        return PlayerMenuController()
