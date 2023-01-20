import os
import ctypes
import requests
import random
import string
import threading
import time
import colorama
from colorama import Fore
print(Fore.LIGHTBLUE_EX + """     ~BB?.               ^^                  ..       :~                 .:      Y@&&#G5J!:
   !BP:.^7~.            .@&     ^           !J       .&&               !J^      .@@@5?!^.. 
 !BY.                   &@@~    :#^        Y&        #@@7           :P#7        J@@G       
.B@Y.                  #@@@#     ?@5      G@:       G@@@&        .?&@Y          &@@~       
  :G@B~               G@? P@~     G@&~  .&@J       5@Y Y@?     ^G@@P.          !@@@.       
    .P@&?.           5@G^^~&&      &@@G7@@#       ?@B^^~#@   ?@@@&.    ..:.    &@@@&BP?~.  
      .Y@@G:        ?@PPPPP5&!     ^@@@@@@.      !@P5PPP5&?  .?&@@5.    .:G!  ~@@@^...     
         ?@@#!     !#.      .B      J@@@@7      ^#.       B     ^G@@?     B.  B@@J         
 :.       :#@@&?  ^5         ~~      #@@B      :P         ^7      .J&&^  5P  :@@&          
  !?. .!P#&B5!:  .!           ~      .@@.     .!           ~         ~GY!@^  G@@Y...       
   :GBG57:       .                    !!      .                        .YG  .&&&BG5J?!^..  """)
time.sleep(0.1)
print("developed by savage")
time.sleep(0.1)
num = int(input('Enter the number: '))

with open("hit.txt", "w", encoding='utf-8') as file:
    print("Wait…")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("hit.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"valid / {nitro}")
            break
        elif r.status_code == 429:
            print(f"{Fore.YELLOW}  Rate Limited {Fore.YELLOW}[{Fore.RESET}429{Fore.YELLOW}] {Fore.CYAN}| {Fore.RESET}{nitro}")
        else:
            with open("invalid.txt", "w", encoding='utf-8') as file:
                file.write(f"invalid | {nitro}\n")
threads = []
for _ in range(int(thrd)):
    t = threading.Thread(target=nitro)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
print("WE WILL REMAIM")

time.sleep(0.2)

input("ERROR 911")

