#function to check the input doesn't exceed the maximum length capacity (to protect neat table formatting)

def createTask():
    #Task created with placeholder values

    #Index 3 is for priority, Index 4 is for task length
    new_task = list(range(5))
    return new_task

taskName = "Empty"

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
    new_task = createTask()
    new_task[0] = taskName
    print(new_task)


