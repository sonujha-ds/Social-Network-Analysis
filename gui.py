import tkinter as tk
from tkinter import messagebox
import json
from tkinter import filedialog

# Social network graph
social_network = {}

# Main window
root = tk.Tk()
root.title("Social Network Analysis")
root.geometry("1200x850")
root.minsize(1000, 750)
root.configure(bg="#EAF0FF")

# Scrollable window
container = tk.Frame(root, bg="#EAF0FF")
container.pack(fill="both", expand=True)

canvas = tk.Canvas(
    container,
    bg="#EAF0FF",
    highlightthickness=0
)
scrollbar = tk.Scrollbar(
    container, orient="vertical", command=canvas.yview
)

scrollable_frame = tk.Frame(
    canvas,
    bg="#EAF0FF"
)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

window_id = canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="n",
    width=850
)

def center_content(event):
    canvas.coords(
        window_id,
        event.width / 2,
        0
    )

canvas.bind("<Configure>", center_content)


canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def on_mousewheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)), "units"
    )

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Heading
# Heading
heading = tk.Label(
    scrollable_frame,
    text="Social Network Analysis",
    font=("Arial", 30, "bold"),
    bg="#EAF0FF",
    fg="#263B80"
)
heading.pack(pady=(30, 10), anchor="center")

subtitle = tk.Label(
    scrollable_frame,
    text="Connection and Recommendation System",
    font=("Arial", 14),
    bg="#EAF0FF",
    fg="#64748B"
)
subtitle.pack(pady=(0, 25), anchor="center")

# Add User section
# Add User Section
add_user_label = tk.Label(
    scrollable_frame,
    text="Add New User",
    font=("Arial", 18, "bold"),
    bg="#EAF0FF",
    fg="#263B80"
)
add_user_label.pack(pady=(25, 12), anchor="center")

user_entry = tk.Entry(
    scrollable_frame,
    font=("Arial", 14),
    width=35,
    bd=1,
    relief="solid"
)
user_entry.pack(pady=8, anchor="center")

def add_user():
    user = user_entry.get().strip()

    if not user:
        messagebox.showwarning("Warning", "Enter a user name!")
    elif user in social_network:
        messagebox.showwarning("Warning", "User already exists!")
    else:
        social_network[user] = []
        messagebox.showinfo("Success", user + " added!")
        user_entry.delete(0, tk.END)

# Add User Button
add_user_btn = tk.Button(
    scrollable_frame,
    text="  +  Add User  ",
    bg="#2563EB",
    fg="white",
    font=("Arial", 13, "bold"),
    width=20,
    height=2,
    relief="flat",
    cursor="hand2",
    activebackground="#1D4ED8",
    activeforeground="white",
    command=add_user
)
add_user_btn.pack(pady=10, anchor="center")

# Add Connection Section
connection_heading = tk.Label(
    scrollable_frame,
    text="Add Connection",
    font=("Arial", 18, "bold"),
    bg="#EAF0FF",
    fg="#15803D"
)
connection_heading.pack(pady=(25, 15), anchor="center")

# First User
tk.Label(
    scrollable_frame,
    text="First User:",
    font=("Arial", 13),
    bg="#F2F5FA"
).pack(pady=5)

first_entry = tk.Entry(
    scrollable_frame,
    font=("Arial", 14),
    width=30
)
first_entry.pack(pady=5)

# Second User
tk.Label(
    scrollable_frame,
    text="Second User:",
    font=("Arial", 13),
    bg="#F2F5FA"
).pack(pady=5)

second_entry = tk.Entry(
    scrollable_frame,
    font=("Arial", 14),
    width=30
)
second_entry.pack(pady=5)

def add_connection():
    user1 = first_entry.get().strip()
    user2 = second_entry.get().strip()

    if user1 not in social_network or user2 not in social_network:
        messagebox.showerror("Error", "Both users must exist!")
    elif user1 == user2:
        messagebox.showwarning("Warning", "Cannot connect a user to themselves!")
    elif user2 in social_network[user1]:
        messagebox.showwarning("Warning", "Connection already exists!")
    else:
        social_network[user1].append(user2)
        social_network[user2].append(user1)

        messagebox.showinfo(
            "Success",
            user1 + " and " + user2 + " are connected!"
        )

        first_entry.delete(0, tk.END)
        second_entry.delete(0, tk.END)

tk.Button(
    scrollable_frame,
    text="Connect Users",
    bg="#16A34A",
    fg="white",
    font=("Arial", 13, "bold"),
    width=20,
    height=2,
    command=add_connection
).pack(pady=15)

