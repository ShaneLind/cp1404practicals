"""
CP1404 Practical
Wikipedia API and Python Library
"""
import wikipedia

search_input = None
while search_input != "":
    try:
        search_input = input("Page Title/Search Phrase: ")
        print(f"Page Title:\n {wikipedia.page(search_input, auto_suggest=False).title}")
        print(f"Page Summary:\n {wikipedia.summary(search_input, auto_suggest=False)}")
        print(f"Page URL:\n {wikipedia.page(search_input, auto_suggest=False).url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.WikipediaException:
        print("Exit Program")
