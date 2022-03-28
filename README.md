# Contact-Management-System
Contact Management System in Python

****Requirements and Installation****

Use pip3 instead of pip for Linux and Mac.

Install PyMySQL
☛pip install PyMySQL

Install Tkinter
☛pip install tk



****Install MySQL server****



****Create a Database and a Table****

Create a database with this name: "contact_management"
☛create database contact_management;

Create a table "contact_register" under the "contact_management" database.
☛create table contact_register(
	f_name VARCHAR(50) NOT NULL,
	l_name VARCHAR(50) NOT NULL,
	address VARCHAR(200) NOT NULL,
	contact VARCHAR(15) NOT NULL,
	email VARCHAR(100) NOT NULL,
	PRIMARY KEY ( contact )
);
