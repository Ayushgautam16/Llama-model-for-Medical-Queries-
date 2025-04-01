# import os
# from pathlib import Path
# import logging 

# logging.basicConfig(level=logging.INFO, format ='[%(asctime)s]:%(message)s:')

# "ye aapka kaam asaan kar degga taaki aapko har forlder or files na banai padey"
# list_of_files = [
    # "src/_init_.py",  
    # # its the constructor file
    # "src/helper_.py",
    # "src/prompt_.py",
    # ".env",
    # it basically gives the functionality 
    "requirements>txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
,
]

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
   " test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")