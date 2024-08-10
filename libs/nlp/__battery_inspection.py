from _listenSpeak import say, listen
from _nlp import match , phrase_match

def battery_inspection():
    battery_info = []


    say("Enter the battery make ")
    battery_make = listen()
    battery_info.append(battery_make)


    say("Enter the battery replacement date")
    replacement_date = listen()  
    battery_info.append(replacement_date) # date implimentation


    say("Enter the battery voltage ")
    text = listen()
    pattern = [{"LIKE_NUM":True}]
    matches=match(pattern,text)
    try:
        battery_voltage = matches[0][0]
        battery_info.append(battery_voltage)
    except:
        battery_info.append(0)


    say("Enter the battery water level ")
    text = listen()
    match_good=phrase_match(['good','Good','GOOD'],text)
    match_ok=phrase_match(['ok','Ok','OK'],text)
    match_low=phrase_match(['low','LOW','Low'],text)
    water_level = 0 if match_ok else None
    water_level = 1 if match_good else None
    water_level = -1 if match_low else None
    battery_info.append(water_level)


    say("Is there any damage to the battery? ")
    text = listen()
    match_yes=phrase_match(['yes','Yes','YES'],text)
    damage_condition = 1 if match_yes else 0
    battery_info.append(damage_condition)
    if damage_condition:
        say("Attach an image of the damage")
        #image  
        

  
    say("Is there any leak or rust in the battery? ")
    text = listen()
    match_yes=phrase_match(['yes','Yes','YES'],text)
    leak_rust_condition = 1 if match_yes else 0
    battery_info.append(leak_rust_condition)

    return battery_info


