#Opening page
import instructions
import taskCreater
import taskPopulator

instructions.showInstructions()

taskPopulator.requestTaskName()

taskPopulator.requestTaskTime()

taskPopulator.requestTaskPriority()
#Eventually could break down insert attribute so tasks are added once at a time.
taskPopulator.insertAtribute()



