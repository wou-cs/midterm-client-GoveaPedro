import requests

BASE_URL = "http://chrisbrooks.pythonanywhere.com/api/programmers"    # url for the api


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        return len(data.get('programmers', []))
    return 0
    

 
    
def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    response = requests.get(f"{BASE_URL}/{pid}")
    if response.status_code == 200:
        data = response.json()
        if 'first' in data and 'last' in data:
            return data
    return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    response = requests.get(f"{BASE_URL}/by_first_name/{first_name}")
    if response.status_code == 200:
        data = response.json()
        programmers = data.get("programmers", [])
        if programmers:
            first = programmers[0].get("first", "")
            last = programmers[0].get("last", "")
            return f"{first} {last}"
    return None
