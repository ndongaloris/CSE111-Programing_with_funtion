"""Author: Loris Jared Ndonga"""

import tkinter as tk
from tkinter import Frame, Entry, Label, Radiobutton, StringVar, ACTIVE, END, Listbox, Button
def main():
    """set the title of the application and define a default size.
    call the design function.
    """
    root = tk.Tk()
    root.config(bg="tan")
    root.title("Blood Alcohol Calculator")
    root.geometry("450x280+100+100")
    root.resizable(False, False)

    main_frame = Frame(root)
    main_frame.configure(bg="tan")

    app_name = Label(main_frame, text="Blood Alcohol Calculator",font =("Arial", 30), bg="tan")
    app_name.grid(row=0,column=0,columnspan=3, sticky="ew")
    design(main_frame, root)

    main_frame.grid(row=0, column=0, sticky="nsew")
    root.mainloop()

def design(frame, root):
    """A nested function that contains two other functions.
    create the layout of the app, do the calculation
    ask for the user of the amount of alcohol it drunk,
    for his weight, the last time he drinks, the gender and the location
    and calculate and gives back the rate of alcohol intoxication 
    and print to the user a message telling him if he can drive or not
    """

    # set the text and the entry box for the amount of drink
    amount = Label(frame, text="How many bottle of drinks did you have: ", bg="tan")
    amount.grid(row=1, column=0, sticky= "w")
    amount_box = Entry(frame, bg="tan")
    amount_box.grid(row=1, column=1, sticky="w")
    bottle = Label(frame, text="bottle(s)",bg="tan")
    bottle.grid(row=1, column=2, sticky="w")

    # set the text and the entry box for the weight
    weight = Label(frame, text="Enter how much you weight: ", bg="tan")
    weight.grid(row=2, column=0, sticky="w")
    weight_box = Entry(frame, bg="tan")
    weight_box.grid(row=2, column=1, sticky="w" )
    Kg = Label(frame, text="KG",bg="tan")
    Kg.grid(row=2, column=2, sticky="w")

    # set the text and the entry box to determine the last time the user drunk
    time = Label(frame, text="How long has past since your last drink:", bg="tan")
    time.grid(row=3, column=0, sticky="w")
    time_box = Entry(frame, bg="tan")
    time_box.grid(row=3, column=1, sticky="w")
    time_unit = Label(frame, text="Hours", bg="tan")
    time_unit.grid(row=3, column=2, sticky="w")

    # create Radiobutton to get the gender of the user
    gender = Label(frame, text="Are you a man or a woman", bg='tan')
    gender.grid(row=4, column=0, sticky="w")
    gender_var = StringVar(root)
    gender_var.set(None) # set the gender to none
    gender_man = Radiobutton(frame, text="man", value="man", bg="tan" , variable=gender_var)
    gender_man.grid(row=4, column=1, sticky="w")
    gender_woman = Radiobutton(frame, text="woman", value="woman", bg="tan", variable=gender_var)
    gender_woman.grid(row=4, column=1, sticky="e")

    # a list a countries for the location part
    countries = ["South Africa", "Rep. Of Congo","Cote D'Ivoire","Ethiopia","Canada", "Japan", "Australia", "Ghana", "Brazil"]				
    country = Label(frame, text="Select you country:", bg="tan")
    country.grid(row=5, column=0, sticky="e")
    country_list = Listbox(frame, bg="tan", listvariable=countries, height=1)
    for country in countries:
        country_list.insert(END, country)
    country_list.grid(row=5, column=1)

    # the print messages that will appear, ex: it will print the bac number of the user or an error of input if there is any.
    result_label = Label(frame, text="", fg="Black", bg= "tan")
    result_label.grid(row=8, column=0, columnspan=2)
    result_label_2 = Label(frame, text="", fg="Black", bg= "tan")
    result_label_2.grid(row=9, column=0, columnspan=2)

    def calculate(event=None):
        """Calculate the BAC with inputs from the user
        Call the BAC_calculation and BAC_result 
        """
        countries = {"South Africa": 0.05,
                     "Rep. Of Congo": 0.05,
                     "Cote d'Ivoire": 0.08,
                        "Ethiopia": 0.08, 
                        "Canada": 0.05,
                        "Japan": 0.03,
                        "Australia": 0.05,
                        "Ghana": 0.08,
                        "Brazil": 0.06}
        ratios = {"man": 0.73 , "woman": 0.66}
        try:
            A = float(amount_box.get()) #get the amount of alcohol the user drunk and store it to the A variable
            W = float(weight_box.get()) #get the weight of the user and store it to the W variable
            H = float(time_box.get()) #get the number of hours the user spend since his last drink and store it to the H variable
        except Exception:
            result_label_2.config(text ="Invalid input \nCheck your first three entries")

        #get the gender of the user    
        if gender_var.get() == "man":
            gender = "man"
        elif gender_var.get() == "woman":
            gender = "woman"
        else:
            result_label.config(text = "Please select your gender")
            return
        
        if gender not in ratios:
            result_label_2.config(text = "invalid gender input.")
        else:
            #process with calculation
            ratio = ratios[gender]
            BAC = BAC_calculation(A, W, ratio, H)
            result_label_2.config(text = f"Your BAC is {BAC:.2f}")

        country = country_list.get(ACTIVE)
        if country in countries:
            limit = countries[country]
            message = BAC_result(country, limit, BAC)
            result_label.config(text=message)
            # if limit <= BAC:
            #     result_label.config(text = f'It is not legal for you to drive in {country}.')
            # else:
            #     result_label.config(text = "You can go, sorry for the inconvenience.")
        else:
                result_label.config(text = "Something is wrong, we don't have information for those limit.")
    def clear_btn():
        """reset some of the data allowing the user to reenter and calculate
        """

        Clear.focus
        amount_box.delete(0,END)
        weight_box.delete(0,END)
        result_label.config(text=" ")
        result_label_2.config(text=" ")
        time_box.delete(0,END)
        gender_var.set(None)
        amount_box.focus  
    #create the clear button to clear the data
    Clear = Button(frame, text="Clear", bg="light yellow", command=clear_btn)
    Clear.grid(row=6, column=2, sticky = "nsew")

    #create the calculate button to operate
    Calculate = Button(frame, text="Calculate", bg="light yellow", command=calculate)
    Calculate.grid(row=6, column=1, sticky = "nsew")
    amount_box.focus()
    amount_box.focus()
    for child in frame.winfo_children():
        child.grid_configure(padx=1, pady=1)
    root.bind("<Return>", calculate)
    print(result_label)

def BAC_calculation(alcohol, weight, ratio, time):
    """This function was created aside to do the calculation
    it could have been done straight in the calculate function 
    but this make it easy to test the calculation using pytest
    """
    BAC = (alcohol * 5.14 / (weight * ratio)) - (0.015 * time)
    return BAC

def BAC_result(country, limit, BAC):
    """This function is created aside to determine which message should appear
    whether the person can drive or not, t could have been done straight in 
    the calculate function but this make it easy to test using pytest
    """
    if limit <= BAC:
        return f'It is not legal for you to drive in {country}.'
    else:
        return f"It's okay. You can drive."

if __name__ == "__main__":
    main()