from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Never give up.",
    "Dream big and dare to fail.",
    "Success comes from hard work.",
    "Stay positive and strong.",
    "Do something today your future self will thank you for."
]

@app.route("/")
def home():
    random_quote = random.choice(quotes)
    return render_template("quote.html", quote=random_quote)

if __name__ == "__main__":
    app.run(debug=True, port=5005)
