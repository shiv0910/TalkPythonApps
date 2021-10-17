import os.path

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("sorry, cannot search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("we cannot search anything!")
        return

def print_header():
    print("----------------------------------")
    print("          FILE SEARCH APP")
    print("----------------------------------")

def get_folder_from_user():
    folder = input(" what folder you want to search? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input(" what are you searching for [single phrases only]?" )
    return text.lower()

def search_folders(folder, text):

    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue

        matches = search_file(full_item, text)
        all_matches.extend(matches)
    return all_matches

def search_file(filename, search_text):
    matches = []
    with open(filename, "r", encoding= "utf-8") as fin:  # ??????????????????

        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = searchresult(line = line_number, file = filename, text = line)
                matches.append(m)

        return matches








main()

