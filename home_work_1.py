def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    def step2_umbrella():
        print(
            'кря'
        )

    def step2_no_umbrella():
        print(
            'кря-кря'
        )

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
