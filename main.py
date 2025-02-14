import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageChops,ImageEnhance,ImageFilter
from tkinter import ttk
import os.path
from PIL.ImageFilter import (
    GaussianBlur, MedianFilter, MinFilter, MaxFilter
    )
import PIL as pl
import matplotlib.pyplot as plt


def browse_file():
    global image_copy,extension,image,image_resized,image_init,Fname
    file_path = filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_path)[1]
    Fname = os.path.splitext(file_name)[0]
    print(extension)
    # print(file_name)
    print(Fname)
    image = Image.open(file_path)
    image_init = image.copy()
    image_resized = image.resize((300, 300), Image.Resampling.LANCZOS)
    image_copy= image_resized.copy()
    img = ImageTk.PhotoImage(image_copy)
    label.config(image=img)
    label.image = img
    label.grid(row=0,column=6,padx=10,ipady=0, pady=10,rowspan=5)
    
    label_original.config(image=img)
    label_original.image = img
    label_original.grid(row=0,column=0,padx=10,ipady=0, pady=10,rowspan=5)

def reset():
    global image_resized,image, image_copy
    image_copy= image_resized.copy()
    image= image_init.copy()
    img = ImageTk.PhotoImage(image_copy)
    label.config(image=img)
    label.image = img

    amelioration_entry.delete(0,'end')
    # gamma_entry.delete(0,'end')
    filtre_entry.delete(0,'end')

# def inverse():
#     global image_copy,image
#     image_copy = ImageChops.invert(image_copy)
#     image = ImageChops.invert(image)
#     img = ImageTk.PhotoImage(image_copy)
#     label.config(image=img)
#     label.image = img
def inverse():
    global image_copy, image, img  # Add 'img' to global variables
    if image.mode == 'RGBA':
        # Split the image into RGB and alpha channels
        r, g, b, a = image.split()
        # Invert the RGB channels
        r = ImageChops.invert(r)
        g = ImageChops.invert(g)
        b = ImageChops.invert(b)
        # Merge the inverted RGB channels with the original alpha channel
        image = Image.merge('RGBA', (r, g, b, a))
        image_copy = Image.merge('RGBA', (r, g, b, a))
    else:
        # Invert the image directly if it doesn't have an alpha channel
        image = ImageChops.invert(image)
        image_copy = ImageChops.invert(image_copy)
    
    # Update the displayed image
    img = ImageTk.PhotoImage(image_copy)  # Create a new PhotoImage
    label.config(image=img)
    label.image = img  # Keep a reference to avoid garbage collection
def inverse_save():
    global image_copy,extension,image
    image.save("inversee"+extension)
    print('Inverting has been saved')

def Enhancing(event):
    global image_copy,select,image_enhanced,image,image_enhanced_init
    ColEnhanced = ImageEnhance.Color(image_copy)
    BriEnhanced= ImageEnhance.Brightness(image_copy)
    ContrEnhanced= ImageEnhance.Contrast(image_copy)
    SharpEnhanced= ImageEnhance.Sharpness(image_copy)

    ColEnhanced_init = ImageEnhance.Color(image)
    BriEnhanced_init= ImageEnhance.Brightness(image)
    ContrEnhanced_init= ImageEnhance.Contrast(image)
    SharpEnhanced_init= ImageEnhance.Sharpness(image)

    select = amelioration_combo.get()
    fact = float(amelioration_entry.get())
    if (select=="Colors"): 
        image_enhanced = ColEnhanced.enhance(fact)
        image_enhanced_init = ColEnhanced_init.enhance(fact)
        img = ImageTk.PhotoImage(image_enhanced)
        label.config(image=img)
        label.image = img

    if (select=="Contrast"):    
        image_enhanced = ContrEnhanced.enhance(fact)
        image_enhanced_init = ContrEnhanced_init.enhance(fact)
        img = ImageTk.PhotoImage(image_enhanced)
        label.config(image=img)
        label.image = img

    if (select=="Brightness"):    
        image_enhanced = BriEnhanced.enhance(fact)
        image_enhanced_init = BriEnhanced_init.enhance(fact)
        img = ImageTk.PhotoImage(image_enhanced)
        label.config(image=img)
        label.image = img

    if (select=="Sharpness"):    
        image_enhanced = SharpEnhanced.enhance(fact)
        image_enhanced_init = SharpEnhanced_init.enhance(fact)
        img = ImageTk.PhotoImage(image_enhanced)
        label.config(image=img)
        label.image = img

