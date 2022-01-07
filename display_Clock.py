import math 
import datetime
import tkinter as tk

class Display_Clock:
    def __init__(self):
        """
        Description: Creates a 200x200 window that includes buttons as well as the outline of the clock (front end).
        """
        self.window = tk.Tk() 
        self.window.title("Current Time") 
        self.window.geometry("200x200")
        self.top = tk.Frame(self.window)
        self.top.grid()
        self.bottom = tk.Frame(self.window)
        self.bottom.grid(row = 1, column = 0)
        self.canvas = tk.Canvas(self.top, width = 200, height = 200)
        self.canvas.grid()
        self.time_now = datetime.datetime.now()#Use datetime.now method within the time module
        self.delta_time_millis = 1000
        self.button_state = 1 #the number 1 is representative of the clock running
        self.radius = 80
        self.second_hand = self.radius * .8
        self.minute_hand = self.radius*0.65
        self.hour_hand = self.radius*0.5
    

        self.canvas.create_oval(200/2-self.radius, 200/2-self.radius, 200/2+self.radius, 200/2+self.radius) #uses radius (80) as well as window size to create oval which is the outline of the clock

        #defining center points
        self.x_half = 100 
        self.y_half = 100
        

        #Creates and adds 3,6,9, and 12 hour labels to the clock 
        self.canvas.create_text(100+self.radius-10, 100, text = "3")
        self.canvas.create_text(100, 100+self.radius-10, text = "6")
        self.canvas.create_text(100-self.radius+10, 100, text = "9")
        self.canvas.create_text(100,100-self.radius+10, text = "12")

        #creates and initializes required buttons 
        self.start_button = tk.Button(self.bottom, bg = 'white', text = 'Stop', command = self.stop_start_button)
        self.start_button.grid(row = 1, column = 0, padx = 1, pady = 1)
        self.quit_button = tk.Button(self.bottom, bg = 'white', text = 'Quit', command = self.quit)
        self.quit_button.grid(row = 1, column = 1, padx = 1, pady = 1)
        
        self.time_handler()
        self.window.mainloop()


    def stop_start_button(self):
        """
        Description: Depending on the button state (if its running/off) it updates the state itself and the button text. Also stops or starts clock
        """

        if self.button_state == 0: 
            self.time_handler()
            self.button_state = 1 
            self.start_button["text"] = 'Stop'
        else:
            self.window.after_cancel(self.timer) #using after_cancel method the clock is stopepd
            self.button_state = 0 
            self.start_button['text'] = 'Start'
    


    def time_handler(self):
        """
        Description: gets current time and updates it every 1000 milliseconds (1 second)

        """
        self.time_now = datetime.datetime.now()
        self.update_time()
        self.timer = self.window.after(self.delta_time_millis,self.time_handler)#

    def quit(self):
        """
        Description: Uses after_cancel method to terminate the window/program

        """
        self.window.destroy()
    
    def update_time(self): 
        """
        Description: Creates an event loop using update_time function that updates the clocks three 
        hands to display the current time. 

        """
        self.canvas.delete("hands") #deletes the three hands everytime the time is updated

        #Display the second hand
        second = self.time_now.second
        x_second = self.x_half + self.second_hand *math.sin(second*(2*math.pi/60))
        y_second = self.y_half - self.second_hand *math.cos(second*(2*math.pi/60))
        self.canvas.create_line(self.x_half, self.y_half, x_second, y_second, fill = "red", tag = "hands")

            #display the minute hand
        minute = self.time_now.minute

        x_minute = self.x_half+self.minute_hand *math.sin(minute*(2*math.pi/60))
        y_minute = self.y_half-self.minute_hand *math.cos(minute*(2*math.pi/60))
        self.canvas.create_line(self.x_half, self.y_half, x_minute, y_minute, fill = "blue", tag = "hands")#Gets current angle/hypotenuse for the second hand 


            #display the hour hand
        hour =self.time_now.hour#converts the hours  from military to regular time (conventional format)
        x_hour = self.x_half + self.hour_hand * math.sin((hour + minute/60) * (2*math.pi/12))
        y_hour = self.y_half - self.hour_hand * math.cos((hour + minute/60) * (2*math.pi/12))
        self.canvas.create_line(self.x_half, self.y_half, x_hour, y_hour, fill = "green", tag = "hands")

        time_text = str(hour) + ":" + str(self.time_now.minute) +":"+ str(self.time_now.second)#time_text creates and shows the time seen underneath the clock
        self.canvas.create_text(100, 190, text = time_text, tag = "hands")
        
if __name__ == "__main__":
    Display_Clock()