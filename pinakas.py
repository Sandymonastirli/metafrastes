#Kapsimalis Athanasios 2265 cs122265
#Monastirli Chrysanthi 1716 cs091716


# o sintaktikos analitis elegxei an o pigaios kwdikas anikei stin Starlet i oxi

# i idea ston diko mas sintaktiko analiti einai oti elegxoyme se kathe kanona pou briskomaste
# an exoyme paei sto epomeno kommati toy wste na kseroume oti teleiwse to proigoumeno kommati tou
# analitika i epeksigisi dinetai sto report pou paradwsame

# episis na tonisoume oti se periptwsi pou se kapoio kanona exoume or keno 
# tote opws ipothike kai stis dialekseis tou mathimatos den xrisimopoioume else

# gia na mporesoyme na xrisimopoihsoyme arxeio apo to termatiko me grammi entolwn kanoyme import sys
import sys

# i sinartisi lektikos(), diladi o lektikos mas analitis ,kaleitai apo ton sintaktiko analiti 
katastash = 0
leksh = ""

#anoigoume ena arxeio apo to termatiko
arxeio = open(sys.argv[1], "r")
grammi = 1

label = "0"
counter = 1
tetrades = []
onomaProgrammatos = ""

exitList = []
#exei tis metavlites pou exoume dhlwsei
metavlhtes = []
metavlhtesTemp = []

pinakasSymvolwn = []
vathosFwliasmatos = 0

loopCounter = 0
returnCounter = 0


# i sinartisi lektikos() diabazei gramma gramma ton pigaio kwdika
# kai epistrefei mia lektiki monada kai ton akeraio poy tin xaraktirizei
def lektikos():

    global katastash, leksh, grammi

    endiameses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# arxika to aytomato poy sxediasame xeirografa kai metatrapsame se kwdika arxizei apo mia arxiki katastasi
# kai me tin eisodo kathe xaraktira allazei katastasi mexri na brei teliki katastasi

    katastash = 0
    leksh = ""
    while katastash in endiameses:
# diabazw enan neo xaraktira apo to arxeio
        c = arxeio.read(1)

# to automato mas anagnwrizei to alfabito tis Starlet
        if katastash == 0 and (c == " " or c == "\t"):
            katastash = 0
        elif katastash == 0 and c == "\n":
            katastash = 0
            grammi = grammi + 1
# elegxw an i katastasi einai i arxiki kai an 
#to string poy diabasa apo to arxeio einai kapoio gramma
        elif katastash == 0 and c.isalpha() == True:
            katastash = 1
        elif katastash == 0 and c.isdigit() == True:
            katastash = 2
        elif katastash == 0 and c == "+":
            katastash = "+tk"
        elif katastash == 0 and c == "-":
            katastash = "-tk"
        elif katastash == 0 and c == "*":
            katastash = "*tk"
        elif katastash == 0 and c == "/":
            katastash = 6
        elif katastash == 0 and c == "<":
            katastash = 3
        elif katastash == 0 and c == ">":
            katastash = 4
        elif katastash == 0 and c == "=":
            katastash = "=tk"
        elif katastash == 0 and c == ":":
            katastash = 5
        elif katastash == 0 and c == "(":
            katastash = "(tk"
        elif katastash == 0 and c == ")":
            katastash = ")tk"
        elif katastash == 0 and c == "[":
            katastash = "[tk"
        elif katastash == 0 and c == "]":
            katastash = "]tk"
        elif katastash == 0 and c == ";":
            katastash = ";tk"
        elif katastash == 0 and c == ",":
            katastash = ",tk"
# elegxw an briskomaste stin katastasi 0 kai an briskomai sto telos toy arxeioy
# to eoftk simainei end of file token
        elif katastash == 0 and c == "":
            katastash = "eoftk"

        elif katastash == 1 and (c == " " or c == "\t"):
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "\n":
            katastash = "anagnoristikotk"
            grammi = grammi + 1
        elif katastash == 1 and c.isalpha() == True:
            katastash = 1
        elif katastash == 1 and c.isdigit() == True:
            katastash = 1
        elif katastash == 1 and c == "+":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "-":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "*":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "/":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "<":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == ">":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "=":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == ":":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "(":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == ")":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "[":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "]":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == ";":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == ",":
            katastash = "anagnoristikotk"
        elif katastash == 1 and c == "":
            katastash = "anagnoristikotk"

