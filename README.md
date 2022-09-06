# AirBnB clone - The console

## About
AirBnB clone is a replica of the AirBnB website. This part of the project entails building instances that will be later used to create a dynamic website. It focuses on the backend operations, particularly developing a console that will facilitate the creation, updating and deletion of objects.

### **The Console:**
is a command line interpreter for creating, deleting, updating and printing instances It allows interaction with BaseModel class objects and objects of its subclasses. It is useful in managing backend operation of AirBnB website
#### **Console commands:**
* create 
	Syntax: `create <class name>` or `<class.name>.create()`
```	
$ create BaseModel
$ BaseModel.create()
```
* show
```	
$ show BaseModel 1234
$ BaseModel.show(1234)
```
* destroy
```
$ destroy BaseModel 1234
$ BaseModel.destroy(1234)
```
* all 
```
$ all
$ all User
$ User.all
```

* count
```
	$ count User
	$ User.count()
```

* update
```
	$ update User 1234 first_name "John"
	$ User.update("1234", "first_name", "Doe)
	$ User.update("1234", {'first_name': "John", last_name = "Doe" )
```
