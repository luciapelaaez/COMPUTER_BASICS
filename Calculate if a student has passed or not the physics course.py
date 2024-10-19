print ("I´m going to tell you if you have passed or failed the physic's course.")
total_classes = 40
attended_classes= int (input("There are 40 classes in total,please tell me how many you have attended.") or 32)

def evaluate_attendance (total_classes,attended_classes):
    percentage_attendance= (attended_classes/total_classes)*100
    return percentage_attendance

percentage_attendance = evaluate_attendance(total_classes, attended_classes)

exam_score= int (input ("Now please give me your exam score,(out of 100) and I will finally tell you if you have passed or not, given your attendance percentage")or 75)
if exam_score >= 70 and percentage_attendance >= 80:
    print("Congratulations! You have passed the physics course.")
else:
    print("Sorry, you have failed the physics course.")


