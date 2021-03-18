class View(object):

    @staticmethod
    def show_players(players):
        print('--- {} LISTE ---' )
        for player in players:
            print('* {}' .format(player))

    @staticmethod
    def show_number_point_list(players):
        print('--- {} LISTE ---')
        for i, player in enumerate(players):
            print('{}. {}' .format(i+1, player))

    @staticmethod
    def show_player(player):
        print('//////////////////////////////////////////////////////////////')
        player = str(player)
        print('Voici le joueur ' + player)
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_player_error(player, err):
        print('**************************************************************')
        print('Ce joueur {} n\'est pas inscrit!'.format(player.upper()))
        print('**************************************************************')

    @staticmethod
    def display_player_already_stored_error(player, err):
        print('**************************************************************')
        print('Le joueur {} est déjà inscrit!'
              .format(player.upper()))
        print('**************************************************************')

    @staticmethod
    def display_player_not_yet_stored_error(player, err):
        print('**************************************************************')
        print('Ce joueur {} n\'est pas inscrit'
              .format(player.upper()))
        print('**************************************************************')

    @staticmethod
    def display_player_stored(player):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Le joueur {} a été ajouté'
              .format(player.upper()))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

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
        print('Le joueur {} a été supprimé'.format(lastname))
        print('--------------------------------------------------------------')