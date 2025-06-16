from dateutil.parser import parse

def extract_datetime(text):
    """
    Extract the first datetime found in a string using fuzzy matching.
    """
    try:
        return parse(text, fuzzy=True)
    except ValueError:
        return None
