#Getting the necessary packages
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
import pygame
import pyttsx3
import os
#configuring the basics of tkinter
root = customtkinter.CTk()
root.title("okkk")
root.geometry("1280x720")
root.minsize(width=1280, height=720)
root.maxsize(width=3840, height = 2160)
#configuring the flag variables necessary for screen
start_display = False
option_display = False
quiz_display = False
learning_display = False
pygame.mixer.init() # initialising the mixer (music)
pygame.mixer.music.load("music\music1.mp3")
pygame.mixer.music.play(loops=-1)
fullscreen_on = False #a flag varialbe to indicate that fullscreen is off
music_on = True #a flag varialbe to indicate that music is on
language_name= "ENGLISH" #setting the default langauge 
#functions


def exit():
    root.destroy() #very simple, it destroys the root which is the master of everything

def learning_next(): #next button for the learning display
    global shapenumber #allowing shapenumber to be used everywhere
    if shapenumber < 4: # making sure that shape number stays within the limit since besides the first shape[triangle], there are four other shapes
        shapenumber = shapenumber + 1 #incrementation of shape number
        Shape_label.configure(text=Shape_name[shapenumber]) #Changes the shape name to the correct shape depending on the number
        shape_info_label.configure(text=shape_info[shapenumber]) #Changes the information for the shape so that it corresponds with shape label
        
        if shapenumber == 1: #shapenumber for the second shape[sqauare]
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\SQUARE.png").resize((int(400 * relativex), int(320 * relativey))))) #changes shape image
            Shapeimage.place(relx=0.4, rely=0.6) #places the image 
            learning_backbutton.configure(text=text_list[9])#Changes the text of back button to back, this is necessary since it becomes HOME when shape number is 0 as seen from the backbutton command
        if shapenumber == 2: #same as previous one but for 3rd shape and so on
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RECTANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
        if shapenumber == 3:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RHOMBUS.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
        if shapenumber == 4:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\PARALLELOGRAM.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
            learning_nextbutton.configure(text=text_list[21], command=quiz) #changes text to quiz
            
    else:pass

def learning_backward(): #simialr to the nextbutton
    global shapenumber 
    if shapenumber == 0: #if the shapenumber is zero [first shape shown] and back is pressed, it returns to menu
        L_label.destroy()#destroys the screen components
        shape_info_label.destroy()
        Shape_label.destroy()
        learning_backbutton.destroy()
        start()#starts up the menu
    else:
        shapenumber = shapenumber -1 #lowers the shape number and desplays the shape corresponding to the number
        Shape_label.configure(text=Shape_name[shapenumber])
        shape_info_label.configure(text=shape_info[shapenumber])
        if shapenumber == 0:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\TRIANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx =0.4, rely = 0.70)
            learning_backbutton.configure(text=text_list[23]) #Says HOME instead of BACK

        if shapenumber == 1:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\SQUARE.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
        if shapenumber == 2:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RECTANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
        if shapenumber == 3:
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RHOMBUS.png").resize((int(400 * relativex), int(320 * relativey)))))
            Shapeimage.place(relx=0.4, rely=0.6)
            learning_nextbutton.configure(text=text_list[10])
            #Makes the QUIZ BUTTON return to NEXT BUTTON
        

def fullscreen():
    global fullscreen_on
    if fullscreen_on== False: #if fullscreen is false and it is clicked it will make the window fullscreen and toggle it

        root.attributes("-fullscreen", True)
        fullscreen_on = True
    else: #conversely it does the same for when it is True
        root.attributes("-fullscreen", False)
        fullscreen_on = False


def music():
    global music_on
    if music_on== True: #If music is on and is pressed it will stop music and toggle it off
        pygame.mixer.music.stop()
        music_on=False

    else: #conversely true
        pygame.mixer.music.load("music\music1.mp3")
        pygame.mixer.music.play(loops=-1)
        music_on = True


