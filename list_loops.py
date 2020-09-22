songs = ["ROCKSTAR", "Do It", "For The Night"]

# task 1: print first and last element of song list
print(songs[0], ", ", songs[2])

# task 2: print out "Do It"and "For The Night" using a list slice on the songs list
print(songs[1:3])

# task 3:  update the last element in the songs list with a new song of your choice
songs[2] = "僕は一寸"
print(songs)

# Task 4: add three songs of your choice to your songs list
songs.extend(["사랑하기 때문에", "Gymnopédie No. 1", "J'en Ai Marre"])
print(songs)

# Task 5: delete one of the elements in your songs list in your list_loops.py file
songs.pop(5)
print(songs)


animals = ["Cat", "Dog", "Bird"]
animals.append("Axolot")
print(animals[2])
animals.pop(0)
print(animals)

for animal in animals:
    print(animal)
