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

 #need to make this a more generic function that can be recycled for all of the inputs   
 #I decided to make this function just for the name because the other inputs have to be manipulated before being added to the list.
def requestTaskName():
    taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
    exceedsMaxLength = checkInputLength(taskName)
    while exceedsMaxLength:
        print("Your description is too long. PLease re-enter a description that does not exceed 50 characters.")
        taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
        exceedsMaxLength = checkInputLength(taskName)
    return taskName

def requestTaskTime():
    timeUnit= str(input(""""Estimate how long you think it will take to complete the task. 
                            First, specify if your estimate is in hours, minutes or number of Pomodoro session
                            For hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."""))
    validTimeUnits = ['h','H','M','m','P','p']

    while timeUnit not in validTimeUnits:
        print("The time unit you entered is in valid.")
        timeUnit = str(input("For hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."))
        return timeUnit
    
    pomodoroNo = 0

    if timeUnit == 'H' or timeUnit == 'h':
        taskTime = float(input("Enter your estimate of how long it will take to complete the task in HOURS."))
        pomodoroNo = taskTime / 2.4
        pomodoroNo = round(pomodoroNo, 0)
        return pomodoroNo

    elif timeUnit == 'M' or timeUnit == 'm':
        taskTime = int(input("Enter your estimate of how long it will take to complete the task in MINUTES."))
        pomodoroNo = taskTime / 25
        pomodoroNo = round(pomodoroNo, 0)
        return pomodoroNo
    
    else:
        taskTime = int(input("Enter your estimate of how long it will take to complete the task in number of POMODORO sessions."))
        pomodoroNo = taskTime 
        return pomodoroNo
    taskTime = str(input)

#simplify this function as you progress by making it like this insertAtribute(field,index)
def insertAtribute():
    new_task = createTask()
    new_task[0] = taskName
    new_task[1] = pomodoroNo
    
    print(new_task)

#works up to here