# Display Network Function
def display_network():

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, "===== SOCIAL NETWORK =====\n\n")

    if not social_network:
        result_box.insert(tk.END, "No users found!")
        return

    for user, friends in social_network.items():
        result_box.insert(
            tk.END,
            user + " : " + str(friends) + "\n"
        )


# Network Details Heading
tk.Label(
    scrollable_frame,
    text="Network Details",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)


# Result Box
result_box = tk.Text(
    scrollable_frame,
    height=6,
    width=65,
    font=("Arial", 12),
    bg="white",
    fg="#1E293B",
    relief="solid",
    bd=1,
    wrap="word"
)
result_box.pack(pady=10)

# Display Network Button
tk.Button(
    scrollable_frame,
    text="Display Network",
    bg="#7C3AED",
    fg="white",
    font=("Arial", 12, "bold"),
    width=22,
    height=2,
    cursor="hand2",
    command=display_network
).pack(pady=12)

# Mutual Friends Function
def find_mutual_friends():

    user1 = mutual_user1.get().strip()
    user2 = mutual_user2.get().strip()

    result_box.delete("1.0", tk.END)

    if user1 not in social_network or user2 not in social_network:
        result_box.insert(tk.END, "User not found!")
        return

    common = set(social_network[user1]) & set(social_network[user2])

    if common:
        result_box.insert(tk.END, "Mutual Friends: " + str(list(common)))
    else:
        result_box.insert(tk.END, "No mutual friends found!")

# Friend Recommendation Function
def recommend_friends():
    user = recommend_entry.get().strip()

    recommend_result.delete("1.0", tk.END)

    if user not in social_network:
        recommend_result.insert(tk.END, "User not found!")
        return

    recommendations = {}

    for other_user in social_network:

        if other_user == user:
            continue

        if other_user in social_network[user]:
            continue

        mutual = set(social_network[user]) & set(social_network[other_user])

        if mutual:
            recommendations[other_user] = len(mutual)

    if recommendations:
        sorted_recommendations = sorted(
            recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )

        recommend_result.insert(tk.END, "Recommended Friends:\n\n")

        for friend, count in sorted_recommendations:
            recommend_result.insert(
                tk.END,
                f"{friend} - {count} mutual friends\n"
            )
    else:
        recommend_result.insert(
            tk.END, "No friend recommendations found!"
        )

# Mutual Friends Section
tk.Label(
    scrollable_frame,
    text="Find Mutual Friends",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)

mutual_user1 = tk.Entry(
    scrollable_frame,
    font=("Arial", 13),
    width=30
)
mutual_user1.pack(pady=6)

mutual_user2 = tk.Entry(
    scrollable_frame,
    font=("Arial", 13),
    width=30
)
mutual_user2.pack(pady=6)

tk.Button(
    scrollable_frame,
    text="Find Mutual Friends",
    bg="#EA580C",
    fg="white",
    command=find_mutual_friends
).pack(pady=10)

# BFS Shortest Path Function
def find_shortest_path():

    start = bfs_start.get().strip()
    end = bfs_end.get().strip()

    result_box.delete("1.0", tk.END)

    if start not in social_network or end not in social_network:
        result_box.insert(tk.END, "User not found!")
        return

    queue = [[start]]
    visited = {start}

    while queue:

        path = queue.pop(0)
        current = path[-1]

        if current == end:
            result_box.insert(
                tk.END,
                "Shortest Path: " + " -> ".join(path)
            )
            return

        for friend in social_network[current]:

            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])

    result_box.insert(tk.END, "No path found!")


# BFS Heading
tk.Label(
    scrollable_frame,
    text="Find Shortest Path (BFS)",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)

bfs_start = tk.Entry(scrollable_frame, font=("Arial", 11))
bfs_start.pack(pady=5)

bfs_end = tk.Entry(scrollable_frame, font=("Arial", 11))
bfs_end.pack(pady=5)

tk.Button(
    scrollable_frame,
    text="Find Shortest Path",
    bg="#0891B2",
    fg="white",
    command=find_shortest_path
).pack(pady=10)

# Remove User Function
def remove_user():
    user = remove_entry.get().strip()

    if user not in social_network:
        messagebox.showerror("Error", "User not found!")
        return

    for friend in social_network[user]:
        social_network[friend].remove(user)

    del social_network[user]

    messagebox.showinfo("Success", user + " removed successfully!")
    remove_entry.delete(0, tk.END)


# Remove User Section
tk.Label(
    scrollable_frame,
    text="Remove User",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)

remove_entry = tk.Entry(
    scrollable_frame,
    font=("Arial", 12),
    width=30
)
remove_entry.pack(pady=5)

