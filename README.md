# django-elszabadul
Django gets released


--GREAT SOURCE--

"https://www.youtube.com/embed/videoseries?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK"


........................

--CREATING NEW PROJECT--

........................


django-admin startproject BLACKPERSON

........................

--USEFUL PIP COMMANDS--

........................


'''UNINSTALLING CURRENT MODULES'''

pip freeze > requirements.txt #this can be any can of text file, but we usually use requirements.txt#

pip uninstall -r requirements.txt -y

'''INSTALLING PIP MODULES FROM A TEXT FILE'''

pip install -r requirements.txt

........................

--USING PIPENV--

........................

sudo apt install python3-pyvenv

python3 -m venv #random name#

........................

--RUN THE SERVER--

........................

cd BLACKPERSON

python manage.py runserver

'''CREATE YOUR APP'''

python manage.py startapp

........................

--USEFUL GIT COMMANDS--

........................

git init

'''LIST LOCAL BRANCES'''

git branch

'''DELETE LOCAL BRANCH'''

git branch -d #Insert your local branch here#

'''DELETE REMOTE BRANCH'''

git push origin --delete #Insert your remote branch here#

'''CREATE NEW LOCAL BRANCH'''

git checkout -b #Enter your test branch from where the pull request can be merged to master#

'''Test branches are being deleted automatically after the merge'''
'''Merge requires review from administrators or from other contributors'''

'''SWITCH LOCAL BRANCH'''

git checkout <Enter your existing branch, just in case if you want to switch>
