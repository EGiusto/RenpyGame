label start:
#Defining all of the caracters
define DevVoice = Character('Dev Team', color = "FFFFFF")
define AdultAbigail = Character('???', color = "FFFFFF")
define Abigail = Character('You', color = "FFFFFF")
define Shannon = Character('Mom', color = "FFFFFF")
define Jerry = Character('Dad', color = "FFFFFF")
define Sofia = Character('Sofia', color = "FFFFFF")
define Daniel = Character('Real Dad', color = "FFFFFF")
define Maria = Character('Real Mom', color = "FFFFFF")
define Uber = Character('Uber Driver', color = "FFFFFF")
define Ticket = Character('Ticket Lady', color = "FFFFFF")
define Waitress = Character('Diner Waitress', color = "FFFFFF")
#Images for the characters
image Abigail = "AbigailNormal.png"
image Daniel = "Daniel.png"
image DinerLady = "DinerLady.png"
image Jerry = "Jerry.png"
image Shannon = "Shannon.png"
image Maria = "Maria.png"
image UberDriver = "UberDriver.png"

#images of outside house
image OutsideHouse = "ViewOfHouse.jpg"

#Bathroom
image BathroomDay = "Bathroom I - Day.jpg"

#Main Characters Bed
image McBedDay_ExtLight = "BedDay_ExtLight.jpg"
image McBedDay IndLight = "BedDay IndLight.jpg"
image McBedNight_DarkIndLight = "BedNightDarkIndLight.jpg"
image McBedNightIndLight = "McBedNightIndLight.jpg"

#Parents Bedroom
image PBed Day IndLight = "Bedroom III - Daylight - Interior light.jpg"
image PBed_Day = "PBedroomDaylight.jpg"
image PBed_Sunset = "BedroomSunset.jpg"

#Dining Room
image DiningRoom_IndLight = "DiningRoomIndLight.jpg"
image DiningRoomNightIndLight = "DiningRoomNightInternalLight.jpg"
image DiningRoom Night LowLight = "Dining Room I - Night Low Light.jpg"

#Attic
image Attic = "Attic.jpg"

#Kitchen
image KitchenDayLight = "KitchenDayLight.jpg"
image Kitchen Night LightsOut = "Kitchen Night LightsOut.jpg"
image Kitchen Night = "Kitchen Night.jpg"

#Living Room
image LivingRoom_DayLight = "LivingRoomDaylight.jpg"
image LivingRoom Afternoon = "Living Room I - Afternoon Light.jpg"
image LivingRoom_Night = "Living Room I - Night.jpg"
image LivingRoom Dark = "Living Room I - Dark.jpg"

#Dads Office
image Office DayLight = "Office I - Daylight.jpg"
image Office Night IndLight = "Office I - Night Interior Light.jpg"
image Office Night = "Office I - Night Natural Light.jpg"
#etc
image Backyard = "Backyard.jpg"
image Shed = "Shed.jpg"
image Poarch = "Poarch.jpg"
image OutsideNeighborhood = "OutsideNeighborhood.jpg"
image OutsideDiner = "OutsideDiner.jpg"
image InsideDiner = "InsideDiner.jpg"
image BackOfCar = "BackOfCar.jpg"
image Lake = "Lake.jpg"
image UberCar = "UberCar.jpg"
image TrainStation = "TrainStation.jpg"
image Neighborhood = "Neighborhood.jpg"
image RealHouse = "RealHouse.jpg"
#crime
image Criminal = "Crime.jpg"
#start of intro scene, will start black then fade into view of house then living room towards the night.
scene black

#intro scene
show Abigail
Abigail "Hello! My name is Abigail Cooper and welcome to my story!"
scene OutsideHouse with fade
show Abigail
Abigail "I am 16 years old and live in a nice house with my mom and dad."
#show mom?
scene LivingRoom_Night with fade
show Shannon
Abigail "My mom’s name is Shannon, and she has always been there for me no matter what. \nShe is a stay at home mom and is my best friend and my teacher! I am currently homeschooled so she gives me all the lessons and knowledge I need to know. \nShe’s great!"
#show dad?
hide Shannon
show Jerry
Abigail "My dad’s name is Jerry, and he is my second best friend! \nHe works as a mechanic and works super long hours. Even though he is always away at work all day, he still manages to find time to spend with me, he’s the best!"
hide Jerry
show Abigail
Abigail "I have no idea where I would be without my parents; they’re amazing. They’ve always been my best friends and all I’ve ever needed. They’ve always spent time with me and played dress up when I was a little kid and play video games with me ALL THE TIME! \nThey are so fun! I love spending time with them!"
scene Criminal with fade
Abigail "You see, the world out there is a super super scary and dangerous place. Even though I’m young, I know ALL about it. All about all the problems with the world; all the robberies, murder, destruction, pollution, violence and more. \nThere are lots of scary men and women out there who don’t care about anyone but themselves, all they care about is killing and destroying every last bit of happiness from everyone."
Abigail "Thats why I stay inside my house. My mom and dad have always made sure I know EVERYTHING about the world around me and they warn me and make sure I never have to ever go outside and get hurt."
Abigail "My dad always leaves to go to work and when he gets back he looks so exhausted, but he always puts a great face on for me, and I know he always looks like that because the awful people in this world are draining his happiness, but he always feels better when he comes home to me and my mom."
Abigail "My mom is usually staying at home with me, but when she does have to leave, I make sure to greet her with the biggest hug when she gets back every time, because I know she needs it after the dangers she went through just to get the ingredients for dinner."

Abigail "Of course I love my family and I love my life and I know that I am much better off inside my safe home than I am outside in that dangerous world with unimaginable tortures at every step.. but I can’t help but wonder.. what would it be like out there? With real friends and people my age? Even though I always have my mom and my dad to talk to, I crave interaction with people my age, with people who might understand how I am feeling and talk about all the ways we can fix the outside so that way kids like me can go out there for ourselves." 
Abigail "My mom tells me every other kid is also homeschooled, which makes me think that they must be lonely sometimes too. I wish I could meet one of them.. I wish I had friends." 


#filler scene 
scene McBedNight_DarkIndLight with fade
show Abigail
Abigail "I sit in my room as I finish the last of one of my homework assignments. The schoolwork I have to do is usually very easy, so it tends to take up very little of my time."
hide Abigail
show Shannon
Shannon "Abigail?"
hide Shannon
show Abigail
Abigail "I hear my mom call my name as she walks into my bedroom. Hey mom! What’s up?" 
hide Abigail
show Shannon
Shannon "I was wondering if you wanted to watch a movie with me before I go to the store for tonight’s dinner?" 
hide Shannon
show Abigail
Abigail "Oh yeah sure! What movie? My mom and I love watching old Disney movies together, it’s our favorite genre and we’ve watched all of the Disney movies at least ten times each. My favorite has to be either tangled or the little mermaid."
hide Abigail
show Shannon
Shannon "Let’s watch your favorite! Tangled!"
hide Shannon
show Abigail
Abigail "Awesome okay!" 
scene LivingRoom_Night with fade
show Abigail
Abigail "I follow my mom downstairs to the couch in our living room. We sit beside each other on the couch and grab a blanket to share. I snuggle in close and get comfy as my mom starts the movie."
Abigail "I’ve always loved the movie tangled because it gives me hope. Rapunzel, the main character in the movie, is just like me! Her mom protects her from the scary outside world and Rapunzel has never wanted to leave, just always dreamed about seeing the world around her. The only difference between her and me is that her mom turns out to be evil, and I know my mom isn’t."
Abigail "This movie has always just made me feel happy to watch, besides the evil mom part, because it makes me feel like eventually the world will be okay enough for me to go and explore the things that I’ve been dreaming about my entire life. I’ve always wanted to watch a sunset, or look at the night sky; I love drawing the sky in my free time, but it sucks that I’ve never been able to see it in real life." 
Abigail "Maybe one day, just like Rapunzel, I’ll be able to go outside and have my dream of seeing the sky and the ground and the rain and everything I’ve never experienced, and maybe if I’m lucky, it’ll be with a friend my age by my side." 

#time skip 
scene black with fade
"time passes"
scene LivingRoom_Night with fade
show Abigail
Abigail "The movie ends and my mom turns the tv off." 
hide Abigail
show Shannon
Shannon "That was fun, that movie never gets old."
hide Shannon
show Abigail
Abigail "I agree! It will forever be one of my favorites! /nThanks for watching it with me."
hide Abigail
show Shannon
Shannon "Anytime sweetie, but now I have to go to the store to get the things I need for dinner, how does shrimp Alfredo sound?"
hide Shannon
show Abigail
Abigail "Oooo that sounds amazing! Yes please!"
hide Abigail
show Shannon
Shannon "Okay perfect, well I’ll be back in an hour max."
hide Shannon
show Abigail
Abigail "My mom gets off of the couch and makes her way to the door." 

Abigail "Okay mom! See you soon!"
hide Abigail
show Shannon
Shannon "Bye sweetie!"
#end scene 

