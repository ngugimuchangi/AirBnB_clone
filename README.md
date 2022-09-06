# AirBnB clone - The console

## About
AirBnB clone is a replica of the AirBnB website. This part of the project entails building instances that will be later used to create a dynamic website. It focuses on the backend operations, particularly developing a console that will facilitate the creation, updating and deletion of objects.

### **The Console:**
is a command line interpreter for creating, deleting, updating and printing instances It allows interaction with BaseModel class objects and objects of its subclasses. It is useful in managing backend operation of AirBnB website
#### **Console commands:**
* **create:** creates new objects

Syntax: `create <class name>` or `<class name>.create()`
```	
$ create BaseModel
$ BaseModel.create()
```
* **show:** displays an instance of a specific class

Syntax: `show <class name> <id>` or `<class name>.show("id")`
```	
$ show BaseModel 1234
$ BaseModel.show("1234")
```
* **destroy:** deletes an existing object
Syntax: `destroy <class name> <id>` or `<class name>.destroy("id")`
```
$ destroy BaseModel 1234
$ BaseModel.destroy(1234)
```
* **all:** Print all instances of a specific class or all instances available

Syntax: `all` or `all <class name>` or `<class name>.all()`
```
$ all
$ all User
$ User.all
```

* **count:** count objects belonging to a specific class

Syntax: `count <class_name>` or `<class name>.count()`
```
$ count User
$ User.count()
```

* **update:** updates attributes of an oject

```
$ update User 1234 first_name "John"
$ User.update("1234", "first_name", "Doe)
$ User.update("1234", {'first_name': "John", last_name = "Doe" )
```
