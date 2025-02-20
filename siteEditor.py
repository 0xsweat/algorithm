import json
from os import path
from sys import argv

def loadFromFile() -> dict:
    if path.exists("sites.json"):
        with open("sites.json", 'r') as f:
            sites: dict = json.load(f)
            f.close()
    else:
        print("Creating site file.")
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

def add(name: str, url: str, minimum=3, maximum=16) -> None:
    sites: dict = loadFromFile()
    sites['url'][name] = url
    sites['length'][name] = {"min": minimum, "max": maximum}
    with open("sites.json", 'w') as f:
        f.write(json.dumps(sites, indent=4))
        f.close()

def remove(name: str) -> bool:
    sites: dict = loadFromFile()
    if sites['url'][name]:
        del sites['url'][name]
        del sites['length'][name]
        with open("sites.json", 'w') as f:
            f.write(json.dumps(sites, indent=4))
            f.close()
        return True
    return False

if __name__ == "__main__":
    if len(argv) > 6 or len(argv) < 3:
        print("""   Insufficient values supplied.
        USAGE:
            python3 siteEditor.py add name url minUserLength maxUserLength
            python3 siteEditor.py add name url
            python3 siteEditor.py remove name
        EXAMPLE:
            python3 siteEditor.py github https://github.com/ 1 39""")
    elif len(argv) == 6 and argv[1] == "add":
        add(str(argv[2]),str(argv[3]),int(argv[4]),int(argv[5]))
    elif argv[1] == "remove":
        remove(str(argv[2]))
    else:
        add(str(argv[2]),str(argv[3]))
    