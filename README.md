# AirBnB Clone - The Console & Web Static

## About
AirBnB clone is a replica of the AirBnB website. This part of the project entails building instances that will be later used to create a dynamic website. It focuses on developing:
* A console that will facilitate the creation, updating and deletion of objects.
* A static web design of AirBnB

## **The Console:**
It is a command line interpreter for creating, deleting, updating and printing instances It allows interaction with BaseModel class objects and objects of its subclasses. It is useful in managing backend operation of AirBnB website

### **Console commands:**

* **help:** displays brief summary on console commands 
```
Synopsis: help [command]
Examples:
$ help
$ help create
```

* **create:** creates new objects
```
Synopsis: create <class name> or <class name>.create()
Examples:
$ create BaseModel
$ BaseModel.create()
```

* **show:** displays an instance of a specific class
```
Synopsis: show <class name> <id> or <class name>.show("id")
Examples:
$ show BaseModel 1234
$ BaseModel.show("1234")
```

* **destroy:** deletes an existing object
```
Synopsis: destroy <class name> <id> or <class name>.destroy("id")
Examples:
$ destroy BaseModel 1234
$ BaseModel.destroy("1234")
```

* **all:** prints all instances of a specific class or all instances available
```
Synopsis: all [class name] or <class name>.all()
Examples:
$ all
$ all User
$ User.all()
```

* **count:** counts objects belonging to a specific class
```
Synopsis: count <class_name> or <class name>.count()
Examples:
$ count User
$ User.count()
```

* **update:** updates attributes of an oject
```
Synopsis: update <class_name> <id> <attribute_name> "<attribute_value>" or
	  <class name>.update("id", "attribute_name", "attribute value") or 
	  <class name>.update("id", dictionary)
Examples:
$ update User 1234 first_name "John"
$ User.update("1234", "first_name", "Doe)
$ User.update("1234", {'first_name': "John", last_name = "Doe"})
```

* **EOF:** exit the console
```
Synopsis: EOF or ctrl + D
Examples:
$ EOF
```

* **quit:** exit the console
```
Synopsis: quit
Examples:
$ quit
```

## **Web Static**
AirBnB static website

## Contributors
<details>
<summary>Duncan Ngugi</summary>

[Github](https://github.com/ngugimuchangi)

</details>
<details>
<summary>Samuel Ekati</summary>

[Github](https://github.com/Samuthe)

</details>
