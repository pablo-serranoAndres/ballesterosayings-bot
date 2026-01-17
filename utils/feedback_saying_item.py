from utils.locale import LOCALE


def feedback_saying_item(field_name, value, warning):
    if (field_name == LOCALE["saying"]["title"]) : 
        return f"{LOCALE["icons"]["attention"]} *{field_name}*: {warning}" if not value else f"{LOCALE["icons"]["title"]} *{field_name}*: {value}"
    
    elif (field_name == LOCALE["saying"]["description"]) : 
        return f"{LOCALE["icons"]["attention"]} *{field_name}*: {warning}" if not value else f"{LOCALE["icons"]["description"]} *{field_name}*: {value}"
    
    elif (field_name == LOCALE["saying"]["author"]) : 
        return f"{LOCALE["icons"]["attention"]} *{field_name}*: {warning}" if not value else f"{LOCALE["icons"]["author"]} *{field_name}*: {value}"

