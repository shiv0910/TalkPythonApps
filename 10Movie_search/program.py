import movie_svc
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print("----------------------------------------------------")
    print("                MOVIE SEARCH APP")
    print("----------------------------------------------------")
    print()

def search_event_loop():
    search = "ONCE_THROUGH_THE_LOOP"

    while search != "x":
        try:
            search = input("Movie search (x to exit): ")
            if search != "x":
                results = movie_svc.find_movies(search) # using the movie_svc file here
                print(f"Found {len(results)}.")
                for r in results:
                    print(f" {r.year} -- {r.title}")
                    print()
        except requests.exceptions.ConnectionError:
            print(f"Error: Your network is down")
        except ValueError:
            print("Error: Search text is required")
        except Exception as x:
            print(f"Unexpectewd error. Details: {x}")



    print("exiting..")

if __name__ == '__main__':
    main()


