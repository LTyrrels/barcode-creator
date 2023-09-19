import random, requests, time
from colorama import Fore, Style

API_KEY = 'RGAPI-6f676400-06db-4902-af07-c77a7b3bc4cc'
REGION = 'euw1'
REQUEST_INTERVAL = {
    "second": 1,
    "minute": 120,
}

def gen_psd(length):
    pseudo = ''.join(random.choice('lI') for _ in range(length))
    return pseudo

def check_psd(pseudo):
    url = f'https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{pseudo}?api_key={API_KEY}'
    response = requests.get(url)

    if(response.status_code == 200):
        return False
    elif response.status_code == 404:
        return True
    else:
        print(f"Erreur lors de la vérification : {pseudo}")
        return False

register_psd = set()

with open('usernames.txt', 'w') as file:    
    while True:
        pseudo = gen_psd(12)
        available = check_psd(pseudo)
        if available:
            if pseudo not in register_psd:
                print(f"{Fore.GREEN} [+] {pseudo}" + Style.RESET_ALL)
                register_psd.add(pseudo)
                file.write(f"{pseudo}\n")
        else:
            print(f"{Fore.RED} [-] {pseudo}" + Style.RESET_ALL )
        time.sleep(REQUEST_INTERVAL["second"])
            