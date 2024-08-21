gifts = ["twelve Drummers Drumming, ", "eleven Pipers Piping, ", "ten Lords-a-Leaping, ",
         "nine Ladies Dancing, ", "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ",
         "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ",
         "two Turtle Doves, ", "a Partridge in a Pear Tree."]
days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
        "ninth", "tenth", "eleventh", "twelfth"]

def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]

def verse(n):
    song = f"On the {days[n - 1]} day of Christmas my true love gave to me: "
    for i in range(n, 1, -1):
        song += gifts[-i]
    song += ('and ' if n != 1 else '') + gifts[-1]
    return song