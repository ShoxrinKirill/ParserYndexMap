import time
import Parse
import json

def main():
    url = 'https://yandex.ru/maps/org/shartashskiy_lesopark/155882288890/?ll=60.681040%2C56.860309&z=12'
    organizations = []
    organizations.append(Parse.parse(url))
    time.sleep(5)

    with open('Data/organizations.json', 'a', encoding='utf-8') as file:
        json.dump(organizations, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()