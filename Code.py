
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
import pygame

root = customtkinter.CTk()
root.title("okkk")
root.geometry("1280x720")
root.minsize(width=1280, height=720)
root.maxsize(width=3840, height = 2160)

start_display = False
option_display = False
quiz_display = False
learning_display = False
pygame.mixer.init() # initialising the mixer (music)
pygame.mixer.music.load("music\music1.mp3")
pygame.mixer.music.play(loops=-1)
fullscreen_on = False #a flag varialbe to indicate that fullscreen is off
music_on = True
#functions


def exit():
    root.destroy()

def next():
    global shapenumber
    if shapenumber < 4:
        shapenumber = shapenumber + 1
        Shape_label.configure(text=Shape_name[shapenumber])
        shape_info_label.configure(text=shape_info[shapenumber])
    else:pass

def backward():
    global shapenumber
    if shapenumber == 0:
        L_label.destroy()
        shape_info_label.destroy()
        Shape_label.destroy()
        learning_backbutton.destroy()
        start()
    else:
        shapenumber = shapenumber -1
        Shape_label.configure(text=Shape_name[shapenumber])
        shape_info_label.configure(text=shape_info[shapenumber])

def fullscreen():
    global fullscreen_on
    if fullscreen_on== False:

        root.attributes("-fullscreen", True)
        fullscreen_on = True
    else:
        root.attributes("-fullscreen", False)
        fullscreen_on = False


def music():
    global music_on
    if music_on== True:
        pygame.mixer.music.stop()
        music_on=False

    else:
        pygame.mixer.music.load("music\music1.mp3")
        pygame.mixer.music.play(loops=-1)
        music_on = True





def resize_image(number):
    global new_height, new_width, relativex, relativey, relative_scale, photo
    new_width = number.width #sets new width depending on the  number given
    new_height = number.height
    relativex = new_width/1920 #since my laptop is 1920x1080
    relativey = new_height/1080 
    relative_scale = (relativex+relativey)/2 #the average relative scale

    if start_display == True:
        try:
            S_image = S_copy_of_image.resize((new_width, new_height)) #scales the background image
            S_photo = ImageTk.PhotoImage(S_image)
            S_label.config(image = S_photo)
            S_label.image = S_photo
            
            start_button.configure(font=("Arial",50*relative_scale), width=120*relativex, height=40*relativey )
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
            
            
            Shapeimage.configure(image=ImageTk.PhotoImage(Image.open("button_images\\TRIANGLE.png").resize((int(400 * relativex), int(320 * relativey)))))
            
        except: pass
                


def list_file():
    global text_list
    file = open("languages\english.txt")

    text_list = []

    for i in file.readlines():
        text = i.replace("\n", "")
        text_list.append(text)
    

def option():
    global option_display, start_display, quiz_display, learning_display, copy_of_image, option_text, music_box, music_check, fullscreenbutton, fullscreen_check, option_backbutton, O_image, O_copy_of_image, O_photo, O_label
    option_display = True
    start_display = False
    quiz_display = False
    learning_display = False
    
    S_label.destroy()
    start_button.destroy()
    option_button.destroy()
    exit_button.destroy()
    geometric_prop.destroy()
    S_label.destroy()
    O_image = Image.open('background\startandoption.png')
    O_copy_of_image = O_image.copy()
    O_photo = ImageTk.PhotoImage(O_image)
    O_label = ttk.Label(root, image = O_photo)
    O_label.bind('<Configure>', resize_image)
    O_label.pack(fill=BOTH, expand = YES)

    
    
    #music_check = customtkinter.IntVar(value = 1) #this is for the music button, the value is initally turned off so the checkbox is unclicked. This is so that we can use checkbox and their different functions for on and off.
    


    #LABELS
    option_text = customtkinter.CTkLabel(root, text=text_list[2], font=("Segoe Script", 50), bg_color="white", fg_color="white", text_color="black", wraplength=300)
    option_text.place(relx=0.6, rely=0.45) 
    #Buttons
    music_box = customtkinter.CTkCheckBox(root, text = text_list[5], font=("Ariel", 40), command=music)
    music_box.place(relx=0.01, rely = 0.35) 

    if music_on==True:
        music_box.select()
    fullscreenbutton = customtkinter.CTkCheckBox(root, text = text_list[4], font=("Ariel", 40), command=fullscreen)
    fullscreenbutton.place(relx=0.01, rely = 0.45) 
    #fullscreen_check = customtkinter.IntVar(value = 0)
    if fullscreen_on == True:
        fullscreenbutton.select()
    
    option_backbutton_image = ImageTk.PhotoImage(Image.open("button_images\REVERSE.png").resize((20,20)))
    option_backbutton = customtkinter.CTkButton(root, image= option_backbutton_image, text= text_list[9], width = 10, height = 10, command=start)
    option_backbutton.place(relx =0.01, rely = 0.01)