#kanoume elegxo gia tin katastasi 2 kai gia leukous xaraktires
        elif katastash == 2 and (c == " " or c == "\t"):
            katastash = "statheratk"
        elif katastash == 2 and c == "\n":
            katastash = "statheratk"
            grammi = grammi + 1
        elif katastash == 2 and c.isalpha() == True:
            katastash = "statheratk"
        elif katastash == 2 and c.isdigit() == True:
            katastash = 2
        elif katastash == 2 and c == "+":
            katastash = "statheratk"
        elif katastash == 2 and c == "-":
            katastash = "statheratk"
        elif katastash == 2 and c == "*":
            katastash = "statheratk"
        elif katastash == 2 and c == "/":
            katastash = "statheratk"
        elif katastash == 2 and c == "<":
            katastash = "statheratk"
        elif katastash == 2 and c == ">":
            katastash = "statheratk"
        elif katastash == 2 and c == "=":
            katastash = "statheratk"
        elif katastash == 2 and c == ":":
            katastash = "statheratk"
        elif katastash == 2 and c == "(":
            katastash = "statheratk"
        elif katastash == 2 and c == ")":
            katastash = "statheratk"
        elif katastash == 2 and c == "[":
            katastash = "statheratk"
        elif katastash == 2 and c == "]":
            katastash = "statheratk"
        elif katastash == 2 and c == ";":
            katastash = "statheratk"
        elif katastash == 2 and c == ",":
            katastash = "statheratk"
        elif katastash == 2 and c == "":
            katastash = "statheratk"

        elif katastash == 3 and (c == " " or c == "\t"):
            katastash = "<tk"
        elif katastash == 3 and c == "\n":
            katastash = "<tk"
            grammi = grammi + 1
        elif katastash == 3 and c.isalpha() == True:
            katastash = "<tk"
        elif katastash == 3 and c.isdigit() == True:
            katastash = "<tk"
        elif katastash == 3 and c == "+":
            katastash = "<tk"
        elif katastash == 3 and c == "-":
            katastash = "<tk"
        elif katastash == 3 and c == "*":
            katastash = "<tk"
        elif katastash == 3 and c == "/":
            katastash = "<tk"
        elif katastash == 3 and c == "<":
            katastash = "<tk"
        elif katastash == 3 and c == ">":
            katastash = "<>tk"
        elif katastash == 3 and c == "=":
            katastash = "<=tk"
        elif katastash == 3 and c == ":":
            katastash = "<tk"
        elif katastash == 3 and c == "(":
            katastash = "<tk"
        elif katastash == 3 and c == ")":
            katastash = "<tk"
        elif katastash == 3 and c == "[":
            katastash = "<tk"
        elif katastash == 3 and c == "]":
            katastash = "<tk"
        elif katastash == 3 and c == ";":
            katastash = "<tk"
        elif katastash == 3 and c == ",":
            katastash = "<tk"
        elif katastash == 3 and c == "":
            katastash = "<tk"


        elif katastash == 4 and (c == " " or c == "\t"):
            katastash = ">tk"
        elif katastash == 4 and c == "\n":
            katastash = ">tk"
            grammi = grammi + 1
        elif katastash == 4 and c.isalpha() == True:
            katastash = ">tk"
        elif katastash == 4 and c.isdigit() == True:
            katastash = ">tk"
        elif katastash == 4 and c == "+":
            katastash = ">tk"
        elif katastash == 4 and c == "-":
            katastash = ">tk"
        elif katastash == 4 and c == "*":
            katastash = ">tk"
        elif katastash == 4 and c == "/":
            katastash = ">tk"
        elif katastash == 4 and c == "<":
            katastash = ">tk"
        elif katastash == 4 and c == ">":
            katastash = ">tk"
        elif katastash == 4 and c == "=":
            katastash = ">=tk"
        elif katastash == 4 and c == ":":
            katastash = ">tk"
        elif katastash == 4 and c == "(":
            katastash = ">tk"
        elif katastash == 4 and c == ")":
            katastash = ">tk"
        elif katastash == 4 and c == "[":
            katastash = ">tk"
        elif katastash == 4 and c == "]":
            katastash = ">tk"
        elif katastash == 4 and c == ";":
            katastash = ">tk"
        elif katastash == 4 and c == ",":
            katastash = ">tk"
        elif katastash == 4 and c == "":
            katastash = ">tk"


        elif katastash == 5 and (c == " " or c == "\t"):
            katastash = ":tk"
        elif katastash == 5 and c == "\n":
            katastash = ":tk"
            grammi = grammi + 1
        elif katastash == 5 and c.isalpha() == True:
            katastash = ":tk"
        elif katastash == 5 and c.isdigit() == True:
            katastash = ":tk"
        elif katastash == 5 and c == "+":
            katastash = ":tk"
        elif katastash == 5 and c == "-":
            katastash = ":tk"
        elif katastash == 5 and c == "*":
            katastash = ":tk"
        elif katastash == 5 and c == "/":
            katastash = ":tk"
        elif katastash == 5 and c == "<":
            katastash = ":tk"
        elif katastash == 5 and c == ":":
            katastash = ":tk"
        elif katastash == 5 and c == "=":
            katastash = ":=tk"
        elif katastash == 5 and c == ":":
            katastash = ":tk"
        elif katastash == 5 and c == "(":
            katastash = ":tk"
        elif katastash == 5 and c == ")":
            katastash = ":tk"
        elif katastash == 5 and c == "[":
            katastash = ":tk"
        elif katastash == 5 and c == "]":
            katastash = ":tk"
        elif katastash == 5 and c == ";":
            katastash = ":tk"
        elif katastash == 5 and c == ",":
            katastash = ":tk"
        elif katastash == 5 and c == "":
            katastash = ":tk"

        elif katastash == 6 and (c == " " or c == "\t"):
            katastash = "/tk"
        elif katastash == 6 and c == "\n":
            katastash = "/tk"
            grammi = grammi + 1
        elif katastash == 6 and c.isalpha() == True:
            katastash = "/tk"
        elif katastash == 6 and c.isdigit() == True:
            katastash = "/tk"
        elif katastash == 6 and c == "+":
            katastash = "/tk"
        elif katastash == 6 and c == "-":
            katastash = "/tk"
        elif katastash == 6 and c == "*":
            katastash = 9
        elif katastash == 6 and c == "/":
            katastash = 7
        elif katastash == 6 and c == "<":
            katastash = "/tk"
        elif katastash == 6 and c == ":":
            katastash = "/tk"
        elif katastash == 6 and c == "=":
            katastash = "/tk"
        elif katastash == 6 and c == ":":
            katastash = "/tk"
        elif katastash == 6 and c == "(":
            katastash = "/tk"
        elif katastash == 6 and c == ")":
            katastash = "/tk"
        elif katastash == 6 and c == "[":
            katastash = "/tk"
        elif katastash == 6 and c == "]":
            katastash = "/tk"
        elif katastash == 6 and c == ";":
            katastash = "/tk"
        elif katastash == 6 and c == ",":
            katastash = "/tk"
        elif katastash == 6 and c == "":
            katastash = "/tk"


        elif katastash == 7 and (c == " " or c == "\t"):
            katastash = 7
        elif katastash == 7 and c == "\n":
            katastash = 0
            grammi = grammi + 1
        elif katastash == 7 and c.isalpha() == True:
            katastash = 7
        elif katastash == 7 and c.isdigit() == True:
            katastash = 7
        elif katastash == 7 and c == "+":
            katastash = 7
        elif katastash == 7 and c == "-":
            katastash = 7
        elif katastash == 7 and c == "*":
            katastash = 7
        elif katastash == 7 and c == "/":
            katastash = 8
        elif katastash == 7 and c == "<":
            katastash = 7
        elif katastash == 7 and c == ":":
            katastash = 7
        elif katastash == 7 and c == "=":
            katastash = 7
        elif katastash == 7 and c == ":":
            katastash = 7
        elif katastash == 7 and c == "(":
            katastash = 7
        elif katastash == 7 and c == ")":
            katastash = 7
        elif katastash == 7 and c == "[":
            katastash = 7
        elif katastash == 7 and c == "]":
            katastash = 7
        elif katastash == 7 and c == ";":
            katastash = 7
        elif katastash == 7 and c == ",":
            katastash = 7
        elif katastash == 7 and c == "":
