import requests

word = requests.get(f"https://random-word-api.vercel.app/api?words=1&length=5")

if word.status_code == 200:
    word = str(*word.json())
    
    print(word)