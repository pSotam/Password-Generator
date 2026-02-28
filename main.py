import random

'''Gera uma senha aleatória

Você escolhe o tamanho da senha

Pode gerar quantas quiser'''
chars_list = [['A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R'
            ,'S','T','U','V','W','X','Y','Z'],
            ['a','b','c','d','e','f','g','h','i'
            ,'j','k','l','m','n','o','p','q','r'
            ,'s','t','u','v','w','x','y','z'], 
            ['!','@','#','$','%','&','*','/','.','_','-','?','']]

print('[ 1 ] Generate new password\n' \
'[ 2 ] See generated passwords\n' \
'[ 3 ] Quit')
menu_option = int(input('Choose option: '))

if(menu_option == 1):
    print('='*30)

    tamanho_senha = int(input('Password Length: '))
    upper_chars = str

    senha = ''
    for i in range(0, tamanho_senha):
        sublist = random.choice(chars_list)
        choice_char = random.choice(sublist)
        senha += choice_char

    print(senha)