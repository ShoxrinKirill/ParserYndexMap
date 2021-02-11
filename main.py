import time
import Parse

def main():
    url = 'https://yandex.ru/profile/78003645021'
    
    organizations = Parse.parse(url)
    time.sleep(5)

    print(organizations)

if __name__ == '__main__':
    main()