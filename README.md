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