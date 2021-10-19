import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line, text")

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("sorry, cannot search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("we cannot search anything!")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        # print(m) { dont need this as it will give too much output }
        # print("_____________MATCH___________")
        # print("file: " + m.file)
        # print(f"line: {m.line}")
        # print("match: " + m.text.strip())
        # print()

    print(f"Found {match_count:,} matches")

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
    print(f"Searching {folder} for {text}")

    # all_matches = []

    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):

            # matches = search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #   yield m
            # yield from matches
            yield from search_folders(full_item, text)

        else:
            # matches = search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #    yield m
            yield from search_file(full_item, text)


    # return all_matches

def search_file(filename, search_text):
    # matches = []
    with open(filename, "r", encoding= "utf-8") as fin:  # ??????????????????

        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_number, file=filename, text=line)
                # matches.append(m)
                yield m    #generator method

        # return matches



if __name__ == '__main__':
    main()


