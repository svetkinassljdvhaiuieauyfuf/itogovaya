
import requests 

def isGhoul():
    res= requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "Ghoul".encode()in res.content 

def isGho():
    res= requests.get("https://kitsu.io/api/edge/anime?filter[text]=tokio")
    return "Gho".encode()in res.content

def isElfenLied():
    res= requests.get("https://kitsu.io/api/edge/anime?filter[text]=Lied")
    return "Elfn".encode()in res.content


def isDeathNote():
    res= requests.get("https://kitsu.io/api/edge/anime?filter[text]=note")
    return "Deah".encode()in res.content

def isNeon():
    res= requests.get("https://kitsu.io/api/edge/anime?filter[text]=Evangelion")
    return "Neon".encode()in res.content




print("is Ghoul?",isGhoul())

print("is Ghoul?",isGho())

print("is Elfen?",isElfenLied())

print("is Death?",isDeathNote())

print("is Neon?", isNeon())

