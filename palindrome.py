def hello(word: str):
    word = word.lower()
    word = ''.join(w for w in word if w.isalnum())
    print(word)
    return word == word[::-1]

print(hello("makan 12321 nakam"))

users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Budi"},
    {"id": 3, "name": "Cici"},
]

user = next((u for u in users if u["id"]== 1), None)
print(user)
