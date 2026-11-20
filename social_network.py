# Social Network Connection and Recommendation Analysis

# Creating an empty graph
social_network = {}

# Adding users
social_network["Sonu"] = []
social_network["Rahul"] = []
social_network["Aman"] = []
social_network["Priya"] = []
social_network["Neha"] = []

# Displaying users
print("Social Network Users:")
print(social_network)

# Function to connect two users

def add_connection(user1, user2):

    if user1 in social_network and user2 in social_network:

        social_network[user1].append(user2)
        social_network[user2].append(user1)

        print(user1, "and", user2, "are now connected!")

    else:
        print("User not found!")


# Creating connections
add_connection("Sonu", "Rahul")
add_connection("Sonu", "Aman")
add_connection("Rahul", "Priya")
add_connection("Aman", "Neha")

# Function to display all users and their friends

def display_network():

    print("\n--- Social Network Connections ---")

    for user in social_network:
        print(user, ":", social_network[user])


# Calling the function
display_network()

# Function to find mutual friends

def mutual_friends(user1, user2):

    if user1 in social_network and user2 in social_network:

        friends1 = social_network[user1]
        friends2 = social_network[user2]

        common = []

        for friend in friends1:
            if friend in friends2:
                common.append(friend)

        print("Mutual Friends:", common)

    else:
        print("User not found!")


# Testing mutual friends
mutual_friends("Sonu", "Priya")

# BFS - Find shortest connection path

def bfs_shortest_path(start, end):

    if start not in social_network or end not in social_network:
        print("User not found!")
        return

    queue = [[start]]
    visited = set()

    while queue:

        path = queue.pop(0)
        current_user = path[-1]

        if current_user == end:
            print("Shortest Path:", path)
            return

        if current_user not in visited:
            visited.add(current_user)

            for friend in social_network[current_user]:
                if friend not in visited:
                    new_path = path + [friend]
                    queue.append(new_path)

    print("No connection path found!")


# Testing BFS
bfs_shortest_path("Sonu", "Neha")

# DFS - Explore social network

def dfs(start):

    if start not in social_network:
        print("User not found!")
        return

    visited = set()

    def explore(user):

        if user not in visited:

            print(user, end=" ")
            visited.add(user)

            for friend in social_network[user]:
                if friend not in visited:
                    explore(friend)

    explore(start)
    print()


# Testing DFS
print("DFS Traversal:")
dfs("Sonu")

# MAIN MENU

while True:

    print("\n===== SOCIAL NETWORK ANALYSIS =====")

    print("1. Add User")
    print("2. Add Connection")
    print("3. Display Network")
    print("4. Find Mutual Friends")
    print("5. Find Shortest Path (BFS)")
    print("6. Explore Network (DFS)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("Enter user name: ")

        if user not in social_network:
            social_network[user] = []
            print("User added successfully!")
        else:
            print("User already exists!")

    elif choice == "2":
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        add_connection(user1, user2)

    elif choice == "3":
        display_network()

    elif choice == "4":
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        mutual_friends(user1, user2)

    elif choice == "5":
        start = input("Enter starting user: ")
        end = input("Enter destination user: ")
        bfs_shortest_path(start, end)

    elif choice == "6":
        start = input("Enter starting user: ")
        dfs(start)

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")