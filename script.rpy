label start:
#Defining all of the caracters
define DevVoice = Character('Dev Team', color = "FFFFFF")
define AdultAbigail = Character('???', color ="FFFFFF")
define Abigail = Character('You', color ="#FFFFFF")
define Shannon = Character('Mom', color ="#FFFFFF")
define Jerry = Character('Dad', color ="#FFFFFF")

#Images for the characters
image AbigailSprite = "AbigailSprite.png"
image AbigailPajamas = "AbigailPajamasSprite.png"
image AbigailCasual = "AbigailCasualSprite.png"
image ShannonSprite = "MomSprite.png"
image JerrySprite = "DadSprite.png"

#images of outside house
image OutsideHouse = "ViewOfHouse.jpg"

#Bathroom
image BathroomDay = "Bathroom I - Day.jpg"

#Main Characters Bed
image McBedDay_ExtLight = "BedDay_ExtLight.jpg"
image McBedDay IndLight = "BedDay IndLight.jpg"
image McBedNight_DarkIndLight = "BedNightDarkIndLight.jpg"
image McBedNight IndLight = "McBedNight IndLight.jpg"

#Parents Bedroom
image PBed Day IndLight = "Bedroom III - Daylight - Interior light.jpg"
image PBed_Day = "PBedroomDaylight.jpg"
image PBed Sunset = "Bedroom III - Sunset.jpg"

#Dining Room
image DiningRoom_IndLight = "DiningRoomIndLight.jpg"
image DiningRoom Night IndLight = "Dining Room I - Night Internal Light.jpg"
image DiningRoom Night LowLight = "Dining Room I - Night Low Light.jpg"

#Kitchen
image Kitchen DayLight = "Kitchen DayLight.jpg"
image Kitchen Night LightsOut = "Kitchen Night LightsOut.jpg"
image Kitchen Night = "Kitchen Night.jpg"

#Living Room
image LivingRoom_DayLight = "LivingRoomDaylight.jpg"
image LivingRoom Afternoon = "Living Room I - Afternoon Light.jpg"
image LivingRoom Night = "Living Room I - Night.jpg"
image LivingRoom Dark = "Living Room I - Dark.jpg"

#Dads Office
image Office DayLight = "Office I - Daylight.jpg"
image Office Night IndLight = "Office I - Night Interior Light.jpg"
image Office Night = "Office I - Night Natural Light.jpg"

#start of intro scene, will start black then fade into view of house then living room towards the night.
scene black
AdultAbigail "Alright alright, it's time to go to bed you two."
AdultAbigail "What's that? You want to hear a story..."
AdultAbigail "... Alright, it's about time you heard this one.\nIt happened when I was only 16, on a cool winter night.."

scene OutsideHouse
with fade
Abigail "My name.. is Abigail Cooper."
show AbigailSprite
with fade
Abigail "I live in my home here in Nevada with my parents."
Abigail "It's a quiet and peaceful neighborhood, although a little bland..\nAll the houses are built the same, and painted the same too."
hide AbigailSprite

scene black
Shannon "Abigail! Dinner's ready."
Abigail "Coming mom!"

scene DiningRoom_IndLight
with fade
show ShannonSprite
Abigail "This is my Mom, Shannon Cooper."
Abigail "Due to being homeschooled, she stays home and teaches me everything I need to know about the world.\nShe's wicked smart."
hide ShannonSprite
show JerrySprite 
Abigail "And this is my Dad. Jerry Cooper."
Abigail "I don't get to see him much outside of the morning and afternoon.\nHe is always busy working so we can have everything we need."
Jerry "Man, this looks good!\nWork was extremely busy today.. This is just what I needed."
hide JerrySprite
show ShannonSprite
Shannon "Well, I'm glad you like it."
Shannon "I finally managed to get an appointment with the mechanic tomorrow to look go look at my car."
hide ShannonSprite
show JerrySprite
Jerry "Oh! Forgot that was happening this week.\nThat darn thing always seems to have something wrong with it."
hide JerrySprite
show AbigailSprite
Abigail "Mmm! This food is really good mom, how long will you be gone?"
hide AbigailSprite
show ShannonSprite
Shannon "I don't know.. He said this might take a couple of hours from the sound of things.."
hide ShannonSprite
show AbigailSprite
Abigail "Does that mean I can take a day off from school since you aren't going to be here for a while!?"
hide AbigailSprite
show ShannonSprite
Shannon "No way young lady! You know how to do your homework without me."
hide ShannonSprite
show JerrySprite
Jerry "Hahaha, alright no more car talk at the table, let's enjoy dinner."
hide Jerry

scene black
with fade
Abigail "Goodnight Dad!"

scene McBedNight_DarkIndLight
with fade
show AbigailPajamas
Abigail "Goodnight Mom... see you when you get back home."
hide AbigailPajamas
show ShannonSprite
Shannon "Goodnight Abigail. Don't forget to do your schoolwork!\n I'll be checking it when I get back."
Shannon "...And remember the rules Abigail.."
hide ShannonSprite
show ShannonSprite
with fade
Shannon "never leave the house.\nIt's dangerous out there."
Shannon "Goodnight!"
hide ShannonSprite

scene black
Abigail "Yeah, yeah Mom, I know  that already... Goodnight."

scene McBedDay_ExtLight
with fade
"*Thud*"
Shannon "Crap! My alarm didn't go off I'm going to be late!"
"*Door Slam*"
show AbigailPajamas
Abigail "Huh, Mom must have overslept, she usually isn't in a hurry like that."
Abigail "Well, guess I should start my day"
hide AbigailPajamas

scene LivingRoom_DayLight
with fade
show AbigailCasual
Abigail "Man.. I hate studying.\nI could paint in my room instead, but I just ran out of acrylics.."
Abigail "..Plus Mom will be checking to make sure I did my work."
hide AbigailCasual

scene black
Abigail "Huh... Woah! Mom left the door cracked.. Their bedroom is always locked."
Abigail "She really must have been late.."

scene PBed_Day
with fade
show AbigailCasual
Abigail "Man, I know I'm not supposed to be in here, but I'm sure just a peek won't hurt."
Abigail "Huh, don't know what I was expecting really...\nIts..pretty basic."
Abigail "Oh well, that was fun but I don't wanna risk getting into trouble."

scene black
Abigail "Huh.. What's this drawer?"
Abigail "A missing poster, newspapers, this is from 13 years ago?!"
Abigail "Why would they have this!"

DevVoice "Aaand that's all we have so far, from here you will make choice after choice, unraveling the secrets of your parents."
DevVoice "Turns out, it's a lot harder to make a game than we thought, especially coming up with a cohesive story, gameplay mechanics,..script writing.. etc."
DevVoice "We hope you look forward to the finished polished product! Thanks!"

return