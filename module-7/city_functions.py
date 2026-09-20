def city_country(city, country, population=None, language=None):
    """Return a formatted city and country string."""
    location = f"{city.title()}, {country.title()}"

    if population:
        location += f" - population {population}"

    if language:
        location += f", {language.title()}"

    return location


print(city_country("santiago", "chile"))
print(city_country("atlanta", "united states", 5000000))
print(city_country("kingston", "jamaica", 1000000, "english"))