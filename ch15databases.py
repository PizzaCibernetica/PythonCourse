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
# -  HSQL, SQLite, Postgres, ... 
