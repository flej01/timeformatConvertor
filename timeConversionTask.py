import re

def extractTime(text):
    """
    :param text: takes text as an input and applying regular expression on it
    :return: time that matches regular expression in pattern variable as a string
    """
    # creating pattern that matches string in format: hours:minutes:seconds and two letters behind it (space is not required)
    pattern = "[0-9]{1,2}:[0-9]{2}:[0-9]{2}\s?([a-z]{2}|[A-Z]{2})"
    # searching for a match in text
    match = re.search(pattern, text)
    # returns first match
    matched = match[0]
    return matched


# Function to convert the date format
def convertTimeFormat(text):
    """
    :param text: takes time in 12 hour format
    :return: time in 24 hour format
    """
    # check if input contains AM in last two elements and 12 in first two elements
    if text[-2:] == "AM" and text[:2] == "12":
        return "00" + text[2:-2]

        # removing AM string
    elif text[-2:] == "AM":
        return text[:-2]

        # doing the same for PM option
    elif text[-2:] == "PM" and text[:2] == "12":
        return text[:-2]

    else:
        # removing PM
        return str(int(text[:2]) + 12) + text[2:8]
