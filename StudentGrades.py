def grading():
    project_score=float(input("Enter the Student's project score"))
    internal_score = float(input("Enter the Student's internal score"))
    external_score = float(input("Enter the Student's external score"))
    if project_score < 0 or internal_score < 0 or external_score < 0:
        print("Scores cannot be negative.")
        return

    if(project_score>=50 and internal_score>=50 and external_score>=50):
        total=project_score+internal_score+external_score
        if(total>90):
            print("A Grade")
        elif(total>80):
            print("B Grade")
        else:
            print("C Grade")
    else:
        if(project_score<50):
            print("You're Failed in project with score: ",project_score)
        if(internal_score<50):
            print("You're Failed in internal with score: ", internal_score)
        if(external_score<50):
            print("You're Failed in external with score: ", external_score)
grading()