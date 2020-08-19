


## Installation

Navigate to [python.org](https://www.python.org/downloads/) to install Python 3+.

Navigate to [git-scm.com](https://git-scm.com/book/en/v1/Getting-Started-Installing-Git) to install Git.

Open a terminal window and type the below command to clone the GitHub QApp repo.

With the terminal window open, type the below command to install all of the dependencies.

```bash
pip3 install -r requirements.txt
```

## Create and IBM Q Experience Account

Navigate to [quantum-computing.ibm.com](https://quantum-computing.ibm.com/) and create a new account.

Navigate to [quantum-computing.ibm.com/account](https://quantum-computing.ibm.com/account) and click the 'Copy token' button in blue to obtain your API.  Open up a text editor and paste in the token temporarily.

Open a terminal window and type the below command to setup your API key with your software.  Make sure you replace the 'MY_API_TOKEN' below with your API key you have stored in your text editor.  Be sure to paste the API key between the single quotes as shown below.

```python
python3
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> quit()
```
##Import jquery,css, bootstrap and set image repo for web page access(can be in seprate static folder)
## Run Application

With the terminal window open, type the below command to run your qapp.

```bash
python3 app.py
```

Navigate to [localhost:5000](http://localhost:5000) to launch your qapp in your default web browser.


## Thanks
