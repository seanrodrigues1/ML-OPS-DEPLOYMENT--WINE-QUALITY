import os

dirs =[os.path.join("data","raw"),        # or simply dirs= [data/raw,notebooks,..]
       os.path.join("data","processed"),  # / for linux \ for windows
       "notebooks",        # hence we use use os.path.join which uses the right syntax based on yoru os
       "saved_models",
       "src"]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass