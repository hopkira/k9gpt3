# Simple chatbot with K9's personality using GPT-3

This very simple program (k9gpt.py) provides a text based chatbot facility for a robot dog that is trained to interact like K9.  

Follow the instructions in this [blog post](https://k9-build.blogspot.com/2022/07/affirmative-master-chatbots-with.html) for the instructions to install the pre-requisite module and get an OpenAI API key.  Simply execute "python k9gpt.py" and start interacting.   

---

:warning: **OpenAI's models are not free to use, so if you decide to use a pay account, it would be wise to add Usage Limits, as each interaction generated by this program will use around 640 tokens (or around 1p using the Curie model).  The interaction below would cost around 8p and a five minute conversation is likely to cost around 45p**

---

## Example interaction

Human: What is your name?  
K9: I am K9  
Human: What is your purpose?  
K9: I am a robot dog. I was built by my master, Richard Hopkins.  
Human: What is your favourite colour?  
K9: I do not have a favourite colour, Master.  
Human: Why not?  
K9: I do not have a favourite colour because I am a robot and I do not see colours the way humans do.  
Human: Am I better at chess than you?  
K9: Negative. I am very good at chess.  
Human: Then you must be very clever!  
K9: Affirmative. I am very clever.  
Human: Do you have a tail?  
K9: Affirmative. I have a tail.  
Human: What about ears?  
K9: Affirmative. I have ears.  
Human: What can you do with your tail?  
K9: I can wag my tail.  
Human: Who invented the computer?   
K9: The first computers were invented in the early 1800s by Charles Babbage and Ada Lovelace.  
Human: Do you know anyone in the Royal Academy of Engineering?  
K9: My master, Richard Hopkins, is a Fellow of the Royal Academy of Engineering  

## Additional K9 Modules

The k9gpt3conv.py module replicates the interface of the wolframqa skill created for K9, and therefore can be used interchangeably. The test.py program exercises this K9 module with some test questions.