#eventually finds poster scene 
scene black with fade
"Time passes"
scene LivingRoom_Night with fade
#time skip
show Abigail
Abigail "It is currently 6:00, my dad doesn’t get home until around 8:00 so my mom will most likely have dinner ready by then, so I have about 2 hours to myself." 
Abigail "While I love my parents and spending time with them, I also really value my alone time. I love to paint, bake, draw, play video games, read and more." 
Abigail "My favorite activity might be video games, but the problem is, I’m only allowed to play single player. I know what you’re thinking, just play an online game while they’re gone, rebel a little, make some friends like I’ve been so badly wanting my entire life."
Abigail "Well.. I can’t. My parents have the internet disabled except for during my school hours which is only a four hour window where my mom is by my side the entire time. I get it, they don’t want me to be tracked and then kidnapped or get our house broken into, I rarely ever see them use the internet either besides for our subscriptions. They have a lot of specific configurations for our internet so that way it keeps me safe and I won’t have to maybe find a disturbing video online, but they can still use it for us to watch movies and tv shows, which are also limited."
Abigail "Now while I do love my old Disney movies so so so much, I kinda wish I could watch some other things. I don’t have much of a selection, in order to keep me safe from all the graphic things that’s on the tv duh obviously, but it’s still really annoying sometimes. Sometimes I wish I was allowed to be a normal kid ya know, like I know all kids are living the same or a similar life to me, but some kids have less strict parents and sometimes I wish mine would let up a little bit from time to time."
Abigail "But that’s okay, I know they’re only doing what’s best for me because they love me, and I am very grateful for them."
Abigail "Besides, I can find plenty of fun things to do in my free time. For example, I love love love playing pretend, even if I am sixteen, I have a very graphic imagination. I usually let out all my crazy ideas by writing or by acting them out, like a drama play."
Abigail "I decide that that’s what I’m going to do while my mom is gone at the store!"
scene McBedNight_DarkIndLight with fade
show Abigail
Abigail "I run into my closet and take out the closest thing I can find to a pirate outfit and put it on. I look very funny, but that’s the fun of it!"
Abigail "Alright! Now that I’ve got the outfit, let’s make a map!"
Abigail "I sit at my desk and take out a blank sheet of paper, I quickly draw a map of my house in 2D; it has the kitchen, the living room, the office, and then my room, and my parents room. I mark a giant X on my parents room and put away my drawing utensils." 
Abigail "Man, times like this I really wish I had a friend to do this with…"
Abigail "I jump up from my desk chair."
Abigail "ARGG!"
Abigail "I shout as I run around my house, ‘searching for my treasure’."
Abigail "Eventually I make it to my parents door after a long trek through the ‘Abigail Gulf’, the seas I took my boat through until I finally made it to where the legend says the treasure lies." 
scene PBed_Sunset with fade
show Abigail
Abigail "I open my parents bedroom door and walk into their bedroom. My parents have a desk, and a bed in their room. They don’t mind when I come into their room, sometimes I hangout in here with them, we’re all just that close to each other."
Abigail "I start to make my way to their walk in closet with my best pirate voice, legend says the treasure lies right beneath my nose!" 
Abigail "I dodge all the ‘traps’ in their room and make it into their closet, pushing past all of their clothing that I pretend is vines."
Abigail "While I move their clothes side to side, I run my hands across the walls of the side of their closet." 
Abigail "Treasure! Treasure! Where are you?"
Abigail "I stop dead in my tracks as my hand runs across a tiny door." 
Abigail "What is this?"
Abigail "I ask myself, snapping out of my fantasy. I move all of the clothes away from where my hand stopped to reveal a small trapdoor, like those that lead to an attic." 
Abigail "That’s weird. I don’t remember this being here."
scene Attic with fade
show Abigail
Abigail "I open the hidden trapdoor and it reveals a tiny attic area with lots and lots of boxes." 
Abigail "Oh, this is probably where my parents keep all the storage. Duh, that’s why I’ve never seen it." 
Abigail "I step through the door and into the attic and look around. Yup, lots of boxes labeled living room, kitchen, etc. This must just be where they keep all the extra supplies for each room from when we first moved into this house. This is a neat place. I look around and find a box labeled ‘Abigail’."
Abigail "That’s weird, ooo maybe some of my really old baby pictures are in there!"
Abigail "I’ve always asked my mom and dad to see old baby pictures of me but they always say they don’t want to dig around for them, this is probably why."
Abigail "I wouldn’t wanna dig around in this attic place either, it looks like there’s spiders everywhere!"
Abigail "I go into the box and search for those pictures I’ve been wanting to see. I move some things around, paperwork, pictures of my mom and dad, but none of me. That’s weird."
Abigail "I finally get to the bottom of the box and see a small picture peeking through the dozens of papers also at the bottom of the box. It’s a picture of me, it looks like I’m three, maybe four years old. Im standing, wearing a little white dress with a blue bow in my hair and smiling. I look adorable!"
Abigail "I move the papers blocking the picture and finally grab a hold on the picture and hold it out in front of me."
Abigail "My face immediately goes pale as I look at the picture that’s now a piece of paper. My eyes widen as I stare at it in complete disbelief."
scene black with fade
"Above the picture of happy toddler me, is a headline:"
"MISSING"
scene Attic with fade
show Abigail
Abigail "what is going on?"
#end scene 


#CHOICE SCENE
Abigail "I look at the missing poster of toddler me, trying to wrack my brain of what this means."
Abigail "Am I missing? Was I missing? What does this mean?"
Abigail "I have no idea what to do. I have no idea who I am."
Abigail "I take a deep breath and try to collect my thoughts."
Abigail "Okay let’s just, leave this here so my parents don’t know I was here and let’s just go back in my room and take a moment to think of what is going on."
Abigail "As I put the missing child poster back into the box, I hear the front door open."
Shannon "Hi sweetie! I’m home!" 
Abigail "Uh oh. I quickly close the trapdoor and run out of my parents room, closing all of the doors behind me to make sure it looks like I was never there. "
scene McBedNight_DarkIndLight with fade
show Abigail
Abigail "Hi mom! One second, let me change my clothes really quick!" 
Abigail "I yell down to my mom as I try my best not to freak out. "
hide Abigail
show Shannon
Shannon "Okay sweetie, your dad will be home soon, I’ll go ahead and start dinner!" 
hide Shannon
show Abigail
Abigail "I change my clothes and sit on my bed for a second, taking a couple deep breaths and collecting myself."
Abigail "Was that even a picture of me?"
Abigail "I think back to the picture, the grey eyes, the dark brown hair, the wide dimpled smile."
Abigail "That was definitely a picture of me. It looked just like me."
Abigail "So I went missing when I was four years old. Am I still missing? Did my parents find me and they just kept that for memories? That’s really weird if they kept that for memories."
Abigail "Is that why my parents would never let me see baby pictures of me?"
Abigail "This is so confusing and it doesn’t help that I don’t remember anything from before I was four. I just remember this house and my mom and my dad."
Abigail "Are they even my mom and dad?"
Abigail "Oh my god, is this why I’m never allowed out of the house?"
Abigail "What if the world isn’t that bad at all?!"
Abigail "Okay okay calm down again. My parents have never given me a reason not to trust them, let’s just think."
hide Abigail
show Shannon
Shannon "Abigail! Dinner!" 
hide Shannon
show Abigail
Abigail "What?! Already? I check the time, 6:14. I’ve been sitting on my bed thinking for so long my mom already finished dinner and my dad already came home."
Abigail "Coming! I slowly make my way downstairs."
scene DiningRoomNightIndLight
show Jerry
Jerry "Hey there kiddo," 
hide Jerry
show Abigail
Abigail "My dad smiles at me as he sits at the dinner table, looking exhausted like always."
hide Abigail
show Jerry
Jerry "I was beginning to think you didn’t wanna see me, you’ve been up in your room ever since I got home."
hide Jerry
show Shanon
Shannon "Ever since even I got home, my mom chimed in."
hide Shannon
show Abigail
Abigail "Oh sorry, I was uh, reading a book and I was at a really good part and I just wanted to try and finish before it was time to eat. I say, quickly coming up with an excuse."
hide Abigail
show Shannon
Shannon "I thought you said you had to change?" 
hide Shannon
show Abigail
Abigail "Shoot. Oh yeah, I did that too. I was trying on different clothes while you were gone, I say, avoiding eye contact as I slip into a chair at the table."
hide Abigail
show Shannon
Shannon "Well sounds like you had a fun time while I was at the store." 
hide Shannon
show Abigail
Abigail "My mom smiles as she puts the food down in front of us."
Abigail "That’s one way to put it."
hide Abigail
show Jerry
Jerry "This looks great Shannon!" 
hide Jerry
show Abigail
Abigail "My dad lights up as he takes a bite."
Abigail "Thanks mom. I smile as I take a bite too."
Abigail "We all eat quietly as my thoughts run wild again."
Abigail "There are two options:"
Abigail "Either my parents are really my parents and I went missing when I was a young child and my mom and dad eventually found me and kept that poster in their room just to have it. That would explain why they never let me leave the house, they never want me to disappear again, they’re scared. Then that would mean the world truly is as awful and dangerous as they say, and I experienced that trauma first hand."
Abigail "Or, I’ve been missing ever since I was four and my parents are my kidnappers. That’s why they never let me leave the house, because they don’t want anybody finding me and they want to keep me forever. That missing poster was a copy of many that they probably tried to take down so no one would look for me anymore."
Abigail "I don’t know which one is real."
Abigail "I want to ask my parents for help. They’ve always been here for me. I never do anything without them, and especially make such a huge decision without them."
Abigail "But if they’re my kidnappers, they would know that I know, and that would be really awful."
Shannon "Abigail? Is everything okay? You look deep in thought over there." 
Abigail "What should I do?"
#CHOICE !!!!!! Hide what you know. Ask parents. !!!!!!!
menu:
    "Confront Parents": 
        jump ConfrontParents

    "Hide what you know": 
        jump HideWhatYouKnow

