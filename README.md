# HBNB - The Console</h1>

This repository contains the initial stage of a student project to build a clone of the AirBnB website.

This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage.

Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

## Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](./AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](./tests/) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](./models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](./models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](./models/engine/file_storage.py), [/models/__init __.py](./models/__init__.py), [/models/base_model.py](./models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](./console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) [/models/user.py](./models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](./models/user.py) [/models/place.py](./models/place.py) [/models/city.py](./models/city.py) [/models/amenity.py](./models/amenity.py) [/models/state.py](./models/state.py) [/models/review.py](./models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |

---

## General Use

- First clone this repository.

- Once the repository is cloned locate the "console.py" file and run it as follows:

``` sh
/AirBnB_clone_v2$ ./console.py
```

- When this command is run the following prompt should appear:

``` sh
(hbnb)
```

- This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

### Commands

- create - Creates an instance based on given class

- destroy - Destroys an object based on class and UUID

- show - Shows an object based on class and UUID

- all - Shows all objects the program has access to, or all objects of a given class

- update - Updates existing attributes an object based on class name and UUID

- quit - Exits the program (EOF will as well)

### Alternative Syntax

Alternative syntax is implemented for the following commands:

- all - Shows all objects the program has access to, or all objects of a given class

- count - Return number of object instances by class

- show - Shows an object based on class and UUID

- destroy - Destroys an object based on class and UUID

- update - Updates existing attributes an object based on class name and UUID

---

## Examples

### Primary Command Syntax

#### Example 0: Create an object

To :  
create <class_name>

``` sh
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```

#### Example 1: Show an object

Usage:  
show <class_name> <instance_id>

``` sh
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```

#### Example 2: Destroy an object

Usage:  
destroy <class_name> <instance_id>

``` sh
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```

#### Example 3: Update an object

Usage:  
update <class_name> <instance_id>

``` sh
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```

### Alternative Syntax Examples

#### Example 0: Show all User objects

Usage:  
<class_name>.all()

``` sh
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 1: Destroy a User

Usage:  
<class_name>.destroy(<instance_id>)

``` sh
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 2: Update User (by attribute)

Usage:  
<class_name>.update(<instance_id>, <attribute_name>, <attribute_value>)

``` sh
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

#### Example 3: Update User (by dictionary)

Usage:  
<class_name>.update(<instance_id>, <_dict_>)

``` sh
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