def quiz_next():
    global questionnumber
    questionnumber = questionnumber + 6 #adds 6 to questionnumber which basically makes it go to the next question
    if questionnumber == 120: #if it reaches the final question, it will reach index 120 and it will restart/go to start menu
        start() #resets the application when the test is finished
    else:
        Question_Label.configure(text=Question_list[questionnumber]) # this shows the question and its number
        Question_info.configure(text=Question_list[questionnumber+1]) #THE actual question is shown here
        choiceAbutton.configure(text=Question_list[questionnumber+2]) #the following are the choices
        choiceBbutton.configure(text=Question_list[questionnumber+3])
        choiceCbutton.configure(text=Question_list[questionnumber+4])
        choiceDbutton.configure(text=Question_list[questionnumber+5])
        answer.place_forget() #hides answer
        quiz_nextbutton.forget() #hides next button
        quiz_nextbutton.place_forget() 
        choicevalue.set(0) #unchecks the buttons
        choiceAbutton.configure(state="normal") #makes sure the buttons are pressable
        choiceBbutton.configure(state="normal")
        choiceCbutton.configure(state="normal")
        choiceDbutton.configure(state="normal")

    

def answer_checker():
    
    global score, choicevalue, questionnumber
    quiz_nextbutton.place(relx =0.47, rely = 0.90) #when button is pressed, regardless of whether its correct or not, the next button is shown
    quiz_nextbutton.configure(text=text_list[10])  #configures the text for next button
    if questionnumber == 0: #for question 1
        if choicevalue.get() == 2: #choice 2 means B, 3 = C, 4 = D; in this case choice B is correct
            answer.configure(text=text_list[145], text_color="green") #GREEN TEXT FOR CORRECT ANSWER
            answer.place(relx=0.47, rely=0.7) 
            
            choiceAbutton.configure(state=DISABLED) #disables the other choices
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1 #score is increased
        else:
            answer.configure(text=text_list[146], text_color="red") #red for wrong answer, explanation is provided
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED) #disables button
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 6: #for question 2, the same thing for the rest
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[147], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 12: #for question 3
        if choicevalue.get() == 1:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[148], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 18:#for question 4
        if choicevalue.get() == 4:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[149], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 24:#for question 5
        if choicevalue.get() == 4:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[150], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 30:#for question 6
        if choicevalue.get() == 4:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[151], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 36:#for question 7
        if choicevalue.get() == 3:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[152], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 42:#for question 8 
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[153], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 48:#for question 9
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[154], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 54:#for question 10
        if choicevalue.get() == 3:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[155], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 60:#for question 11
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[156], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 66:#for question 12
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[157], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 72:#for question 13
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[158], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 78:#for question 14
        if choicevalue.get() == 3:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[159], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 84:#for question 15
        if choicevalue.get() == 3:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[160], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 90:#for question 16
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[161], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 96:#for question 17
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[162], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 102:#for question 18
        if choicevalue.get() == 3:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[162], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
    if questionnumber == 108:#for question 19
        if choicevalue.get() == 4:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
        else:
            answer.configure(text=text_list[164], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)

    if questionnumber == 114:#for question 20
        if choicevalue.get() == 2:
            answer.configure(text=text_list[145], text_color="green")
            answer.place(relx=0.47, rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            
            score = score + 1
            score_label.configure(text="Your score is " + score)
            score_label.place(relx=0.47, rely=0.6)
            
        else:
            answer.configure(text=text_list[165], text_color="red")
            answer.place(relx=0.37,rely=0.7)
            
            choiceAbutton.configure(state=DISABLED)
            choiceBbutton.configure(state=DISABLED)
            choiceCbutton.configure(state=DISABLED)
            choiceDbutton.configure(state=DISABLED)
            score_label.configure(text="Your score is " + str(score), fg_color='#f2f2f2', text_color= "black")
            score_label.place(relx=0.43, rely=0.8)




def resize_image(number): #scales the image
    global new_height, new_width, relativex, relativey, relative_scale, photo
    new_width = number.width #sets new width depending on the  number given
    new_height = number.height #same for height
    relativex = new_width/1920 #since my laptop is 1920x1080
    relativey = new_height/1080 
    relative_scale = (relativex+relativey)/2 #the average relative scale

    if start_display == True:
        try:
            S_image = S_copy_of_image.resize((new_width, new_height)) #scales the background image
            S_photo = ImageTk.PhotoImage(S_image) #sets the background on the new scale
            S_label.config(image = S_photo)
            S_label.image = S_photo
            
            start_button.configure(font=("Arial",50*relative_scale), width=120*relativex, height=40*relativey ) #scales the button, using relativexy and scale
            geometric_prop.configure(font=("Segoe Script",50*relative_scale), width=120*relativex, height=40*relativey)
            option_button.configure(font=("Arial",50*relative_scale), width=120*relativex, height=40*relativey )
            exit_button.configure(font=("Arial",50*relative_scale), width=120*relativex, height=40*relativey )
        except:
            pass
    if option_display == True:
        try:
            O_image = O_copy_of_image.resize((new_width, new_height)) #scales the background image
            O_photo = ImageTk.PhotoImage(O_image)
            O_label.config(image = O_photo)
            O_label.image = O_photo
            
            option_text.configure(font=("Segoe Script",50*relative_scale), width=120, height=40*relativey)
            option_backbutton.configure(width = 10*relativex, height = 10*relativey, font=("Ariel", 30*relative_scale))
            fullscreenbutton.configure(font=("Ariel", 40*relative_scale), width = 10*relativex, height = 10*relativey)
            music_box.configure(font=("Ariel", 40*relative_scale), width=10*relativex, height=10*relativey)

            language_box.configure(font=("Arial", 30*relative_scale),width=200*relativex )
            confirm_button.configure(font=("Arial", 30*relative_scale),width=0*relativex )
            confirm_button.configure(image=ImageTk.PhotoImage(Image.open("button_images\\REVERSE.png").resize((int(40 * relativex), int(40 * relativey)))))
        except: 
            pass
    if learning_display == True:
        try: 
            L_image = L_copy_of_image.resize((new_width, new_height)) #scales the background image
            L_photo = ImageTk.PhotoImage(L_image)
            L_label.config(image = L_photo)
            L_label.image = L_photo

                    
            Shape_label.configure(font=("Ariel", 45*relativex), width = 10*relativex, height = 10*relativey)
            shape_info_label.configure(font=("Ariel", 25*relative_scale), width = relativex, wraplength = 550*relativex)
            learning_backbutton.configure(width = 10*relativex, height = 10*relativey, font=("Ariel", 30*relative_scale))
            learning_nextbutton.configure(width = 10*relativex, height = 10*relativey, font=("Ariel", 30*relativey))
            
            if shapenumber==0: #scales the shape image depending on the shape
                Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\TRIANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            if shapenumber == 1:
                Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\SQUARE.png").resize((int(400 * relativex), int(320 * relativey)))))
            if shapenumber == 2:
                Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RECTANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            if shapenumber == 3:
                Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\RHOMBUS.png").resize((int(400 * relativex), int(320 * relativey)))))
            if shapenumber == 4:
                Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\PARALLELOGRAM.png").resize((int(400 * relativex), int(320 * relativey)))))
            
            tts_learning_button.configure(image=ImageTk.PhotoImage(Image.open("button_images\\TTS.png").resize((int(40 * relativex), int(40 * relativey)))))
        except: pass
                

    if quiz_display == True:
        try:
            Q_image = Q_copy_of_image.resize((new_width, new_height)) #scales the background image
            Q_photo = ImageTk.PhotoImage(Q_image)
            Q_label.config(image = Q_photo)
            Q_label.image = Q_photo
            Question_Label.configure(font=("Ariel", 55*relativex), width = 10*relativex, height = 10*relativey)
            Question_info.configure(font=("Ariel", 35*relative_scale), wraplength=700*relativex, width = relativex, height = relativey)

            choiceAbutton.configure(font=("Ariel", 25*relativex), width = 10*relativex, height = 10*relativey)
            choiceBbutton.configure(font=("Ariel", 25*relativex), width = 10*relativex, height = 10*relativey)
            choiceCbutton.configure(font=("Ariel", 25*relativex), width = 10*relativex, height = 10*relativey)
            choiceDbutton.configure(font=("Ariel", 25*relativex), width = 10*relativex, height = 10*relativey)
            #again scales them similarly to the previous ones
            answer.configure(font=("Ariel", 25*relativex), width = 10*relativex, height = 10*relativey)
            quiz_nextbutton.configure(font=("Ariel", 35*relativex), width = 10*relativex, height = 10*relativey)
            score_label.configure(font=("Ariel", 35*relativex), width = 10*relativex, height = 10*relativey)
            #the one below scales the image inside the button as well
            tts_quiz_button.configure(image=ImageTk.PhotoImage(Image.open("button_images\\TTS.png").resize((int(40 * relativex), int(40 * relativey)))))
        except: pass
def list_file():
    global text_list, language_name
    text_list = [] #creates a list
    try:
        language_name = language_box.get() #gets the desired language 
    except: pass
    file_directory = "languages/"+language_name+".txt" #places it in the directory[from my computer]
    file = open(file_directory, encoding="utf-8")
    for i in file.readlines():
        add = i.replace("Ã·","÷")
        add = add.replace("\n","")
        text_list.append(add) #text list is created
    try:
        music_box.configure(text=text_list[5]) #translates  the option menu
        option_text.configure(text=text_list[2])
        fullscreenbutton.configure(text=text_list[4])
        option_backbutton.configure(text=text_list[9])
    except: pass


    return text_list

def tts():
    engine = pyttsx3.init()
    if learning_display == True: #text to speech for learning display
        engine.say(shape_info[shapenumber]) #reads the shape information
        engine.runAndWait()
    if quiz_display == True:
        engine.say(Question_list[questionnumber+1]) #reads the question
        engine.runAndWait()
def option():
    global option_display, start_display, quiz_display, learning_display, copy_of_image, option_text, music_box, music_check, fullscreenbutton, fullscreen_check, option_backbutton, O_image, O_copy_of_image, O_photo, O_label, language_box, language_list, confirm_button
    option_display = True #ensures only option display flag is on
    start_display = False
    quiz_display = False
    learning_display = False
    
    S_label.destroy() #destroy previous gui components 
    start_button.destroy()
    option_button.destroy()
    exit_button.destroy()
    geometric_prop.destroy()
    S_label.destroy()
    O_image = Image.open('background\startandoption.png') #changes the background
    O_copy_of_image = O_image.copy()
    O_photo = ImageTk.PhotoImage(O_image)
    O_label = ttk.Label(root, image = O_photo) #places it
    O_label.bind('<Configure>', resize_image) #calls the scalar function
    O_label.pack(fill=BOTH, expand = YES)

    
    
    #music_check = customtkinter.IntVar(value = 1) #this is for the music button, the value is initally turned off so the checkbox is unclicked. This is so that we can use checkbox and their different functions for on and off.
    
#various buttons and labels
    option_text = customtkinter.CTkLabel(root, text=text_list[2], font=("Segoe Script", 50), bg_color="white", fg_color="white", text_color="black", wraplength=300)
    option_text.place(relx=0.6, rely=0.45) 
    #Buttons
    music_box = customtkinter.CTkCheckBox(root, text = text_list[5], font=("Ariel", 40), command=music) #calls the music function
    music_box.place(relx=0.01, rely = 0.35) 

    if music_on==True:
        music_box.select() #so that music is selected if it is pressed
    fullscreenbutton = customtkinter.CTkCheckBox(root, text = text_list[4], font=("Ariel", 40), command=fullscreen)
    fullscreenbutton.place(relx=0.01, rely = 0.45) 
    #fullscreen_check = customtkinter.IntVar(value = 0)
    if fullscreen_on == True:
        fullscreenbutton.select() # so that fullscreen is selected when pressed
    
    option_backbutton_image = ImageTk.PhotoImage(Image.open("button_images\REVERSE.png").resize((20,20))) #makes the image smaller
    option_backbutton = customtkinter.CTkButton(root, image= option_backbutton_image, text= text_list[9], width = 10, height = 10, command=start) #button with image
    option_backbutton.place(relx =0.01, rely = 0.01)
    #very long list of languages below, for combobox
    language_list = ["AFRIKAANS", "ALBANIAN", "ARABIC", "ARMENIAN", "BASQUE", "BENGALI", "BULGARIAN", "CATALAN", "CAMBODIAN", "CHINESE", "CROATIAN", "CZECH", "DANISH", "DUTCH", "ENGLISH", "ESTONIAN", "FINNISH", "FRENCH", "GEORGIAN", "GERMAN", "GREEK", "GUJARATI", "HEBREW", "HINDI", "HUNGARIAN", "ICELANDIC", "INDONESIAN", "IRISH", "ITALIAN", "JAPANESE", "JAVANESE", "KOREAN", "LATIN", "LATVIAN", "LITHUANIAN", "MACEDONIAN", "MALAY", "MALAYALAM", "MALTESE", "MAORI", "MARATHI", "MONGOLIAN", "NEPALI", "NORWEGIAN", "PERSIAN", "POLISH", "PORTUGUESE", "PUNJABI", "ROMANIAN", "RUSSIAN", "SAMOAN", "SERBIAN", "SLOVAK", "SLOVENIAN", "SPANISH", "SWAHILI", "SWEDISH", "TAMIL", "TATAR", "TELUGU", "THAI", "TONGA", "TURKISH", "UKRAINIAN", "URDU", "UZBEK", "VIETNAMESE", "WELSH", "XHOSA"]
    language_box = customtkinter.CTkComboBox(root, values = language_list, width=200)
    #sets the current languguage
    language_box.set(language_name)
    language_box.place(relx = 0.01, rely = 0.55)
    #calls the list file function to actually change the language
    confirm_button = customtkinter.CTkButton(root, image= option_backbutton_image, text="", width = 10, height = 10, command=list_file)
    confirm_button.place(relx = 0.12, rely = 0.55)
def learning():
    global option_display,start_display,quiz_display, learning_display, L_image, L_copy_of_image, L_photo, L_label, Shape_label, shape_info_label, learning_backbutton, learning_nextbutton, shapenumber, Shape_name, shape_info, Shapeimagedirectory, Shapeimage, tts_image, tts_learning_button, learning_nextbutton_image
    option_display = False
    start_display = False
    quiz_display = False
    learning_display = True #flag variable config

    
    start_button.destroy()
    option_button.destroy()
    exit_button.destroy()
    geometric_prop.destroy()#erase previous gui 
    S_label.destroy()


    L_image = Image.open('background\learning.jpg')
    L_copy_of_image = L_image.copy()
    L_photo = ImageTk.PhotoImage(L_image)
    L_label = ttk.Label(root, image = L_photo)
    L_label.bind('<Configure>', resize_image)
    L_label.pack(fill=BOTH, expand = YES) #set NEW IMAGE

    Shape_name = [text_list[11], text_list[13], text_list[15], text_list[17], text_list[19]] #shape name
    shape_info = [text_list[12], text_list[14], text_list[16], text_list[18], text_list[20]] #shape information
    shapenumber = 0 #keeps track of shape name
    #labels!!!
    Shape_label = customtkinter.CTkLabel(root, text=Shape_name[shapenumber], font=("Arial", 45), fg_color="white", text_color="black") #set to show the first shape
    Shape_label.place(relx=0.5, rely = 0.25, anchor=CENTER)
    shape_info_label = customtkinter.CTkLabel(root, text=shape_info[0], font=("Arial", 25), fg_color="white", text_color="black", wraplength=550) #shape info for triangle
    shape_info_label.place(relx=0.37,rely=0.3)

    learning_backbutton_image = ImageTk.PhotoImage(Image.open("button_images\REVERSE.png").resize((20,20))) #backbutton
    learning_backbutton = customtkinter.CTkButton(root, image= learning_backbutton_image, text= text_list[9], width = 10, height = 10, command=learning_backward)
    learning_backbutton.place(relx =0.01, rely = 0.01)

    learning_nextbutton_image = ImageTk.PhotoImage(Image.open("button_images\FORWARD.png").resize((20,20))) #next button
    learning_nextbutton = customtkinter.CTkButton(root, image= learning_nextbutton_image, text= text_list[10], width = 10, height = 10, command=learning_next)
    learning_nextbutton.place(relx = 0.92, rely = 0.01)
    
    Shapeimagedirectory = ImageTk.PhotoImage(Image.open("button_images\TRIANGLE.png").resize((400,320))) #A diagram for each shape
    Shapeimage = customtkinter.CTkLabel(root, image= Shapeimagedirectory, text="", width = 10, height = 10)
    Shapeimage.place(relx =0.4, rely = 0.70)
    

    tts_image = ImageTk.PhotoImage(Image.open("button_images\TTS.png").resize((20,20))) #TTS BUTTON
    tts_learning_button = customtkinter.CTkButton(root, image= tts_image, text="", width = 10, height = 10, command=tts)
    tts_learning_button.place(relx =0.49, rely = 0.15)


def quiz():
    global option_display,start_display,quiz_display, learning_display, Q_image, Q_copy_of_image, Q_label, Q_photo, Question_list, Question_Label, questionnumber, Question_info, choiceAbutton, choiceBbutton, choiceCbutton, choiceDbutton, choicevalue, answer, quiz_nextbutton_image, quiz_nextbutton, score, score_label, tts_quiz_button
    option_display = False
    start_display = False
    quiz_display = True #sets the right flag
    learning_display = False
    score = 0 #resets score
    Shape_label.destroy()
    shape_info_label.destroy()#clears previous gui
    learning_backbutton.destroy()
    learning_nextbutton.destroy()
    Shapeimage.destroy()
    tts_learning_button.destroy()
    L_label.destroy()

    Q_image = Image.open('background\quiz.jpg')
    Q_copy_of_image = Q_image.copy() #sets the background
    Q_photo = ImageTk.PhotoImage(Q_image)
    Q_label = ttk.Label(root, image = Q_photo)
    Q_label.bind('<Configure>', resize_image)
    Q_label.pack(fill=BOTH, expand = YES)

    choicevalue= IntVar() #for the four choices 

    questionnumber = 0 #using this variable to keep track of the question and to change it
    Question_list= text_list[25:145] #starts at index 25 and stops at index 145
    Question_Label = customtkinter.CTkLabel(root, text=Question_list[questionnumber], fg_color='#f2f2f2', text_color= "black",font=("Arial", 55), anchor=CENTER)
    Question_Label.place(relx=0.44, rely=0.30) #question label shows the q number
    Question_info =customtkinter.CTkLabel(root, text=Question_list[questionnumber+1], fg_color='#f2f2f2', text_color= "black",font=("Arial", 35), wraplength=700)
    Question_info.place(relx=0.33, rely=0.40)  #shows information/ the question
    choiceAbutton = customtkinter.CTkRadioButton(root, text=Question_list[questionnumber+2], bg_color='#f2f2f2', text_color= "black", font=("Arial", 35), variable =choicevalue, value = 1, command=answer_checker)
    choiceAbutton.place(relx=0.33, rely=0.5) #button A
    
    choiceBbutton = customtkinter.CTkRadioButton(root, text=Question_list[questionnumber+3], bg_color='#f2f2f2', text_color= "black", font=("Arial", 35), variable =choicevalue, value = 2, command=answer_checker)
    choiceBbutton.place(relx=0.33, rely=0.55) #button B

    choiceCbutton = customtkinter.CTkRadioButton(root, text=Question_list[questionnumber+4], bg_color='#f2f2f2', text_color= "black", font=("Arial", 35), variable =choicevalue, value = 3, command=answer_checker)
    choiceCbutton.place(relx=0.33, rely=0.6) #button C

    choiceDbutton = customtkinter.CTkRadioButton(root, text=Question_list[questionnumber+5], bg_color='#f2f2f2', text_color= "black", font=("Arial", 35), variable =choicevalue, value = 4, command=answer_checker)
    choiceDbutton.place(relx=0.33, rely=0.65) #button D

    answer =customtkinter.CTkLabel(root, text="", fg_color='#f2f2f2', text_color= "black",font=("Arial", 35))
    answer.place(relx=0.47, rely=0.7)
    answer.place_forget() #answer is hidden initally
    quiz_nextbutton_image = ImageTk.PhotoImage(Image.open("button_images\FORWARD.png").resize((20,20))) #next button 
    quiz_nextbutton = customtkinter.CTkButton(root, text="", width = 10, height = 10, command=quiz_next)
    quiz_nextbutton.place(relx =0.47, rely = 0.90)
    quiz_nextbutton.place_forget()

    score_label = customtkinter.CTkLabel(root, text="", width = 10, height = 10)
    score_label.place(relx=0.47, rely=0.6)
    score_label.place_forget() #score only shown after the test

    tts_quiz_button = customtkinter.CTkButton(root, image= tts_image, text="", width = 10, height = 10, command=tts)
    tts_quiz_button.place(relx =0.49, rely = 0.15) #TTS FOR QUIZ

    
def start():
    global copy_of_image, image, photo, label, start_button, option_display,start_display,quiz_display,learning_display,geometric_prop, option_button, exit_button, S_image, S_label, S_copy_of_image, S_photo
    
    if option_display == True:
        music_box.destroy()
        option_text.destroy()
        fullscreenbutton.destroy()
        option_backbutton.destroy()
        O_label.destroy()
    if quiz_display == True:
        Q_label.destroy()
        Question_Label.destroy()
        Question_info.destroy()
        choiceAbutton.destroy()
        choiceBbutton.destroy()
        choiceCbutton.destroy()
        choiceDbutton.destroy()
        answer.destroy()
        quiz_nextbutton.destroy()
        score_label.destroy()
    else: pass

    option_display = False
    start_display = True
    quiz_display = False
    learning_display = False

    S_image = Image.open('background\startandoption.png')
    S_copy_of_image = S_image.copy()
    S_photo = ImageTk.PhotoImage(S_image)
    S_label = ttk.Label(root, image = S_photo)
    S_label.bind('<Configure>', resize_image)
    S_label.pack(fill=BOTH, expand = YES)
    
    geometric_prop = customtkinter.CTkLabel(root, text=text_list[0], font=("Segoe Script", 50), fg_color="white", text_color="black", wraplength=400)
    geometric_prop.place(relx=0.6, rely=0.4)
                            
    start_button = customtkinter.CTkButton(master=root, text = text_list[1], font=("Ariel", 50),command=learning )
    start_button.place(relx=0.01, rely = 0.35) 
    
    option_button = customtkinter.CTkButton(master=root, text = text_list[2], font=("Ariel", 50), command=option )
    option_button.place(relx=0.01, rely = 0.45) 

    exit_button = customtkinter.CTkButton(master=root, text = text_list[3], font=("Ariel", 50), command=exit )
    exit_button.place(relx=0.01, rely = 0.55)                          





list_file() #runs the language file to default it to english

start() #starts the first function/display which calls out the others




#Label











root.mainloop() #necessary to run tkinter