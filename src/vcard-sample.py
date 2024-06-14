"""
Note: It's much easier to generate these field if you generate the .vcf first
send the file to your self and copy the content here

To do: Convert these elements into a env or inputs from an application / API
"""
# Declare all the variables here
first_name = "John"
last_name = "Doe"
email = "john.doe@example.com"
email_label = "Work"
general_email = "johndoe@example.com"
general_email_label = "Personal"
# Phone number must be in the format "(123) 456-7890"
main_phone = "(123) 456-7890"
cell_phone = "(987) 654-3210"
wa_phone = "(555) 555-5555"
city = "New York"
state = "NY"
zipcode = "12345"
country = "USA"
ca_city = "Toronto"
ca_state = "ON"
ca_zipcode = "M1M1M1"
ca_country = "Canada"
twitter = "https://twitter.com/johndoe"
linkedin_url = "https://www.linkedin.com/in/johndoe"
note = "This is a sample vCard"
personal_github = "https://github.com/johndoe"
org_github = "https://github.com/organization"
homepage = "https://www.example.com"
# WhatsApp Business number must be in the format "1234567890"
wa_business = "1234567890"

VCARD = f"""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iPhone OS 17.4.1//EN
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
item1.EMAIL;type=INTERNET;type=pref:{email}
item1.X-ABLabel:{email_label}
item2.EMAIL;type=INTERNET:{general_email}
item2.X-ABLabel:{general_email_label}
TEL;type=HOME;type=VOICE;type=pref:{main_phone}
TEL;type=CELL;type=VOICE:{cell_phone}
item3.TEL:{wa_phone}
item3.X-ABLabel:WhatsApp
item4.ADR;type=pref:;;;{city};{state};{zipcode};{country}
item4.X-ABLabel:US Office
item4.X-ABADR:us
item5.ADR:;;;{ca_city};{ca_state};{ca_zipcode};{ca_country}
item5.X-ABLabel:Canada Office
item5.X-ABADR:ca
X-SOCIALPROFILE;type=twitter:{twitter}
X-SOCIALPROFILE;type=linkedin:{linkedin_url}
NOTE:{note}
item6.URL;type=pref:{personal_github}
item6.X-ABLabel:GitHub - Personal
item7.URL:{org_github}
item7.X-ABLabel:GitHub - Org
item8.URL:{homepage}
item8.X-ABLabel:_$!<HomePage>!$_
item9.IMPP;X-SERVICE-TYPE=WA Business;type=pref:x-apple:{wa_business}
item9.X-ABLabel:WA Business
END:VCARD
"""