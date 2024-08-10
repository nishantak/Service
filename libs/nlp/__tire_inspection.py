from _listenSpeak import say , listen
from _nlp import match,phrase_match

def tire_inspection():
    tire_data = []

    def get_tire_info(position):
        say(f"Enter tire pressure for {position}")
        text = listen()
        pattern = [{"LIKE_NUM":True}]
        matches=match(pattern,text)
        try:
            tire_pressure =  matches[0][0]
        except:
             tire_pressure = 0 

        say(f"Enter tire condition for {position} ")
        text = listen()
        match_good=phrase_match(['good','Good','GOOD'],text)
        match_ok=phrase_match(['ok','Ok','OK'],text)
        match_NR=phrase_match(['Needs Replacement','needs replacement','NEEDS REPLACEMENT'],text)
        tire_condition = 0 if match_ok else None
        tire_condition = 1 if match_good else None
        tire_condition = -1 if match_NR else None
        
        tire_data.append([tire_pressure,tire_condition])
        

    positions = ["Left Front", "Right Front", "Left Rear", "Right Rear"]
    
    for position in positions:
        get_tire_info(position)
    
    return tire_data
