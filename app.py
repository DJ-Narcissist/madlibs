from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from Stories import story

app = Flask(__name__)
debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    prompt = story.prompts
    return render_template("home.html", prompts=prompts)
     
@app.route('/story')
def say_story():
    text = story.generate(request.args)
    return render_template("hello.html", text=text)


if __name__ =="__main__":
    app.run(debug=True)