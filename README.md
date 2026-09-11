# AUTO LOGIN BOT #


## Features ##

**🔐 User Authentication**
Create an account and log in to the application.
Securely manage personal data.

**💾 Credential Storage**
Save website URLs, usernames, and passwords.
Store multiple accounts per user.

**🚀 Automatic Login :**
    Automatically fills login forms using Selenium.
Submits credentials with a single click.

**🌐 Multi-Website Support :**
    Store credentials for different websites.
Manage all saved logins from one dashboard.

**🔍 Credential Search :**
    Search saved accounts by website name or URL.

**✏️ Edit Saved Logins :**
    Update usernames, passwords, or URLs.

**🗑️ Delete Saved Logins :**
    Remove outdated or unused login entries.
Security Features

**🔒 Password Encryption :**
    Encrypt passwords before storing them in the database.

**👤 User Isolation :**
    Users can only access their own saved credentials.

**🔑 Secure Login Session :**
    Validate user identity before revealing sensitive information.
## Installation ##
**clone the website**
<code>git@github.com:CreatedbySarika/Auto-login-bot.git</code>

**navigate to the folder**\
```<code>python run.py </code>```

## Virtual environment ##

### How to setup the virtual environment inside the project? ###
**create python virtual environment**\

<code>python -m venv #name of the virtual environment#</code>\

<code>python -m venv venv</code>

**Activate the Virtual Environment**

<code>.\venv\Scripts\activate</code>

### How to Setup virtual Environment? ###

often times even after being inside venv the modules are install inside the global environment.to make sure the modules are installed in venv

<code>python -m pip install # module name # </code>

<code>python -m pip install selenium </code>

**verify install in venv**

<code>python -m pip show #module name#</code>

<code>python -m pip show selenium </code>

The out put location should 

<code>Location: C:\Users\hp\Documents\GitHub\Auto-login-bot\venv\Lib\site-packages </code>

if the output is 

<code>AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages</code>

then the module is installed in the global environment




