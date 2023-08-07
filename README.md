# CrossLabs CookingRobot: Translating natural language to code

## Step One
Sample the internet for recipes (currently cocktail recipes). From each recipe, I extract action verbs such as "transfer" that I think will make good high-level abstractions.

## Step Two
Create a spreadsheet of abstract modules from the verbs sampled. For each, include paramaters that a robot would need to execute the module, as well as some example use cases.

## Step Three
Prompt engineer the Falcon 7b Instruct model to work on one line of an instruction, translating the natural language into a string of modules. At the moment, not sure how to determine how many modules it should create, so it often overshoots.
