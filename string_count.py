""" Программа подсчета гласных букв в тексте.
    ver.  1.3"""


#main:
while True:
    print("\n" + "="*38)
    print("""Подсчет гласных букв в строке.
        Для выхода из программы ведите комбинацию: qq """)
    print('=' * 38)

    #variables defining
    i = 0
    
    #input target string:
    target_text = str(input('Введите произвольную или нужную строку: '))
    

    #count script:
    for txt in target_text:
        glas_chars = ['a', 'e', 'o', 'u', 'i']
        caps_glas_chars = ['A', 'E', 'O', 'U', 'I']
        glas_chars_rus = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        caps_glas_chars_rus = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
        if (txt in glas_chars) or (txt in glas_chars_rus) or (txt in caps_glas_chars) or (txt in caps_glas_chars_rus):
            i +=1
    print(f"Всего букв: {i}")
    
    if target_text == 'qq':
       break


# можно решить было и через итератор...  захотелось так...