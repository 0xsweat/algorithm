"""
File : algorithm.py
Author : 0xsweat
Date : 2/19/2025
Version : 1

The purpose of this file (algorithm.py) is for checking username availability across websites.
"""
import sys
import requests
from threading import Thread
import os
import json
from time import sleep

def generate() -> dict:
    """
    Generates a site list.
    """
    sites: dict = {
        "url" : {
            "github":"https://github.com/",
            "replit":"https://replit.com/@",
            "instagram":"https://instagram.com/",
            "twitter":"https://x.com/",
            "x":"https://x.com/",
            "tryhackme":"https://tryhackme.com/p/",
            "codewars":"https://codewars.com/users/",
            "codechef":"https://codechef.com/users/"
        },
        "length" : {
            "github": {"min": 1, "max": 39},
            "replit": {"min": 3, "max": 16},
            "instagram": {"min": 3, "max": 16},
            "twitter": {"min": 1, "max": 15},
            "x": {"min": 1, "max": 15},
            "tryhackme": {"min": 4, "max": 16},
            "codewars": {"min": 3, "max": 16},
            "codechef": {"min": 3, "max": 16}
        }
    }

    with open("sites.json", 'w') as f:
        f.write(json.dumps(sites, indent=4))
        f.close()
    return sites

class Checker:

    def __init__(self):
        if os.path.exists("sites.json"):
            with open("sites.json", 'r') as f:
                self.sites: dict = json.load(f)
                f.close()
        else:
            self.sites = generate()
        print(f"Checking {list(self.sites['url'])}!\nMade by 0xsweat and incon")
        self.tally: int = 0
        self.total: int = len(self.sites['url'])
        self.results: dict = {}
        self.exit: bool = False
        try:
            if os.path.exists(sys.argv[1]):
                with open(sys.argv[1], 'r') as f:
                    self.usernames: list[str] = f.read().split("\n")
                    f.close()
            else:
                raise FileNotFoundError("usernames file does not exist.\nUSAGE : python3 algorithm.py USERFILE")
        except IndexError:
            print("usernames file not supplied.\nUSAGE : python3 algorithm.py USERFILE")
            quit()

    def check(self, site: str) -> None:
        """
        This function checks a website for username availability.
        """
        self.results[site]: list[str] = []
        url = self.sites["url"][site]
        for user in self.usernames:
            if len(user) > self.sites["length"][site]["max"] or len(user) < self.sites["length"][site]["min"]:
                pass
            else:
                request = requests.get(f"{url}{user}")
                if request.status_code == 404:
                    self.results[site].append(user)
            if self.exit:
                break
        self.tally += 1
    
    def start(self) -> None:
        """
        This function starts the threads for checking each website, 1 thread per site.
        """
        for x in self.sites["url"]:
            Thread(target = self.check, args = (x,)).start()
        stages: list = ['|','/','-','\\','|']
        stage: int = 0
        while self.tally < self.total:
            sleep(0.1)
            sys.stdout.flush()
            sys.stdout.write(f"\r{stages[stage]} {self.tally}/{self.total} sites finished {stages[stage]}")
            stage += 1 if stage != len(stages)-1 else -(len(stages)-1)
        with open("results.json", 'w') as f:
            f.write(json.dumps(self.results, indent=4))

if __name__ == "__main__":
    try:
        checker: object = Checker()
        checker.start()
    except KeyboardInterrupt:
        checker.exit: bool = True
        print("\nbye!")
        exit(0)
