import basic_backend
import mvc_exceptions as mvc_exc

class ModelBasic(object):


    def __init__(self,application_players):
        self._player_type = 'joueur'
        self.create_players(application_players)


    @property
    def player_type(self):
        return self._player_type

    @player_type.setter
    def player_type(self, new_player_type):
        self._player_type = new_player_type


    def create_player(self, lastname, firstname, birthday, sexe, rank ):
        basic_backend.create_player(lastname, firstname, birthday, sexe, rank)


    def create_players(self, players):
        basic_backend.create_players(players)


    def read_player(self, lastname):
        return basic_backend.read_player(lastname)


    def read_players(self):
        return basic_backend.read_players()


    def update_player(self, lastname, firstname, birthday, sexe, rank):
        basic_backend.update_player(lastname, firstname, birthday, sexe, rank)


    def delte_player(self, lastname, firstname, birthday, sexe, rank):
        basic_backend.delete_player(lastname)


class View(object):

    @staticmethod
    def show_bullet_point_list(player_type, players):
        print('--- {} LIST ---' .format(player_type.upper()))
        for player in players:
            print('* {}' .format(player))

    @staticmethod
    def show_number_point_list(player_type, players):
        print('--- {} LIST ---' .format(player_type.upper()))
        for i, player in enumerate(players):
            print('{}. {}' .format(i+1, player))

    @staticmethod
    def show_player(player_type, player, player_info):
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have some {}!'.format(player.upper()))
        print('{} INFO: {}'.format(player_type.upper(), player_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_player_error(player, err):
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(player.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_player_already_stored_error(player, player_type, err):
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(player.upper(), player_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_player_not_yet_stored_error(player, player_type, err):
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(player.upper(), player_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_player_stored(player, player_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(player.upper(), player_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_player_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change player type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_player_updated(player, o_firstname, o_birthday, o_sexe, o_rank,
                               n_firstname, n_birthday, n_sexe, n_rank):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} firstname: {} --> {}'
              .format(player, o_firstname, n_firstname))
        print('Change {} birthday: {} --> {}'
              .format(player, o_birthday, n_birthday))
        print('Change {} sexe: {} --> {}'
              .format(player, o_sexe, n_sexe))
        print('Change {} rank: {} --> {}'
              .format(player, o_rank, n_rank))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_player_deletion(lastname):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(lastname))
        print('--------------------------------------------------------------')


class Controller(object):

    def __init__(self,model, view):
        self.model = model
        self.view = view


    def show_players(self, bullet_points=False):
        players = self.model.read_players()
        item_type = self.model.player_type
        if bullet_points:
            self.view.show_bullet_point_list(player_type, players)
        else:
            self.view.show_number_point_list(player_type, players)


    def show_player(self, player_name):
        try:
            player = self.model.read_player(player_name)
            player_type = self.model.player_type
            self.view.show_player(player_type, player_name, player)
        except mvc_exc.PlayerNotRegistered as e:
            self.view.display_missing_player_error(player_name, e)


    def insert_player(self, lastname, firstname, birthday, sexe, rank):
        assert firstname != None, 'le prénom doit être remplie'
        assert birthday >= 0, 'la date de naissance doit être supérieur à 0'
        assert sexe == 'male' or sexe == 'female', 'le sexe doit être homme ou femme'
        assert rank >= 0, 'le classement doit être supérieur ou équale à 0'
        player_type = self.model.player_type
        try:
            self.model.create_player(lastname, firstname, birthday, sexe, rank)
            self.view.display_player_stored(lastname, player_type)
        except mvc_exc.PlayerAlreadyRegistered as e:
            self.view.display_already_registered_player_error(lastname, player_type, e)

    def update_player(self, lastname, firstname, birthday, sexe, rank):
        assert firstname != None, 'le prénom doit être remplie'
        assert birthday >= 0, 'la date de naissance doit être supérieur à 0'
        assert sexe == 'male' or sexe == 'female', 'le sexe doit être homme ou femme'
        assert rank >= 0, 'le classement doit être supérieur ou équale à 0'
        player_type = self.model.player_type
        try:
            older = self.model.read_player(lastname)
            self.model.update_player(lastname, firstname, birthday, sexe, rank)
            self.view.display_player_updated(
                lastname, older['firstname'], older['birthday'], older[sexe],
                older[rank], firstname, birthday, sexe, rank)
        except mvc_exc.PlayerNotRegistered as e:
            self.view.display_player_not_yet_registered_error(lastname, player_type, e)


    def update_player_type(self, new_player_type):
        old_player_type = self.model.player_type
        self.model.player_type = new_player_type
        self.view.display_change_player_type(old_player_type, new_player_type)

    def delete_player(self, lastname):
        player_type = self.model.player_type
        try:
            self.model.delete_player(lastname)
            self.view.display_player_deletion(lastname)
        except mvc_exc.PlayerNotRegistered as e:
            self.view.display_player_not_yet_registered_error(lastname, player_type, e)


