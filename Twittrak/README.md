These are the instructions to run our project.


First, the operator should download the relevant files that we submitted to the project assignment. After this, the operator should import the files to their choice of software to run python code (we chose to use vs code). Next, the operator should open the integrated terminal and ensure that their codespace is up to date. The operator should also ensure that the proper packages are imported. In order to install the proper packages, the user should execute the following lines in their terminal:
pip install numpy (this will install numpy)
pip install pandas (this will install pandas, a data science package)
pip install sklearn (this will install sklearn, a machine learning package)
pip install requests (this will install requests)
pip install pytz (this will install pytz)
pip install tweepy (this will install tweepy)

In addition the operator should make sure that they have downloaeded the os and json files.

Once the operator has ensured that the proper packages and files are present, then they should run the code by executing "flask run" for app.py. This will execute the html code and generate the webpage. If successful, the operator should then follow the link to the generated webpage. 

On the webpage, the operator should see a text input box and a submit button. The operator should input the username of a twitter user who they think may impact the price of SPY. Then, the webpage should display text that tells the operator the predicted change in price and the predicted new price in five minutes. If the operator inputs an invalid twitter username, they will be redirected back to the main page, where they can input a valid twitter username. 
