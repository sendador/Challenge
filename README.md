# Table of contents
- [Chapter 1](#chapter1)  
- [Chapter 2](#chapter2)
- [Chapter 3](#chapter3)



# Chapter1

Usage:

To start a script just simple type:
<pre>*your dir* python chapter_1.py</pre>

In the console you will have to input three values:
- pax_count -- number of passengers riding in the car (including the driver),
- car_mass -- mass of the empty car (in kg),
- gear_count -- number of gears.

and then you will see total mass of the car

To run tests:
<pre>*your dir* python chapter_1_tests.py</pre>

# Chapter2

To start a script just simple type:
<pre>*your dir* python chapter_2.py positional_arg --optional_arg1 "example" --positional_arg2 "example"</pre>

Where args can be:

<pre>
positional arguments:
  operation             Which operation do you want? There is "add", "update", "remove" and "list"

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name of your task
  -dead DEADLINE, --deadline DEADLINE
                        Deadline of your task. Date should be looks like: YYYY-MM-DD
  -desc DESCRIPTION, --description DESCRIPTION
                        Description of your task
  --hash HASH           Input your task hash to update or delete
  --all                 Used with list operation. It display all tasks
  --today               Used with list operation. It display task for today</pre>


For example:

<pre>*your dir* python chapter_2.py add --name "Cleaning" --deadline "2020-03-17" --description "Clean living room and the kitchen"</pre>

After that there will be a database created and first task. Task is identyfied by its hashcode. You can see the hashcode when you will display list of all tasks.

<pre>*your dir* python chapter_2.py --all (for all tasks) or --today (just for today)</pre>


  # Chapter3

To start a script just simple type:
<pre>*your dir* python chapter_3.py</pre>

Range of the number was strictly specified but if you want change something just edit line 37
<pre>number_list = numbers_range(your_start_number, your_end_number)</pre>

