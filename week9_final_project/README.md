# Country Insights and News App
#### **Video Demo:**  <https://youtu.be/3YkU214mY3g>
#### **Description:** Welcome to the app where you can read news from other countries, in the language that you want.

## Overview

This Python application provides users with information about a selected country, including:

- Current time in the capital.
- Weather in the capital.
- Currency exchange rates compared to 'USD' and 'EUR'.
- Top news headlines in various categories.

It combines multiple APIs to deliver real-time data and allows users to navigate through news categories and articles in an interactive console interface.

---

## Features
1. **Country Selection**: Choose a country to retrieve relevant information.
2. **Language Selection**: Specify a language for news articles.
3. **News Categories**: Browse news from predefined categories.
4. **Currency Exchange**: View exchange rates for the country's currency against USD and EUR.
5. **Weather Update**: Get the latest weather details for the capital city.
6. **Current Time**: Check the current time in the country's capital.
7. **Article Explorer**: Navigate and read summaries of news articles, with links for further reading.

---

## Requirements

### Python Version
- Python 3.9 or above.

### Dependencies
Install the required libraries using:
```bash
pip install -r requirements.txt
```
### Required libraries:

- requests
- freecurrencyapi
- python-dotenv
- countryinfo
- iso639
- iso3166

### Environment Variables
Create a `.env` file in the root directory with your API keys:

```dotenv
API_KEY_NEWSDATA=your_newsdata_api_key
API_KEY_FREECURRENCYAPI=your_freecurrencyapi_key
```

---

## Usage

### Running the App

1. Clone the repository.
2. Ensure the `.env` file contains valid API keys.
3. Run the program:

```
python project.py
```

### Steps

1. Enter a country name.
2. Specify the language for news articles.
3. Choose a news category from the displayed list.
4. Explore the latest articles in the chosen category.
5. Access real-time data, such as the weather, time, and currency exchange rates for the selected country.

---

## API Integrations

- **NewsData API:** Fetches the latest news headlines.
- **TimeAPI:** Retrieves the current time based on geographical coordinates.
- **FreeCurrencyAPI:** Provides real-time currency exchange rates.
- **Wttr.in:** Offers real-time weather information.

---

## File Structure

- `project.py`: Main application file.
- `lists.py`: Contains predefined lists and ASCII art.
- `.env`: File to store API keys (not included; create manually).

---

## Known Issues

- **Error Handling:** Limited validation for API responses.
- **Capital Coordinates:** Certain countries might not have complete data.

---

## Author

- [@andremazzei](https://www.github.com/andremazzei)

---

### Enjoy exploring the world with the Country Insights and News App! 🌍