def amelio_save():
    global image_enhanced,extension,select,image,image_enhanced_init
    image_enhanced_init.save(Fname+'__'+select+extension)
    print('Enhancement has been saved')

def Filtre(event):
    global image_copy,image_filtr_init,image
    try:
        matrix = eval(filtre_entry2.get())
    except (SyntaxError, ValueError):
        print("Error: Invalid matrix expression")
        
    try:
        fact = eval(filtre_entry.get())
    except (SyntaxError, ValueError):
        print("Error: Invalid radius value")    
    
    if(filtre_combo.get()=='GaussianBlur'):
        image_filtred = image_copy.convert('RGB')
        image_filtred = image_filtred.filter(GaussianBlur(radius=fact))
        image_filtr_init = image.convert('RGB')
        image_filtr_init = image_filtr_init.filter(GaussianBlur(radius=fact))
        img = ImageTk.PhotoImage(image_filtred)
        label.config(image=img)
        label.image = img
    if(filtre_combo.get()=='MedianFilter'):
            image_filtred = image_copy.convert('RGB')
            image_filtred = image_filtred.filter(MedianFilter(size=matrix))
            image_filtr_init = image.convert('RGB')
            image_filtr_init = image_filtr_init.filter(MedianFilter(size=matrix))
            img = ImageTk.PhotoImage(image_filtred)
            label.config(image=img)
            label.image = img
    if(filtre_combo.get()=='MaxFilter'):
            image_filtred = image_copy.convert('RGB')
            image_filtred = image_filtred.filter(MaxFilter(size=matrix))
            image_filtr_init = image.convert('RGB')
            image_filtr_init = image_filtr_init.filter(MaxFilter(size=matrix))
            img = ImageTk.PhotoImage(image_filtred)
            label.config(image=img)
            label.image = img
    if(filtre_combo.get()=='MinFilter'):
            image_filtred = image_copy.convert('RGB')
            image_filtred = image_filtred.filter(MinFilter(size=matrix))
            image_filtr_init = image.convert('RGB')
            image_filtr_init = image_filtr_init.filter(MinFilter(size=matrix))
            img = ImageTk.PhotoImage(image_filtred)
            label.config(image=img)
            label.image = img

def filter_save():
    global image,image_filtr_init
    image_filtr_init.save(Fname+'__'+filtre_combo.get()+extension)  
    print(Fname+'__'+filtre_combo.get()+' has been saved')

def histogram():
    global image 
    print(image.mode)
    if (image.mode == "RGBA") : image = image_init.convert(mode='L')
    if image.mode == "RGB" or image.mode == "RGBA" :
        def getRed(R): return '#%02x%02x%02x'%(R,0,0)
        def getGreen(G): return '#%02x%02x%02x'%(0,G,0)
        def getBlue(B):return '#%02x%02x%02x'%(0,0,B)
        hst=image.histogram()
        l1=hst[0:256]      # indicates Red
        l2=hst[256:512]  # indicated Green
        l3=hst[512:768]   # indicates Blue
        plt.figure(0)             # plots a figure to displayHistogram
        for i in range(0, 256):
            plt.bar(i,( l1[i], l2[i], l3[i]), color = ["red","green","blue"],alpha=0.5)
        plt.show()
    elif image.mode == "L":
        hst = image.histogram()
        plt.figure(1)
        plt.bar(range(256), hst, color='gray', alpha=0.7)
        plt.title("Grayscale Histogram")
        plt.xlabel("Gray Level")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Image mode is neither RGB nor grayscale.")

