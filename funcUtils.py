import MenuApplication


def append_file(self):
    return "a"


def overwrite_file(self):
    return "w"


def return_back(self):
    return MenuApplication.Menu()


class funcUtils():
    def __init__(self):
        self.a = a

    def sel_opt_save(obj):
        switch_save_file = {
            1: append_file,
            2: overwrite_file,
            3: return_back
        }
        return switch_save_file.get(obj, "Nothing")