def learning():
    global option_display,start_display,quiz_display, learning_display, L_image, L_copy_of_image, L_photo, L_label, Shape_label, shape_info_label, learning_backbutton, learning_nextbutton, shapenumber, Shape_name, shape_info, Shapeimagedirectory, Shapeimage
    option_display = False
    start_display = False
    quiz_display = False
    learning_display = True

    
    S_label.destroy()
    start_button.destroy()
    option_button.destroy()
    exit_button.destroy()
    geometric_prop.destroy()
    S_label.destroy()


    L_image = Image.open('background\learningandtest.jpg')
    L_copy_of_image = L_image.copy()
    L_photo = ImageTk.PhotoImage(L_image)
    L_label = ttk.Label(root, image = L_photo)
    L_label.bind('<Configure>', resize_image)
    L_label.pack(fill=BOTH, expand = YES)

    Shape_name = [text_list[11], text_list[13], text_list[15], text_list[17], text_list[19]]
    shape_info = [text_list[12], text_list[14], text_list[16], text_list[18], text_list[20]]
    shapenumber = 0
    #labels!!!
    Shape_label = customtkinter.CTkLabel(root, text=Shape_name[shapenumber], font=("Arial", 45), fg_color="white", text_color="black")
    Shape_label.place(relx=0.5, rely = 0.25, anchor=CENTER)
    shape_info_label = customtkinter.CTkLabel(root, text=shape_info[0], font=("Arial", 25), fg_color="white", text_color="black", wraplength=550)
    shape_info_label.place(relx=0.37,rely=0.3)

    learning_backbutton_image = ImageTk.PhotoImage(Image.open("button_images\REVERSE.png").resize((20,20)))
    learning_backbutton = customtkinter.CTkButton(root, image= learning_backbutton_image, text= text_list[9], width = 10, height = 10, command=backward)
    learning_backbutton.place(relx =0.01, rely = 0.01)

    learning_nextbutton_image = ImageTk.PhotoImage(Image.open("button_images\FORWARD.png").resize((20,20)))
    learning_nextbutton = customtkinter.CTkButton(root, image= learning_nextbutton_image, text= text_list[10], width = 10, height = 10, command=next)
    learning_nextbutton.place(relx = 0.92, rely = 0.01)
    
    Shapeimagedirectory = ImageTk.PhotoImage(Image.open("button_images\TRIANGLE.png").resize((400,320)))
    Shapeimage = customtkinter.CTkLabel(root, image= Shapeimagedirectory, text="", width = 10, height = 10)
    Shapeimage.place(relx =0.4, rely = 0.70)
def quiz():
    pass
def start():
    global copy_of_image, image, photo, label, start_button, option_display,start_display,quiz_display,learning_display,geometric_prop, option_button, exit_button, S_image, S_label, S_copy_of_image, S_photo
    
    if option_display == True:
        music_box.destroy()
        option_text.destroy()
        fullscreenbutton.destroy()
        option_backbutton.destroy()
        O_label.destroy()
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





list_file()

start()




#Label











root.mainloop()