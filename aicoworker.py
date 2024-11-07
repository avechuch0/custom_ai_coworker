#!/usr/bin/env python3
import gradio as gr
import os
import argparse
from colorama import Fore, Style, init
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import (    
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,    
    VectorStoreIndex,
)

# Provide your OpenAI API key
api_key = os.environ["OPENAI_API_KEY"] = ''

init()

robot_ascii_art = f"""
{Fore.RED}     _______              
{Fore.RED}    /       \  AI Coworker - By avechuch0      
{Fore.CYAN}   |{Fore.YELLOW}  O   O  {Fore.CYAN}|           
{Fore.CYAN}   |{Fore.RED}    >    {Fore.CYAN}|           
{Fore.CYAN}   |  {Fore.RED}\___/  {Fore.CYAN}|           
{Fore.CYAN}   |_________|            
{Fore.CYAN}    /  | |  \            
{Fore.CYAN}   |___|_|___|           
{Fore.CYAN}     |_| |_|
{Style.RESET_ALL} """

def select_model():
    print("Select the GPT model you want to use (ordered by cost from cheapest to most expensive):")
    print("1. gpt-4o-mini")           
    print("2. gpt-4o")                
    print("3. gpt-4-turbo")           

    choice = input("Enter the number corresponding to the model you want to choose: ")

    if choice == "1":
        return "gpt-4o-mini"
    elif choice == "2":
        return "gpt-4o"
    elif choice == "3":
        return "gpt-4-turbo"
    else:
        print("Invalid choice. Defaulting to gpt-4o-mini.")
        return "gpt-4o-mini"

def create_and_save_index(directory_path, model, temperature):
    # check if storage already exists
    PERSIST_DIR = directory_path
    if not os.path.exists(PERSIST_DIR):
        # Load the documents and create the index
        documents = SimpleDirectoryReader("docs").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # Store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    Settings.llm = OpenAI(temperature=temperature, model=model)
    return index

def generate_response(input_text, history):
    # Load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)    
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response.response

def launch_interface(title, model, temperature):
    iface = gr.ChatInterface(fn=generate_response, type="messages", title = title)
    
    with gr.Blocks() as chat: 
        iface.render()        
        with gr.Row():                
            gr.Markdown("Ask and get assistance of your AI coworker")   

    create_and_save_index("./storage", model, temperature)
    chat.launch(share=True)

if __name__ == "__main__":
    print(robot_ascii_art)
    parser = argparse.ArgumentParser(description="Use AI to train your data stored in the 'docs' folder")
    parser.add_argument("-title", type=str, required=True, help="Title or topic for your AI coworker")
    parser.add_argument("-temp", type=float, required=False, default=0.5, help="The temperature setting for the GPT model (e.g., 0.0 to 1.0)")
    args = parser.parse_args()

    # Call the select_model function to get the desired model
    selected_model = select_model()

    # Launch the interface with the selected title, model, and temperature
    launch_interface(args.title, selected_model, args.temp)