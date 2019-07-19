import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']

# The multilinguist documentation tells us that this class represents a world-traveller who speaks many languages. 

# The first child class that we're going to define represents a world-travelling math genius who can speak many languages and mentally add up huge lists of numbers.
# Instances of this class should be able to accept a list of numbers and returtouchn a sentence stating the sum of the numbers. 
# Make use of the inherited Multilinguist methods to ensure this sentence will always be delivered in the local language.
# me = MathGenius()
# print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# me.travel_to("India")
# print(me.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# me.travel_to("Italy")
# print(me.report_total([324,245,6,343647,686545])) # È Il totale 1030767

# Quote collector
# The second child class we're going to define represents a person who loves to memorize quotes and then travel the world, 
# unleashing poor translations of them to unsuspecting passers-by.

# Each instance of this class should have its own ever-growing collection of favourite quotes. 
# It should have the ability to add a new quote to its collection as well as the ability to select a random quote to share in the local language.

# Stretch goals
# Improve the quote collector's conversational skills be allowing them to keep track of the topic of each quote (eg. "wisdom", "friendship") 
# and add the ability to share a quote according to a specific topic, in addition to being able to share a random one.
# Come up with a third child class that can make use of the multilinguist's abilities.
# Give the math genius additional math-related skills besides adding long lists of numbers. Check out Python's Math module for inspiration.

jason = Multilinguist()
jason.travel_to("Brazil")
print(jason.say_in_local_language("Hello world, this is some text that is being translated into portugese"))

class MathGenius(Multilinguist):
  def report_total(self, list_of_numbers):
    return self.say_in_local_language(f' The total is: {sum(num for num in list_of_numbers)}')

me = MathGenius()
print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
me.travel_to("India")
print(me.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
me.travel_to("Italy")
print(me.report_total([324,245,6,343647,686545])) # È Il totale 1030767


class QuoteCollector(Multilinguist):
  known_quotes=[
    "A Bird in the hand is worth two in the bush",
    "Do or do not there is no try",
    "Talent borrows, genius steals"
  ]

  def learn_quote(self, new_quote):
    self.known_quotes.append(new_quote)
  
  def random_quote(self):
    quotepick = random.choice(self.known_quotes)
    translate_quote = self.say_in_local_language(quotepick)
    return(translate_quote)

you = QuoteCollector()
print(you.random_quote())
you.travel_to("Italy")
print(you.random_quote())