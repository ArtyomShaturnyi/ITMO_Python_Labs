import time

ESC = "\033"

##def loading(num_of_tusks):
#    max_bar = 30
 #   for task in range (num_of_tusks):
  
  #  for a in range (max_bar):
   
   #         filled = a
    
    #        time.sleep(0.1)
     #       bar = "#"*filled
      #      print (f"{i}%\r", end='', flush=time)

#if __name__ == "__name__":
 #   loading(3)

k=0
def draw_line(offset, fill, color):
    line = " " * fill
    offset_part = " " * offset 
    print (f"{offset_part}{ESC}[\f{color} {line} {ESC}[\f{color}")

def romb():
    k=0
    height = 15
    center = height // 2
    offset = height // 2
    step = 1
    length = 1
    colors = [31, 41]

    while k<10:
        for color in colors:
            for line in range (height):
                draw_line(offset, length, color)
                if line < center:
                    offset -= 1
                    length += 2
                else:
                    offset += 1
                    length -= 2
        k+=1

romb()