# to errortk einai gia error end of file mesa se sxolia
            katastash = "errortk"


        elif katastash == 8 and (c == " " or c == "\t"):
            katastash = 7
        elif katastash == 8 and c == "\n":
            katastash = 0
            grammi = grammi + 1
        elif katastash == 8 and c.isalpha() == True:
            katastash = 7
        elif katastash == 8 and c.isdigit() == True:
            katastash = 7
        elif katastash == 8 and c == "+":
            katastash = 7
        elif katastash == 8 and c == "-":
            katastash = 7
        elif katastash == 8 and c == "*":
            katastash = "error2tk"
        elif katastash == 8 and c == "/":
            katastash = "error2tk"
        elif katastash == 8 and c == "<":
            katastash = 7
        elif katastash == 8 and c == ":":
            katastash = 7
        elif katastash == 8 and c == "=":
            katastash = 7
        elif katastash == 8 and c == ":":
            katastash = 7
        elif katastash == 8 and c == "(":
            katastash = 7
        elif katastash == 8 and c == ")":
            katastash = 7
        elif katastash == 8 and c == "[":
            katastash = 7
        elif katastash == 8 and c == "]":
            katastash = 7
        elif katastash == 8 and c == ";":
            katastash = 7
        elif katastash == 8 and c == ",":
            katastash = 7
        elif katastash == 8 and c == "":
            katastash = "errortk"


        elif katastash == 9 and (c == " " or c == "\t"):
            katastash = 9
        elif katastash == 9 and c == "\n":
            katastash = 9
            grammi = grammi + 1
        elif katastash == 9 and c.isalpha() == True:
            katastash = 9
        elif katastash == 9 and c.isdigit() == True:
            katastash = 9
        elif katastash == 9 and c == "+":
            katastash = 9
        elif katastash == 9 and c == "-":
            katastash = 9
        elif katastash == 9 and c == "*":
            katastash = 10
        elif katastash == 9 and c == "/":
            katastash = 11
        elif katastash == 9 and c == "<":
            katastash = 9
        elif katastash == 9 and c == ":":
            katastash = 9
        elif katastash == 9 and c == "=":
            katastash = 9
        elif katastash == 9 and c == ":":
            katastash = 9
        elif katastash == 9 and c == "(":
            katastash = 9
        elif katastash == 9 and c == ")":
            katastash = 9
        elif katastash == 9 and c == "[":
            katastash = 9
        elif katastash == 9 and c == "]":
            katastash = 9
        elif katastash == 9 and c == ";":
            katastash = 9
        elif katastash == 9 and c == ",":
            katastash = 9
        elif katastash == 9 and c == "":
            katastash = "errortk"

        elif katastash == 10 and (c == " " or c == "\t"):
            katastash = 9
        elif katastash == 10 and c == "\n":
            katastash = 9
            grammi = grammi + 1
        elif katastash == 10 and c.isalpha() == True:
            katastash = 9
        elif katastash == 10 and c.isdigit() == True:
            katastash = 9
        elif katastash == 10 and c == "+":
            katastash = 9
        elif katastash == 10 and c == "-":
            katastash = 9
        elif katastash == 10 and c == "*":
            katastash = 10
        elif katastash == 10 and c == "/":
            katastash = 0
        elif katastash == 10 and c == "<":
            katastash = 9
        elif katastash == 10 and c == ":":
            katastash = 9
        elif katastash == 10 and c == "=":
            katastash = 9
        elif katastash == 10 and c == ":":
            katastash = 9
        elif katastash == 10 and c == "(":
            katastash = 9
        elif katastash == 10 and c == ")":
            katastash = 9
        elif katastash == 10 and c == "[":
            katastash = 9
        elif katastash == 10 and c == "]":
            katastash = 9
        elif katastash == 10 and c == ";":
            katastash = 9
        elif katastash == 10 and c == ",":
            katastash = 9
        elif katastash == 10 and c == "":
            katastash = "errortk"


        elif katastash == 11 and (c == " " or c == "\t"):
            katastash = 9
        elif katastash == 11 and c == "\n":
            katastash = 9
            grammi = grammi + 1
        elif katastash == 11 and c.isalpha() == True:
            katastash = 9
        elif katastash == 11 and c.isdigit() == True:
            katastash = 9
        elif katastash == 11 and c == "+":
            katastash = 9
        elif katastash == 11 and c == "-":
            katastash = 9
        elif katastash == 11 and c == "*":
# to error2tk einai gia error sxoliwn
            katastash = "error2tk"
        elif katastash == 11 and c == "/":
            katastash = "error2tk"
        elif katastash == 11 and c == "<":
            katastash = 9
        elif katastash == 11 and c == ":":
            katastash = 9
        elif katastash == 11 and c == "=":
            katastash = 9
        elif katastash == 11 and c == ":":
            katastash = 9
        elif katastash == 11 and c == "(":
            katastash = 9
        elif katastash == 11 and c == ")":
            katastash = 9
        elif katastash == 11 and c == "[":
            katastash = 9
        elif katastash == 11 and c == "]":
            katastash = 9
        elif katastash == 11 and c == ";":
            katastash = 9
        elif katastash == 11 and c == ",":
            katastash = 9
        elif katastash == 11 and c == "":
            katastash = "errortk"

        else:
            print("Grammi %d: Mh apodektos xarakthras"%grammi)
            exit(0)
        if katastash == 0:
            leksh = ""
        else:
