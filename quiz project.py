print("Welcome to my Cybersecurity quiz!")

score = 0

print("What does HTTPS stand for?")
 
print("A) Hypertext Transfer Protocol Secure")
print("B) High Transfer Text Protocol System")
print("C) Hypertext Transmission Protocol Standard")
print("D) Hyper Technical Transfer Protection")

answer = input("Is the answer A, B, C or D")


if answer.upper() == "A":
 
    print("Correct")
    

    score = score + 1 


else:
    print("Incorrect")

print(f"You've scored {score} out of 1 so far")


print("What is the name of the attack that exploits victims by using phone calls to steal sensitive data?")

print("A) Smishing")
print("B) Farming")
print("C) Whaling")
print("D) Vishing")

answer = input("Is the answer A, B, C or D")

if answer.upper() == "D":
 
    print("Correct")
    

    score = score + 1 


else:
    print("Incorrect")

print(f"You've scored {score} out of 2 so far")

print("What is a zero-day vulnerability?")

print("A) A virus that deletes files after midnight")
print("B) A flaw that is exploited before the developer has issued a fix")
print("C) A firewall that blocks all incoming traffic")
print("D) An attack that targets mobile devices only")

answer = input("Is the answer A, B, C or D")

if answer.upper() == "B":
 
    print("Correct")
    

    score = score + 1 


else:
    print("Incorrect")

print(f"You've scored {score} out of 3 so far")

print("What is the principle of least privilege?")

print("A) Firewalls should block all suspicious traffic by default")
print("B) All employees share the same password")
print("C) Users should only have the minimum access rights they need")
print("D) Only admins can use the internet")

answer = input("Is the answer A, B, C or D")

if answer.upper() == "C":
 
    print("Correct")
    

    score = score + 1 


else:
    print("Incorrect")

print(f"You've scored {score} out of 4 so far")

print("What is a rainbow table used for?")

print("A) Generating random encryption keys")
print("B) Mapping IP addresses to domain names")
print("C) Monitoring network traffic in real time")
print("D) Cracking hashed passwords using precomputed values")

answer = input("Is the answer A, B, C or D")

if answer.upper() == "D":
 
    print("Correct")
    

    score = score + 1 


else:
    print("Incorrect")

print(f"Quiz complete you've scored {score} out of 5!")



