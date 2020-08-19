from csinscapp import *
from trace_goto import *

app = CSinSCApp()

clicky = Button()
clicky.x = 100
clicky.y = 50
clicky.data = "Slide >>"
clicky.width = 85
clicky.height = 25
app.add(clicky)

app.run()

label .next_event

event = app.wait_for_event(CLICK)

if event.control == clicky:
  clicky.x = clicky.x + 10

goto .next_event


  