#lambanoume ipopsi  mono ta trianta prwta grammata
            if len(leksh) < 30:
                leksh = leksh + c

    if katastash == "anagnoristikotk" or katastash == "statheratk" or katastash == "<tk" or katastash == ">tk" or katastash == ":tk" or katastash == "/tk":
        arxeio.seek(-1,1)                         #gia metafora kersora mia thesi aristera
        leksh = leksh[0:len(leksh)-1]             #gia na mi metrame ton teleytaio xaraktira
        if c == "\n":
            grammi = grammi - 1

    if katastash == "errortk":
        print("Grammi %d: EOF mesa sta sxolia"%grammi)
        exit(0)
    elif katastash == "error2tk":
        print("Grammi %d: Sxolia mesa sta sxolia"%grammi)
        exit(0)

		
# to aytomato mas anagnwrizei desmeymenes lekseis kai metabainei stis antistoixes telikes katastaseis
    if leksh == "program":
        katastash = "programtk"
    elif leksh == "endprogram":
        katastash = "endprogramtk"
    elif leksh == "declare":
        katastash = "declaretk"
    elif leksh == "if":
        katastash = "iftk"
    elif leksh == "then":
        katastash = "thentk"
    elif leksh == "else":
        katastash = "elsetk"
    elif leksh == "endif":
        katastash = "endiftk"
    elif leksh == "dowhile":
        katastash = "dowhiletk"
    elif leksh == "enddowhile":
        katastash = "enddowhiletk"
    elif leksh == "while":
        katastash = "whiletk"
    elif leksh == "endwhile":
        katastash = "endwhiletk"
    elif leksh == "loop":
        katastash = "looptk"
    elif leksh == "endloop":
        katastash = "endlooptk"
    elif leksh == "exit":
        katastash = "exittk"
    elif leksh == "forcase":
        katastash = "forcasetk"
    elif leksh == "endforcase":
        katastash = "endforcasetk"
    elif leksh == "incase":
        katastash = "incasetk"
    elif leksh == "endincase":
        katastash = "endincasetk"
    elif leksh == "when":
        katastash = "whentk"
    elif leksh == "endwhen":
        katastash = "endwhentk"
    elif leksh == "default":
        katastash = "defaulttk"
    elif leksh == "enddefault":
        katastash = "enddefaulttk"
    elif leksh == "function":
        katastash = "functiontk"
    elif leksh == "endfunction":
        katastash = "endfunctiontk"
    elif leksh == "return":
        katastash = "returntk"
    elif leksh == "in":
        katastash = "intk"
    elif leksh == "inout":
        katastash = "inouttk"
    elif leksh == "inandout":
        katastash = "inandouttk"
    elif leksh == "and":
        katastash = "andtk"
    elif leksh == "or":
        katastash = "ortk"
    elif leksh == "not":
        katastash = "nottk"
    elif leksh == "input":
        katastash = "inputtk"
    elif leksh == "print":
        katastash = "printtk"

    if katastash == "statheratk":
#oi akeraioi arithmoi prepei na exoun times apo -32767 ws 32767
#stin Starlet bebaia to prosimo einai proairetiko
        if int(leksh) > 32767:
            print("Grammi %d: Exeis dwsei megalo noumero"%grammi)
            exit(0)
			
			
			
#arxizoume kai elegxoyme tous kanones tis grammatikis tis Starlet enan enan
def program():
    global katastash, leksh, grammi, onomaProgrammatos

    if katastash == "programtk":
        lektikos()
# id einai to anagnwristiko mas
        if katastash == "anagnoristikotk":
            onomaProgrammatos = leksh

            lektikos()
            eisagwghScope(onomaProgrammatos)

            block(onomaProgrammatos)

            diagrafhScope()
            if katastash != "endprogramtk":
                print("Grammi %d: (syntaktikos) Den teleiwnei to programa me to endprogram"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma programmatos"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den ksekinaei to programa me to program"%grammi)
        exit(0)

#to onomaProgrammatos einai to onoma tou program
#to onoma san parametros deixnei to onoma tou block(synarthshs h tou programmatos)
#xreiazomaste kai ta 2 gia na 3eroume pote tha valoume to halt
#kai gia na valoume to begin block, onoma
def block(onoma):
    global onomaProgrammatos, pinakasSymvolwn, returnCounter

    declarations()
    subprograms()

    #phgainume sto entity pou afora thn synarthsh pou pame na 3ekinhsume kai vazume san startquad(thesh 2 sto entity) to label tou begin block
    #to entity einai panta teleytaio sthn lista me ta entities tou katw scope
    if onoma != onomaProgrammatos:
        pinakasSymvolwn[1][2][len(pinakasSymvolwn[1][2]) -1][2] = nextquad()
    genquad("begin block", onoma, "_", "_")
    returnCounter = 0
    statements()

    if onoma == onomaProgrammatos:
        genquad("halt", "_", "_", "_")
        if returnCounter != 0:
            print("Grammi %d: (shmasiologikos) Yparxei return sto kyriws programma"%grammi)
            exit(0)
    else:
        #gia tis synarthseis vazoume sthn thesh 3 to framelength sto entity me thn idia logikh me to startquad
        #to framelength einai sthn thesh 3 tou scope gia thn synarthsh
        pinakasSymvolwn[1][2][len(pinakasSymvolwn[1][2]) -1][3] = pinakasSymvolwn[0][3]
        if returnCounter == 0:
            print("Grammi %d: (shmasiologikos) Den yparxei return sthn synarthsh"%grammi)
            exit(0)
    genquad("end block", onoma, "_", "_")

def declarations():
    while katastash == "declaretk":
        lektikos()
        varlist()
        if katastash == ";tk":
            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ;"%grammi)
            exit(0)

