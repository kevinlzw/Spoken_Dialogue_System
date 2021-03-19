# LING575-Spoken Dialogue System Project

This is a frame-based implementation for the pizza-ordering system.
To run, the configuration must pass in the parameter "-s FrameSimple"
If you choose to run the system with ASR, add "-a ASR" to the parameter.

**driver.py** is the entry point for the program.

### Prerequisite

You need to have the following packages installed specified in requirements.txt in order to run the system. 
```
pip install -r requirements.txt
```

Other than that, you also need to download two corpora in nltk
```
nltk.download('vader_lexicon')
nltk.download('nps_chat')
```

I have saved my trained model for question detection as "question_detection.sav", the system will automatically load the model when it starts.

## Example dialog

```markdown
Welcome to the pizza ordering system. How can we help you?
> How are you? I really like your place. I come every Tuesday
Good for you! What topping do you want to add to your pizza?
> Actually, I would like to order a hawaiian pizza
Let me repeat you, you want a hawaiian pizza
> Yes!
Okay. What crust for your pizza?
> umm.. thin crust maybe
Let me repeat you, your crust selection is thin crust
> exactly
Okay. Which size do you want? We have small, medium and large.
> I don't like your voice. It sounds like a cold robot. I hate it!!
I am so sorry for what happened. Do you want to continue the order?
> yeah, it's fine. I am kidding
Okay. Which size do you want? We have small, medium and large.
> What do you recommend on size?
Small is for 2-3 people, medium is for 4-5 people and large is party size mainly for more than 6 people.
> Thank you! That's very helpful
I am glad you found it useful! Good for you! Which size do you want? We have small, medium and large.
> medium is fine.
Just want to be sure, your pizza size is medium size
> You are right!!
Okay. Do you want a delivery or pick-up?
> pick-up plz
Let me repeat you, you want a pick-up service
> right
Okay. What is your phone number?
> It is 123-456-7890
Just want to be sure, your phone number is 123-456-7890
> no, it is not correct
Okay. What is your phone number?
> It is 333-444-5555
Just to make sure I understand, your phone number is 333-444-5555
> yep
Thank you, your order for a medium pizza with thin crust and pineapple,ham,mozzarella toppings pizza is on the way
```