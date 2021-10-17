
# this file is made to store our data so that when we run the program agn it lists it out
import os.path


def load(name):
    """
    this method will create and load a new journal.
    :param name: base name of the journal to be loaded.

    :return: a new journal data structure with the file data.
    """
    data = []
    filename = get_full_path_name(name)

    if os.path.exists(filename):
        with open(filename) as filestream2:
            for entry in filestream2.readlines():
                data.append(entry.rstrip())

    return(data)



def save(name, journal_data):
    filename = get_full_path_name(name)
    print(".... saving to: {}".format(filename))

    #filestream =  open(filename, "w") #using while loop so that in case error comes then also the file is closed
    with open(filename, "w") as filestream:

        for entry in journal_data:
            filestream.write(entry + "\n")

    #filestream.close()


def get_full_path_name(name): # from refractor we did extract method
    filename = os.path.abspath(os.path.join(".\\journals\\" + name + ".jrl"))
    return filename


def add_entry(text, jounal_data):
    jounal_data.append(text)
