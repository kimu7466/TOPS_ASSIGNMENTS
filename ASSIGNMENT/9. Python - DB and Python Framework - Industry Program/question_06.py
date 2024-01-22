# Q.6:- Mention what command line can be used to load data into Django? 

"""
In Django, you can use the loaddata management command to load data into the database from a fixture file. A fixture file is a serialized representation of the database data. The command looks like this:


python manage.py loaddata <fixture_file>


Here, <fixture_file> should be replaced with the path to your fixture file. The fixture file can be in various formats, such as JSON, YAML, or XML, and it should contain serialized data for your Django models.

For example, if you have a fixture file named data.json, you would run the following command:


python manage.py loaddata data.json


Make sure to run this command from the same directory where your Django project's manage.py file is located.

Additionally, you can specify multiple fixture files as arguments to the loaddata command if you want to load data from multiple files in a single command.

"""