# Custom AI Coworker

![Coworker AI](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/logo.png)

AI Coworker is an AI-powered assistant designed to help you with various tasks in a workspace environment. It utilizes OpenAI's language models to provide intelligent responses, helping you make informed decisions and streamline your workflow.

This project leverages RAG (Retrieval-Augmented Generation) powered by LlamaIndex and the latest LLMs of OpenAI to generate accurate and contextually relevant responses based in your documentation. By using this tool, you would train and create a personal AI Coworker with your own custom data... And will be able to interact and chat with the Coworker based on that data trained.

"LLMs are trained on enormous bodies of data but they aren't trained on your data", a quote from LlamaIndex.

## Hold on, what is RAG?

Retrieval-Augmented Generation (RAG) is a technique that enhances the response generation of AI models by retrieving relevant information from external sources or documents. Instead of relying solely on pre-trained knowledge, RAG dynamically fetches and incorporates up-to-date or context-specific data, leading to more accurate and contextually relevant responses. 

## How this tool works?

To enable the program to function correctly, you must place the documents you want to use about the topic you like to work in with the AI Coworker in the `docs` folder. The program will then index these documents, using them as the foundation for generating informed and precise outputs in a question-answer chat.

This is the general view of a RAG concept, courtesy of LlamaIndex below

![RAG](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/RAG.png)

## Features

- **Model Selection:** Choose from different GPT models, including `gpt-4o-mini`, `gpt-4o`, and `gpt-4-turbo`.
- **Customizable Settings:** Adjust the temperature setting to control the creativity of the AI's responses.
- **User-Friendly Interface:** Powered by Gradio for a simple and interactive experience.
- **Storage Integration:** Save and load indexes with ease, ensuring persistent and retrievable data.
- **Command-Line Options:** Customize your experience with command-line arguments for model selection and temperature control.

## Requirements & Installation

To run AI Coworker, you need the following Python packages `llama-index`, `openai`, `gradio`, `argparse`, `colorama`.

1. Download / clone the repo
2. Install required packages: ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt``` 
3. Provide the OpenAI apikey next to the equal sign and within the quotes ```api_key = os.environ["OPENAI_API_KEY"] = 'your_apikey_here'```
4. Include your documents in the `docs` folder. You can use MS Office files, PDF, txt, etc.

## Usage

**Command-Line Arguments**
- **-title**: Set the title for your session, you can use your particular topic, process etc of your trained data. This is a required argument.
- **-temp**: Set the temperature for the model’s responses. Acceptable range is 0.0 to 1.0. If not used, by default is setup in 0.5.
After running it, you would be asked about the model to use, just select between 1 to 3.

**Examples**
python coworker_ai.py -title "CustomData"
python coworker_ai.py -title "ACME Corp" -temp 0.5

## Interface
Once the program is running, you can interact with AI Coworker via a Gradio-powered web interface. Just enter your queries and receive intelligent responses.

## Proof of Concept
To illustrate, I used ChatGPT to create a couple of documents of a ficticious company called ACME Corp including some details of technology deployed, it was intentionally made with vulnerabilities and misconfigurations. I used this project with ACME docs to train this new model to get advise and recommendations provided by the prompts sent to the LLM in Gradio web interface. 

There are many use cases of this project, it's up to you :)

![POC1](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/POC_1.png)

![POC2](https://github.com/avechuch0/custom_ai_coworker/blob/main/images/POC_2.png)

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open a pull request or an issue.

## Support
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/avechuch0)

Just click on the image above if you enjoyed my work, consider to support me on buymeacoffee to keep going and get colombian coffee or some other beverages for the hours invested in future projects.

## Contact
Twitter (X): [@avechuch0](https://twitter.com/avechuch0)