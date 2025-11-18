# Using a dict comprehension invert the dict (swap key with value), creating a mapping of country codes to countries

country_to_country_code = {
    "Poland": "+48",
    "USA": "+1",
    "Vatican": "+379",
    "Italy": "+39"
}

country_code_to_country = {
    code: country for country, code in country_to_country_code.items()
}

assert country_code_to_country == {'+48': 'Poland', '+1': 'USA', '+379': 'Vatican', '+39': 'Italy'}
print("OK")
