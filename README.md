# CrossLabs Cooking Robot: Translating Natural Language to Code

In an effort to explore how large language models (LLMs) can be used to aid the planning of robots to translate natural language tasks into code for a general purpose robot, CrossLabs explores the conversion of cocktail recipes into robot-readable instructions.

[Check out our report here!](https://www.overleaf.com/read/qmggjkjvnkbq)

## Diagram

The following is a flowchart diagramming the idea of the cooking robot. This repository specifically focuses on the LLM swimlane and the defining of the available modules in the modules database/API.

![Overall Flowchart](images/overall-flowchart.png)

## Steps

The following are the steps that we followed to achieve the task.

1. Sample the internet for recipes (currently cocktail recipes). From each recipe, I extract action verbs such as "transfer" that I think will make good high-level abstractions.

2. Create a spreadsheet of abstract modules from the verbs sampled. For each, include paramaters that a robot would need to execute the module, as well as some example use cases.

3. Prompt engineer the Falcon 7b Instruct model to work on one line of an instruction, translating the natural language into a string of modules.

## Usage Instructions

After downloading all the packages from requirements.txt, make sure the appropriate LLM (something from the Falcon family for now) from HuggingFace.
Then create a folder with all your prompts as txt files. 
An example prompt is shown here:
```
>>INTRODUCTION<<I want to rewrite instructions using one of the two predefined modules: stir(c), where c is something to be stirred; transfer(i,d), where i is an item to be added to the container d. Enclose your answer in square brackets. Don't ask any more questions.
>>QUESTION<<Rewrite "Stir the juice".
>>ANSWER<<[stir(juice)]
>>QUESTION<<Rewrite "Stir the rum slowly, then stir the wine".
>>ANSWER<<[stir(rum) stir(wine)]
>>QUESTION<<Rewrite "Pour the water into the cup".
>>ANSWER<<[transfer(water, cup)]
>>QUESTION<<Rewrite "Add the soup into the bowl, then stir the soup".
>>ANSWER<<[transfer(soup, bowl) stir(soup)]
```
You can find another example prompt in the file exampleprompt.txt too. Make sure that you end your prompt with a square bracket as shown, so that the appended text from api.py makes sense to the postprocessor.

The key to writing prompts for Falcon models is to make use of the reserved tokens INTRODUCTION, QUESTION, and ANSWER [as shown here](https://huggingface.co/tiiuae/falcon-7b-instruct/discussions/1).

Next, adjust the parameters in api.py appropriately (i.e. number of trials, batch size, max token length, etc). Feed it the location of your prompt file and the desired recipe like so:
```
nohup python api.py prompts/prompt1.txt "vodka martini" > results/result1.txt
```

This will obtain a translation that the LLM believes is most accurate, along with confidence scores for its translation corresponding to the percent of trials that agreed on a given translated module.
From here, we recorded the final results onto a spreadsheet and analyzed the best prompts by seeing which ones gave correct answers with the highest confidence.

## Documentation

Here is a list of other important documentation that we have in this repository.

- [Module List](docs/moduleList.md) - this is a list of all the modules that we plan on using in the future
- [Architectural Decision Record](docs/adr.md) - this file is a running record of all major decisions in the project

## Contributors

- [Oliver Wang](https://github.com/burnttomato)
- [Grant Cheng](https://github.com/CatFish47)
- Luc Caspar
- Akira Yokota
- Mahdi Khosravy
- et. al.

## Acknowledgements

- [Microsoft - ChatGPT for Robotics](https://www.microsoft.com/en-us/research/group/autonomous-systems-group-robotics/articles/chatgpt-for-robotics/)
- [Falcon 7b Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
- Crosslabs from Cross Compass