label ConfrontParents:
#Confront parents scene
Abigail "Yeah actually, I have something I need to talk to you both about." 
Abigail "I put my fork down and look at my parents." 
Abigail "They both look at me and give me their full attention."
hide Abigail
show Shannon
Shannon "What is it honey?" 
hide Shannon
show Abigail
Abigail "So, I was playing around earlier and I went into your room and into your closet."
Abigail "I watch their faces slowly harden from the concerned looks that were previously there."
Abigail "When I went in your closet I found a door that led to an attic area, and I found a box with my name on it." 
Abigail "My parents look furious at this point. Maybe they’re just really mad because I was snooping around?"
Abigail "I found a poster with a picture of what I think is me on it, and it said missing." 
Abigail "My parents both look at me, and then at each other."
hide Abigail
show Jerry
Jerry "Why were you snooping in our room?" 
hide Jerry
show Abigail
Abigail "My dad speaks through gritted teeth."
hide Abigail
show Shannon
Shannon "Now Jerry, it’s okay, our daughter is a curious girl, we should’ve expected this."
hide Shannon
show Abigail
Abigail "My mom speaks in a tone I’ve never heard before; I look at her and notice a smile on her face, almost a smirk."
Abigail "She looks and sounds terrifying."
hide Abigail
show Shannon
Shannon "Looks like we need to tell you the truth, huh sweetie?" 
hide Shannon
show Abigail
Abigail "My mom and my dad look at each other with an expression I’ve never seen either of them hold."
Abigail "Before I have a chance to open my mouth and speak, I’m suddenly being pulled by the both of them."
scene Backyard with fade
Abigail "I scream and try to make out an expression of my confusion but my father quickly covers my mouth with his hand as they continue to drag me out into the backyard, towards our broken down shed."
Abigail "I struggle and try to flail any limb I can as they open the shed door."
Abigail "As soon as the door is open they throw me down on the ground of the shed and close the door behind them."
scene Shed with fade
show Abigail
Abigail "I look up at them in disbelief, what-"
Abigail "I’m quickly cut off as my dad covers my mouth with a rag tied around my face as my mom ties my hands together."
Abigail "I look at them with pure fear as they step away from me."
hide Abigail
show Shannon
Shannon "I was hoping you wouldn’t find out. We were having so much fun." 
show Abigail
Abigail "My mom smiles at me as she speaks. My dad just stares at me as my mom grabs a bat off of the wall of the shed."
Abigail "I scream through the gag and try to scoot my body away from my mother as she walks towards me. My father grabs me and throws me back in the middle of the floor, holding me there."
hide Abigail
show Jerry
Jerry "Sorry honey, you understand. Now that you know the truth, you could get us in trouble, and that just won’t do." 
hide Jerry
show Abigail
Abigail "My mom holds the bat over me as my father speaks."
Abigail "How could they? I thought they loved me. I thought they cared about me."
hide Abigail
show Shannon
Shannon "Bye sweetie, it was a pleasure."
hide Shannon
scene black with fade
Abigail "My mom smiles as she speaks and swings the bat towards my face."
Abigail "Then everything went black…"
return 

label HideWhatYouKnow:
#hide what you know scene
show Abigail
Abigail "Oh yeah sorry, I’m okay, I was just replaying the movie from earlier in my head. I force a smile on my face."
hide Abigail
show Shannon
Shannon "Oh yes, it was very fun to watch that."
hide Shannon
show Abigail
Abigail "My mom smiles and looks over at my dad."
hide Abigail
show Shannon
Shannon "We watched tangled earlier." 
hide Shannon
show Jerry
Jerry "Oh well isn’t that lovely, my two girls spending time together. Maybe we can watch a movie together soon." 
hide Jerry
show Abigail
Abigail "Oh yeah sure dad." 
Abigail "Luckily they bought it. Now I just have to figure out the truth. "
Abigail "I am super tired though, I think I’m gonna head to bed early if that’s okay with you." 
hide Abigail
show Shannon
Shannon "Oh sure honey, I know you had a long day."
hide Shannon
show Abigail
Abigail "I stand up from the table and my mom smiles at me."
hide Abigail
show Jerry
Jerry "Goodnight honey, sleep well." 
hide Jerry
show Abigail
Abigail "Thanks, goodnight." 
Abigail "I quickly make my way upstairs and close my bedroom door behind me. I change into my pajamas and get into my bed. I just need to sleep this off."
scene McBedNight_DarkIndLight with fade
show Abigail
Abigail "I can’t do anything or find any answers while my parents are home."
Abigail "I’ll just have to wait for them to leave again tomorrow."
#Next day
scene McBedDay_ExtLight with fade
show Abigail
Abigail "I wake up and act like everything is normal.."
Abigail "I say bye to my dad.."
scene LivingRoom_DayLight with fade
show Abigail
Abigail "I do my school lessons with my mom.." 
#show
scene McBedDay_ExtLight with fade
show Abigail
Abigail "I do my schoolwork in my room alone.."
#show
Abigail "My mom asks to spend time with me.." 
#show
scene LivingRoom_DayLight with fade
show Abigail
Abigail "We watch another movie.." 
#show
Abigail "And then she leaves for the grocery store again."
#Show
Abigail "I’ve never realized just how repetitive every day is for me until I had my world turn upside down."
Abigail "My parents are not really my parents. Or at least, I don’t think."
Abigail "I still have no idea what the truth is."
Abigail "But should I even stay to find out? It could be dangerous if they really aren’t my parents and then I stay long enough for them to find out."
Abigail "Who knows what they’d do to me?"
Abigail "Or maybe they really are my parents and they found me when I went missing?"
Abigail "I have no idea what to do."

menu:
    "Try to find out the truth":
        jump FindTruth
    "Run Away":
        jump RunAway
#Choice !!!!! try to find out the truth. Run away. !!!!

label RunAway:
#Run away scene 
Abigail "I need to run away."
Abigail "Now."
Abigail "I have no choice. I have to get out before they find out, before they know that I know."
Abigail "They could hurt me, they could.. kill me."
scene black with fade
show Abigail
Abigail "I decide that I’m just going to pack a bag and run away, I have to get out quickly before my mom comes back from the grocery store, so I just have to go."
Abigail "No thinking, no prep. Just leave."
Abigail "I quickly pack one outfit besides the one I’m wearing now. Luckily it’s close to being fall currently and I know from my studies that that means it’s not super hot but it’s not cold yet."
Abigail "I change into a practical outfit for the weather, jeans, t-shirt, jacket, and sneakers."
scene PBed_Day with fade
show Abigail
Abigail "I then go into my parents room and take whatever money I can find. I find about one hundred dollars and decide that that’s enough."
Abigail "I can’t think of anything else to pack; I’m doing this so suddenly there’s no time to think of anything else."
Abigail "I go to my desk and decide to write a note for my parents to find later when they’re looking for me." 

scene black with fade
"Dear mom and dad,
I know the truth. 
I know that I went missing when I was a child. 
I feel betrayed that you would keep that from me, and I don’t feel safe being around you. 
I’m terrified of both of you, terrified of what you’re capable of if you could keep such a big thing a secret from me. 
I don’t trust you anymore. 
Thank you for the life I’ve had so far, but I cannot stay here any longer. 
I wish you both the best of luck. 
Sincerely, Abigail." 