def varlist():
    global metavlhtes

    if katastash == "anagnoristikotk":
        metavlhtes.append(leksh)

       #to offset einai to trexon framelength ths synarthshs
        offset = pinakasSymvolwn[0][3]
        #gia metavlhth to entity einai ths morfhs: [typos, onoma, offset]
        entity = ['metavlith', leksh, offset]
        eisagwghEntity(entity)
        lektikos()
        while katastash == ",tk":
            lektikos()
            if katastash == "anagnoristikotk":
                metavlhtes.append(leksh)

                #to offset einai to trexon framelength ths synarthshs
                offset = pinakasSymvolwn[0][3]
                #gia metavlhth to entity einai ths morfhs: [typos, onoma, offset]
                entity = ['metavlith', leksh, offset]
                eisagwghEntity(entity)
                lektikos()
            else:
                print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma metavliths"%grammi)
                exit(0)

#katanalwnoume to functiontk tis subprogram gia na doume an ontws
#iparxei o kanonas subprograms
def subprograms():
    while katastash == "functiontk":
        lektikos()
        subprogram()

def subprogram():
    if katastash == "anagnoristikotk":
        onoma = leksh
        lektikos()

        #eisagoume thn synarthsh kai san scope kai san entity
        #epeidh den 3eroume akoma ta startquad kai framelength ta vazoume -1
        entity = ['function', onoma, -1, -1]
        eisagwghEntity(entity)
        eisagwghScope(onoma)

        funcbody(onoma)

        diagrafhScope()
        if katastash == "endfunctiontk":
            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka to endfunction"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma synartishs"%grammi)
        exit(0)

def funcbody(onoma):
    formalpars()
    block(onoma)

def formalpars():
    if katastash == "(tk":
        lektikos()
        formalparlist()

        if katastash == ")tk":
            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
        exit(0)

#gia na uparxei i formalparlist tha prepei na uparxei i formalparitem i opoia 
#ksekinaei me in, inout i inandout
def formalparlist():
    if katastash == "intk" or katastash == "inouttk" or katastash == "inandouttk":
        formalparitem()
        while katastash == ",tk":
            lektikos()
            formalparitem()

def formalparitem():
    if katastash == "intk":
        lektikos()
        if katastash == "anagnoristikotk":
            offset = pinakasSymvolwn[0][3]
            #gia parametro to entity einai ths morfhs: [typos, onoma, offset]
            entity = ["CV", leksh, offset]
            eisagwghEntity(entity)
            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma parametrou"%grammi)
            exit(0)
    elif katastash == "inouttk":
        offset = pinakasSymvolwn[0][3]

        lektikos()
        if katastash == "anagnoristikotk":
            #gia parametro to entity einai ths morfhs: [typos, onoma, offset]
            entity = ["REF", leksh, offset]
            eisagwghEntity(entity)

            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma parametrou"%grammi)
            exit(0)
    elif katastash == "inandouttk":
        offset = pinakasSymvolwn[0][3]
        #gia parametro to entity einai ths morfhs: [typos, onoma, offset]

        lektikos()
        if katastash == "anagnoristikotk":
            entity = ["CP", leksh, offset]
            eisagwghEntity(entity)

            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma parametrou"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka in, inout h inandout"%grammi)
        exit(0)


def statements():
    statement()
    while katastash == ";tk":
        lektikos()
        statement()

def statement():
    global exitList, loopCounter, returnCounter
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <assignment-stat>
    if katastash == "anagnoristikotk":
        anagnoristiko = leksh
        lektikos()
        assignment_stat(anagnoristiko)
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <if-stat>
    elif katastash == "iftk":
        lektikos()
        if_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <while-stat>
    elif katastash == "whiletk":
        lektikos()
        while_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <do-while-stat>
    elif katastash == "dowhiletk":
        lektikos()
        do_while_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <loop-stat>
    elif katastash == "looptk":
        lektikos()
        loop_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <exit-stat>
    elif katastash == "exittk":
        if loopCounter == 0:
            print("Grammi %d: (shmasiologikos) Den vrhka anoixto loop"%grammi)
            exit(0)
        elist = makelist(nextquad())
        genquad("jump", "_", "_", "_")
        exitList = merge(exitList, elist)
        lektikos()
#diabazw/"krifokoitaw" tin prwti lektiki monada forcase
    elif katastash == "forcasetk":
        lektikos()
        forcase_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada incase
    elif katastash == "incasetk":
        lektikos()
        incase_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <return-stat>
    elif katastash == "returntk":
        returnCounter += 1
        lektikos()
        return_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada input
    elif katastash == "inputtk":
        lektikos()
        input_stat()
#diabazw/"krifokoitaw" tin prwti lektiki monada tis <print-stat>
    elif katastash == "printtk":
        lektikos()
        print_stat()

def assignment_stat(anagnoristiko):
    entity = eyreshEntity(anagnoristiko)
    if entity[0] == 'function':
        print("Grammi %d: (shmasiologikos) To %s einai synarthsh "%(grammi, place))
        exit(0)
    if katastash == ":=tk":
        lektikos()
        eplace = expression()
        genquad(":=", eplace, "_", anagnoristiko)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka :="%grammi)
        exit(0)


