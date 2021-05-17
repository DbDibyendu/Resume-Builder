
<img src="https://github.com/DbDibyendu/Resume-Builder/blob/main/main/static/images/resume.png?raw=true" width="150">

# [Resume-Builder](https://db-cli.herokuapp.com/)

Quick and Easy Official Resume Builder for your College. 


 
### Purpose
The project is made by me, to help students making their official college resumes.
  - You can create multiple resumes for different job profiles and save them in the data-base.
  - For each Resume get different templates to print out your Resume in the following format.

### Setup

#####  Prerequisites
What things you need to install the software and how to install them          
            
1.Install Python3 along with pip : [reference](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)   
          
2 Install Django
```
$ python3 -m pip install Django
```
##### Testing on local Server
Clone this repository onto your system
```
$ cd Resume-Builder
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
### Basic Architecture of the Project

![image](https://github.com/DbDibyendu/Resume-Builder/blob/main/main/static/images/Architecture.png?raw=true)

##### Features and resources
- User Login, Signup facility is available for multiple user.
- Javascript has been used for converting html page to pdf, for saving the resume in pdf format.
- The database used is sqlite3 for local system, and heroku postgres is used for online deployment.

### Contributers           
- Back End : [Dibyendu](https://github.com/DbDibyendu)
- Front End :  [Eshita](https://github.com/eshitachandwani)

