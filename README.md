# CrossLabs CookingRobot: Translating natural language to code

## Step One
Sample the internet for recipes (currently cocktail recipes). From each recipe, I extract action verbs such as "transfer" that I think will make good high-level abstractions.

## Step Two
Create a spreadsheet of abstract modules from the verbs sampled. For each, include paramaters that a robot would need to execute the module, as well as some example use cases.

## Step Three
Prompt engineer the Falcon 7b Instruct model to work on one line of an instruction, translating the natural language into a string of modules. At the moment, not sure how to determine how many modules it should create, so it often overshoots.







Natural Language Recipe Models being tested:
model_list=["mosaicml/mpt-30b-instruct","lmsys/vicuna-13b-delta-v0","JosephusCheung/Guanaco","tiiuae/falcon-40b-instruct","gpt2", "tiiuae/falcon-7b-instruct","tiiuae/falcon-7b"]

Prototype prompt:
"Please give me a step-by-step recipe for a lemon sour alcoholic cocktail.",

Prototype conversion prompt:
"I want a string of robot instructions. The robot has pre-programmed modules/functions. The following all capital-lettered words are the function name, while description that follows is the description of the function: CUT(x): cuts an ingredient x, WAIT(s): waits for s seconds, ADD(i, d): which will pour or add an ingredient i into a destination d, which is usually the shaker or the cup, SHAKE(s): which will shake the shaker for s seconds. Now take the following food and make a step by step recipe for it using a string of only these given function names, without descriptions: Lemon Sour Alcohol Drink.",

Prototype Modules:
- CUT(x)
- WAIT(s)
- ADD(i, d)
- SHAKE(s)