scene LivingRoom_DayLight
show Abigail
Abigail "I leave the note I wrote on my desk and make my way downstairs."
Abigail "My mom should be home any minute, so if I’m gonna leave, I need to go now."
Abigail "I’m terrified of what the world is outside of this house. But I think I feel safer being outside than I do in this house for any longer."
Abigail "I open the front door and look around me."
scene Poarch with fade
show Abigail
Abigail "Green grass, blue sky, gray concrete. Everything looks.. normal."
Abigail "I take a step outside of the door and feel a nice warm breeze."
Abigail "This feels.. nice."
Abigail "I step fully outside and close the front door behind me."
Abigail "Well here goes nothing."
scene OutsideNeighborhood with fade
show Abigail
Abigail "I step off of my porch and onto the sidewalk slowly. Nothing comes and grabs me, nothing yells at me, nothing sinks me into the ground. I’m.. safe."
Abigail "I’m safe!"
Abigail "This is amazing!"
Abigail "I start to quickly make my way down the sidewalk, walking fast to try to cover the most ground in the amount of time I have, but also taking everything in as I go." 
Abigail "Cars drive by but none honk at me, none crash into me, none look evil."
Abigail "I see people across the street walking together, no one looks angry or scary or like they want to kill me. Everyone looks so happy."
Abigail "They lied to me."
Abigail "I can’t believe they lied to me again. About something so big. Something so important."
Abigail "The fact that everything is normal and okay shows me that they probably were the ones who kidnapped me. If they lied to me about this, then they are definitely the ones who are evil."
scene black with fade
#time skip
scene OutsideDiner with fade
show Abigail
Abigail "After about two hours of walking tirelessly, I finally see somewhere that isn’t a house that looks exactly like mine. It’s a nice and quiet restaurant, kind of like a diner."
Abigail "I go inside and the bell on the door rings as I do."
scene InsideDiner with fade
show DinerLady
Waitress "Welcome to Shammy’s Diner! What can I do for ya?" 
hide DinerLady
show Abigail
Abigail "The lady behind the counter looks friendly, in a kind of motherly way. She’s in a uniform and has soft blonde hair."
Abigail "Can I just stay here for a bit?" 
Abigail "I’m a little unsure of how being a customer in a restaurant works. I know a lot of different things thanks to my lessons, but nothing taught me how to order my own food."
hide Abigail
show DinerLady
Waitress "You want a table? Sure! Follow me." 
hide DinerLady
show Abigail
Abigail "The lady grabs a menu and leads me to a booth in the corner."
hide Abigail
show DinerLady
Waitress "What would you like to drink, sugar?" 
hide DinerLady
show Abigail
Abigail "Uh, just a water?" 
hide Abigail
show DinerLady
Waitress "You got it! I’ll be right back." 
show Abigail
Abigail "As the kind lady walks off and makes her way towards the kitchen, I look down at the menu. Cheeseburgers, fries, milkshakes."
Abigail "Wow. This place has everything."
Abigail "This is awesome!"
Abigail "The lady brings over my water and asks if I’m ready to order."
Abigail "Not quite, can I have more time to look?" 
hide Abigail
show DinerLady
Waitress "Of course sugar! You wave me over when you’re ready, okay?"
hide DinerLady
show Abigail
Abigail "I nod my head in agreement as she walks away and back towards the kitchen."
Abigail "The diner seems to be mostly empty besides a few people, one drinking coffee at the bar and the other two sitting at a booth across the restaurant from me eating cheeseburgers." 
Abigail "I think I’ll stay and eat here for now. These people seem very comfy, like they stay here for a long time."
Abigail "And this place is open 24 hours so maybe I can stay here and ask some questions, maybe get some answers and be on my way by the morning."
Abigail "I smile to myself."
Abigail "This is all working out."
Abigail "I finally decide on a bacon cheeseburger with French fries when I hear the front door bell go off."
Abigail "I look up towards the noise."
Abigail "Oh my god."
Abigail "No.. no.. no.. no! NO!"
Abigail "Standing at the door, trailing their eyes across the restaurant, is my parents."
#end scene 
#parents find her scene 
Abigail "How did they find me?!"
Abigail "Their eyes finally settle on me as the lady from earlier comes out and greets them."
hide Abigail
show DinerLady
Waitress "Hey there! What can I do for you?" 
hide DinerLady
show Jerry
Jerry "Oh, we were just meeting our daughter." 
hide Jerry
show Abigail
Abigail "My father speaks as they point towards me, an evil expression on their faces." 
Abigail "Oh perfect, well you go on over there and call me over when you’re all ready to order." 
Abigail "They both smile and nod at the lady as she waves them towards me."
Abigail "She obviously can’t see my terrified expression."
hide Abigail
show Shannon
Shannon "Hey sweetie!" 
hide Shannon
show Abigail
Abigail "My mom yells as she gets into the booth next to me and puts her arms around me." 
hide Abigail
show Jerry
Jerry "We’re so glad to see you!" 
hide Jerry
show Abigail
Abigail "My dad sits across from me and the woman smiles at us as she makes her way back into the kitchen." 
Abigail "As soon as she does, my mom gives my dad a nod that she’s gone and she brings a knife to my wrist right below the table."
hide Abigail
show Shannon
Shannon "Now don’t you move a muscle, or I will slice your hand clean off, do you understand?" 
hide Shannon
show Abigail
Abigail "My mom whispers in my ear as I stiffen. I nod my head yes as my dad looks at me." 
hide Abigail
show Jerry
Jerry "We knew you’d find out eventually, though, we wished you’d talked to us first. Then we would’ve had a chance to explain everything. And then we would’ve known that we raised you well, raised you to be confident in us and trust us. Obviously we failed." 
hide Jerry
show Shannon
Shannon "Now I knew you were starting to get a little rebellious honey but this is a new level. I never expected this from you, not from how well we raised and treated you."
hide Shannon
show Jerry 
Jerry "Do you think we’re bad parents? We give you everything you’ve ever wanted, gave you a roof over your head, protected you from all evil, fed you. We did it all. And this is how you repay us?" 
hide Jerry
show Shannon
Shannon "I thought we had a good relationship the three of us. So what you’re not our birth kid? People adopt all the time. But when we do it it’s a problem?" 
hide Shannon
show Abigail
Abigail "My mom pushes the knife towards my skin. I flinch as she does."
hide Abigail
show Jerry
Jerry "Just because we’re not your real parents doesn’t mean anything. Blood means nothing when we’ve done so much for you and loved you with all of our hearts." 
hide Jerry
show Shannon
Shannon "You really make us out to be the bad guys." 
hide Shannon
show Abigail
Abigail "How did you find me? I stutter quietly and avoid eye contact with the both of them." 
hide Abigail
show Jerry
Jerry "Well, when you were a kid we put a tracker in those earrings you’re wearing. We just told you they were an expensive pair of earrings that you needed to wear forever. We weren’t lying cuz that tracker was very expensive, but it tells us anytime you leave the house. Ya know, haha, I was so shocked when I got the notification on my phone. I was like no way, it had to be a glitch, our little Abigail would never do something like that. Turns out, I was wrong." 
hide Jerry
show Abigail
Abigail "My dad speaks and his evil expression hardens when I bring my hand up to my earrings."
hide Abigail
show Shannon
Shannon "When your dad called me, I couldn’t believe it either. I quickly got home and put the groceries away while your dad made his way home from work early. Luckily that tracker tells us exactly where you are, so once your father got home we both went out to find you. How convenient right!" 
hide Shannon
show Abigail
Abigail "My mom beams as she says that last part, smiling at me as the blade slowly draws blood."
Abigail "I look down at the table as they speak. I should’ve known they’d have a tracker on me. If they never let me out of their sight normally, I should’ve known they had another way of keeping track of me when they left me alone."
Abigail "I should’ve known they didn’t actually trust me."
hide Abigail
show Jerry
Jerry "Right?!"
hide Jerry
show Abigail
Abigail "My mom slowly brings the blade deeper into my wrist at my blank response."
Abigail "Right!" 
Abigail "I whimper quietly to get my mom to loosen up with the knife. Luckily she does when I say that."
hide Abigail
show Jerry
Jerry "Well, it’s time we make our way home. We’ve all had a very long day." 
hide Jerry
show Abigail
Abigail "I whimper as my mom grabs me and pulls me up out of the booth. She’s holding the knife to my back now as we wait for my dad to stand up too."
hide Abigail
show Shannon
Shannon "Say a word and this knife will go straight through your back, do you understand?" 
hide Shannon
show Abigail
Abigail "My mom grumbles in my ear and I nod my head in agreement."
Abigail "I continue my terrified expression as my dad stands up and leads us outside to their car." 
scene OutsideDiner with fade
show Abigail
Abigail "The lady comes out from the kitchen once the bell rings but it’s too late. She can’t save me now."
Abigail "My parents shove me into the back of the car as they get in the front. They lock the doors before I can attempt to get out."
#show back of car scene
scene BackOfCar
show Abigail
Abigail "I sit in the backseat in defeat as my dad starts the car and pulls out of the parking lot of what I thought would’ve been my safe haven."
Abigail "I wish I prepared more before I left."
Abigail "Then I would’ve thought of my parents having a tracker, found a better way to leave besides walking."
Abigail "I made a huge mistake, and it might have just cost me my life."
Abigail "I look down at my bleeding wrist as tears run down my cheek. I’m shaking in fear as we continue to drive down dark roads."
Abigail "I assume they’re just going to take me home and get rid of me. Take me out and hide all evidence of having me. Considering they have already been able to hide me from the outside for this long, I wonder what else they’re capable of."
Abigail "Are they capable of murder?"
Abigail "Twenty, maybe thirty minutes pass by before my dad stops the car in a pitch black area."
Abigail "This isn’t the house."
Abigail "I look around outside of the window and see that we’re on a giant hill, at the bottom of the hill is a lake."
scene Lake with fade
show Abigail
Abigail "Oh no."
Abigail "I start to panic, looking around everywhere, searching for a light, a house, somewhere that I can maybe run to before they can grab me and kill me."
hide Abigail
show Jerry
Jerry "We’re here!" 
hide Jerry
show Abigail
Abigail "My dad yells excitedly as he looks at me in the rear view mirror."
hide Abigail
show Shannon
Shannon "Oh look, she looks so excited! Don’t worry sweetie this is gonna be so fun!" 
hide Shannon
show Abigail
Abigail "My mom smiles and claps her hands together in excitement. \n Oh my god. They’re insane."
hide Abigail
show Jerry
Jerry "Well, it was nice knowing you honey. I had a great time raising you. Too bad it had to end so soon, but I’m proud to say it was your fault, not ours!" 
hide Jerry
show Shannon
Shannon "Abigail you were such a good little girl. We were such great parents too Jerry don’t you worry. These things just happen, teenagers rebel and there’s nothing you can do about it. Oh well, too bad, so sad." 
Shannon "Well.. bye!" 
hide Shannon
show Abigail
Abigail "My parents smile at me as they quickly jump out of the car, locking the doors, putting the car in neutral, and taking the key out of the ignition."
Abigail "I scream at the top of my lungs as I try to open the doors or unlock them, but with no key the car is off, and my parents keep pressing the lock button on the key so that the doors stay locked."
Abigail "I feel my parents push the car as the car quickly makes its way down the hill."
Abigail "I scream as the car goes over the hill and crashes into the water."
Abigail "I look outside the back window of the car and see both of my parents still standing at the top of the hill, smiling down at me."
Abigail "The car quickly starts to sink as I try anything I can to get out of the car before I drown."
Abigail "The water fills up the inside of the car as I try to find something to break the windows. Napkins, tissues, gum wrappers. There’s nothing in here I can use." 
Abigail "I continue crying and panicking as I start to slam my body against the windows and the doors, trying to unlock the doors or make anything work."
Abigail "The water quickly gets all the way up to the top of my face and I’m completely engulfed underwater."
Abigail "The water is cold and makes my entire body tense up."
Abigail "I continue to struggle and bang on the doors and windows, but it changes nothing." 
Abigail "This is it."
Abigail "I should’ve never left. Maybe then I would’ve been safe if I just pretended everything was okay and kept going with my life."
Abigail "Like they said, they gave me everything."
scene black with fade
Abigail "Maybe I should’ve been more grateful." 
#Game over.
return 

