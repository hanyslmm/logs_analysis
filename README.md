Logs Analysis:

To run this project, you'll need database software (provided by a Linux virtual machine vagrant) or ubuntu operating system and the data to analyze.

This will give you the PostgreSQL database and support software needed for this project.


Next, download the data here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command:
psql -d news -f newsdata.sql.

Use python3 to RUN the programs.
first RUN the view.py program to create 4 database views program will not work without the view.
then RUN the main.py program.

The programs output answers the following questions:
What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?



The output of the program is also saved in logs.txt file attached with the project.

made by
Hany Salama
