#Посмотрите видео и повторите код: Основы Python #15: Исключения

def main():
    d = {
        'website': 'www.google.com',
        'url': 'google.ru'
    }

    try:
       data = d['url']
    except:
       data = 'https://'
    else:
        data = data.upper()

    print(data)


main()