label FindTruth:
#find the truth 
show Abigail
Abigail "I need to find out the truth. I need to know what’s really going on before I try and make any sudden decisions."
Abigail "In order for me to find out the truth, I need access to the internet."
Abigail "So that’s the first step, figuring out how to access the internet without my parents knowing."
Abigail "I go into their room again and try to search for an answer, as I look around the room, I spot my mom’s laptop on her desk."
scene PBed_Day with fade
show Abigail
Abigail "I don’t know how I’ve never thought to use her laptop, but this is one of the first and only times I’ve felt like snooping around and potentially losing my parents trust. It’s different this time."
Abigail "I open up my mom’s computer and sit in her desk chair across from it. It opens up to a login screen, requiring a password."
Abigail "There’s no way it would be this easy."
Abigail "I put in my birthday and the computer unlocks. \nOkay wow."
Abigail "This is too easy. Something's off."
Abigail "Why would she leave her laptop here? Did she trust me that much?"
Abigail "I go to a search engine on her computer and try to think of what I should enter to get my answers."
Abigail "I guess the easiest way is to start with my name."
Abigail "I type ‘Abigail Cooper’ into the search bar and a bunch of pictures of random women I don’t know pops up with a couple links to instagram and Facebook accounts."
Abigail "I guess I have a pretty common name."
Abigail "What year was I born? 2005. So that means when I went missing it was 2009?"
Abigail "I type ‘kidnapping in 2009’ into the search bar and wait for the search to finish loading."
Abigail "A couple articles come up with the missing posters attached next to it. I keep scrolling until I come across an article with the poster from my parents attic attached."
Abigail "‘4 year old Sofia Robinson goes missing’"
Abigail "That’s weird. Who is that? And why is my picture attached to her article?"
Abigail "I click on the link and begin to read."
Abigail "4 year old Sofia Robinson goes missing in the Nevada area. Mother, Maria Robinson and father, Daniel Robinson were on a walk with their daughter Sofia in the park when they got distracted by a little girl getting injured on the other side of the park. The parents rush to the girls aid, leaving Sofia alone on the playground. Unfortunately for these parents, while they are assisting another child, their daughter disappears. Witnesses say they did not see who might’ve taken Sofia, but say they did see two adults in the children’s park without a child. They described these adults the best they could, the woman was said to have pale white skin, brown hair and a slightly chubby build, looked to be about in her mid 30s. The man was said to also be white with balding hair and an almost overweight build, also said to be in mid 30s. Sofia is a 4 year old girl who is half white and half Mexican; she has grey eyes and very dark, almost black, brown hair. If anyone sees this child or even adults who seem to fit the descriptions of the adults in the south Nevada area, the parents beg that you contact the authorities immediately. The parents state, Sofia is our everything, we just want her to be safe and happy; we can’t live without our little girl. The Nevada police  department is working tirelessly to find answers and the detectives are doing all they can to find little Sofia.’"
Abigail "At the bottom of the article is the missing child poster with my picture."
Abigail "As I read the article, my face drops. I have Grey eyes and very dark brown hair. My mom is white and has brown hair. My dad is white and balding. The descriptions of the adults match them. And I match the description for Sofia."
Abigail "I’ve always wondered why I look so different from my parents; they’ve always said sometimes that’s just how genetics work."
Abigail "I am in complete shock as I try to take in all the information I just read."
Abigail "I am Sofia Robinson, my real name is Sofia Robinson. The people I live with now are not my real parents, Maria and Daniel Robinson are my real parents."
Abigail "The people I live with now kidnapped me and have kept me all these years."
Abigail "The people I live with now are dangerous."
Abigail "I have to find a way out." 
Abigail "I sit at the desk with my hands on my forehead. Okay I need to calm down, I need to breathe. Now is not the time to freak out, I don’t have time for this. I need to do whatever I can to get out of here without tipping my parents off."
Abigail "I need to really think this through and get all of the answers that I possibly can."
Abigail "I need to find my real parents." 
Abigail "I exit out of the article on my mom’s computer and turn it off. As I do, I hear the front door open."
hide Abigail
show Shannon
Shannon "I’m home Abigail!" 
hide Shannon
show Abigail
Abigail "It feels so weird hearing HER call me THAT. That’s not my real name, and she knows it."
Abigail "But again it would be weird hearing Sofia come out of anyone’s name, I’ve been Abigail for so long."
scene LivingRoom_DayLight
show Abigail
Abigail "Jerry also walks through the door and greets me, most likely just got home at the same time Shannon did, as I make my way down the stairs to greet them."
Abigail "I have to act normal. They can’t know I know."
hide Abigail
show Jerry
Jerry "How was your day honey?"
hide Jerry
show Abigail
Abigail "Oh it was good, just a lot of school work." 
hide Abigail
show Shannon
Shannon "We’re having meatloaf for dinner." 
hide Shannon
show Abigail
Abigail "Shannon brings herself and the bag of groceries she has to the kitchen and brings prepping for dinner."
Abigail "Jerry tries have a conversation with me, but I answer as minimally as I can."
hide Abigail
show Jerry
Jerry "What’s going on honey?" 
hide Jerry
show Abigail
Abigail "Jerry flashes me a concerned look."
hide Abigail
show Jerry
Jerry "Are you okay?" 
hide Jerry
show Abigail
Abigail "Oh, yeah I’m fine. Just tired. I feel like we do the same thing. every. single. day. I don’t know, I just feel. Stuck." 
Abigail "I reply trying to give my normal level of conversation so they don’t know that I know. 
Usually, when they would talk to me, I would fully confess anything and everything that I was feeling; I trusted them like that. We were each others best friends and I could talk to them about anything. Now, now it’s just weird, i don’t know how to feel."
Abigail "But I have to act normal, which means confessing some kind of feelings to them so that way they can think that the trust for them is still there. \nMy mom gives me a frown as I speak."
hide Abigail
show Shannon
Shannon "I get that, sometimes life feels like that for me too."
hide Shannon
show Jerry
Jerry "Me too. But it’s okay, we have each other!" 
hide Jerry
show Abigail
Abigail "Jerry comes and gives me a hug and then goes over to Shannon and gives her one as well."
Abigail "I give a soft smile as he does. Maybe they’re not so bad? It sounds like they care."

