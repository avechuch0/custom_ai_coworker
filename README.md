# Custom_AI_Coworker

![Coworker AI](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/logo.png)

AI Coworker is an AI-powered assistant designed to help you with various tasks in a workspace environment. It utilizes OpenAI's language models to provide intelligent responses, helping you make informed decisions and streamline your workflow.

This project is a RAG (Retrieval Augmented Generation) algorithm to assist in your particular needs and data not included in LLMs market for obvious reasons. 

"LLMs are trained on enormous bodies of data but they aren't trained on your data", LlamaIndex.

This is the general view of a RAG concept, courtesy of LlamaIndex.

![RAG](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/RAG.png)

## Features

- **Model Selection:** Choose from different GPT models, including `gpt-4o-mini`, `gpt-4o`, and `gpt-4-turbo`.
- **Customizable Settings:** Adjust the temperature setting to control the creativity of the AI's responses.
- **User-Friendly Interface:** Powered by Gradio for a simple and interactive experience.
- **Storage Integration:** Save and load indexes with ease, ensuring persistent and retrievable data.
- **Command-Line Options:** Customize your experience with command-line arguments for model selection and temperature control.

## Installation

1. Download / clone the repo
2. Install required packages: ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt``` 
3. Provide the OpenAI apikey next to the equal sign and within the quotes ```api_key = os.environ["OPENAI_API_KEY"] = 'your_apikey_here' ```

## Usage

**Command-Line Arguments**
- **-title**: Set the title for your session, you can use your particular topic, process etc of your trained data. This is a required argument.
- **-temp**: Set the temperature for the model’s responses. Acceptable range is 0.0 to 1.0.
- After running it, you would be asked about the model to use, just select between 1 to 3.

## Interface
Once the program is running, you can interact with AI Coworker via a Gradio-powered web interface. Just enter your queries and receive intelligent responses.

## Proof of Concept
To illustrate, I used ChatGPT to create a couple of documents of a ficticious company called ACME Corp including some details of technology deployed, it was intentionally made with vulnerabilities and misconfigurations. I used this project with ACME docs to train this new model to get advise and recommendations provided by the prompts sent to the LLM in Gradio web interface. 

There are many use cases of this project, it's up to you :)

![POC1](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/POC_1.png)

![POC2](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/POC_2.png)

## Contact
Twitter: [@avechuch0](https://twitter.com/avechuch0)