from os import name
import requests, string, random, argparse, sys
import trnames
from colorized.banner import banner


sys.stdout.write(banner())

text_file = open("hesaplar.txt", "w")

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate():
    nick = trnames.get_first_name(gender='female') + " " + trnames.get_last_name()
    passw = getRandomString(12)
    email = getRandomString(10)+"@"+getRandomText(5)+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.26 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.26",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "female" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, email+":"+passw)
        else:
            #Details available in r.json()["errors"]
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1", type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
    parser.add_argument("-o", "--output", help="output file, default prints to the console")
    args = parser.parse_args()

    N = args.number if args.number else 3
    file = open(args.output, "w") if args.output else sys.stdout

    print("Hesaplar Olu??turuluyor...", file=sys.stdout)
    print("A????lan Cihaz Modeli : Spotify/8.6.26 Android/29 (SM-N976N)\n", file=sys.stdout)
    for i in range(N):
        result = generate()
        if result[0]:
            print(result[1], file=file)
            text_file.write(result[1]+"\n")

            
        else:
            print(str(i+1)+"/"+str(N)+": "+result[1], file=sys.stdout)

        

    if file is not sys.stdout: file.close()