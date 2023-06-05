from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_prompts, story_options

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route("/")
def get_story_prompts():
    """Ask user for story prompts"""
    prompts = story_prompts
    return render_template("index.html", prompts=prompts)

@app.route("/story", methods=["POST"])
def submit_story():
    """Submit user inputs to create a story"""
    place = request.form["place"]
    noun = request.form["noun"]
    verb = request.form["verb"]
    adjective = request.form["adjective"]
    plural_noun = request.form["plural_noun"]
    chosen_story_key = request.form["story_text"]
    
    user_inputs = {
        "place": place, 
        "noun": noun, 
        "verb": verb, 
        "adjective": adjective, 
        "plural_noun": plural_noun
    }
    
    story_text = story_options[chosen_story_key]
    
    new_story = story_text.generate(user_inputs)
    return render_template("story.html", new_story=new_story)
    