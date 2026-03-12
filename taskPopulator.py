#function to check the input doesn't exceed the maximum length capacity (to protect neat table formatting)


def checkInputLength(field):
    if len(field) > 50:
        return True
    else:
        return False
    

def requestInput():
    taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
    exceedsMaxLength = checkInputLength(taskName)
    while exceedsMaxLength:
        print("Your description is too long. PLease re-enter a description that does not exceed 50 characters.")
        taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
        exceedsMaxLength = checkInputLength(taskName)
      
    return taskName

#simplify this function as you progress by making it like this insertAtribute(field,index)
def insertAtribute():
    new_task[0] = taskName
    print(new_task)

