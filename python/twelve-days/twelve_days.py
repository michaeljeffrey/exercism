def recite(start_verse, end_verse):

    days = [  # list of days and gifts
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves, "),
        ("third", "three French Hens, "),
        ("fourth", "four Calling Birds, "),
        ("fifth", "five Gold Rings, "),
        ("sixth", "six Geese-a-Laying, "),
        ("seventh", "seven Swans-a-Swimming, "),
        ("eighth", "eight Maids-a-Milking, "),
        ("ninth", "nine Ladies Dancing, "),
        ("tenth", "ten Lords-a-Leaping, "),
        ("eleventh", "eleven Pipers Piping, "),
        ("twelfth", "twelve Drummers Drumming, ")
    ]

    song = []
    
    while start_verse <= end_verse: # sing at start verse until the end
        
        day = start_verse - 1  # since we index the first item as 0
        
        # line intro
        line = f"On the {days[day][0]} day of Christmas my true love gave to me: "

        while day >= 0:  # loop in the gifts of each day
            
            # sometimes you need 'and'
            and_word = ""
            if day == 0 and start_verse != 1:
                and_word = "and "
                
            line = line + f"{and_word}" + f"{days[day][1]}"  # combine the line of gifts
            day -= 1
            
        song.append(line)
        start_verse += 1
    
    return(song)
