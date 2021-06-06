import random
import socket
import json
import time
from datetime import datetime

def commitCrime():

    # list of sample values
    suspect = ['Miss Scarett','Professor Plum','Miss Peacock','Mr. Green','Colonel Mustard','Mrs. White', 'Mr. Red', 'Mr. Gates', 'Young Peter', 'Young Claire', 'Grandpa Ray', 'Grandma Shonda', 'Nurse Ane']
    weapons = ['candlestick','knife','lead pipe','revolver','rope','wrench','baseball bat', 'punch', 'harmonica','sword', 'rock']
    actions = ['success','attempt','fail','canceled','arrested','contained']
    crime_types = ['single','multiple','violent','property','organized','white-collar']
    victims = ['John Lister','Ama Holly','Paul Lence','Jessica Mon','Billy Horn','Shonda MCals','Michael Anothony','Geff Gutemberg','Alonso Aguiar','Hugo Martinez']
    rooms = ['kitchen','ballroom','conservatory','dining room','cellar','billiard room','library','lounge','hall','study','swimming pool', 'living room', 'basement', 'garage','game room']
    periods_day = ['afternoon','bedtime','dinnertime','lunchtime','morning','dawn']
    curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    return {"timestamp":curr_time,"suspect":random.choice(suspect), "weapon":random.choice(weapons), "location":random.choice(rooms), "period of the day":random.choice(periods_day), "victim":random.choice(victims), "crime_type":random.choice(crime_types), "action":random.choice(actions)}

def main():
    crimeCounter = 1
    
    host = '129.159.58.78' # <--! Set Splunk Log Collector IP here !-->
    port = 10000# <--! Set Port here !-->

    while True:
        try:
            # SOCKET CREATION
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # SOCKET CONNECTION
            sock.connect((host,port))

            # EVENT CREATION
            event = commitCrime()
            event.update({"crime_number":crimeCounter})
            
            # PACKET CREATION
            message = json.dumps(event)
            
            # PACKET SENDER
            sock.send(bytes(message, encoding="utf-8"))

            # CRIME COUNTER (FOR THE LOG)
            crimeCounter += 1

            # TIME WAIT TO SIMULATE REAL LOG BEHAVIOR
            time.sleep(.3)
        
        # SOCKET CLOSE
        finally:
            sock.close()

if __name__ == '__main__':
    main()