print("Devloped By C15C01337 (Bishal Aryal)")
print("Follow me on Twitter username @C15C01337")


import phonenumbers #pip install phonenumbers

number = input("Enter your number with country code:")

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(service_number, "en"))  