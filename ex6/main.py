import redis
import string

with open("gp.txt", "r") as f:
    data = f.read()

words=[]

lines = data.split("\n")


for l in lines:
    l = l.translate(str.maketrans('','', string.punctuation))
    words = words + l.split(" ")


r = redis.Redis(host="localhost")

for w in words:
    # print(w)
    r.hincrby("words", w, 1)


# Lire toutes les clés et leurs valeurs
hashValues = r.hgetall("words")

# Itérer à travers le dictionnaire pour afficher les valeurs
for key, value in hashValues.items():
    print(f"Clé : \"{key.decode()}\" ; Valeur : {value.decode()}")