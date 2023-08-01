class Story:


    def __init__(self, code, title, words, text):

        self.code=code
        self.title=title
        self.words=words
        self.text=text

    def generate(self, answers):

        text=self.template

        for(key,val) in answers.items():
            text = text.replace("{" + key + "}", val) 
            return text

story1 = Story(

)

story2 = Story(

)

stories = {s.code: s for s in [story1, story2]}