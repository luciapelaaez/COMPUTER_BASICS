#First I will ask his or her name to present eachother
name=str(input("Hi! I'm interested in becoming in your new friend, what's your name?"))
print ("Nice to meet you", name, "!")

#Now I'm asking the user his or her birth to calculate his or her age

from datetime import date

year=int(input("What year were you born?"))
month=int(input("Which month?"))
day=int(input("And in which day?"))
user_date = date (year,month,day)

#Obtein the actual date
today = date.today()
# Calculate the age of the user
age = today.year - user_date.year - ((today.month, today.day) < (user_date.month, user_date.day))
# Show the age
print("OH, so you are", age, "years old.")

#Let the user talk about him or herself a bit and then ask for her or his hobbies
user_answer = (input(f"What do you think about being {age} years old? "))
print ("I agree with you with you!")

user_input= str (input("By the way, what are your hobbies?"))
# Extract the relevant part of the answer
if "i like" in user_input.lower():
    # Extract the parte after "i like"
    hobbies_string = user_input.split("i like")[-1].strip()
    # If there is a comma, separate the hobbies
    hobbies = [hobby.strip() for hobby in hobbies_string.split(",")]
    # Format the answer
    if len(hobbies) > 1:
        hobbies_response = ", ".join(hobbies[:-1]) + " and " + hobbies[-1]
    else:
        hobbies_response = hobbies[0]
    
    print(f"That sounds interesting! I have never tried {hobbies_response}, but I would love to!")
else:
    print(f"That sounds interesting! I have never tried {user_input}, but I would love to!")


#Ask the user how he or she feels today and answer depending on that
today= str(input("And how are you feeling today, fine or bad?"))
if today== "fine" or today== "Fine" or today== "FINE":
    print("I'm glad you had a lovely day!")
else:
    print("I'm sorry,sometimes days can be tough. By the way, you can try to talk to someone you trust about how you feel, do something you enjoy, like listening to music or going for a walk. Just remember that there is always a new day to start over!")







