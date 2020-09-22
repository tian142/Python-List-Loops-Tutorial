songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1])
print(songs[0:2])

# update the first element
songs[0] = "Dynamite"
# print the list
print(songs)

# adds an element to the end of the list
songs.append("Mood")
# adds an element to the beginning of a list
# songs.prepend("Roses")
# adds a list to end of a list
songs.extend(["Laugh Now Cry Later", "Blinding Lights"])
# adds element at specific index followed by item
songs.insert(0, "Life Is Good")
print(songs)
