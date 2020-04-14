import requests
import random
import time

dict = 'abcdefghijklmnopqrstuvwxyz-0123456789'
gen_num = int(input("Generation length (recommended length 6 symbols): "))
while True:
    url = 'http://'
    domain = '.com'
    for x in range(0,gen_num):
        url = url + random.choice(dict)
    url = url + domain
    print("generated url: "+url)
    try:
        req = requests.get(url)
        print("connection done")
        
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        
        with open('result.txt', 'a') as file:
            file.write(url +'\n')
    except:
        print("connection error")
    
