#function to check the input doesn't exceed the maximum length capacity (to protect neat table formatting)

exceedsMaxLength = False

def checkInputLength(field):
    if len(field) > 50:
        exceedsMaxLength = True
    

def requestInput():
    taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
    checkInputLength(taskName)
    while exceedsMaxLength:
        print("Your description is too long. PLease re-enter a description that does not exceed 50 characters.")
        taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
    return taskName

print("CHECK POINT: Works up to here")


#def insertAtribute(field,index):


