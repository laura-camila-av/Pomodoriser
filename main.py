#Opening page

#Eventually could break down insert attribute so tasks are added once at a time.
if __name__ == "__main__":
    import taskPopulator
    import instructions
    
    instructions.showInstructions()

    taskName = taskPopulator.requestTaskName()
    pomodoroNo = taskPopulator.requestTaskTime()
    taskPriority = taskPopulator.requestTaskPriority()
    taskPopulator.insertAtribute()



    

