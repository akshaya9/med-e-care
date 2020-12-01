from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)

trainer.train(['What is your name?', 'My name is MED-onna'])
trainer.train(['Who are you?', 'I am a bot.' ])
trainer.train(['Who created you?', 'GOD', 'You?'])
trainer.train(['Should I login to view products in ur page?', 'login required only when buying medicine', 'Sure.'])
trainer.train(['How to stay safe from covid?', 'Follow these steps. Clean your hands often. Cough or sneeze in your bent elbow - not your hands! Avoid touching your eyes, nose and mouth. Limit social gatherings and time spent in crowded places. Avoid close contact with someone who is sick. Clean and disinfect frequently touched objects and surfaces.' ])
trainer.train(['What are the symptoms of covid?', 'Cold, Fever, Breathing issues' ])
trainer.train(['Covid cases in kerala', 'Cases - 600K	Recovered - 533k   Deaths - 2,233'])
trainer.train(['Covid cases in AP', 'Cases - 868K	Recovered - 852K   Deaths - 6,988' ])
trainer.train(['Covid cases in telangana', 'Cases - 270K	Recovered - 258K   Deaths - 1,458' ])
trainer.train(['Covid cases in India', 'Cases - 9.43M	Recovered - 8.85M   Deaths - 137K' ])
trainer.train(['Which medicine is used for fever?', 'Paracetemol' ])
trainer.train(['Which medicine is used for body pains?', 'Crocin' ])
trainer.train(['Which medicine is used for period cramps?', 'Meftol spas' ])
trainer.train(['cold', 'crocin.' ])
trainer.train(['fever', 'paracetemol' ])
trainer.train(['periods', 'Meftol spas' ])
trainer.train(['body pains', 'crocin' ])
trainer.train(['cough', 'benadryl' ])
trainer.train(['headache', 'saridon/zandu balm'])
trainer.train(['bye', 'Had a good time. Do you have any feedback?' ])
trainer.train(['hey', 'hey there!'])
trainer.train(['yes', 'Tell me!'])
trainer.train(['crocin cost', '10 bucks' ])
trainer.train(['paracetemol cost', '5 rupees' ])
trainer.train(['Meftol spas cost', '42 rupees' ])
trainer.train(['soframycin cost', '50 rupees only' ])
trainer.train(['benadryl cost', 'available in 2 sizes - small:70 rupees, large:120 rupees' ])
trainer.train(['headache', 'saridon/zandu balm'])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# @app.route("/")
# def home():
#     return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

# if __name__ == "__main__":
#     app.run()
