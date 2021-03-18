from tinydb import TinyDB, Query
from collections import OrderedDict

class PlayerAlreadyRegistered(Exception):
    pass


class PlayerNotRegistered(Exception):
    pass


class ModelBasic(object):

    players = list()

    def create_players(tournoi):
        global players
        players = TinyDB(tournoi + '.json')

    def create_player(lastname, firstname, birthday, sexe, rank):
        global players
        players.insert({'nom': lastname, 'prénom': firstname,
                        'date de naissance': birthday, 'sexe': sexe, 'classement': rank})

    def read_player(lastname):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            return players.search(my_players.nom == lastname)
        else:
            raise PlayerNotRegistered


    def read_players_alphabetic():
        global players
        return [player for player in players]

    def update_player(lastname, firstname, birthday, sexe, rank):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            players.update_multiple([({'prénom': firstname}, my_players.nom == lastname),
                                     ({'date de naissance': birthday}, my_players.nom == lastname),
                                     ({'sexe': sexe}, my_players.nom == lastname),
                                     ({'classement' : rank}, my_players.nom == lastname)])
        else:
            raise PlayerNotRegistered

    def delete_player(lastname):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            players.remove(my_players.nom == lastname)
        else:
            raise PlayerNotRegistered










