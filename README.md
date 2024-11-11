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
