'''
Project Name: Personalized Message In Bulk Generator
By: Donald Lee
Date Started: May 2nd, 2020
'''
def Checkfornamechange():
    global Greeting
    global FileName
    global text
    Greeting = Greeting.strip()
    Greeting = Greeting.capitalize()

    if Greeting == "Namechange":
        FileName=input("Please enter the new name of your file:")
        FileName = FileName.strip()
        print("The name of your text file has been changed to \"" + FileName +".txt\"")
        print("")
        print("Some great greetinng examples would be, \"Dear\", \"Hi\", \"Hey\", \"To\", \"Welcome\", \"Congratulations\"")
        Greeting = input("Enter your greeting message:")
        Checkfornamechange()
    elif Greeting == "Save":
        print("Saved \nProgram ended!")
        return "finish"
    else:
        text = open(FileName + ".txt", "a+")  # 1st argument=file name, 2nd argument=type of access you want (a=appends the file, and +=create file if it doesn't already exist)
        Next()

def Next():
    global Message
    global Farewell
    print("")
    print(
        "Some example messages are, \"This is a friendly reminder that...\", \"Congratulations! You've been...\", \"Unfortunately our event...\"")
    Message = input("Enter your message:")
    Message = Message.strip()
    Message = Message.capitalize()
    if Message == "Save":
        print("Saved \nProgram ended!")
        return "finish"
    else:
        print("")
        print("Some great farewell phrases are, \"Sincerely, (Your Name)\", \"Take care.\", \"Best regards.\", \"Sorry for the inconvenience.\"")
        Farewell = input("Enter your farewell message:")
        Farewell = Farewell.strip()
        if Farewell == "SAVE":
            print("Saved \nProgram ended!")
            return "finish"
        else:
            print("")

            formattext()
#Writes and saves the desired message in a text file
def perfoming():
    if CapitalName== "Save":
        print("Saved \nProgram ended!")
        return "finish"
    else:
        text.write("\n" + Greeting + " "+ CapitalName + ",\n\n" + Message + "\n\n" + Farewell + "\n")
        formattext()

def formattext():
    global CapitalName
    global Message
    global Farewell

    #Asks for the recipient's name
    name = input("Recipients name:")
    FormattedName= name.strip()  #Remove spaces in the name
    CapitalName= FormattedName.capitalize()  #Captializes the first letter of the name

    perfoming()

print("\n*******************************************")
print("\tTo end this program, type \"SAVE\"")
print("*******************************************")
print("")
print("****************************************************************************************************************************************************************")
print("\tThis program will save your text into a text file called, \"PersonalizedGreetings.txt\", to change the name of the file, type \"NAMECHANGE\" as your Greeting")
print("****************************************************************************************************************************************************************\n")

print("Some great greetinng examples would be, \"Dear\", \"Hi\", \"Hey\", \"To\", \"Welcome\", \"Congratulations\"")
Greeting = input("Enter your greeting message:")
FileName = "PersonalizedGreetings"
Checkfornamechange()