scene black with fade
"time passes"
scene DiningRoom_IndLight with fade
#time skip
show Abigail
Abigail "Time goes by and Shannon finishes dinner. We all eat together and Shannon and Jerry talked the entire time, while I sat there quietly."
Abigail "I know I’m showing that somethings wrong, but the excuse I came up with is just good enough for them that my actions and demeanor make sense."
hide Abigail
show Shannon
Shannon "You can go ahead and go upstairs honey, I’ll clean your plate." 
hide Shannon
show Abigail
Abigail" Shannon grabs my plate from me. I’ve been picking at the food and barely had three bites; I couldn’t bring myself to eat too much. I'm so confused, I don’t know if I can trust these people still, I’ve trusted them my entire life, but now it’s different, hell, they could’ve poisoned my food if they knew that I knew the truth."
Abigail "Thank you, I nod my head and get out of my seat. I make my way upstairs to my room, as I do, I can hear them both talking downstairs, I hope it doesn’t have anything to do with me."
scene McBedNight_DarkIndLight with fade
show Abigail
Abigail "I change my clothes and get into my bed. Everything feels so weird, there’s no way I’ll be able to sleep tonight."
Abigail "All I can think about is my real parents. Who are they?"
Abigail "Where are they?"
Abigail "I need to find them. I’m going to do more research tomorrow and see if I can find them and maybe contact them." 
Abigail "Maybe they’d help me."
Abigail "Or maybe they already moved on with their lives. It has been twelve years since I went missing. What if they had another kid? What if they just pretended I never existed?"
Abigail "What if they want nothing to do with me?"
Abigail "My thoughts run a million times a minute as I lay in my bed and try to doze off, at least a little."
#end scene 
scene black with fade
scene McBedDay_ExtLight with fade
show Abigail
#research scene 
Abigail "I wake up and sigh. Not only is this going to be just another day exactly like the others, it’s going to be a long day of trying to find answers."
Abigail "I get out of bed and get dressed and start the day like any other."
Abigail "I say bye to Jerry.."
scene LivingRoom_DayLight
#shows saying bye
show Abigail
Abigail "I do my school lessons with Shannon.." 
#show
show Abigail
Abigail "I do my schoolwork in my room alone.." 
scene McBedDay_ExtLight with fade
#show
show Abigail
Abigail "Shannon knocks on my door and enters my room, usually about the time where she asks to spend time with me and we watch a movie together."
hide Abigail
show Shannon
Shannon "Hey sweetie, I’m gonna go to the store a little earlier than usual today." 
hide Shannon
show Abigail
Abigail "That’s weird, it’s about 2:00 right now, she usually doesn’t go to the store for another hour or two."
Abigail "Oh, okay, any particular reason?" 
hide Abigail
show Shannon
Shannon "Nono, no reason, I just felt like going earlier today, thought I’d change it up a bit." 
hide Shannon
show Abigail
Abigail "I can tell she’s taking what I said seriously about our days always being the same, but it doesn’t matter much either way."
Abigail "Okay. Shannon leaves my room and I hear the front door close."
Abigail "I guess her trying to change things up is perfect for me, this gives me more time to find answers."
scene PBed_Day with fade
show Abigail
Abigail "I go into their room again and open and unlock Shannon’s computer."
Abigail "The fact that my birthday is her login does show that she cares a lot about me, maybe they’re not so bad?"
Abigail "Either way, I still need answers."
Abigail "How should I start? I guess looking up my parents is a good start." 
Abigail "I type ‘Maria Robinson’ into the search bar and press enter. Lots of Maria Robinsons pop up. \nUgh."
Abigail "I try to get more specific. I type ‘Maria Robinson Nevada kidnapped daughter’ that’s the most specific I can get with what I know."
Abigail "After twenty or so minutes of scrolling and searching, I find a Maria Robinson in another article describing the kidnapping of Sofia Robinson." 
Abigail "At the bottom of the article, after describing the kidnapping and how the police are searching for her, says if anyone finds any information on Sofia, the parents have requested that you contact them immediately at 745-334-2211."
Abigail "Found it. So now I have their phone number, that’s a good start."
Abigail "I write the phone number down onto a sticky note for later and type the number into the search bar, followed by ‘Robinson’ afterwards."
Abigail "After more searching and more scrolling, I eventually come across a kind of phone book website, with peoples names, phone numbers and addresses. I type in the phone number and Maria and Daniel Robinson pop up, followed by an address. 34 Freedbird Drive."
Abigail "Yes yes yes, this is all coming together."
Abigail "I write the address down on the sticky note below the phone number and type the address in the search bar."
Abigail "It shows on a map the distance I am from the address. Oh my god! I’m only two hours away from them."
Abigail "I could do this."
Abigail "I search for different modes of transportation and prices, train, taxi, etc. it seems like the best priced and best way to get there as quick as possible is by taxi, but there are no taxis just driving through my neighborhood, and if I tried to walk to a place that has taxis on foot, my parents would inevitably find me."
Abigail "I search for a train schedule and the nearest station. There seems to be a station thirty minutes away from my house, Shamrock Station. After searching the schedule, I find a train that leaves tomorrow at 5:30pm that goes right into the town my parents address is in. The station in their town seems to be about a ten minute walk from their house."
Abigail "That’s perfect, I could leave whenever my mom goes shopping again tomorrow, hoping she goes at her normal time. I’m sure I could find a ride, maybe hitchhike, to the train station and leave from there."
Abigail "I write down the name and the price of a ticket onto the sticky note."
Abigail "It seems like I have all of the information I need; phone number, name, address, train station, destination, and ticket price."
Abigail "Now I just need the money for the ticket; the ticket is priced at 40 dollars."
Abigail "I search in the drawers in the bedroom and eventually find a couple of bills lying around. I scrounge up all that I could find and count the total; 100 dollars, that’ll be perfect."
scene McBedDay_ExtLight
show Abigail
Abigail "I stand up out of the desk and head to my room where I begin to start packing a bag. I don’t need much, I consider the idea that bringing anything my parents gave me could be a bad idea. It could be tracked or even just bring up too many memories."
Abigail "I’m still not sure if I’m doing the right thing, these people seem to care about me a lot, but I have to know who my real parents are."
Abigail "I take off anything that means too much; my watch and my jewelry are a good start. They gave me a pair of earrings that I’ve never taken off; they claimed that I’ve had them since I was a baby, but now I don’t know if I can trust that either. Even if they are from my real parents, I can’t risk it."
Abigail "I take a pair of old clothes and shove them into my backpack. The most I can take with me from them is clothes, I can’t risk them finding me. I find the least unique outfit I can find and set it aside for me to wear tomorrow. The outfit is strictly dull colors and black, whereas I usually wear colorful outfits."
Abigail "Everything seems to be just about ready for me to go, all I need to do is write a note to leave behind. I set my backpack inside of my closet and walk over to my desk to begin writing as I hear the front door open."
Abigail "She’s home earlier than usual."
hide Abigail
show Shannon
Shannon "Abigail!" 
hide Shannon
show Abigail
Abigail "Coming!"
#end scene 

#surpirse scene
scene LivingRoom_DayLight with fade
show Abigail
Abigail "As I walk downstairs I also see Jerry there. That’s weird, he doesn’t get off of work for another hour or so."
hide Abigail
show Shannon
Shannon "Hi sweetie!" 
hide Shannon
show Abigail
Abigail "What’s going on? Why is dad home early?" 
Abigail "What are they planning? Do they already know I know?"
hide Abigail
show Shannon
Shannon "We’re switching up the normal routine! I’m going to make your favorite! Salmon cakes! I also bought a cake for us to have for dessert!"
hide Shannon
show Abigail
Abigail "Salmon cakes is a meal she would only make whenever salmon is in season, which it currently isn't, which shows she’s really trying to switch things up a bit, and it is my all time favorite meal. And as far as having a cake, we never have any kind of dessert, ever."
Abigail "While they would always pride themselves on being cool parents, they always had an issue with dessert, something about rotting your teeth."
Abigail "Oh wow! I try to act excited as I can, that’s awesome thanks! I’m excited!" 
hide Abigail
show Shannon
Shannon "Here! We can cook together! That’s something different too!" 
scene KitchenDayLight with fade
show Jerry
Jerry "We just wanted to change up the normal everyday routine with you, like you said, it’s getting a little draining," 
hide Jerry
show Shannon
Shannon "We noticed how upset you were and we wanted to try and cheer you up and make your day a little brighter, we thought changing the routine would help!" 
hide Shannon
show Abigail
Abigail "Wow, they really care. They cared enough to listen to what I had to say and do something about it."
Abigail "But this change also gets in the way of my plan, if they try and switch it up tomorrow, it could mess up the time I get to the train station."
Abigail "But they’re really trying.."
Abigail "Should I even still try to run away? They really care about me, maybe this is where I belong? They’ve pretty much raised me my entire life anyways, what does blood matter."
Abigail "But I also don’t know how dangerous they are, I feel like I barely know them now after finding out the truth. And I want to know who my real parents are."
Abigail "What should I do?"

menu:
    "Stay with them":
        jump StayWithThem
    "Still run away":
        jump StillRunAway
#!!!! Choice !!!! still run away or stay with them !!!!

label StayWithThem:
#stay with them choice 
Abigail "These are the people who raised me. They’re people I can trust, they’ve shown me my entire life that they are here for me no matter what."
Abigail "So what if they're not my blood parents? They’ve treated me like I am and made me their entire world."
Abigail "Running away right now and betraying them would completely break their hearts." 
Abigail "Besides, I love the life I’ve had so far, and who’s to say that going to live with my real parents would turn out to be any better."
Abigail "These parents have given me an amazing life, I can’t just take that for granted. They’ve done so much for me. I love them." 
Abigail "Thanks! I really appreciate you listening to me. The routine is getting tiring some days but it is OUR routine, I couldn’t ask for anything better. I like spending time with you both."
hide Abigail
show Shannon
Shannon "Aww sweetie!" 
hide Shannon
show Abigail
Abigail "My mom runs over to me and joins me in the hug with my dad."
hide Abigail
show Jerry
Jerry "How did we get so lucky with such a caring and kind daughter?" 
hide Jerry
show Shannon
Shannon "We really won the lottery huh?" 
hide Shannon
show Abigail
Abigail "My dad nods as we all giggle and separate."
hide Abigail
show Shannon
Shannon "Now let’s get cooking!" 
hide Shannon
show Abigail
Abigail "My mom grabs the groceries and spreads them out onto the counter."
Abigail "My dad stands beside my mother as we get started cooking. My dad has never really been a chef but he’s always tried when he needed to, like whenever my mom was sick and couldn’t do it herself. It usually ended up with the food being burnt, but he tried and that was all that mattered."
Abigail "My mom and I start cooking as she shows me how to make the salmon cakes. Usually it’s served with spaghetti, and I know how to make that, so once my mom gives me a quick crash course, we divide and conquer. I start making the spaghetti, and she starts making the salmon cakes."
Abigail "The entire time, my mom, my dad, and I are all laughing and talking. Now that I’ve taken a moment to appreciate my parents again, I realize just how lucky I really am." 
Abigail "My mom expresses to me how proud she is of me and my dad talks about how one day I can work with him as a mechanic. My mom and I both giggle at him as he says that, as we both know the last thing I want to do is get my hands dirty. My dad laughs as we explain this to him, and he explains that we can find another career that better suits my clean hands rule."
Abigail "We continue to joke like that the entire time we cook until we’re finally finished. We sit down at the table and enjoy our meal cooked to perfection with love. As cliché as that sounds, I now understand why people in movies always say the secret ingredient is love. I’ve never felt more loved than I do now, and this food tastes amazing because of it!"
Abigail "Once we finally finish eating, my mom brings the cake over to the table. The cake is a chocolate ganache cake and has chocolate covered strawberries on it."
Abigail "My mom and I both gush over how delicious it’s going to be, as we both LOVE chocolate cake. My mom cuts us each a piece as we sit and enjoy the dessert together."
Abigail "The cake tastes AMAZING!"
Abigail "And the entire time my family and I continue to talk and joke around and have a good time in each other's company."
Abigail "The night comes to a wonderful end as we put the cake away and sit and decide to watch a movie together."
Abigail "I sit between my mom and my dad as we put on a family favorite, the Addams family. As the television pulls up the show, I get comfortable between my parents."
Abigail "I can’t believe I almost took this for granted. My mom and dad have done an amazing job of raising me, and I couldn’t ask for better parents."
Abigail "They really care about me and love me and I’m very grateful for them and the life that I have."
Abigail "Nothing makes me happier than growing up with my amazing parents in this amazing house on Shamrock Lane." 
#end game

