# squares

squares = [i**2 for i in range(1, 100)]
print(squares)


remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)


movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption",
"Toy Story", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life",
"The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters",
"To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey",
"Raiders of the Lost Ark", "Groundhog Day", "Close Encounters of the Third Kind"]

gmoveies = [title for title in movies if title.startswith("G")]
print(gmoveies)

movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001),
("It's a Wonderful Life", 1946), ("Gattaca", 1997),
("No Country for Old Men", 207), ("Rear Window", 1954),
("The Lord of the Rings: The Fellowship of the Ring", 2001),
("Groundhog Day", 1993), ("Close Encouters of the Third Kind", 1977),
("The Royal Tanenbaums", 2001), ("The Aviator", 2004),
("Raiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movies2 if year < 2000]
print(pre2k)