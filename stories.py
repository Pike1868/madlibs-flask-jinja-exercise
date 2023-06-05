"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    
story_prompts = ["place", "noun", "verb", "adjective", "plural_noun"]

short_story = Story(
    story_prompts,
    "I love to {verb} a good {adjective} {noun}, at {place} with {plural_noun}."
)

medium_story = Story(
    story_prompts,
    "In a distant {place}, there was a very {adjective} {noun}. Every day, it would {verb} with other {plural_noun} in the {place}"
)

long_story = Story(
    story_prompts ,
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} all of the {plural_noun}. Everyone knew about the {adjective} {noun}."""
)

story_options = {"short": short_story, "medium": medium_story, "long": long_story}


