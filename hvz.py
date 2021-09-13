import requests
import time
import json

human_members = ["Joseph Abbate", "Jake Dawson", "Kyle Baptiste"]
zombie_members = []

def check():
    for member in human_members:
        name = member.replace(" ","%20")
        team = requests.get("https://hvz.rit.edu/api/v2/status/players?search=" + name, verify=False).json()['players'][0]['team']
        if team == "zombie":
            print( member, "has been infected!" )
            human_members.remove(member)
            zombie_members.append(member)

    for member in zombie_members:
        name = member.replace(" ","%20")
        team = requests.get("https://hvz.rit.edu/api/v2/status/players?search="+name, verify=False).json()
        if team == "human":
            print( member, "has gotten an AV!" )
            zombie_members.remove(member)
            human_members.append(member)

def main():
    while True:
        check()
        time.sleep(300)

main()