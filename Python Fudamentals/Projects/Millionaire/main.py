questions =[
["Who is the first president of India","Rajendra Prasad","Narendra Modi","Jawaharlal Nehru","Mahatma Gandhi",1],
["What is the capital of India","Mumbai","New Delhi","Chennai","Kolkata",2],
["Which planet is known as the Red Planet","Earth","Venus","Mars","Jupiter",3],
["Who invented the telephone","Alexander Graham Bell","Thomas Edison","Isaac Newton","Albert Einstein",1],
["What is the largest ocean in the world","Indian Ocean","Atlantic Ocean","Pacific Ocean","Arctic Ocean",3],
["Which animal is known as the King of the Jungle","Elephant","Lion","Tiger","Leopard",2],
["How many days are there in a leap year","364","365","366","367",3],
["What is the national flower of India","Rose","Lotus","Sunflower","Lily",2],
["Which gas do plants absorb","Oxygen","Nitrogen","Carbon Dioxide","Hydrogen",3],
["Which is the smallest prime number","0","1","2","3",3]
]

for question in questions:
  print(question[0])
  print(f"1. {question[1]}")
  print(f"2. {question[2]}")
  print(f"3. {question[3]}")
  print(f"4. {question[4]}")

  ans=int(input("Enter your answer: "))
  if(question[5]==ans):
    print("Correct!!!")
  else:
    print(f"Wrong!!! \n Answer is {question[5]}")
    break
    