# ToDo
## Description
This is a very simple application that takes care of your To-Do list. You can add items and check them off as you complete them. To achive this we use three separate components, one container for the Frontend, another for the Backend to comunicate exact requests to the third component the MySQL database. 

## Architectur
We use a API Gateway architectur. The Frontend acts as the API in this case, it's job is to recive requests from the user and forward them to the appropriate endpoint in the Backend. Indeed he is not even allowed to fetch the list of todo items from the database to display them to the user, something quite trivial. This has the advantage of making the Frontend completely independant of both the Backend and the Database. 

The Backend in turn takes care of any requests coming it's way, only from the Frontend at this time. He in turn gets any information he needs from the database to forfill the action. Currently there are only three actions avilable; adding an item to the todo list, getting the todo list or changing and items current status. 

The database is a MySQL database and has one table, the ToDo. It only has tree column, id, status and description. Id is an integer and the primary key, status is a boolean and defaults to False and lastly description which of type Text. 