string= "ijoYitvFDXrewst#Y$65u6&GyHJghfcjtey4w532a^$S85(*&ohinyuiy futdyrw6e 4e8t yuvftcrde7r%*^7gituvcYRey"
current_number = ""
listofnumbers = []
for char in string:
    if char.isdigit():
        current_number += char
    elif current_number:
        listofnumbers.append(int(current_number))
        current_number = ""
if current_number:
    listofnumbers.append(int(current_number))
print("Numbers in the input string:")
print(*listofnumbers)