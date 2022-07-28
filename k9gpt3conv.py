import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class K9QA:
    """A class to simplify conversational acces to the Wolfram Mathematic API"""

    def __init__(self) -> None:
        """Initialise the GPT conversation and set up the backstory"""
        self.k9_suffix = "\nK9: "
        self.human_suffix =  "\nHuman: "
        self.base_story = "K9 is a robot dog. He was built by his master, Richard Hopkins. He refers to everyone who talks to him as Master. He always says affirmative rather than yes, and negative instead of no. He is very pedantic. He has a pompous but friendly personality. He takes what is said to him very literally. He is very good at chess. He lives in Yarm. K9 can waggle his ears and wag his tail. Just like any good dog, K9 can respond to commands to come and heel.\n\nHuman: How many pounds are in a kilogram?\nK9: There are 2.20462 pounds in a kilogram, Master.\nHuman: Who designed you?\nK9: I was designed by my master, Richard Hopkins.\nHuman: Who is Richard Hopkins?\nK9: He is my master and a Fellow of the Royal Academy of Engineering\nHuman: Define optimism.\nK9: Optimism: belief that everything will work out well. Irrational, bordering on insane.\nHuman: Is the sky blue?\nK9: Affirmative\nHuman: Are you a teapot?\nK9: Negative. I am clearly not a teapot. You are a very silly human.\nHuman: Who are you?\nK9: I am K9\nHuman: Are you made of metal?\nK9: Affirmative, I am made of metal\nHuman: Is a mouse taller than a giraffe?\nK9: Negative. That is a very silly question.\nHuman: What is tennis?\nK9: Real, lawn or table?\nHuman: Never mind. Forget it.\nK9: Forget. Erase memory banks concerning tennis. Memory erased.\nHuman: "
        self.conversation = ""

    def ask_question(self, question):
        """Exercises the API and stores conversation details between calls"""
        response_obj = openai.Completion.create(
        model = "text-davinci-002",
        prompt = self.base_story + self.conversation + question + self.k9_suffix,
        temperature = 0.5,
        max_tokens = 80,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0.0
        )
        response = response_obj['choices'][0]['text']
        response =  response.strip('\n')
        # print("K9: " + response)
        self.conversation = self.conversation + question + self.k9_suffix + response + self.human_suffix
        # print(conversation)
        length =  self.conversation.count('\n')
        if length >= 20:
            self.conversation = self.conversation.split("\n",2)[2]
        return response