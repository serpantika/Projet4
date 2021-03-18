from tinydb import TinyDB, Query

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


    def read_players():
        global players
        return [player for player in players]

    def update_player(lastname, firstname, birthday, sexe, rank):
        global players
        idxs_players = list(
        filter(lambda i_x: i_x[1]['lastname'] == lastname, enumerate(players)))
        if idxs_players:
            i, item_to_update = idxs_players[0][0], idxs_players[0][1]
            players[i] = {'nom': lastname, 'prénom': firstname,
                          'date de naissance': birthday, 'sexe': sexe, 'classement': rank}
        else:
            raise PlayerNotRegistered

    def delete_player(lastname):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            players.remove(my_players.nom == lastname)
        else:
            raise PlayerAlreadyRegistered










