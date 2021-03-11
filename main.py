from model import ModelBasic, Controller,View

if __name__ == "__main__":
    my_players = [
            {'lastname': 'Mitchel', 'firstname': 'Edward', 'birthday': '30101992',
             'sexe': 'male', 'rank': '5621'},
            {'lastname': 'Morane', 'firstname': 'Bob', 'birthday': '18061993',
             'sexe': 'female', 'rank': '254'},
            {'lastname': 'Mcdonald', 'firstname': 'Rose', 'birthday': '15061958',
             'sexe': 'male', 'rank': '9874'},
            {'lastname': 'Sarkozy', 'firstname': 'Nicolas', 'birthday': '30121968',
             'sexe': 'male', 'rank': '32000'}
        ]

    c = Controller(ModelBasic(my_players), View())