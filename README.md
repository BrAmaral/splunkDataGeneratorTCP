# splunkDataGeneratorTCP

This is a simple python script that generates fake JSON data and send it to Splunk via TCP (Inspired by [George Starcher's code](https://github.com/georgestarcher/Splunk-Class-httpevent))



## Requirements

- Python 3.x

## Basic Usage

1. Set the Splunk log collector (Universal Forwarder/Heavy Forwarder/Single Instance) IP and the listening port (in code line 24 and 25)

2. Execute the script with the command:

   ```
   python3 splunkDataGeneratorTCP.py
   ```

   
