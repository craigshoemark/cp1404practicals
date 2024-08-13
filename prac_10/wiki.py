"""
Wikipedia API:
"""
import wikipedia


def search_wikipedia():
    search_phrase = input("Enter page title: ")
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(wikipedia.search(search_phrase))

        except wikipedia.exceptions.PageError as e:
            print(f"Page id '{search_phrase}' does not match any pages. Try another id!")

        search_phrase = input("Enter page title: ")

    print("Thank you.")


search_wikipedia()
