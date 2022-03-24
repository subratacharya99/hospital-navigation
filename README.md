# UIHC Navigation App
This app was developed to navigate people around the University of Iowa Hospitals and Clinics (UIHC). It utilizes Neo4j database with a Flask backend and HTML/CSS/JS frontend. Developed by Subrat Acharya, Alaa Fadelsied, Holly Kuchel, and Karlee Kuntzman.

## Set Up

### Basic Requirements
First download Python if you do not have it already. In order to check if you already have it, in the terminal(Mac) or command prompt(windows) type the following:
```
python --version
```
or
```
python3 --verson
```
Ensure you have a version of Python that is atleast 3.8 or newer. Then navigate to a directory where you can store the files for the app using the _cd_ command. Once in the directory, clone this git project using the HTTPS url found in green **code** button on the repository page.
```
git clone <url>
```
After you have cloned the repository, navigate inside it using
```
cd flaskapp
```
Now we set up the virtual environement. If you don't have it alrady download the virtual environment python package using the command:
```
pip install virtualenv
```
Once inside the flaskapp folder create a new virtual environment using the command:
```
python -m venv flask
```
Then activate the virtual environment,  
windows:
```
.\flask\scripts\activate
```
mac:
```
source flask/bin/activate
```
If there is a (flask) to the very left of your command line input, then the environment was activated successfully. Once inside the virtual environment, install all packages needed for this app by using the command:
```
pip install -r requirements.txt
```
If the following command fails, cd to the folder that contains the requirements.txt and type the command in again.
The setup for the app is now completed!

## Helpful Resources
[Neomodel Documentation](https://neomodel.readthedocs.io/en/latest/getting_started.html)  
[Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)  
[Flask Tutorial Playlist - Corey Schaefer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
[WTForms for Flask](https://wtforms.readthedocs.io/en/2.3.x/)

