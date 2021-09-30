#Group Project, Coded by Cory, story by partner #
print('Interactive Story')
# Loop Code #
for x in " 5 4 3 2 1 Go ":
  print(x)
name= input("What is your name? \n")
print("You are " + name +" and a boy. \nYou take interst in girl in your college class. She starts \ntalking about a guy she likes.")
print('Do ask her out to a movie?')
# Output/input #
movie =int(input("1) Yes \n2) No \n")) 
# Conditionals # 
if movie == 1:
  print("She agrees but asks if she can bring her friends.")
  print("Do you allow her to bring friends?")
  #  Function #
  friend =int(input("1) Of Course \n2) I'd rather it be just us \n"))
  if friend == 1:
    print("You go to watch the movie with her and her friends. Inside the theater \n you notice a seat open next to her and one open away from her.")
    seat =int(input("1) Sit next to her \n2) Sit away from her \n"))
    if seat == 1:
      print("You both hit it off well. Later that night you both hookup")
    if seat == 2:
      print("You distance yourself from her on the first date. She ends up leaving soon afterwards. Smooth move")
  if friend == 2:
    print("She tells you she's comfortable with seeing the movie with just you.")
    print("A week later you both meetup at the theatre. She asks what movie you should \n both watch.")
    # Operator #
    moviechoice =int(input("1) Mall Cop 3 \n2) Whatever is playing next \n"))
    if moviechoice == 1:
      print("Nobody likes Paul Blart except you. The night is a disaster. Good job " + name+" ")
    if moviechoice == 2:
      print("Suprisingly it turns out well.")
      print("During the movie you hesitate to hold her hand.")
      final =int(input("1) Hold her hand \n2) Do nothing \n"))
      if final == 1:
        print("You reach over and hold her hand. The date goes well and you plan your next \n date together.")
      if final == 2:
        print("She sees you hesitate and grabs your hand instead. The date goes well \nand you plan your next date together.")
if movie == 2:
  print ("You sit there awkwardly in silence.")
  print ("You lost your chance to ask her out. A new guy in class asks her out. \nWhat do you do about it?")
  fight =int(input("1) Fight him \n2) Try to forget \n"))
  if fight == 1:
    print("You tried to fight him and failed. You die in the hospital later \nthat night from your injuries.")
  if fight == 2:
    print("The news that night reports that a boy by the name \nof " + name +" was found dead after taking their own life")

    # Mayjah story #
