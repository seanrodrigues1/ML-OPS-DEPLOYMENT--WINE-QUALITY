1. create new environment  : conda create -n wine_quality
2. create requirements.txt file

3. create folder structure : we used template.py to create the folder structure,
   but it can be created manually too

4. initialize an empty git repository :
   git init

5. initialize a DVC(data version control) project for version control of files
   dvc init

# The dvc add command is analogous to git add, in that it makes DVC aware of the target data,
   in order to start versioning it. It creates a .dvc file to track the added data.

6. add source file to be be tracked by dvc , this source file is present in the data given folder
dvc add data_given\winequality.csv

7. git add .  , then git commit -m "first commit   # we add our files to our empty repo with versioning

8. create a new repository on github and connect to it, after it connects 
   all files in the directory can be pushed to that repo. Note: you have to 
   intitialize a git repo first always using git init 

- git remote add origin <repo link on github after creating it>

git remote add origin https://github.com/seanrodrigues1/ML-OPS-DEPLOYMENT--WINE-QUALITY

9.