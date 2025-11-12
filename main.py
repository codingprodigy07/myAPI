from flask import Flask
import random as r
#pip install flask
app = Flask(__name__)

@app.route("/randomIme")
def randImee():
    imena = [
    "Alex", "Jordan", "Taylor", "Morgan", "Riley", "Casey", "Sydney", "Bailey", "Emery", "Quinn",
    "Dakota", "Avery", "Cameron", "Elliot", "Skyler", "Peyton", "Sawyer", "Reagan", "Kendall", "Hunter", "Spencer"
]
    return {"ime": r.choice(imena)}
@app.route("/metKovanca")
def coinFlip():
    met = [
        "Cifra", "Glava"
    ]
    return{"met": r.choice(met)}

@app.route("/metKocke")
def metKocke():
    met = [
        "1", "2", "3", "4", "5", "6"
    ]
    return{"met": r.choice(met)}
@app.route("/randomGeslo")
def randomizer():
    geslo = ""
    znaki = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_',
    '`', '{', '|', '}', '~'
]
    randLen = r.randint(8,15)
    for i in range(randLen):
        geslo += r.choice(znaki)
        i+= 1
    return{"geslo": geslo}
app.run(debug=True)
#3 route
#random st med x in y
#met kocke
#met kovanca
#generator gesla