# import the time module
import time
# define the countdown func.
def countdown(t):
  while t:
    mins,secs =divmod(t,60)
    timer='{:02d}:{:02d}'.format(mins,secs)
    print(timer, end="\t")
    time.sleep(1)
    t-=1
    print()
#input time in seconds
t=input("Enter the time in second:")
#function call 
countdown(int(t))
print("Completed!")
