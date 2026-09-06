# TCHS Aero Tryout 9/6/26

This is TCHS Aero's Software Tryout for the September 2026 season!

- - -
This tryout was designed to be difficult *on purpose*. **You will not be graded on your performance, but rather the effort you apply and your eagerness to learn.** If you prove to us through this tryout that you are at least putting in 100% effort, you will have a higher chance of making the team.

Here's what's up. This is the first part of your tryout. Your goal is simple; **Reverse engineer a provided script, and make one of your own modeled after the first.** If you did some high quality reading of the skillset pdf, you should be good to go!
- - -

# Reverse Engineering

In this repository, you will find a script labeled `ReverseEngineer.py`. You will fork this repository by clicking on the fork button, and make changes accordingly.

Edit `ReverseEngineer.py` and comment the code as much as possible according to what you think everything does. Do not be afraid to go back and make changes; always read everything first.

*`ReverseEngineer.py` is a sneak-peek into what you will be doing later on in the year, and is an optimized snippet of pre-existing code.*

An example of the bare minimum is shown below. (Bonus points if you include PEP 8 compliant docstrings!)

Uncommented code:
```python
from time import sleep
from platform import system

def typewrite(text, delay=0.1):
	for character in text:
		print(character, end="", flush=True)
		sleep(delay)
	print("\n")

typewrite("What is your name?")
name = input("Name: ")
typewrite(f"Hello, {name}! I see that you are currently running {system()}. How fun!")
```

Commented code:
```python
# import essential modules to be used later
from time import sleep # import sleep function to add delay between character outputs
from platform import system # import system func to retrieve os type

# define a function that takes a string and outputs each character one by one for easy re-use of code
def typewrite(text, delay=0.1): # a delay of 0.1 seconds between each character, defaults to 0.1 if no value provided
	# iterate through all characters in the string to isolate them
	for character in text:
		# print each character individually, specifying no linebreak
		print(character, end="", flush=True)
		# wait for the provided delay before moving onto the next char to simulate typing
		sleep(delay)
	# add a line break when finishing printing to simulate a normal print statement
	print("\n")

# call typewrite func and provide a string that will be written
typewrite("What is your name?")
# grab user input as a string to be used in the message
name = input("Name: ")
# use a formatted string to typewrite everything fully, including the os type
typewrite(f"Hello, {name}! I see that you are currently running {system()}. How fun!")
```

The more accurate, the better. **You will not be given an opportunity to test the code.** You will be going off of pure theory and "educated" guesses.

> [!WARNING]
> As of September 4th, 2026, this Tryout Repository was leaked by an unknown individual. As such, an additional part will be added to this portion.

As a secondary task, you must comment out redundant and/or useless code, aswell as fix any syntax/logic errors you find. The `ReverseEngineer.py` file contains some extra code that does essentially nothing towards it's purpose, or contains some syntax or logic errors.
If you find and fix all of these problems, you immediately pass this portion and will be considered for the team, guaranteed.
# Individual Programming

Now that you have completed the reverse engineering portion, it is time to write your own file. It does not have to be anywhere near as complex as the provided program, as the more efficient the better. 

For context, `ReverseEngineer.py` was not designed exclusively for speed, but for scalability and readability.

You are allowed to use the internet, and anything is fair game as long as you do not use Generative AI. This includes **Gemini Spotlight**. (See below)

![Gemini Spotlight Example](https://github.com/TCHS-aero/TCHS-Aero-Tryout-9-6-26/blob/main/assets/Spotlight%20Example.png?raw=true)

You will be guided into disabling spotlight before beginning this portion, and you will be guided to re-enable it afterwards.

### Any blatant use of AI will not be tolerated.

Your task is simple: 
- Takeoff into the air
- Wait 10 seconds
- Fly forwards for 10 meters at 5 m/s
- Return to launch (including landing)

*You are permitted to use `ReverseEngineer.py` to your advantage.*
You *totally* shouldn't be using offboard commands to move \*cough* \*cough*

Feel free to ask questions, but they will not be directly answered.

# Submission

Your submission will be in the form of a pull request. You will be guided on how to do this.
- - -

This concludes the first half of the software tryout. Good luck! ☺️👐
