# Neighbourhood

##### By [Ronald Kiprotich](https://github.com/RonaldKiprotich) and [Collins Kipkoech](https://github.com/kipkoech-msojo)

## Links
* Back end repository: [View](https://github.com/RonaldKiprotich/Neighborhood.git)
* Back end live site: [View Site](https://rayneighborhood.herokuapp.com/)
* Front end repository: [View](https://github.com/felkiriinya/Neighbourhood-Frontend)
* Front end live site: [View Site](https://neighbourhoodgroup.netlify.app/)

## End Points.
* https://rayneighborhood.herokuapp.com/api/adminprofile/
* https://rayneighborhood.herokuapp.com/api/occupantlist/
* https://rayneighborhood.herokuapp.com/api/neighborhood/
* https://rayneighborhood.herokuapp.com/auth/signup/
* https://rayneighborhood.herokuapp.com/api/business/
* https://rayneighborhood.herokuapp.com/api/v1/post/
* https://rayneighborhood.herokuapp.com/api/token/
* https://rayneighborhood.herokuapp.com/api/token/refresh/
* https://rayneighborhood.herokuapp.com/logout/
* https://rayneighborhood.herokuapp.com/api/v1/profile/



  
# Description  
This is a neighborhood application where a user have to signup first and be able to view different neighbourhoods. A user can join or leave a neighbourhood and once he/she joins, they can view information about that neighbourhood.


 
## User Story  
As a user I would like to:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.  
  

  
## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/RonaldKiprotich/Neighborhood.git
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  


##### Navigate into the folder:
 ```bash 
cd G-Hood 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations ghood
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/1.1/)  
* [Heroku](https://heroku.com)  

## Figma Design
[View Design](https://1drv.ms/p/s!AhtkLGb6CU57hh5WwxwWiOG9TqdA?e=VNHhW7)

## ERD Diagram

[View Diagram](https://drive.google.com/file/d/1o488_x9x5Dk6rLW-Y-N8P8L7nCEw5TjO/view?usp=sharing)
  
  
## Known Bugs  
* There are no known bugs at the moment.
  
## Contact Information   
If you have any question or contributions, please email me at protich12@gmail.com.
  

## License
* [[License: MIT]](LICENSE.md)
* Copyright (c) 2020 **Ronald Kiprotich**||**Collins Kipkoech**