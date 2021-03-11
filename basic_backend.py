import mvc_exceptions as mvc_exc

players = list()


def create_players(app_players):
    global players
    players = app_players


def create_player(lastname, firstname, birthday, sexe, rank):
    global players
    results = list(filter(lambda x: x['lastname'] == lastname, players))
    if results:
        raise mvc_exc.PlayerAlreadyRegistered('"{}" already registered!' .format(lastname))
    else:
        players.append({'nom': lastname, 'prénom': firstname,
                        'date de naissance': birthday, 'sexe': sexe, 'classement': rank})


def read_player(lastname):
    global players
    my_players = list(filter(lambda x: x['lastname'] == lastname, players))
    if my_players:
        return my_players[0]
    else:
        raise mvc_exc.PlayerNotRegistered('can\'t read "{}" because it\'s not registered' .format(lastname))


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
        raise mvc_exc.PlayerNotRegistered(
            'can\'t update "{}" because it\'s not registered' .format(lastname))


def delete_player(lastname):
    global players
    idxs_players = list(
        filter(lambda i_x: i_x[1]['name'] == lastname, enumerate(players)))
    if idxs_players:
        i, player_to_delete = idxs_players[0][0], idxs_players[0][1]
        del players[i]
    else:
        raise mvc_exc.PlayerAlreadyRegistered(
            'Can\'t delete "{}" because it\'s not registered'. format(lastname))
