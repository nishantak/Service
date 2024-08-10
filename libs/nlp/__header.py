from _listenSpeak import say , listen
from _nlp import match

def header():
    header_values = []
    
    say("Enter truck serial number")
    truck_serial_number = listen()
    header_values.append( truck_serial_number)
    
    say("Enter truck model")
    truck_model = listen()
    header_values.append( truck_model)

    say("Enter inspection id")
    inspection_id = listen()
    header_values.append( inspection_id)

    say("Enter date time")
    date_time = listen() #implemnet date and time module
    header_values.append( date_time)

    say("Enter location")
    location = listen()
    header_values.append( location)

    say("Enter geo Coordinates")
    geoCoordinates = listen()
    header_values.append( geoCoordinates)

    say("Enter service meter hours")
    text = listen()
    pattern = [{"LIKE_NUM":True}]
    matches=match(pattern,text)
    try:
        service_meter_hours = matches[0][0]
        header_values.append(service_meter_hours)
    except:
        header_values.append(0)

    say("Enter customer name")
    customer_name = listen()
    header_values.append( customer_name)

    say("Enter CAT id")
    CAT_id = listen()
    header_values.append( CAT_id)

    return header_values


