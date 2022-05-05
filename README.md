# UIHC Navigation App
This app was developed to navigate people around the University of Iowa Hospitals and Clinics (UIHC). It utilizes Neo4j database with a Flask backend and HTML/CSS/JS frontend. Developed by Subrat Acharya, Alaa Fadelsied, Holly Kuchel, and Karlee Kuntzman.

## Set Up

### Basic Requirements
Ensure you have a version of Python that is atleast 3.8 or newer. Then navigate to a directory where you can store the files for the app using the _cd_ command. Once in the directory, clone this git project using the HTTPS url. This app also requires a up and running neo4j database in order to run. Create a neo4j database, and keep note of the username, password, and uri of the database. You will need these to connect to the database later. 
```
git clone <url>
```
After you have cloned the repository, navigate inside the flaskapp folder. Set up the virtual environement. Once inside the flaskapp folder create a new virtual environment then activate the virtual environment. Once inside the virtual environment, install all packages needed for this app by using the command:
```
pip install -r requirements.txt
```
If the following command fails, cd to the folder that contains the requirements.txt and type the command in again. After all the requirements are set up, set up environmental variables for the neo4j database that the app will communicate with: USER = <username>, PASSWORD = <password>, URI = <database uri>.
The setup for the app is now completed!
  
## Database Setup
Unfortunately while developing this application, we were unable to utilize the neo4j ORM package "neomodel" because one of its dependencies was not compatible with windows. If working exclusively on mac, then this ORM may be implemented to make querying the database easier. If not, then links to documentation for Cypher, the query language for neo4j databases, is listed under helpful resources below.  
   
This database was setup with two types of nodes, Elevator and Location nodes. Each elevator node has properties "name" and "floor". Location nodes have properties "name", "floor", and "building". There is only one type of relationship that connects all nodes name "CONNECTS". This relationship is unidirectional, but can have bidirectional properties. Currenlty the "CONNECTS" relationship only has one property, "name". When setting up locations that branch off of elevators, the name property of the relationship stores the direction FROM the location to the elevator. However, in the future it can be set up so that these relationships store the directions to the elevator and from the elevator.  

## Other Notes
There are still plenty of improvements that can be made to this application. Please implement them as you will. Here is a list of improvements that can be made to give some ideas:  
1. Implementing the Closures and Contacts Page
2. Implementing the settings page with accessibility features
3. Better directions stored in the database
4. Visual directions
  
Thank you for taking the time to read this. I hope you are able to use this as a foundation for a truly great solution to navigating the UIHC.

## Helpful Resources
[Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)  
[WTForms for Flask](https://wtforms.readthedocs.io/en/2.3.x/)
[Cypher Query Language Documentation](https://neo4j.com/developer/cypher/)
  