def if_stat():
    if katastash == "(tk":
        lektikos()
        condTrue, condFalse = condition()
        if katastash == ")tk":
            lektikos()
            if katastash == "thentk":
                lektikos()

                backpatch(condTrue, nextquad())

                statements()

                jumplist = makelist(nextquad())
                genquad("jump","_","_","_")

                backpatch(condFalse, nextquad())
                elsepart()

                backpatch(jumplist, nextquad())

                if katastash == "endiftk":
                    lektikos()
                else:
                    print("Grammi %d: (syntaktikos) Den vrhka endif"%grammi)
                    exit(0)
            else:
                print("Grammi %d: (syntaktikos) Den vrhka then"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
        exit(0)

#epeidi exoume or keno gia ayto kai den elegxoume gia else alles periptwseis
def elsepart():
    if katastash == "elsetk":
        lektikos()
        statements()

def while_stat():
    startWhile = nextquad()
    if katastash == "(tk":
        lektikos()
        condTrue, condFalse = condition()
        if katastash == ")tk":
            lektikos()

            backpatch(condTrue, nextquad())

            statements()

            genquad("jump", "_", "_", startWhile)
            if katastash == "endwhiletk":
                lektikos()

                backpatch(condFalse, nextquad())

            else:
                print("Grammi %d: (syntaktikos) Den vrhka endwhile"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
        exit(0)

def do_while_stat():

    startDo = nextquad()

    statements()

    if katastash == "enddowhiletk":
        lektikos()
        if katastash == "(tk":
            lektikos()
            condTrue, condFalse = condition()

            backpatch(condTrue, startDo)
            if katastash == ")tk":
                backpatch(condFalse, nextquad())
                lektikos()
            else:
                print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka while"%grammi)
        exit(0)

def loop_stat():

    global exitList, loopCounter

    loopCounter += 1

    exitListTouEkswLoop = exitList

    startLoop = nextquad()
    exitList = emptylist()

    statements()

    if katastash == "endlooptk":
        loopCounter -= 1

        lektikos()
        genquad("jump", "_", "_", startLoop)
        backpatch(exitList, nextquad())

        exitList = exitListTouEkswLoop
    else:
        print("Grammi %d: (syntaktikos) Den vrhka endloop"%grammi)
        exit(0)

def forcase_stat():

    startForcase = nextquad()
    jumplist = emptylist()

    while katastash == "whentk":
        lektikos()
        if katastash == "(tk":
            lektikos()
            condTrue, condFalse = condition()
            if katastash == ")tk":
                lektikos()
                if katastash == ":tk":
                    backpatch(condTrue, nextquad())
                    lektikos()
                    statements()
                    jlist = makelist(nextquad())
                    genquad("jump", "_", "_", "_")
                    jumplist = merge(jumplist, jlist)

                    backpatch(condFalse, nextquad())
                else:
                    print("Grammi %d: (syntaktikos) Den vrhka :"%grammi)
                    exit(0)
            else:
                print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
            exit(0)

    if katastash == "defaulttk":
        lektikos()
        if katastash == ":tk":
            lektikos()
            statements()

            genquad("jump", "_", "_", startForcase)

            if katastash == "enddefaulttk":
                lektikos()
                if katastash == "endforcasetk":
                    lektikos()
                    backpatch(jumplist, nextquad())
                else:
                    print("Grammi %d: (syntaktikos) Den vrhka endforcase"%grammi)
                    exit(0)
            else:
                print("Grammi %d: (syntaktikos) Den vrhka enddefault"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka :"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka default"%grammi)
        exit(0)

def incase_stat():

    startIncase = nextquad()
    flag = newtemp()
    genquad(":=", "0", "_", flag)

    while katastash == "whentk":
        lektikos()
        if katastash == "(tk":
            lektikos()
            condTrue, condFalse = condition()
            if katastash == ")tk":
                lektikos()
                if katastash == ":tk":
                    lektikos()
                    backpatch(condTrue, nextquad())
                    genquad(":=", "1", "_", flag)

                    statements()

                    backpatch(condFalse, nextquad())
                else:
                    print("Grammi %d: (syntaktikos) Den vrhka :"%grammi)
                    exit(0)
            else:
                print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
            exit(0)

    genquad("=", flag, "1", startIncase)

    if katastash == "endincasetk":
        lektikos()
    else:
        print("Grammi %d: (syntaktikos) Den vrhka endincase"%grammi)
        exit(0)

def return_stat():
    eplace = expression()
    genquad("retv", "_", "_", eplace)

def print_stat():
    eplace = expression()
    genquad("out", "_", "_", eplace)

def input_stat():
    if katastash == "anagnoristikotk":
        genquad("inp", "_", "_", leksh)
        entity = eyreshEntity(leksh)
        if entity[0] == 'function':
            print("Grammi %d: (shmasiologikos) To %s einai synarthsh "%(grammi, place))
            exit(0)

        lektikos()
    else:
        print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma metavliths"%grammi)
        exit(0)

def actualpars():
    if katastash == "(tk":
        lektikos()
        actualparlist()

        if katastash == ")tk":
            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka ("%grammi)
        exit(0)

#i actualparlist krifokoitaei tin actualparitem kai 
#katanalwnei tin prwti lektiki monada: in, inout i inandout
def actualparlist():
    if katastash == "intk" or katastash == "inouttk" or katastash == "inandouttk":
        actualparitem()
        while katastash == ",tk":
            lektikos()
            actualparitem()

def actualparitem():
    if katastash == "intk":
        lektikos()
        eplace = expression()
        genquad("par", eplace, "CV", "_")
    elif katastash == "inouttk":
        lektikos()
        if katastash == "anagnoristikotk":
            genquad("par", leksh, "REF", "_")

            entity = eyreshEntity(leksh)
            if entity[0] == 'function':
                print("Grammi %d: (shmasiologikos) To %s einai synarthsh "%(grammi, place))
                exit(0)

            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma parametrou"%grammi)
            exit(0)
    elif katastash == "inandouttk":
        lektikos()
        if katastash == "anagnoristikotk":
            genquad("par", leksh, "CP", "_")

            entity = eyreshEntity(leksh)
            if entity[0] == 'function':
                print("Grammi %d: (shmasiologikos) To %s einai synarthsh "%(grammi, place))
                exit(0)

            lektikos()
        else:
            print("Grammi %d: (syntaktikos) Den vrhka anagnoristiko, dld onoma parametrou"%grammi)
            exit(0)
    else:
        print("Grammi %d: (syntaktikos) Den vrhka in, inout h inandout"%grammi)
        exit(0)



def condition():

    bt1True, bt1False = boolterm()
    while katastash == "ortk":

        backpatch(bt1False, nextquad())
        lektikos()
        bt2True, bt2False = boolterm()

        bt1True = merge(bt1True, bt2True)
        bt1False = bt2False

    condTrue = bt1True
    condFalse = bt1False

    return condTrue, condFalse

def boolterm():

    bf1True, bf1False = boolfactor()
    while katastash == "andtk":

        backpatch(bf1True, nextquad())
        lektikos()
        bf2True, bf2False = boolfactor()

        bf1True = bf2True
        bf1False = merge(bf1False, bf2False)

    btTrue = bf1True
    btFalse = bf1False

    return btTrue, btFalse

def boolfactor():
    if katastash == "nottk":
        lektikos()
        if katastash == "[tk":
            lektikos()
            condTrue, condFalse = condition()

            if katastash == "]tk":
                lektikos()
                bfTrue = condFalse
                bfFalse = condTrue
                return bfTrue, bfFalse

            else:
                print("Grammi %d: (syntaktikos) Den vrhka ]"%grammi)
                exit(0)
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ["%grammi)
            exit(0)
    elif katastash == "[tk":
        lektikos()
        condTrue, condFalse = condition()

        if katastash == "]tk":
            lektikos()
            bfTrue = condTrue
            bfFalse = condFalse
            return bfTrue, bfFalse
        else:
            print("Grammi %d: (syntaktikos) Den vrhka ]"%grammi)
            exit(0)
    else:
        e1place = expression()
        relop = relational_oper()
        e2place = expression()

        bfTrue = makelist(nextquad())
        genquad(relop, e1place, e2place, "_")
        bfFalse = makelist(nextquad())
        genquad("jump","_","_","_")

        return bfTrue, bfFalse

def expression():
    optional_sign()
    t1place = term()
#krifokoitame tin <add-oper> gia sin i plin operators
    while katastash == "+tk" or katastash == "-tk":
        if katastash == "+tk":
            op = "+"
        else:
            op = "-"
        lektikos()
        t2place = term()

        w = newtemp()
        genquad(op, t1place, t2place, w)
        t1place = w
    eplace = t1place

    return eplace

def term():

    f1place = factor()

#krifokoitame kai katanalwnoume tin prwti lektiki monada dld * i / operators
    while katastash == "*tk" or katastash == "/tk":
        if katastash == "*tk":
            op = "*"
        else:
            op = "/"

        lektikos()
        f2place = factor()

        w = newtemp()
        genquad(op, f1place, f2place, w)
        f1place = w

    tplace = f1place

    return tplace

def factor():
    if katastash == "statheratk":
        place = leksh
        lektikos()
        return place
    elif katastash == "(tk":
        lektikos()
        place = expression()
        if katastash == ")tk":
            lektikos()
            return place
        else:
            print("Grammi %d: (syntaktikos) Den vrhka )"%grammi)
            exit(0)
    elif katastash == "anagnoristikotk":
        place = leksh
        lektikos()
        #to idtail ean den einai keno shmainei oti exw klhsh synarthshs kai to apotelesma
        #einai h parametros RET poy tha vrei. Pername thn stathera poy exoyme wste afenos na thn valoyme
        #sto call afeterou na thn epistrepsoume ean to idtail einai to keno(e)
        place = idtail(place)
        return place
    else:
        print("Grammi %d: (syntaktikos) Den vrhka stathera, metavlith h ("%grammi)
        exit(0)


def idtail(place):
#elegxoume gia ( ,dld krifokoitame actualpars
    if katastash == "(tk":
        entity = eyreshEntity(place)
        if entity[0] != 'function':
            print("Grammi %d: (shmasiologikos) To %s den einai synarthsh "%(grammi, place))
            exit(0)
        actualpars()
        w = newtemp()
        genquad("par", w, "RET", "_")
        genquad("call", place, "_", "_")
        return w
    else:
        entity = eyreshEntity(place)
        if entity[0] == 'function':
            print("Grammi %d: (shmasiologikos) To %s einai synarthsh "%(grammi, place))
            exit(0)
        return place

def relational_oper():
    if katastash == "=tk" or katastash == "<=tk" or katastash == ">=tk" or katastash == ">tk" or katastash == "<tk" or katastash == "<>tk":
        if katastash == "=tk":
            relop = "="
        elif katastash == "<=tk":
            relop = "<="
        elif katastash == ">=tk":
            relop = ">="
        elif katastash == ">tk":
            relop = ">"
        elif katastash == "<tk":
            relop = "<"
        elif katastash == "<>tk":
            relop = "<>"
        lektikos()

        return relop
    else:
        print("Grammi %d: (syntaktikos) Den vrhka telesth sysxetishs"%grammi)
        exit(0)

#krifokoitame tin <add-oper> gia + i - operators        
def optional_sign():
    if katastash == "+tk" or katastash == "-tk":
        lektikos()


def nextquad():
    return label

def newtemp():
    global counter, metavlhtesTemp
    temp = "T_" + str(counter)
    counter = counter + 1

    offset = pinakasSymvolwn[0][3]
    #gia metavlith proswrinh to entity einai ths morfhs: [typos, onoma, offset]
    entity = ["proswrinh", temp, offset]
    eisagwghEntity(entity)
    metavlhtesTemp.append(temp)
    return temp

def genquad(op, x, y, z):
    global tetrades, label

    tetrada = [label, op, x, y, z]
    tetrades.append(tetrada)

    l = int(label)
    l = l + 10
    label = str(l)

def emptylist():
    return []

def makelist(x):
    return [x]

def merge(l1, l2):

    return l1+l2

def backpatch(list1, z):
    global tetrades

    #gia kathe etiketa sthn lista list1
    for l in list1:
        #thn elegxw me kathe tetrada
        for i in range(len(tetrades)):
            #otan vrw thn tetrada poy antistoixei sthn etiketa thn symplhrwnw me to z
            #to tetrades[i][0] einai h thesh ths etiketas sthn tetrada
            if tetrades[i][0] == l:
                #h thesh poy prepei na symplhrwsw einai h 4 afou to z einai 4o(exoume kai thn etiketa giayto paei sto 4)
                tetrades[i][4] = z
                break

def ektypwshEndiamesou():
    global tetrades

    #krataw to onoma tou arxeiou eisodou xwris thn katalh3h stl
    onomaArxeiou = sys.argv[1][:len(sys.argv[1])-3]
    #kai tou vazw katalh3h int gia ton endiameso kwdika
    onomaArxeiou = onomaArxeiou + "int"
    arxeioInt = open(onomaArxeiou, "w")
    for i in range(len(tetrades)):
        print(tetrades[i])
        arxeioInt.write(",".join(tetrades[i]) +"\n")
    arxeioInt.close()


def ektypwshC():
    global tetrades

    #krataw to onoma tou arxeiou eisodou xwris thn katalh3h stl
    onomaArxeiou = sys.argv[1][:len(sys.argv[1])-3]
    #kai tou vazw katalh3h int gia thn C
    onomaArxeiou = onomaArxeiou + "c"
    arxeioC = open(onomaArxeiou, "w")
    arxeioC.write("#include <stdio.h>\n")
    arxeioC.write("int main(){\n")

    for i in range(len(metavlhtes)):
        arxeioC.write("int "+metavlhtes[i] +";\n")
    for i in range(len(metavlhtesTemp)):
        arxeioC.write("int "+metavlhtesTemp[i] +";\n")


    for i in range(len(tetrades)):
        arxeioC.write("//"+",".join(tetrades[i]) +"\n")
        if tetrades[i][1] == "+":
            arxeioC.write("Label"+tetrades[i][0] +": "+tetrades[i][4] + "=" +tetrades[i][2] + "+"+tetrades[i][3]+";\n")
        elif tetrades[i][1] == "-":
            arxeioC.write("Label"+tetrades[i][0] +": "+tetrades[i][4] + "=" +tetrades[i][2] + "-"+tetrades[i][3]+";\n")
        elif tetrades[i][1] == "*":
            arxeioC.write("Label"+tetrades[i][0] +": "+tetrades[i][4] + "=" +tetrades[i][2] + "*"+tetrades[i][3]+";\n")
        elif tetrades[i][1] == "/":
            arxeioC.write("Label"+tetrades[i][0] +": "+tetrades[i][4] + "=" +tetrades[i][2] + "/"+tetrades[i][3]+";\n")
        elif tetrades[i][1] == ":=":
            arxeioC.write("Label"+tetrades[i][0] +": "+tetrades[i][4] + "=" +tetrades[i][2]+";\n")
        elif tetrades[i][1] == "jump":
            arxeioC.write("Label"+tetrades[i][0] +": "+"goto Label" +tetrades[i][4] + ";\n")
        elif tetrades[i][1] == "<":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + "<" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == "<=":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + "<=" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == ">":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + ">" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == ">=":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + ">=" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == "<>":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + "!=" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == "=":
            arxeioC.write("Label"+tetrades[i][0] +": if("+tetrades[i][2] + "==" +tetrades[i][3]+") goto Label"+tetrades[i][4]+";\n")
        elif tetrades[i][1] == "out":
            arxeioC.write("Label"+tetrades[i][0] +": printf(\"%d\\n\","+tetrades[i][4]+");\n")
        elif tetrades[i][1] == "inp":
            arxeioC.write("Label"+tetrades[i][0] +": scanf(\"%d\",&"+tetrades[i][4]+");\n")
        else:
            arxeioC.write("Label"+tetrades[i][0] +": ;\n")
    arxeioC.write("return 0;\n")
    arxeioC.write("}\n")

    arxeioC.close()

#to onoma einai to onoma tou scope pou eisagw
def eisagwghScope(onoma):
    global vathosFwliasmatos, pinakasSymvolwn
    #vathosFwliasmatos, onoma, listaEntity, framelength
    scope = [vathosFwliasmatos, onoma, [], 12]

    pinakasSymvolwn = [scope] + pinakasSymvolwn

    vathosFwliasmatos += 1

def diagrafhScope():
    global vathosFwliasmatos, pinakasSymvolwn


    vathosFwliasmatos -= 1

    #ektypwnoyme ton pinaka symvolwn
    print
    #gia kathe scope
    for i in range(len(pinakasSymvolwn)):
        #typwnoume to vathosFwliasmatos to onoma kai to framelength
        print str(pinakasSymvolwn[i][0])+"-"+pinakasSymvolwn[i][1]+"-"+str(pinakasSymvolwn[i][3])
        #kai meta kathe entity ena tab pio deksia gia kalyterh efmanish
        for j in range(len(pinakasSymvolwn[i][2])):
            print "\t"+str(pinakasSymvolwn[i][2][j])
    #diagrafw thn prwth grammh tou pinaka symvolwn
    pinakasSymvolwn = pinakasSymvolwn[1:len(pinakasSymvolwn)]

def eisagwghEntity(entity):
    global pinakasSymvolwn

    #prin kanw eisagwgh tha dw mhpws exw to idio onoma sthn prwth grammh
    for i in range(len(pinakasSymvolwn[0][2])):
        if entity[1] == pinakasSymvolwn[0][2][i][1]:
            print("Grammi %d: (shmasiologikos) Vrhka 3ana to %s"%(grammi, entity[1]))
            exit(0)
    #eisagw to entity sthn lista me ta entities tou scope sthn arxh tou pinaka symvolwn
    #h lista me ta entities einai sthn thesh 2 tou scope
    pinakasSymvolwn[0][2].append(entity)
    #sthn thesh 0 tou entity exw ton typo tou
    #ean den einai synarthsh ay3anw to framelength ths synarthshs( einai sth thesh 3 tou scope)

    if entity[0] != 'function':
        pinakasSymvolwn[0][3] += 4

def eyreshEntity(onoma):
    global pinakasSymvolwn

    for i in range(len(pinakasSymvolwn)):
        for j in range(len(pinakasSymvolwn[i][2])):
                if onoma == pinakasSymvolwn[i][2][j][1]:
                    return pinakasSymvolwn[i][2][j]

    print("Grammi %d: (shmasiologikos) Den vrhka to %s"%(grammi, onoma))
    exit(0)
#gia swsti leitourgia tou lektikou analiti gia olo to megethos tou arxeiou
lektikos()
program()
ektypwshC()
ektypwshEndiamesou()
