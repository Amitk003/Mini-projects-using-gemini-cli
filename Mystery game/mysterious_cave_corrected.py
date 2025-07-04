def start_game():
    print("You wake up in a dark, damp cave. A faint light flickers in the distance.")
    print("You can hear the sound of dripping water and a low, guttural growl.")
    print("\nWhat do you do?")
    print("1. Head towards the light.")
    print("2. Try to find another way out in the darkness.")

    choice = input("> ").strip()

    if choice == "1":
        path_light()
    elif choice == "2":
        path_darkness()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()

def path_light():
    print("\nYou cautiously move towards the flickering light. As you get closer, you see it's a torch.")
    print("Next to the torch, there's a rusty old sword and a small, leather-bound book.")
    print("\nWhat do you do?")
    print("1. Pick up the sword.")
    print("2. Read the book.")
    print("3. Ignore both and continue deeper into the cave.")

    choice = input("> ").strip()

    if choice == "1":
        print("\nYou pick up the sword. It's heavy and surprisingly sharp. You feel a bit more confident.")
        print("Suddenly, a giant spider drops from the ceiling!")
        print("You bravely fight the spider with your sword. After a fierce battle, you defeat it!")
        print("Beyond the spider's lair, you find an exit leading to a beautiful forest. You are free!")
        print("\n--- THE END (Victory!) ---")
    elif choice == "2":
        print("\nYou open the book. It's a journal, detailing the cave's history and warning of its dangers.")
        print("As you read, you hear a rustling behind you. A cave troll emerges from the shadows!")
        print("You try to run, but the troll is too fast. It captures you.")
        print("\n--- THE END (Captured!) ---")
    elif choice == "3":
        print("\nYou ignore the items and press on. The growling sound gets louder.")
        print("You stumble into a large cavern, and a massive dragon awakens from its slumber!")
        print("The dragon breathes fire, and you are instantly incinerated.")
        print("\n--- THE END (Dragon's Feast!) ---")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        path_light()

def path_darkness():
    print("\nYou decide to brave the darkness, feeling your way along the cave wall.")
    print("After a while, your hand brushes against something cold and metallic.")
    print("It's a hidden lever!")
    print("\nWhat do you do?")
    print("1. Pull the lever.")
    print("2. Leave the lever and keep searching.")

    choice = input("> ").strip()

    if choice == "1":
        print("\nYou pull the lever. A secret passage opens up, revealing a treasure chest!")
        print("Inside, you find untold riches and a map leading to a hidden exit.")
        print("You escape the cave a wealthy adventurer!")
        print("\n--- THE END (Rich and Free!) ---")
    elif choice == "2":
        print("\nYou decide not to risk the lever and continue in the dark.")
        print("You eventually fall into a deep, unseen pit.")
        print("\n--- THE END (Pitfall!) ---")
    else:
        print("Invalid choice. Please choose 1 or 2.")
        path_darkness()

if __name__ == "__main__":
    start_game()