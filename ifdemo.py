# If Demo

subj1grade = int(input("Enter grade for Subject 1: "))
subj2grade = int(input("Enter grade for Subject 2: "))
subj3grade = int(input("Enter grade for Subject 3: "))
subj4grade = int(input("Enter grade for Subject 4: "))
subj5grade = int(input("Enter grade for Subject 5: "))

average = (subj1grade + subj2grade + subj3grade + subj4grade + subj5grade) / 5

print(f"Your average grade is {average}")

if average >= 90:
    print("You are excellent!")
elif average >= 70:
    print("You passed")
    print("Congratulations!")
else:
    print("You failed")