## First === pip install phonenumbers
#### Import the required Libraries 
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import phonemetadata
from phonenumbers import carrier
##### Change the Country Code according to your own country or Choice of urs
ph_num = input("Enter the Phone Number with Country Code:")
phone_number = phonenumbers.parse(ph_num)
print('Getting Phone Number Details')
print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number, 'en'))
print(phonemetadata.NumberFormat(phone_number, 'en'))
