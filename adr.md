# Architectural Decision Record

This file will be used as a running record of all important architectural decisions of the project.

## LLMs

Large language models are integral to the project. While ChatGPT is the most famous and one of the more powerful options, using the ChatGPT API costs money that could be unnecessary. As such, in the context of using an LLM to translate recipes into code, facing the concern of costs and research we decided to use Falcon 7b Instruct to achieve a decent quality in translating recipes to code, accepting the downsides of less reliable responses in comparison to GPT.
