from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    # print(request.get_json())
    user_Text = request.args.get('msg')
    msg = str(english_bot.get_response(user_Text))
    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
