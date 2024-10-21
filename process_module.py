from time_module import get_date, get_time
from internet_connection import internet
from news import get_news
from web_applications import browser
from browser import search
import finance_manager  


def process(query):
    query = query.lower()
    
  
    if "finance manager" in query or "open finance" in query:
        print("Entering Finance Manager...")
        finance_manager.finance_manager()  
        print("Returning to assistant...")
        return "Welcome Back"
    elif "who is" in query or "about" in query or "tell me about" in query or "something" in query:
        return search(query)
    
   
    elif "time" in query:
        return "Time is " + get_time()
    elif "date" in query:
        return get_date()
    

    elif "internet" in query:
        return internet()
    
  
    elif "news" in query:
        return get_news()

    elif "open facebook" in query:
        return browser.open_facebook()
    elif "open google" in query:
        return browser.open_google()
    
  
    else:
        return "I didn't understand that. Please try again."


