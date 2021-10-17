import journal
# prevent writing from journal import *, as different modules can have same methods

def main():
    print_header()
    run_event_loop()





def print_header():
    print("-----------------------------")
    print("      JOURNAL APP            ")
    print("-----------------------------")

def run_event_loop():
    print("What you want to do in journal?")

#define cmd
    cmd = "EMPTY" #to exit when not passing any input n pressing only enter too..

    journal_name = "default"
    journal_data = journal.load(journal_name)

# to make it iterable use while loop:
    while cmd != "x" and cmd:
        cmd = input("[l]ist entries, [a]dd entries, e[x]it:")
        cmd = cmd.lower().strip()  # so that to understand space before letters

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print( "i don't understand '{}'." .format(cmd))

    print(" done ")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("my journal entries: ")
    entries = reversed(data)
    for idx,entry in enumerate(entries):
        print("* [{}], {}" .format(idx+1, entry)) # +1 for correct indexing


def add_entry(journal_data):
    text = input(" type today's entry, press <enter> to exit: ")
    journal.add_entry(text, journal_data)
    # data.append(text)

print("__file__ " + __file__)
print("__name__ " + __name__)

if __name__ == "__main__":
    main()




main()