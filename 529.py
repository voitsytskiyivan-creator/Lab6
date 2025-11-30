cities = {
    "Rome": {
        "country": "Italy",
        "population": "2868000 people",
        "fact": "Rome is one of the oldest cities in the world, the capital of Ancient Rome. "
                "Therefore, Rome is often called the \"eternal city\"."
    },
    "Canberra": {
        "country": "Australia",
        "population": "381448 people",
        "fact": "The design of Canberra was based on the concept of a garden city, which includes "
                "significant areas of natural vegetation, which earned for Canberra the title of "
                "\"bush capital\" (translated from the English \"forest capital\")."
    },
    "Toronto": {
        "country": "Canada",
        "population": "2503281 people",
        "fact": "In the world of professional sports, the city is the most famous hockey team of "
                "Toronto Maple Leafs. The city holds the nickname of the \"hockey universe center\"."
    }
}
for city, info in cities.items():
    print(f"{city}:")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")