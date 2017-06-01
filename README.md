# news_logs_analysis_with_postgreSQL_python
A data analysis python application. This is an internal reporting tool that analyse information from the database to discover some required information.

## Installation

*news_logs_analysis_with_postgreSQL_python* requires [Python](https://www.python.org/) 2.7+ and [Vagrant](https://www.vagrantup.com/downloads.html) to run. If Vagrant is successfully installed, you will be able to run ```vagrant --version```
in your terminal to see the version number.

Download the ```newsdata.zip``` folder and extract the ```newsdata.sql``` file.

After the Python and the Vagrant are installed in your machine, type the following code in your terminal(Linux base machine)/git Bash(Windows):
Starting the Ubuntu Linux installation with ```vagrant up```.
Logging into the Linux VM with ```vagrant ssh```.
Load the data into the PostgreSQL database. Use the command ```psql -d news -f newsdata.sql```.

### There are three tablesin the database: 
* The ```authors``` table includes information about the authors of articles.
* The ```articles``` table includes the articles themselves.
* The ```log``` table includes one entry for each time a user has accessed the site.

### Explore the data:
Once you have the data loaded into your database, connect to your database using ```psql -d news``` and explore the tables using the ```\dt``` and ```\d table``` commands and select statements.

* ```\dt``` — display tables — lists the tables that are available in the database.
* ```\d table``` — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

### Run the SQL statement:
Once the database is set up, run the ```newsdata.py``` on your Vagrant virtual machine by typing ```$ python newsdata.py``` in your terminal/command line. There are six functions inside the application.
* ```get_most_popular_three_articles()```, return the most popular three articles of all time
* ```get_most_popular_article_authors()```, return the most popular article authors of all time
* ```get_days_with_requests_errors()```, return the days with more than 1% of requests lead to errors
* ```display_articles(data)```, receive popular articles information from the given array, the print them in text
* ```display_authors(data)```, receive popular article authors information from the given array, the printm the in text
* ```display_error_days(data)```, receive error logs information from the given array, the print them in text


## License

`news_logs_analysis_with_postgreSQL_python` is a public domain work, dedicated using
[MIT License](https://opensource.org/licenses/MIT). Feel free to do
whatever you want with it.
