from collections import deque
import random

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first(name):
    search_queue = deque()
    search_queue += graph[name]
    
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False


def person_is_seller(person):
    return bool(random.getrandbits(1))

if __name__ == "__main__":
    breadth_first("you")