tk.Button(
    scrollable_frame,
    text="Remove User",
    bg="#DC3545",
    fg="white",
    font=("Arial", 11, "bold"),
    command=remove_user
).pack(pady=10)

# Remove Connection Function
def remove_connection():
    user1 = remove_user1_entry.get().strip()
    user2 = remove_user2_entry.get().strip()

    if user1 not in social_network or user2 not in social_network:
        messagebox.showerror("Error", "Both users must exist!")
        return

    if user1 == user2:
        messagebox.showwarning("Warning", "Cannot disconnect same user!")
        return

    if user2 not in social_network[user1]:
        messagebox.showwarning("Warning", "Connection does not exist!")
        return

    social_network[user1].remove(user2)
    social_network[user2].remove(user1)

    messagebox.showinfo("Success", "Connection removed successfully!")

    remove_user1_entry.delete(0, tk.END)
    remove_user2_entry.delete(0, tk.END)


# Remove Connection Section
tk.Label(
    scrollable_frame,
    text="Remove Connection",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)

remove_user1_entry = tk.Entry(
    scrollable_frame, font=("Arial", 12), width=30
)
remove_user1_entry.pack(pady=5)

remove_user2_entry = tk.Entry(
    scrollable_frame, font=("Arial", 12), width=30
)
remove_user2_entry.pack(pady=5)

tk.Button(
    scrollable_frame,
    text="Remove Connection",
    bg="#DC3545",
    fg="white",
    command=remove_connection
).pack(pady=10)

# Network Statistics Function
def show_statistics():
    total_users = len(social_network)

    total_connections = sum(
        len(friends) for friends in social_network.values()
    ) // 2

    if total_users == 0:
        messagebox.showinfo("Statistics", "No users in network!")
        return

    average_friends = (total_connections * 2) / total_users

    most_connected = max(
        social_network,
        key=lambda user: len(social_network[user])
    )

    isolated_users = [
        user for user in social_network
        if len(social_network[user]) == 0
    ]

    stats_box.delete("1.0", tk.END)

    stats_box.insert(tk.END, "NETWORK STATISTICS\n")
    stats_box.insert(tk.END, "-----------------------------\n")
    stats_box.insert(tk.END, f"Total Users: {total_users}\n")
    stats_box.insert(tk.END, f"Total Connections: {total_connections}\n")
    stats_box.insert(tk.END, f"Average Friends: {average_friends:.2f}\n")
    stats_box.insert(tk.END, f"Most Connected User: {most_connected}\n")
    stats_box.insert(tk.END, f"Friends Count: {len(social_network[most_connected])}\n")
    stats_box.insert(tk.END, f"Users Without Connections: {len(isolated_users)}\n")
    stats_box.insert(tk.END, f"Isolated Users: {isolated_users}\n")


# Network Statistics Section
tk.Label(
    scrollable_frame,
    text="Network Statistics Dashboard",
    font=("Arial", 14, "bold"),
    bg="#F2F5FA"
).pack(pady=10)

stats_box = tk.Text(
    scrollable_frame,
    width=45,
    height=10,
    font=("Arial", 11),
    bd=1,
    relief="solid"
)
stats_box.pack(pady=8)

tk.Button(
    scrollable_frame,
    text="Show Network Statistics",
    bg="#6F42C1",
    fg="white",
    font=("Arial", 11, "bold"),
    command=show_statistics
).pack(pady=10)

# Save Network Function
def save_network():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "w") as file:
            json.dump(social_network, file, indent=4)

        messagebox.showinfo(
            "Success",
            "Network saved successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Load Network Function
def load_network():
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON Files", "*.json")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid network data!")

        new_network = {user: [] for user in data}

        for user, friends in data.items():
            if not isinstance(user, str) or not isinstance(friends, list):
                raise ValueError("Invalid network format!")

            for friend in friends:
                if friend not in data or not isinstance(friend, str):
                    raise ValueError("Invalid connection!")

                if friend != user and friend not in new_network[user]:
                    new_network[user].append(friend)

                if friend != user and user not in new_network[friend]:
                    new_network[friend].append(user)

        social_network.clear()
        social_network.update(new_network)

        messagebox.showinfo(
            "Success",
            "Network loaded successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Save Network Button
tk.Button(
    scrollable_frame,
    text="Save Network",
    bg="#198754",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22,
    command=save_network
).pack(pady=10)


# Load Network Button
tk.Button(
    scrollable_frame,
    text="Load Network",
    bg="#0D6EFD",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22,
    command=load_network
).pack(pady=10)

# Exit button
tk.Button(
    scrollable_frame, text="Exit Application",
    bg="#DC3545", fg="white",
    command=root.destroy
).pack(pady=15)

root.mainloop()