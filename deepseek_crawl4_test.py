from langchain_ollama import ChatOllama #Allows m to interact with the deepseek model
from crawl4ai import WebCrawler #Ai powered webscraper
import json 

llm = ChatOllama(model="deepseek-r1:1.5b", temperature = 0)
llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature = 0, format = "json")

#Creates an instance of the web crawler
crawler = WebCrawler() 

#Warms up the crawler by loading the necessary modelss
crawler.warmup() 

#Will webscrape the facebook tos:
result = crawler.run(url = "https://tosdr.org/en/service/182") 

#print(result.markdown) #Prints the extracted content

#Will summarize the webscrapped data
msg = llm.invoke("Summarize the text: " + result.markdown)

print(msg.content)

#The Response after looking at facebooks ToS
'''
<think>
Okay, so I'm trying to understand this document about Facebook's privacy policy. It looks like it's a pretty detailed document that covers various aspects of how Facebook handles user data and personal 
information. Let me go through each section one by one to get a better grasp.

First, there are sections on Data Privacy, Terms of Service, and Privacy Basics. These seem to lay out the general principles Facebook follows regarding how users' data is collected, used, and shared. I remember that Facebook uses cookies for various purposes like tracking user behavior, personalizing 
content, and ensuring security. So, this document probably outlines the policies around these cookie 
usage.

Then there are sections on Cookie Policy, Data Policy, Privacy Basics, Terms of Service, Terms of Use, and Branding. These all seem to be variations or supplements to the main privacy policy. Maybe some additional details about how Facebook handles different types of data, like personal information versus non-personal (like payment info). I think the Data Policy might specify exactly what kind of data Facebook collects and how it's used.

The document also includes sections on Feedback, API, About, Contact, Privacy Basics, Terms of Use, and Branding. These are probably for user interaction with the privacy policy. The Feedback section might explain how users can provide feedback about their experience, while the API section could detail how Facebook interacts with other services or platforms.

Under "About Us," there's a mention of a project called "ToS; Didn't Read" started in June 2012 to address misinformation on the web. This suggests that the document is part of a movement to correct inaccuracies about privacy policies and terms of service. The sections here talk about what information 
Facebook collects when someone visits a site with a Like button, which I think relates to social sharing features.

The "About Us" section also includes translations for each point in German, English, Spanish, French, Japanese, Dutch, Polish, Russian, Chinese, and others. This makes the document accessible to a wider audience by providing clear explanations in multiple languages.

Looking at the sections on Privacy Basics, Terms of Service, and Terms of Use, these are likely the core parts of the privacy policy that users need to understand before using Facebook. The Terms of Service might outline what users agree to when they sign up or use certain services, while the Terms of 
Use could be similar but perhaps more detailed for different platforms.

The "What information does Facebook get when I visit a site with the Like button?" section is interesting because it explains how social sharing works on Facebook. It probably mentions that liking increases shares and comments, which ties into data collection practices.

I also notice that there are sections about Data Collection, which might detail specific types of data Facebook collects—like location, browsing habits, etc.—and how they're used for various purposes like targeted ads or improving the user experience.

The document seems to be structured in a way that covers all necessary aspects of privacy and terms of service. It's comprehensive but also quite detailed, especially under sections like Data Policy and Privacy Basics. The translations provided are helpful because it makes the document accessible to a 
broader audience, which is important for maintaining trust with users who might not speak English.   

I wonder how this document compares to other privacy policies I've seen. It seems pretty thorough, covering both general principles and specific details about different data types. However, some sections might be too technical or detailed for non-experts, so it's probably best used by those who are already familiar with the concepts involved.

Overall, this document is a valuable resource for anyone looking to understand how Facebook handles personal information. It provides clear explanations in multiple languages and covers all the necessary aspects of privacy and terms of service.
</think>

The document provided is a comprehensive privacy policy document for Facebook, structured into several key sections that cover various aspects of data handling and user interactions. Here's an organized summary:

### Core Sections:
1. **Data Privacy and Terms of Service**: Outlines general principles on how Facebook collects, uses, and shares personal information.
2. **Cookie Policy, Data Policy, Privacy Basics, Terms of Service, Terms of Use, Branding**: Details 
specific policies related to different types of data collection (personal vs. non-personal) and user 
interactions with the platform.

### Feedback and API Sections:
- **Feedback**: Explains how users can provide feedback on their experience.
- **API**: Describes Facebook's interaction with other services or platforms.

### About Us Section:
- **Project "ToS; Didn't Read"**: A movement to correct misinformation about privacy policies, covering various aspects of data collection and usage.

### Language Translations:
The document includes translations in multiple languages (German, English, Spanish, French, Japanese, Dutch, Polish, Russian, Chinese), making it accessible to a broader audience.

### Key Features:
- **Social Sharing**: Explains how Facebook uses likes for sharing features.
- **Data Collection Details**: Outlines specific data types and purposes of collection, such as location and browsing habits.

This document is thorough, covering all necessary aspects of privacy and terms of service, with clear language translations to ensure accessibility. It's best used by those familiar with the concepts involved.
'''

#Will prompt it explain to the end user how this could be detrimental to
#their privacy and security.