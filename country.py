country_code = {
    "India" : "0091",
    "Australia" : "0025",
    "Bangladesh" : "00880"
}

print("Country code for Bangladesh - ")
print(country_code.get("Bangladesh", "Not Found"))

print("Country code for Japan -")
print(country_code.get("Japan", "Not Found"))