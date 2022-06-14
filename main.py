"""
Name(s): Ella Gentile, Neila Shaka
Name of Project: Peculiar Activities 
inspired by stranger things
"""

#Write the main part of your program here. Use of the other pages is optional.



title = input("Welcome to Peculiar Activities. Enter [Play] to begin: ")
while title not in ['play', 'Play']:
      print("Smart choice. But it would be fun.")
      title = input("Welcome to Peculiar Activities. Enter [Play] to begin: ")
if title == 'play' or title == 'Play':
    print("\nLet's begin. \n")

  

def end():
  print("- THE END - \n")

def shed():
  print("\n You take off running towards the shed. As soon as you get there, you shut the door behind you and start searching the drawers and shelves for anything that might help you. You find a shotgun and some bullets in a crate but still want to explore your options. When you open the cabinet next to the crate, you find a can of gasoline and some matches. You can hear footsteps quickly advancing on the shed and the lights start to flicker. What will you use to defend yourself? \n")
  weapon = input("Enter [gun] to start loading the shotgun or [gas] to begin opening the can: ")
  while weapon not in ['gun', 'Gun', 'gas', 'Gas']:
      print("That's not a choice.")
      weapon = input("Enter [gun] to start loading the shotgun or [gas] to begin opening the can: ")
  if weapon == 'gun' or weapon == 'Gun':
    print("\n You grab the ammo and the gun and start loading it with shaky hands. You aim the gun at the door and wait. There's no way this thing is bulletproof, right? Suddenly, the footsteps stop and the flickering light turns back off. Is it gone? You sigh in relief but you aren't sure if you're safe just yet. Your suspicions are proven correct when the light starts glowing on its own. It gets brighter and brighter until it hurts to look. You shut your eyes, but as soon as you open them again, you can tell that you are far from home. \n")
    end()
  elif weapon == 'gas' or weapon == 'gas': 
    print("\n You grab the gasoline and pour some in front of the door. Match in hand, you wait in eerie silence as the footseps get louder. Suddenly, the shed light's flickering speeds up. You hear growling so you light the match and throw it onto the gas puddle. It bursts into flames and you can hear the sound of the monster in pain. It seems that fire actually did some substantial damage. You dash out the back window and run as fast as you can until you reach your friend's house. You know that they're the only people that will believe your story. \n")
    end()

def upsidedown():
  print(" \n As you stand staring at the creature in the dark, the lightbulb above you begins to flicker. It illuminates the room completely, and you finally get a good look at the monster. It's 10 feet tall, with a flower shaped mouth that opens to reveal thousands of teeth. Suddenly, the light flickers off and then back on, and the creature is simply gone. Well, it's finally over. You're safe. The light doesn't stop getting brighter, though. You close your eyes quickly to shield them from the light. When you open them a second later, all you see is blue-ish fog and the silhouette of a tall creature in the distance. \n")
  end()
    
def attic():
  print("\n You sprint up the stairs as you hear the creature breaking through your front door. You quickly pull down the ladder to the attic and begin climbing up as the monster roars downstairs. Once you get to the top, you try to pull up the ladder, but it's stuck. You stand, frozen in fear in the corner of the pitch-black attic, unsure what to do. You see it's claw-like hands reaching over the edges of the floor as it pulls itself up, silently staring at you.")
  upsidedown()
def basement():
  print("\n You grab a glass vase for protection and run down the basement steps. As you're locking the door, you can hear the snarling creature breaking down your front door. Feeling quite secure with the padlock, you walk down the basement steps and wait at the bottom, staring up at the door. You can sense that the monster is right behind it and can hear it scratching at the wood. Seems like the lock might hold up.") 
  print("\n Suddenly, the creature smashed it's head through the door and crawled in, swinging it's head around - looking for you. You looked up at it, terrified. It faced you and stood on the top step, it's claws scratching the banister.")
  upsidedown()

def house():
  print(" \n You decide to stay in the house. Defense is the best offense, and you can already hear the creature screeching in your front yard. Can it see you? Or smell you? Either way, you need to find somewhere safer to hide; you can't just stand in the living room. The upstairs attic would be safe, provided the creature can't climb ladders, but the basement has a fairly strong lock on the door. Make your choice quickly. Will you hide in the basement or the attic? \n")
  choice3  = input("Enter [Attic] to seek shelter in the attic or [Basement] to lock yourself in the basement: ")
  while choice3 not in ['attic', 'Attic', 'basement', 'Basement']:
      print("That's not a choice.")
      choice3 = input("Enter [Attic] to seek shelter in the attic or [Basement] to lock yourself in the basement: ")
  if choice3 == 'attic' or choice3 == 'Attic':
    attic()
  elif choice3 == 'basement' or choice3 == 'Basement':
    basement()

def cont(): 
  print("There's a shed in your backyard, and you know your mom keeps various tools and weapons in there. However, the shed door has no lock; it's not a good hiding place. Will you go to the shed or stay in the house? \n")
  choice2 = input("Enter [Go] to run to the shed or [Stay] to remain in the house: ")
  while choice2 not in ['go', 'Go', 'stay', 'Stay']:
      print("That's not a choice.")
      choice2 = input("Enter [Go] to run to the shed or [Stay] to remain in the house: ")
  if choice2 == 'go' or choice2 == 'Go': 
    shed()
  elif choice2 == 'stay' or choice2 == 'Stay':
    house()

def bike():
    print("\n \n You hop on your bike and start pedaling home. It's almost completely silent; all you can hear is the chirping of crickets in the woods surrounding you. The light on your bike flickers in and out as you pedal. \n")
    print("As you glance up at the road, you see a dark silhouette standing in the middle of the road, illuminated only by a weak streep lamp. You're startled off your seat. \n")
    print("You look up and see the dark figure still standing there, staring in your direction. It's double your height and is making a terrifying growling sound. You grab your backpack and run the rest of the way home, leavin your bike on the street. \n" )
    print("Once you get home, you close the front door and try to call your mom, but you don't have signal. You can hear the roars of the creature getting louder down the street. \n")
    print("- \n")
    cont()

def walk():
  print("\n You decide to leave your bike at your friend's house and pick it up tomorrow. As you head down the empty street, the lamps around you start to flicker. Suddenly, you see a tall, dark figure emerge before you, growling menacingly. Looking at the long claws and multiple mouths, you realize that it is something inhuman. \n")
  print("Terrified, you run off of the road and take the shortcut through the woods home. \n")
  print("Once you get home, you immediately lock the door behind you and try to call your mom. However, all you can hear is static and faint screeching. You can see the figure approaching your house. \n")
  print("- \n")
  cont()



print("You're heading home from your friend's house. It's getting dark; and you live pretty far. \n" )

def start():
    print("Are you riding your bike or walking home? ")
    choice = input("Enter [A] to ride your bike or [B] to walk:  ")
    while choice not in ['A', 'a', 'B', 'b']:
      print("That's not a choice.")
      choice = input("Enter [A] to ride your bike or [B] to walk: ")
    if choice == 'A' or choice == 'a':
        bike()
    elif choice == 'B' or choice == 'b':
        walk()
    


start()


  