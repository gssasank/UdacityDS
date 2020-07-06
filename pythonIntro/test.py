def find_files(suffix, path):
    """
      Find all files beneath path with file name suffix.
      Note that a path may contain further subdirectories
      and those subdirectories may also contain further subdirectories.
      There are no limit to the depth of the subdirectories can be.
      Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system
      Returns:
         a list of paths
    """
    import os
    # use set to avoid repeating same name
    file_list = set()

    def helper(suffix, path):
        if suffix == "" or suffix is None:
            # suffix is empty
            return 0

        elif path == "" or path is None:
            # path name is emty
            return 1

        len_suffix = len(suffix)

        if not os.path.isdir(path):
            # dir not found
            return 2

        for file in os.listdir(path):

            # .DS_Store is a path on my mac which I don't know what it is
            if not file == ".DS_Store":
                # add only file which ends with given suffix
                if file[-len_suffix:] == suffix:
                    file_list.add(os.path.join(path, file))

                # recursively search
                helper(suffix, os.path.join(path, file))

        if len(file_list) == 0:
            # suffix not found
            return 3

        # sort the file list
        return sorted(list(file_list))

    files = helper(suffix, path)

    if files == 0:
        print("invalid suffix!")

    elif files == 1:
        print("invalid path name!")

    elif files == 2:
        print("Directory is not found!")

    elif files == 3:
        print("Could not found any files with given suffix!")

    else:
        for file in files:
            print(file)


print("-----------")
find_files(".c", "./")
print("-----------")
find_files("", "./")
print("-----------")
find_files(".h", "./")
print("-----------")
find_files(".docx", "./")