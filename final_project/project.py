import sys
import os
import requests
import freecurrencyapi
import lists
from dotenv import load_dotenv
from countryinfo import CountryInfo
from iso639 import Lang, is_language
from iso3166 import countries


NUMBER_OF_ARTICLES = 5


class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Selected country: {self.name}\nCountry code: {self.code}\n"


class Language:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return (
            f"Selected language: {self.language}\nLanguage code: {self.language_code}\n"
        )


# Input from user to select the country
def get_country() -> str:
    """Gets a country name and returns its name and code."""
    for _ in range(3):
        name = input("Enter a country: ")
        if name in countries:
            selected_country = countries.get(name)
            print(f"Selected country: '{selected_country.name}'\n")
            return selected_country.name, selected_country.alpha2.lower()
        else:
            print("Country not found. Please try again.\n")
    else:
        sys.exit(f"There is no such country with this name: {name}")


def get_language() -> str:
    """Gets a language name and returns its name and code."""
    for _ in range(3):
        language = input("Now enter the language: ")
        if len(language) > 3:
            language = language.title()
        else:
            language = language.lower()

        if is_language(language):
            lg = Lang(language)
            print(f"Selected language: '{lg.name}'\n")
            return lg.name, lg.pt1
        else:
            print("Language not found. Please try again.\n")
    else:
        sys.exit(f"There is no such language with this name: {language}")


def get_category() -> str:
    number = 0
    for item in lists.news_categories:
        number += 1
        print(f"{number}. {item.title()}")

    for _ in range(3):
        try:
            selection = int(input("\nPick a category by its number: "))
            if lists.news_categories[selection - 1]:
                return lists.news_categories[selection - 1]
        except:
            print("Category not found. Please enter the number again.\n")
            pass
    else:
        sys.exit(f"There is no such number in the list: {selection}")


def get_currency(country: str) -> list:
    """Returns the country's currency"""
    country = CountryInfo(country)
    currency = country.currencies()
    return currency


def get_article(articles: dict, category: str, country: str) -> str:
    """Generates a index and lists articles."""
    number = 0
    print(
        f"\n\nSee below the latest 5 articles in the category {category.title()} from {country}:\n"
    )
    for result in articles["results"]:
        number += 1
        print(f"{number}. {result["title"]}.")

    for _ in range(3):
        selection = int(input("\nPick an article by its number: "))
        if selection > 0 and selection <= NUMBER_OF_ARTICLES:
            title = articles["results"][selection - 1]["title"]
            description = articles["results"][selection - 1]["description"]
            link = articles["results"][selection - 1]["link"]
            return title, description, link
        else:
            print("Article not found. Please enter the number again.\n")
            pass
    else:
        sys.exit(f"There is no such number in the list: {selection}")


# API news
def show_news(
    country_code: str,
    language_code: str,
    category: str,
    max_articles: int = NUMBER_OF_ARTICLES,
) -> dict:
    """Returns the news from API."""
    while True:
        api_key = os.getenv("API_KEY_NEWSDATA")
        response = requests.get(
            f"https://newsdata.io/api/1/news?apikey={api_key}&country={country_code}&language={language_code}&category={category}&size={max_articles}"
        )
        response = response.json()
        if response["totalResults"] == 0:
            print("No results were found.\n")
            category = get_category()
        else:
            break
    return response


# API time zone
def show_time(lat_long: list) -> str:
    """Returns the actual time in the latitude / longitude."""
    response = requests.get(
        f"https://timeapi.io/api/time/current/coordinate?latitude={lat_long[0]}&longitude={lat_long[1]}"
    )
    response = response.json()
    return response["time"]


# API weather
def show_weather(city: str) -> str:
    response = requests.get(f"https://wttr.in/{city}?0")
    return response.text


# API currency
def show_currency_exchange(country: str, currency: list) -> str:
    api_key = os.getenv("API_KEY_FREECURRENCYAPI")
    client = freecurrencyapi.Client(api_key)
    to_usd_eur = client.latest(base_currency=[currency[0]], currencies=["USD", "EUR"])
    if currency[0] == "USD":
        return f"{currency[0]} is the official currency in {country}.\n1.00 {currency[0]} equals {to_usd_eur["data"]["USD"]:.2f} EUR.\n"
    elif currency[0] == "EUR":
        return f"{currency[0]} is the official currency in {country}.\n1.00 {currency[0]} equals {to_usd_eur["data"]["USD"]:.2f} USD.\n"
    else:
        return f"{currency[0]} is the official currency in {country}.\n1.00 {currency[0]} equals {to_usd_eur["data"]["USD"]:.2f} USD or {to_usd_eur["data"]["EUR"]:.2f} EUR.\n"


def main():
    print(lists.logo)

    # Load API keys
    load_dotenv()

    country_name, country_code = get_country()
    language_name, language_code = get_language()

    country = Country(country_name, country_code)
    language = Language(language_name, language_code)
    country_info = CountryInfo(country.code)
    capital = country_info.capital()
    capital_lat_log = country_info.capital_latlng()
    capital_time = show_time(capital_lat_log)

    print("Did you know? 🧐​\n")
    print(f"It's {capital_time} in the capital of {country.name}.")
    print(show_weather(capital))

    try:
        print(f"{show_currency_exchange(country.name, country_info.currencies())}\n")
    except:
        pass

    print(
        f"Now, select one of the categories below to see the top 5 news' headers in {country.name}:\n"
    )
    category = get_category()
    articles = show_news(country.code, language.code, category)

    while True:
        selected_article = get_article(articles, category, country.name)
        print(lists.article_top)
        print(
            f"\nHeader: {selected_article[0]}\n\nDescription: {selected_article[1]}\n\nLink: {selected_article[2]}"
        )
        print(lists.article_botton)
        leave = int(input("\nEnter '1' to check another article or '2' to exit: "))
        if leave == 2:
            break


if __name__ == "__main__":
    main()
