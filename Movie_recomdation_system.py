name = input("Enter your name : ")
age = int(input("Enter your age : "))
genre = input("Enter your genere : ").lower()

if((age<=13)and(genre == "horror")):
    print("movies --> Bhootnath , Makdee")
elif((age<=13)and(genre == "comedy")):
    print("movies --> Chillar Party , Taare Zameen Par , Stanley Ka Dabba")
elif((age<=13)and(genre == "action")):
    print("movies --> Krrish , Krrish 3 , Ra.One ")
elif((age<=13)and(genre == "historical")):
    print("movies --> Tanhaji , Mohenjo Daro , Bajirao Mastani")
elif((age<=13)and(genre == "Thriller")):
    print("movies --> Jagga Jassos , Bhediya ")

if((18<age<13)and(genre == "horror")):
    print("movies --> Stree , Tumbbad")
elif((18<age<13)and(genre == "comedy")):
    print("movies --> 3 Idiots , Hera Pheri , Munna Bhai MBBS")
elif((18<age<13)and(genre == "action")):
    print("movies --> War , Pathaan , jawaan ")
elif((18<age<13)and(genre == "historical")):
    print("movies --> kesari , Padmawat , RRR")
elif((18<age<13)and(genre == "Thriller")):
    print("movies --> Drishyam , Andhadhun ")

if((age>=18)and(genre == "horror")):
    print("movies --> Tumbbad , 1920")
elif((age>=18)and(genre == "comedy")):
    print("movies --> Delhi Belly , Go Goa Gone , Jindagi Na Milega Dobara")
elif((age>=18)and(genre == "action")):
    print("movies --> Animal , kabir Singh , Dhurandhar ")
elif((age>=18)and(genre == "historical")):
    print("movies --> Patmavaat , Bajirao Mastani , Jodha Akhbar ")
elif((age>=18)and(genre == "Thriller")):
    print("movies --> NH10 , Raman Raghav , Andhadhun ")
