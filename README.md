# D4-DVC
# This is just to test out Quilt D4 and DVC for managing remote data stores (on MacOS)
# 
# SET UP VENV
# python3 -m venv env
# source env/bin/activate
# 
# INSTALLATIONS
# pip install quilt3[pyarrow]
# conda install -c conda-forge quilt3
# brew install dvc
# pip install ipython
# 
# GET INITAL LOCAL DATA
# >> ipython
# >> import get_data_local as dt
# >> fruits, veggies = dt.get_data(dt.filename1, dt.filename2)
#   OUT: (['pear',
#          'plum',
#          'peach',
#          'blueberry',
#          'strawberry',
#          'apple',
#          'mango',
#          'cantalope',
#          'honeydew'],
#         ['broccoli', 'asparagus', 'cucumber'])
# 
# MAKE PACKAGE
# >> import get_quilt3 as q3
# >> p = q3.create_package()
# 
# EDIT PACKAGE GLOBAL METADATA
# >> p.meta
# >> q3.add_metadata_package(p)
#   OUT: enter key-value pair for global package metadata separated by a comma. (EX: type,food) ~~To exit enter "x"~~
#   IN: type,food
# >> p.meta
# 
# DELETE FILE
# >> p
#   OUT: (local Package)
#          └─data/
#             └─fav_fruit.csv
#             └─fav_veggies.csv
# >> q3.delete_data(p)
#   OUT: enter name of file you would like to delete 
#   IN: fav_fruits.csv
# >> p
#   OUT: (local Package)
#          └─data/
#             └─fav_veggies.csv