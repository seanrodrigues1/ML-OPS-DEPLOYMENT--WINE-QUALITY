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

git push  origin main ( git push -u origin main -f if that does not work )

9. create get_data.py file (which enables us to acces data through command line by using python src/get_data )
   this file also contains get_data() and read_params() which we require in the load_data.py file we create in the next step

10. create the load_data.py file which loads data in the data/raw folder.To load data in the
   raw folder, type - python src/load_data  ,note here again we do not have to provide the config file path (ie.config file= params file path )as an argument since we already specified it in the default.
   note: we can automatically load the data by writing the stages in the dvc.yaml and typing dvc repro in the command line, this will execute the command present in the dvc.yaml and automatically load the data.(we will do this in the next steps instead of using the cmd manually)
   Thus we add in the stage load_data and its cmd code, dependencies and output as shown below
   

  load_data:
    cmd: python src/load_data.py --config=params.yaml
    deps:
    - src/get_data.py
    - src/load_data.py
    - data_given/winequality.csv
    outs:
    - data/raw/winequality.csv

   note: after typing "dvc repro" all file versions will be updated in the dvc.lock file

11. create split_data.py to create our train test split and save them in data/processed folder. 
    We add the split_data stage in the dvc.yaml,
    then type  "dvc repro" on the command line
    which will execute all code in that stage and actually perform the train test split and save them 

12. After each stage, dont forget to push to remote repository(ie. github in my case) using :git add . ,git commit -m "stage 2 complete" and git push origin main 

13. Create train and evaluate file where we train the model using Elastic net using parameters alpha and l1 ratio, use performance metrics like MAE RSME,and save the model.
    Create a folder report and add params.json and scores.json 
   - We will save our parameters in the report/params.json file .
   - We will save our metrics in report/scores.json file.
   - We will save our model in the saved_models folder 

   Note: dvc metrics show  : this will display the metrics values stored in report/scores
         dvc metrics diff  : this will display the current metrics values and values which have been used in the past
