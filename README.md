# D4-DVC
###  This is just to test out Quilt D4 and DVC for managing remote data stores (on MacOS)
 
# SET UP VENV
 python3 -m venv env
 source env/bin/activate
 
# INSTALLATIONS
 conda install -c conda-forge quilt3
 brew install dvc
 pip install ipython
 
# GET INITAL LOCAL DATA
#### >> ipython
#### >> import get_data_local as dt
#### >> fruits, veggies = dt.get_data(dt.filename1, dt.filename2)
####   OUT: (['pear',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'plum',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'peach',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'blueberry',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'strawberry',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'apple',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'mango',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'cantalope',
####          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'honeydew'],
####         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['broccoli', 'asparagus', 'cucumber'])
 
# MAKE PACKAGE
#### >> import get_quilt3 as q3
#### >> p = q3.create_package()
 
# EDIT PACKAGE GLOBAL METADATA
#### >> p.meta
#### >> q3.add_metadata_package(p)
####   OUT: enter key-value pair for global package metadata separated by a comma. (EX: ype,food) To exit enter "x"
####   IN: type,food
#### >> p.meta
 
# DELETE FILE
#### >> p
####   OUT: (local Package)
####          └─data/
####             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─fav_fruit.csv
####             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─fav_veggies.csv
#### >> q3.delete_data(p)
####   OUT: enter name of file you would like to delete 
####   IN: fav_fruits.csv
#### >> p
####   OUT: (local Package)
####          └─data/
####             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─fav_veggies.csv