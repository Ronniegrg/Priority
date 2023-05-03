import json

# Load the data from the JSON file if it exists
try:
    with open("languages.json") as f:
        languages = json.load(f)
except FileNotFoundError:
    languages = {}


def print_languages():
    # Sort the languages by count and print them
    sorted_languages = sorted(
        languages.items(), key=lambda x: x[1], reverse=True)
    print("Programming languages:")
    print("{:<20} {}".format("Language", "Count"))
    print("--------------------")
    for language, count in sorted_languages:
        print("{:<20} {}".format(language, count))


while True:
    # Ask the user for a new language or command
    user_input = input(
        "Enter a programming language to add, or type 'list', 'remove', or 'quit': ").lower()

    # Handle commands
    if user_input == "quit":
        break
    elif user_input == "list":
        print_languages()
    elif user_input == "remove":
        # Ask the user which language to remove and remove all counts of it from the dictionary
        remove_input = input(
            "Enter the programming language to remove: ").lower()
        if remove_input in languages:
            count = languages[remove_input]
            del languages[remove_input]
            print(f"All {count} counts of {remove_input} removed from the list.")
            # Save the updated data to the JSON file
            with open("languages.json", "w") as f:
                json.dump(languages, f)
        else:
            print(f"{remove_input} not found in the list.")
        print_languages()
    else:
        # Check if the language is already in the dictionary, and either increment its count or add it
        if user_input in languages:
            languages[user_input] += 1
            print(f"{user_input} count increased to {languages[user_input]}.")
        else:
            languages[user_input] = 1
            print(f"{user_input} added to the list.")
        print_languages()

    # Save the data to the JSON file
    with open("languages.json", "w") as f:
        json.dump(languages, f)
    print_languages()
print("Goodbye!")
