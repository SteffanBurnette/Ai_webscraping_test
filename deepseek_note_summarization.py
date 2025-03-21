'''
ollama run deepseek-r1:1.5b
:P
website:  https://ollama.com/library/deepseek-r1:1.5b
'''
#Allows me to interact with the deepseek model
#that is running locally via the ollama software
from langchain_ollama import ChatOllama 
#json format
import json  
#Allows me to interact with the operating system
import os
#Initializing the deepseek model 
#Make sure ollama is running
my_llm = ChatOllama(model="deepseek-r1:1.5b", temperature = 0)

#Returns the current working directory
print(f"My current working directory: {os.getcwd()} \n")

#Location of my file
filename = "c:/Users/Burne/Desktop/txt Notes/python_file_manipulation_tutorial.txt"
#Opens the file with read only permissions
with open(filename, 'r') as file:
    #Reads all of the files contents
    data = file.read()
    #Will summarize the data within the specified file
    msg = my_llm.invoke("Summarize my notes: " + data)
    print(msg.content) #Gets the response via .content

#Opens the file with write permissions and will add new content to the end of the file
with open("lesson_summary.txt", 'a') as file:
    file.write(msg.content) #Appends the ai's response to the file caching it for later use


#Will summarize the data within the specified file and cache said resonse to a new file
#Could add a dilimeter to the end of the file name so that i can slightly change the name to create
#a new file for each new response instead of appending to the same file over and over again