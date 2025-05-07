eng = int(input("enter English marks"))
mar = int(input("enter marks of marathi"))
hindi = int(input("enter marks of hindi"))

total_percentage = (100*(eng+mar+hindi))/300

if (total_percentage>=35 and eng>=33 and mar>=33 and hindi>=33):
    print("Pass", total_percentage)
else :
     print("failed",total_percentage)