<h1> SASE ASU Chapter Website </h1>
<h4> This is the site for the SASE ASU website. It uses a Python framework, Django along with HTML, CSS and JS. Along with being a landing page for SASE ASU. It is also used for signing in students and getting their student info.</h4>
<hr>
<h3> Getting the repository started </h3>
<h5>Requirements</h5>
<ol>
  <li>Python version 3.7.9 or up</li>
  <li>Github</li>
  <li>A working knowledge of CLI commands and Git Commands</li>
</ol>
<h6>Steps to get started working on this repository</h6>


```bash
# Clone the repository
git clone https://github.com/subbel/SASEASU.git

#Access it
cd SASEASU

#Create a virtual environment for testing
python -m venv venv

#(Make sure you use venv as the vurtual env. name, otherwise make sure you're virtual environment is added to .gitignore)

#Activate the virtual environment
. venv/Scripts/activate
#In case you are using Mac you can try this command
. venv/bin/activate

#Intall dependencies
pip install -r requirements.txt

#Run the app
python manage.py runserver

#(You can use python3 for your commands if that is what is required)
```

# Required Knowledge
Basics of Python knowledge required to read this
- OOP (Making models, functions and function calls)
- Programming concepts (Recursion, loops, if-else statements)

Most of the Python that the SASEASU website uses as of 2025 is based off of a framework called Django. If you intend to use it you need to install it using pip and ideally in a venv.

We will be using **Python 3.13.0** as the python version.

---
# Command Prompt
Command Prompt or cmd or terminal(in mac) is an area you will be using most often during this and is used to run code, generally without the use of a GUI. The following are some of the commands you will be using a lot so familiarize yourself with them
``` bash
#used to go inside a directory/folder
cd DirectoryName

#used to make a new directory
mkdir DirectoryName

#used to open python
python

#used to run library module as a script (terminates option list)
python -m command
```

**To continue with the rest below make sure you have python installed**

---
# venv
A venv refers to a virtual environment. To prevent further confusion venv will refer to both the virtual environment and the name of the virtual environment. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available. This is done to isolate the packages being used in the project.

Here is how you create and activate a venv
```bash
#Create a folder (optional if you already have a folder)
mkdir practical

#Go inside the folder
cd practical

#Create the venv
python -m venv venv

#This will create a virtual environment called venv
```

At this point you should see a file called venv. This will have 3 folders called Include, Lib and Scripts/bin(if you have a mac).

But this just means that it is present for use. To actually use and do work inside this venv we need to activate it

```bash
#The following are variations of how you could activate the venv

venv/Scripts/activate

./venv/Scripts/activate

.\venv\Scripts\activate

.\/venv/Scripts/activate

#If you are using a mac you will replace Scripts with bin
```

This will make your cmd have a _(venv)_ next to it to show it has been activated. You can simply type
```
deactivate
```
to deactivate it. You will need to activate this venv every time you want to work inside of it, otherwise you will be using your own python packages.

---
# Django

Please watch or read wither on of these tutorials to learn about django. I will provide a refresher on Django with the assumption that you have already completed either on of these tutorials

[Django Tutorial : Written](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
(You only need to finish until part 5)

[Django Video Tutorial]([https://youtu.be/F5mRW0jo-U4?si=bXz8dHuU5z4_slKM](https://youtu.be/F5mRW0jo-U4?si=bXz8dHuU5z4_slKM "https://youtu.be/F5mRW0jo-U4?si=bXz8dHuU5z4_slKM"))
(Watch the whole thing)

---
# GitHub
