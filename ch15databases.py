# --- Databases ---
print('- - -  Databases - - -')


# Relational Databases

# Relational databases model data by storing rows and columns in tables.
#   The power of the relational database lies in its ability to efficiently retrieve
#   data from those tables and in particular where there are multiple tables and the
#   relationships between those tables involved in the query.

# Terminology

# Database - contains many tables
# Relation (or table) - contains tuples and attributes
# Tuple (or row) - a set of fields that generally represents an “object” like a person or a music track
# Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row

# A relation is defined as a set of tuples that have the same attributes.
#    A tuple usually represents an object and information about that object.
#    Objects are typically physical objects or concepts.
#    A relation is usually described as a table, which is organized into rows and columns.
#    All the data referenced by an attribute are in the same domain and conform to the same constraints.


# SQL
# Structured Query Language is the language we use to issue commands to the database
#   -  Create data (a.k.a Insert)
#   -  Retrieve data
#   -  Update data
#   -  Delete data 
# CRUD = create/retrieve/update/delete


# --- Web Applications w/ Databases ---
# Application Developer - Builds the logic for the application,
#       the look and feel of the application - monitors the application for problems
# Database Administrator - Monitors and adjusts the database as the program runs in production
# Often both people participate in the building of the “Data model”

# --- Database Administrator ---
# A database administrator (DBA) is a person responsible for the design,
#  implementation, maintenance, and repair of an organization’s database.
#  The role includes the development and design of database strategies,
#  monitoring and improving database performance and capacity, and planning
#  for future expansion requirements. They may also plan, coordinate,
#  and implement security measures to safeguard the database.


# --- Database Model ---
# A database model or database schema is the structure or format of a database,
#  described in a formal language supported by the database management system.
#  In other words, a “database model” is the application of a data model
#  when used in conjunction with a database management system.

# --- Common Database Systems ---
# Three major Database Management Systems in wide use
# -  Oracle     : Large, commercial, enterprise-scale, very very tweakable
# -  MySql      : Simpler but very fast and scalable - commercial open source
# -  SqlServer  : Very nice - from Microsoft (also Access)
# Many other smaller projects, free and open source
# -  HSQL, SQLite, Postgres, MariaDB... 

# --- SQLite Browser ---
# SQLite is a very popular database - it is free and fast and small
# SQLite Browser allows us to directly manipulate SQLite files
# http://sqlitebrowser.org/
# SQLite is embedded in Python and a number of other languages

# --- SQL ---
# Structured Query Language is the language we use to issue commands to the database
# C R U D
# -  Create data (a.k.a Insert)
# -  Retrieve data
# -  Update data
# -  Delete data 


# --- SQL: Insert ---
# The insert statement inserts a row into a table

# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

# --- SQL: Delete ---
# Deletes a row in a table based on selection criteria

# DELETE FROM Users WHERE email='ted@umich.edu'

# --- SQL: Update ---
# Allows the updating of a field with a where clause

# UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

# --- Retrieving Records: Select ---
# The select statement retrieves a group of records - you can either
#  retrieve all the records or a subset of the records with a WHERE clause

# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'

# --- Sorting with ORDER BY  ---
# You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order

# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name DESC




# --- SQL Summary ---

# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
# DELETE FROM Users WHERE email='ted@umich.edu'
# UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'
# SELECT * FROM Users ORDER BY email


# --- Example 3 ----
print('--- Example 3 ---')

import sqlite3              # import the library

conn = sqlite3.connect('emaildb.sqlite')        # connection with database which check access to the file
cur = conn.cursor()                             # cursor is like a handle (not quite as simple as a handle)




# ___ Complex Data Models and  Relationships ___