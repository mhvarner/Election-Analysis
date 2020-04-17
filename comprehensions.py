word = "halibut?"

#Loop through each letter in the string
#and push to an array
letters = []
for letter in word:
    letters.append(letter)
print(letters)
#------------------------------------------------
names=["biLly","boB","joE","meRe","hUnter"]
print(names)

namesLowerCase= [name.lower() for name in names]
print(namesLowerCase)

namesTitle= [name.title() for name in names]
print(namesTitle)
#------------------------------------------------
july_temperatures = [87, 85, 92, 79, 108]
hot_days=[]
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
        print(hot_days)
