# Quilt3 to manage packages and metadata
import quilt3

# quilt3: create package & add data
def create_package():
    p = quilt3.Package()
    p.set_dir("data/", "data/")
    return p

# quilt3: edit package
def edit_package(pkg):
    pass

# quilt3: delete package
def delete_fruits(pkg):
    pkg.delete("data/fav_fruits.csv")
    return

# quilt3: add data
def add_fruits(pkg):
    pkg.set("fav_fruits.csv", "data/fav_fruits.csv")
    pass

# quilt3: add metadata
def add_metadata_package(pkg):
    # IGNORE USER INPUT
    # userIn = input('enter key-value pair for global package metadata separated by a comma. (EX: type,food) ~~To exit enter "x"~~  ')
    # userSplit = userIn.split(",")
    # if len(userSplit) != 2:
    #     print("Error: Invalid Input. Package not updated.  ")
    #     return
    pkg.set_meta({"type", "food"})
    return

def add_metadata_data(pkg):
    pass

# quilt3: search by metadata
def search_metadata():
    pass
