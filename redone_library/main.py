#Pedro Souza, Personal Library Program

#Import random so I can more easily randomize things in the program
import random


#Variable creation
playlist = [] #List variable for the list of songs

userChoice = "" #Variable to store what users last action selected was


#Add function, this function adds a song (selected during function call) to the playlist, unless it is already on the playlist, then you get an error message
def add(added, artist, duration, genre, views):
    if added in playlist:
        print("\nThat song is already on the playlist, we don't allow duplicates\n")
    else:
        playlist.append({"song": added,
                      "artist": artist,
                      "duration": duration,
                      "genre": genre,
                      "views": views})

#Remove function, this function removes a song (selected during function call) from the playlist, unless it isnt on the playlist, then you get an error message
def remove(removed):
    for i in playlist:
        if removed == i["song"]:
            playlist.remove(i)
            return
        print("\nThat song is not on your playlist\n")

#Search function, this function tells you if the selected song (selected during function call) is on the playlist yet
def search(searched):
    for i in playlist:
        if searched == i["song"]:
            print(f"\nThe song {searched} was found in your playlist, here is the rest of the info\n{i}\n")
            return
        print(f"\nYou do not have the song {searched} in your playlist yet\n")

#Randomize function, this function simply uses random.choice to pick a random song for the user
def randomize():
    totalSongs = 0
    songWent = 0

    for i in playlist:
        totalSongs += 1
    
    randomArtist = random.randint(0, totalSongs)

    for i in playlist:
        songsWent += 1
        if songsWent == randomArtist:
            print(f"\nYour random song is: {i['song']}\n")
            return
    
#Prints just the names of the songs, unlike when when you get you playlist (on add and remove functions)
def print_simplified():
    for i in playlist:
        print("\nSong list:")
        print(f"{i['song']}")

#Main fucntion, this function manages the UI by printing player the action options and running a different fucntions basedf on user's choice (userChoice var)
def main():
    userChoice = input(f"\nType which you would like to do?\n1) Add\n2) Remove\n3) Search\n4) Get a Random Song in Your Playlist\n5) Print your simplified list\n6) Leave\n")

    #Runs if statements based on choice, some of the fucntions runned here also ask the user for relevant input
    if userChoice == "1":
        add(input(f"\nYour current playlsit is:\n{playlist}\nWhat song would you like to add?:\n").lower(), input(f"\nWhat is the artists name?:\n").lower(), input("\n What is the song duration\n"), input("What is the song genre?").lower(), input("What is the amount of views'?"))
    elif userChoice == "2":
        remove(input(f"\nYour current playlsit is:\n{playlist}\nWhat song would you like to remove?:\n").lower())
    elif userChoice == "3":
        search(input(f"\nWhat song would you like to seach for?:\n").lower())
    elif userChoice == "4":
        randomize()
    elif userChoice == "5":
        print_simplified()
    elif userChoice == "6":
        print("")
        exit("\nBye-bye!\n")
    #Idiot proofing, if the input isnt the strings "1- "5", error message plays
    else:
        print("\nYour input is invalid, please only type numbers 1-5 as inputs\n")

#Runs main function on loop, cannot be interrupted unless user chooses to end the program
while True:
    main()
