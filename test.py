from k9gpt3conv import K9QA
import time
k9qa = K9QA()
questions = ["Who are you?","What is a Morgan car?","What kind of cars do they make?","Do you have ears?","What can you do with them?","Are you made of wood?","Could you pilot the TARDIS?"]
print("WARNING: OpenAI usage is not free; if you are on a paid account, please ensure you have Usage limits set; just running this test will cost roughly 50p!")
for question in questions:
    answer = k9qa.ask_question(question)
    print("Human: " + question)
    print("K9: " + answer)