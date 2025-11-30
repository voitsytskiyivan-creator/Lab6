Floppa = {"owner": "Jim", "animal": "cat"}
Jack = {"owner": "Alex", "animal": "dog"}
Kevin = {"owner": "Elena", "animal": "parrot"}
pets = [Floppa, Jack, Kevin]
for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['animal']}.")