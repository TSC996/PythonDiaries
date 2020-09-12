## First === pip install phonenumbers
#### Import the required Libraries 
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import phonemetadata
from phonenumbers import carrier
##### Change the Country Code according to your own country or Choice of urs
phone_number = phonenumbers.parse("+91 ")

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number, 'en'))
print(phonemetadata.NumberFormat(phone_number, 'en'))