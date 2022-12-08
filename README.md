# CE4201-IoT-FMG
Repository for IoT Project featuring an embedded device to track location of elderly and monitor vital signs

Project structure:
- frontendapp:
    - contains all the code for the app and web app to view the data
- pi:
    - all the scripts the are inside of the raspberry pi 
    - heart rate
    - gps
- server
    - scripts for the api to work
- data
    - data that is collected
    - scripts to process this data i.e. ML, AI
----
## Todo

- **class requirments**
    - 2 min video showing thing working
    - final report
    - presentation dec 8 and 9 in person
- **front end app**:
    - UI:
        - <s> Login screen with username and password </s>
        - <s> Dashboad with map with location ploted </s>
        - <s>dashboard with grandpa name and profile pic (extra credit but not necessary) </s>
        - <s>BPM graph over time</s>
    - Data:
        - <s>populate map with points</s>
        - <s>generate graph with bpm</s>
    - Functionality:
        - <s>login </s>
        - <s>create an account </s> will not be necessary for presentation
        - <s>display grandpa info</s>
        - <s>notification when grandpa is lost (webapp alert) </s>

- **pi**:
    - Data:
        - collect BPM data
        - collect GPS data

    - Functionality:
        - go into deep sleep mode when not required to get data
        - send collected data to api
        - use celular data (good to have)
    - Hardware
        - setup celular data hardware
        - make breadboard prototype with all parts working with server
        - solder everything permenantly
        - make it look good for presnetation
        - battary circuit (**very important**)
- **server**:
    - Data:
        - store data in DB
    - Functionality
        - use data to evaluate if lost using AI
        - decide when to notify frontend about lost grndap or any problem


- **data**:
    - Data:
        - process for AI
    - Functionality
        - make AI to check if grandpa is in right location