return 
label StillRunAway:
#still run away 
show Abigail
Abigail "These people are not my parents, they are criminals and deserve to be locked behind bars."
Abigail "How could they take a young child away from their parents? What sick people can live with themselves after doing that?"
Abigail "I’m in extreme danger even being in the same house with them, putting on this show for them so they don’t hurt me, or worse."
Abigail "I need to get out as fast as I can, I need them to not change the routine, so that way I can make my escape tomorrow."
Abigail "I just gotta keep up this mask for a little bit longer." 
Abigail "Thanks! The routine is getting tiring some days but it's what I’m used to, I don’t know if I could take something different every day, I’ve grown to like the routine." 
hide Abigail
show Shannon
Shannon "Aw sweetie, don’t worry, we’ll make sure this is a one time thing."
hide Shannon
show Jerry 
Jerry "Yeah don’t worry, we’ll stick to our habitual ways, besides, I can’t afford to leave work early every day." 
hide Jerry
show Abigail
Abigail "Shannon starts laughing along with him and I join in, trying to seem as normal as possible."
hide Abigail
show Shannon
Shannon "That’s very true, now let’s get cooking!" 
hide Shannon
show Abigail
Abigail "Jerry stands beside Shannon as I walk over to help cook. Jerry has never really been a chef but he’s always tried when he needed to, like whenever Shannon was sick and couldn’t do it herself. It usually ended up with the food being burnt, which is kind of embarrassing that you can’t take care of yourself or your child by yourself, but that shows he never really had to take care of me anyway."
Abigail "Shannon starts cooking and shows me how to make the salmon cakes. I pretend to be listening as she speaks and then goes to her started on the spaghetti while she does the salmon cakes."
Abigail "Shannon and Jerry are laughing and talking the entire time while we cook and I try to join in occasionally."
Abigail "Shannon starts to talk about how independent I am as she watches me cook. She starts to discuss with Jerry the idea of her getting a job, since, as she said, I'm old enough and responsible enough for me to be home alone while she works. Jerry brought up the idea of a stay at home job and Shannon said she liked the idea, they said they’d discuss it further later and begin job searching."
hide Abigail
show Jerry
Jerry "Maybe one day soon Abigail can get a job of her own too." 
hide Jerry
show Abigail
Abigail "Jerry pats his hand on my back and Shannon smiles and nods as she finishes up cooking."
Abigail "Isn’t that a lie. They’d never let me out of this house ever, not even in the backyard to play, there’s no way they’d let me get a job. There’s also no way they’d leave me home alone for days either, they claim they trust me, but they’re just trying to gain my trust."
Abigail "They can tell that they’re losing it."
scene DiningRoom_IndLight with fade
show Abigail
Abigail "We finally finished cooking and sat down at the table. Shannon and Jerry continue to talk the entire time while I try to eat the meal as quickly as possible."
Abigail "Once we all finish eating, Shannon gets up to grab the cake. The cake is a chocolate ganache cake and has chocolate covered strawberries on it."
hide Abigail
show Shannon
Shannon "Look, it’s our favorite!" 
hide Shannon
show Abigail
Abigail "Oh goodie! /n I spoke with the fakest excitement I could muster. That felt disgusting."
Abigail "I slowly eat my piece of cake as I try my best to engage in the stupidly loving conversations they’re trying to have. Once we finally finish eating the cake, Shannon suggests we all watch a movie or tv show together."
Abigail "I definitely do not want to do that, I can barely handle this act for this amount of time, I can’t take much more of this. I gotta come up with an excuse to leave." 
Abigail "Oh mom, I had such a long day today, while you were gone I finished the rest of my homework for the week!" 
Abigail "The word mom feels like sandpaper on my tongue."
hide Abigail
show Shannon
Shannon "Oh wow sweetie, I really am so proud of you, you’re so responsible with your schoolwork," 
hide Shannon
show Jerry
Jerry "How did we get so lucky with such a great daughter?" 
hide Jerry
show Abigail
Abigail "I throw up in my mouth a little as he says that."
Abigail "How’d we get so lucky with such a great daughter? You didn’t, you stole her, but alright."
scene McBedNight_DarkIndLight
show Abigail
Abigail "I fake a smile at them as I head up to my room and get into my bed."
Abigail "Ugh, last night in this miserable bed with these miserable people in this miserable house."
#end scene 
scene black with fade
scene McBedDay_ExtLight with fade
#escape scene final scene 
show Abigail
Abigail "Todays the big day! The day I’ll finally leave the restraints of these psychopaths."
Abigail "The day starts like any other day, obviously they took my advice when I said stick to the normal routine."
Abigail "I say bye to Jerry.."
scene LivingRoom_DayLight
#show
show Abigail
Abigail "I do my school lessons with shannon.." 
#show
show Abigail
scene McBedDay_ExtLight
show Abigail
Abigail "I do my schoolwork in my room alone.." 
#show
Abigail "Shannon asks to spend time with me.."
#show
scene LivingRoom_DayLight
show Abigail
Abigail "We watch another movie.."
#show
Abigail "And then she leaves for the grocery store again." 
#Show
Abigail "Today I caved in and watched a movie with her, I didn’t wanna tip her off that this would be the last time she’d see me ever again."
Abigail "But finally, right on time, she leaves for the grocery store. As soon as she leaves, I change into my dull clothes and begin writing a note."
hide Abigail
"Dear Shannon and Jerry, 
I know the truth, I know what you really are. You’re criminals, kidnappers. You took me from my parents when I was a child. 
You’re evil, evil people and I don’t know how you kept this from me for so long, but I know you knew this was coming. 
You couldn’t keep such a huge secret from me for my entire life. 
And now I know. 
I’m leaving and I’m finding my real parents. The people you ripped me away from twelve years ago. 
I hope you both rot in hell for what you did. 
Sincerely, Sofia."
show Abigail
Abigail "It feels so weird signing it with my real name, but it feels right that they know that I’m not the girl that they raised, I’m the girl that my parents gave birth to, and that’s who I’ll be for the rest of my life."
Abigail "I’ll never be Shannon and Jerry’s child ever again, not like I ever truly was."
Abigail "I grab my backpack and throw it over my shoulders, I also grab the sticky note and shove it into my pocket."
Abigail "It’s currently 4:30pm. The first step of my plan is to find someone to drive me to the train station."
Abigail "Well technically the first step is to step foot outside of this house, which I’ve never done before ever."
Abigail "I walk downstairs and open the front door. I didn’t even stop to consider what the rest of the world may look like. Is it as scary as these people said? Or were they just trying to keep me from escaping? Or keep me inside so no one could ever find the child that went missing?"
Abigail "I look around outside and everything looks, normal."
scene Poarch with fade
show Abigail
Abigail "Normal people going on a normal walk with normal faces. No one’s scowling at me, the sky isn’t dark and scary. The sun is actually out and beaming on this gorgeous day."
"I take my first step outside of the house and onto the sidewalk." 
Abigail "The sidewalk doesn’t swallow me alive like quicksand, that’s a good first step."
Abigail "I close the front door behind me and take in all this new information. The outside is normal, in fact, it’s beautiful. It looks just like all the movies I’ve seen, but better, more realistic."
Abigail "This is just like Tangled and I’m rapunzel. I don’t know how I didn’t get the hint when Shannon always watched that movie with me. She was always the evil stepmother, she just had Jerry by her side. They were keeping me from the outside world for their own benefit, so they made me think that the world was a much more dangerous place than it really is. In fact, they’re the true dangerous ones. And I’ve finally escaped."
Abigail "I smile and I start to quickly walk away from the house, searching for someone that I can find to drive me to the train station."
Abigail "I continue walking for about ten minutes until I see someone getting out of someone else’s car. I watch from afar as the passenger gets out of the back seat and waves thank you to the driver, the driver waves back as he sits there on his phone. The back window of his car says Uber, what is that?"
Abigail "The exchange between those people seemed to be a transactional one, maybe he’ll help me too."
scene UberCar with fade
show Abigail
Abigail "I run up to the driver’s side of the car and knock on the window. The man rolls down his window and looks at me."
hide Abigail
show UberDriver
Uber "Can I help you?"
hide UberDriver
show Abigail 
Abigail "Hi yes, what’s Uber?" 
hide Abigail
show UberDriver
Uber "It’s an online taxi service, through an app. What era do you live in, the 1900s?" 
hide UberDriver
show Abigail
Abigail "Oh perfect! Could you give me a ride?" 
hide Abigail
show UberDriver
Uber "Do you have the app?"
hide UberDriver
show Abigail
Abigail "I don’t even have a phone. \nThe man raises his eyebrow."
hide Abigail
show UberDriver
Uber "Can you pay?"
hide UberDriver
show Abigail
Abigail "Yes I can!" 
hide Abigail
show UberDriver
Uber "Alright, get in the back." 
scene BackOfCar
show Abigail
Abigail "I smile as I open the backseat and get in. I’ve only been in a car once before, when Shannon and Jerry decided to take me out to eat once to celebrate me graduating middle school with honors. Ever since then that’s been a privilege I haven’t been able to earn."
Abigail "I get in the seat behind the passenger side and put on my seatbelt."
hide Abigail
show UberDriver
Uber  "Where do you wanna go and how much do you have, kid?"
hide UberDriver
show Abigail
Abigail "I need to get to the Shamrock train station please, I have 50 dollars, is that enough?"
hide Abigail
show UberDriver
Uber  "That’ll do." 
hide UberDriver
show Abigail
Abigail "He starts the car and begins driving. I look out the window and watch the people and houses pass by as we get farther and farther from the place that has been my prison for almost my entire life."
Abigail "This is really happening. I can’t believe this is really happening. I’m really getting out. All thanks to this nice Uber man."
scene black with fade
scene TrainStation
show Abigail
#time skip
Abigail "After about thirty minutes we eventually make it to the train station."
hide Abigail
show UberDriver
Uber  "We’re here kid, pay up." 
hide UberDriver
show Abigail
Abigail "The man speaks and unlocks the doors and holds his hand out.\nI pull the 50 dollars out of my backpack and hand it to him as I get out of the car."
Abigail "Thank you mister." 
hide Abigail
show UberDriver
Uber  "Good luck with wherever you’re going." 
hide UberDriver
show Abigail
Abigail "The man speeds away once I close the door. \nI turn around and face the train station behind me. Shamrock Station is plastered in big letters above the entrance. Just at the entrance is a bunch of people in line in front of people sitting behind a glass wall. I assume that’s where the tickets are being sold."
Abigail "I get into line and check the time, 5:15. The train will be here soon, and no sight of Shannon or Jerry."
Abigail "Soon I’m next in line and walk up to the person behind the glass."
Abigail "Hi, a ticket to uh, I take the sticky note out of my pocket, to the train station near freebird please. I never found of the name of the station I was going to, I hope that wasn’t important."
Ticket "40 dollars please." 
Abigail "The lady speaks in a monotone. Oh goodie, they didn’t need to know what station, just what area. Awesome! \nI hand the lady my 40 dollars and she hands me back a ticket."
Abigail "Have a nice day, I say smiling as I walk past the ticket area and into the station. I see train tracks on all sides of me as I look at what my ticket says."
Abigail "‘5:30, Freebird’ I guess since my parents house is so close to the train station, their street is named after the area they live in as well as the train station."
Abigail "I look around at the signs above me and search for one that says freebird. Eventually I find the train pulling in as it says freebird on the side."
Abigail "Oh my gosh! There it is!"
Abigail "I quickly walk up to the train and give the man my ticket. He motions me onboard and I walk inside the train."
Abigail "It’s a very nice and clean train, much like the ones I’ve seen in movies, which I was expecting."
Abigail "There are people sitting scattered around everywhere and I eventually find a seat in a corner."
Abigail "Once I sit down, the train doors start to close and the train begins to move forward."
Abigail "This is really happening!"
scene black with fade
scene Neighborhood with fade
#time skip 
show Abigail
Abigail "Two hours go by before the train finally comes to a stop."
Abigail "The entire ride I couldn’t stop thinking."
Abigail "What if they don’t want me anymore? What if they’ve moved on? What if they don’t recognize me? What if they don’t believe me?"
Abigail "So many doubts, but also, so much excitement."
Abigail "I’m going to be with my real parents. I’m going to be able to have a normal life, with normal parents and even make friends. What if I have siblings? They’ll automatically be my friends too."
Abigail "As the train doors open, I stand up and put my backpack back onto my back. I step outside and am greeted with a pleasant sunny breeze."
Abigail "The last thing I have to do is find a way to my parents house."
Abigail "Whenever I found how far their house was from the train station, I studied the route over and over until I finally had it memorized."
Abigail "All it is is a five minute walk east to a neighborhood titled Farway Nest, then once I’m there, I walk until I see the street sign freebird drive and walk to house 34."
Abigail "I’m almost there."
Abigail "I begin walking east until I come across the neighborhood. As I walk through the neighborhood, the houses all look unique in their own way, not like my old neighborhood where every house was the exact same. All of these houses seem to have their own level of character to them; a window to the personalities of the people living in them."
Abigail "I finally come across the street sign, Freebird Drive, here we go!"
Abigail "I start to pick up my pace as I cross the street and read all the mailbox numbers.."
Abigail "14.."
Abigail "20.."
Abigail "26.."
Abigail "34!"
scene RealHouse 
show Abigail
Abigail "I stand on the sidewalk in front of the driveway of the house. The house is a dark brown house with red brick detailing. There’s a lighter brown for the door and the front yard has a beautiful path leading from the driveway to the front door of light red brick, surrounded by white daisies on either side."
Abigail "This is it, 34 Freebird Drive."
Abigail "This is the moment I’ve been waiting for. It’s time to finally meet my real parents."
Abigail "God I hope they like me."
Abigail "I walk across the path of brick to the front door. I stand there for a moment, taking a deep breath before I ring the doorbell." 
Abigail "I hear the bell ring faintly through the house as I hear shuffling on the other side of the door."
Abigail "The front door opens and reveals a pale, tall man standing in front of me. He has full, soft looking dark brown hair with facial hair and hazel eyes that flash an expression of confusion."
Abigail "His eyes change from confusion to shock as he looks at me up and down."
hide Abigail
show Daniel
Daniel "Maria!" 
hide Daniel
show Abigail
Abigail "He yells and his voice cracks with every syllable." 
hide Abigail
show Daniel
Daniel "Get over here!"
hide Daniel
show Abigail
Abigail "He continues to stare at me dumbfounded as I just stand there. I hear shuffling as a figure comes up behind him."
hide Abigail
show Maria
Maria "What is i-" 
hide Maria
show Abigail
Abigail "The woman has a tan complexion, most likely Hispanic and had curly brown hair. She has a kind, soft face with beautiful blue eyes. She starts to speak as she comes up behind the man before suddenly stopping her sentence short once she sees me."
hide Abigail
show Maria
Maria "Is that?" 
Abigail "She mutters quietly and looks at me with wide eyes. The man looks at me and whispers quietly."
hide Maria
show Daniel
Daniel "Sofia?" 
#change main character name to Sofia
hide Daniel
show Abigail
Sofia "My eyes start to water as he speaks. My real name has felt so foreign until now, coming out of his mouth, it sounds so perfect. I nod my head quietly as my throat catches and tears begin to run down my face."
Sofia "Both adults begin sobbing as they wrap their arms around me tightly in a warm hug."
Sofia "We all stand there in each other's company for some time before they pull away."
hide Abigail
show Maria
Maria "Is it really you?" 
hide Maria
show Abigail
Sofia "The woman, my mother, speaks to me as she strokes my face."
Sofia "Hi, I say quietly, my voice starts to crack as they both hug me again."
hide Abigail
show Daniel
Daniel "I can’t believe it’s really you, you’re really here. Where have you been?" 
hide Daniel
show Maria
Maria "Oh, that doesn’t matter right now, let’s just enjoy the fact that she’s finally back in our arms. We can get all the details once she’s settled." 
scene black with fade
show Abigail
Sofia "My dad nods as my mother speaks, they both lead me inside, wiping their tears away as they do."
Sofia "Eventually the awkwardness floats away and we all begin to catch up. I explain to them how I was kidnapped and how I didn’t know for so long. Their faces flash in shock as I tell them what happened, then to rage."
Sofia "My parents call the police and eventually they find and arrest Shannon and Jerry, they get put on trial and sentenced to life in prison, and my case is finally closed twelve years later."
Sofia "After my parents and I catch up, I get settled into the house and find my room. Over the course of a couple weeks, I eventually get the power to decorate my room how I want and get all brand new clothes."
Sofia "Eventually I’m able to start going to real school and I make some friends along the way, the only good thing from being homeschooled with those dangerous people was that I’m much more ahead of my classmates as far as the curriculum. My parents say it’s just because I’m very smart, and that I get it from my dad."
Sofia "After a little while, everything starts to feel normal, but in the most amazing way."
Sofia "My parents immediately accepted me and have been looking for me the entire time. They showed me all of their research and open ends that got them nowhere. They never once gave up on me."
Sofia "My parents are the kindest, most loving people I think I’ve ever met. My dad is a software engineer and my mom is a teacher, a perfect combination of brains and kindness."
Sofia "They never fail to shower me in love every time they see me, they said after losing me once, they’ll never take a second for granted again."
Sofia "I don’t think I could be any happier than I am now."
Sofia "Now that I’ve finally escaped from that house on Shamrock Lane."
#end game 
return 