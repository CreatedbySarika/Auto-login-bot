# AUTO LOGIN BOT #


## Features ##

## Installation ##

### Virtual environment ###

### How to setup the virtual environment inside the project? ###
**create python virtual environment**\

<code>python -m venv #name of the virtual environment#</code>\

<code>python -m venv venv</code>

**Activate the Virtual Environment**

<code>.\venv\Scripts\activate</code>

### How to Download in virtual Environment? ###

often times even after being inside venv the modules are install inside the global environment.to make sure the modules are installed in venv

<code>python -m pip install # module name # </code>

<code>python -m pip install selenium </code>

**verify install in venv**
<code>python -m pip show #module name#</code>

<code>python -m pip show selenium </code>

The out put location should **Location: C:\Users\hp\Documents\GitHub\Auto-login-bot\venv\Lib\site-packages**

if the output is **AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages** then the module is installed in the global environment