root = tk.Tk()
root.title("Image Filtering")

#--------Select image
label_original = tk.Label(root, text="Click the 'Browse' button to select an image.",bg='#A1A1A1',relief="ridge",borderwidth=5)
label_original.grid(row=0,column=0,padx=10,ipady=140, pady=10,rowspan=5)
label = tk.Label(root, text="Click the 'Browse' button to select an image.",bg='#A1A1A1',relief="ridge",borderwidth=5)
label.grid(row=0,column=6,padx=10,ipady=140, pady=10,rowspan=5)

browse_button = tk.Button(root, text="Browse",fg='black', bg='#A1A1A1',command=browse_file)
browse_button.grid(row=6,column=0,pady=10)

# Reset
reset_button = tk.Button(root, text="Reset",background='#ECD436', command=reset)
reset_button.grid(row=7,column=0,pady=10)

# Quit
exit_button = tk.Button(root, text="Quit",background='#CE0C0C',fg='white',command=exit)
exit_button.grid(row=7,column=3,pady=10,padx=5)

# Inverse
inverse_label = tk.Label(root, text="Invert Colors: ")
inverse_label.grid(row=0,column=1,pady=10,columnspan=2)
inverse_button = tk.Button(root, text="Invert",width=20,bg='#b8b894', command=inverse)
inverse_button.grid(row=0,column=4,pady=10,padx=10)

imicon = Image.open('icons8-save-30.png')
resize_image = imicon.resize((20, 20))
icon = ImageTk.PhotoImage(resize_image)
inverse_save = tk.Button(root, image=icon,height=20,width=20,background='green',fg='white', command=inverse_save)
inverse_save.grid(row=0,column=5,pady=10)

# Enhancement
amelioration_label = tk.Label(root, text="Enhance (0~255): ")
amelioration_label.grid(row=1,column=1,pady=10,columnspan=2)
amelioration_combo = ttk.Combobox(root, values=('Colors', 
                                                'Contrast',
                                                'Brightness',
                                                'Sharpness'),
                                                state="readonly")
amelioration_combo.grid(row=1,column=4,pady=10)
amelioration_combo.bind("<<ComboboxSelected>>", Enhancing)
amelioration_entry = tk.Entry(root,width=4)
amelioration_entry.grid(row=1,column=3,pady=10)

amel_save = tk.Button(root, image=icon,height=20,width=20,background='green',fg='white', command=amelio_save)
amel_save.grid(row=1,column=5,pady=10,padx=10)

# Filters
filtre_label = tk.Label(root, text="Filters: ")
filtre_label.grid(row=3,column=1,pady=10)
filtre_combo = ttk.Combobox(root, values=('GaussianBlur', 
                                                'MedianFilter',
                                                'MaxFilter',
                                                'MinFilter'),
                                                state="readonly")
filtre_combo.grid(row=3,column=4,pady=10)
filtre_combo.bind("<<ComboboxSelected>>", Filtre)
filtre_entry = tk.Entry(root,width=4)
filtre_entry.grid(row=3,column=2,pady=10, ipadx=0)

filtre_entry2 = ttk.Combobox(root, values=('3', 
                                                '5',
                                                '7',
                                                '9'),
                                                state="readonly",width=2)
filtre_entry2.grid(row=3,column=3,pady=10)

filt_save = tk.Button(root, image=icon,height=20,width=20,background='green',fg='white', command=filter_save)
filt_save.grid(row=3,column=5,pady=10,padx=10)

# Histogram
hist_label = tk.Label(root, text="Generate Histogram: ")
hist_label.grid(row=4,column=1,pady=10,columnspan=2)
hist_button = tk.Button(root, text="Histogram",width=20,bg='#b8b894', command=histogram)
hist_button.grid(row=4,column=3,pady=10,padx=10,columnspan=3)

root.mainloop()