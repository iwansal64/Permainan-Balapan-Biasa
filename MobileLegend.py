from time import sleep
print('Mobile Legend')
data = input('y/n')
if(data == 'y'):
    print('Mau make hero apa?')
    sleep(2)
    print('======ROLE======')
    sleep(1)
    print('1.Mage')
    sleep(0.5)
    print('2.MM')
    sleep(0.5)
    print('3.Assasin')
    sleep(0.5)
    print('4.Tank')
    sleep(1)
    data = int(input('1/2/3/4'))
    if(data == 1):
        role = 'Mage'
        print('====Hero====')
        sleep(2)
        print('-Harith')
        sleep(1)
        print('-Harley')
        sleep(1)
        print('-Nana')
        sleep(1)
        print('-Change')
        sleep(1)
        print('-Kagura')
        sleep(2)
        data_1 = input('\nmau yang mana?')
        data = data_1.lower()
        if(data == 'harith'):
            hero = 'Harith' 
        elif(data == 'Harley'):
            hero = 'Harley'
        elif(data == 'nana'):
            hero = 'Nana'
        elif(data == 'change'):
            hero = 'Change'
        elif(data == 'kagura'):
            hero = 'Kagura'
        else:
            print('\ngak ada hero tersebut dalam menu! ulang dari awal!!')
    elif(data == 2):
        role = 'MM'
        print('====Hero====')
        sleep(2)
        print('1.Lesley')
        sleep(1)
        print('2.Layla')
        sleep(1)
        print('3.Miya')
        sleep(1)
        print('4.Granger')
        sleep(1)
        print('5.Beatrix')
        sleep(2)
        data_1 = input('\nmau yang mana?')
        data = data_1.lower()
        if(data == 'lesley'):
            hero = 'Lesley'
        elif(data == 'layla'):
            hero = 'Layla'
        elif(data == 'miya'):
            hero = 'Miya'
        elif(data == 'granger'):
            hero = 'Granger'
        elif(data == 'beatrix'):
            hero = 'Beatrix'
        else:
            print('\ngak ada hero tersebut dalam menu! ulang dari awal!!')
    elif(data == 3):
        role = 'Assasin'
        print('====Hero====')
        sleep(2)
        print('1.Gusion')
        sleep(1)
        print('2.Ling')
        sleep(1)
        print('3.Helcurt')
        sleep(1)
        print('4.Hayabusa')
        sleep(1)
        print('5.Lancelot')
        sleep(2)
        data_1 = input('\nmau yang mana?')
        data = data_1.lower()
        if(data == 'lancelot'):
            hero = 'Lancelot'
        elif(data == 'ling'):
            hero = 'Ling'
        elif(data == 'helcurt'):
            hero = 'Helcurt'
        elif(data == 'gusion'):
            hero = 'Gusion'
        elif(data == 'hayabusa'):
            hero = 'Hayabusa'
        else:
            print('\ngak ada hero tersebut dalam menu! ulang dari awal!!')
    elif(data == 4):
        role = 'Tank'
        print('====Hero====')
        sleep(2)
        print('1.Grock')
        sleep(1)
        print('2.Silvana')
        sleep(1)
        print('3.Tigreal')
        sleep(1)
        print('4.Chou')
        sleep(1)
        print('5.Atlas')
        sleep(2)
        data_1 = input('\nmau yang mana?')
        data = data_1.lower()
        if(data == 'grock'):
            hero = 'Grock'
        elif(data == 'silvana'):
            hero = 'Silvana'
        elif(data == 'tigreal'):
            hero = 'Tigreal'
        elif(data == 'chou'):
            hero = 'Chou'
        elif(data == 'atlas'):
            hero = 'Atlas'
        else:
            print('\ngak ada hero tersebut dalam menu! ulang dari awal!!')
    else:
        print('saya tidak mengerti...')

    print('WELCOME TO MOBILE LEGEND')
    sleep(2)
    print('Your role is', role)
    sleep(2)
    print('Your Hero is', hero, '!')


