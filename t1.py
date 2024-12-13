project_score = int(input("Enter the project score: "))
internal_score = int(input("Enter the internal score: "))
external_score = int(input("Enter the external score: "))
if(project_score>=50 and internal_score>=50 and external_score>=50):
    project=(project_score*70)/100
    internal=(internal_score*10)/100
    external=(external_score*20)/100
    total= project+internal+external
    if(total>=90):
        print("A Grade")
    elif(total>80):
        print("B Grade")
    else:
        print("C Grade")
else:
    if(project_score<50):
        print("You're failed in project with score: ",project_score)
    if(internal_score<50):
            print("You're failed in internal with score: ", internal_score)
    if(external_score<50):
                print("You're failed in external with score: ", external_score)

