print("*** Welcome to Pomodoro Timer ***")
t = input("Will you be inputting the study time in minutes or hours?\nPlease enter M for minutes and H for hours: ")
time = int(input("How long would you like to study for? "))
short_break = 0
if t == "M":
  #converting minutes into hours:
  #hour_val = time / 60
  #print("You will be studying for:" ,hour_val, "hour(s)")
  print("\nYou will be studying for:" ,time, "minutes\n")
  while time > 0:
    #study for 25 min
    print("-- Study for 25 minutes! --")
    time = time - 25
    #5 min break (short break)
    print("-- Take a 5 minute break! --\n")
    time = time - 5
    #short break counter
    short_break = short_break + 1 
    #check for long break
    if short_break % 4 == 0:
      #30 min break (long break)
      print("-- Take a 30 minute break! --\n")
      time = time - 30

elif t == "H":
  min_val = time * 60
  print("\nYou will be studying for:" ,min_val, "minutes\n")
  while min_val > 0:
    #study for 25 min
    print("-- Study for 25 minutes! --")
    min_val = min_val - 25
    #5 min break (short break)
    print("-- Take a 5 minute break! --\n")
    min_val = min_val - 5
    #short break counter
    short_break = short_break + 1 
    #check for long break
    if short_break % 4 == 0:
      #30 min break (long break)
      print("-- Take a 30 minute break! --\n")
      min_val = min_val - 30

print("*** TIMER OVER ***")
  