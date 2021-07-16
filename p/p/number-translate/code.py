# Here we ask for the phrase
abc = input("\nInsert here your phrase or your word: ")

# Here we replace the letter by the number
x = abc.replace("a", "11").replace("b", "12").replace("c", "13").replace("d", "21").replace("e", "22").replace("f", "23").replace("g", "31").replace("h", "32").replace("i", "33").replace("j", "41").replace("k", "42").replace("l", "43").replace("m", "51").replace("n", "52").replace("ñ", "53").replace("o", "61").replace("p", "62").replace("q", "63").replace("r", "71").replace("s", "72").replace("t", "73").replace("u", "81").replace("v", "82").replace("w", "83").replace("x", "91").replace("y", "92").replace("z", "93").replace(" ", "0")
print("> " + x.replace("A", "11").replace("B", "12").replace("C", "13").replace("D", "21").replace("E", "22").replace("F", "23").replace("G", "31").replace("H", "32").replace("I", "33").replace("J", "41").replace("K", "42").replace("L", "43").replace("M", "51").replace("N", "52").replace("Ñ", "53").replace("O", "61").replace("P", "62").replace("Q", "63").replace("R", "71").replace("S", "72").replace("T", "73").replace("U", "81").replace("V", "82").replace("W", "83").replace("X", "91").replace("Y", "92").replace("Z", "93").replace(".", "/").replace(",", "."))

# And here is the loop
q1 = input("\nDo you want to close the program? [Y/N]: ")
if q1 == "Yes" or q1 == "yes" or q1 == "Y" or q1 == "y" or q1 == "yeah" or q1 == "Yeah" or q1 == "Close" or q1 == "close":
    exit()
else:
    b = 10
    
while b == 10:
    abc = input("\nInsert here your phrase or your word: ")
    x = abc.replace("a", "11").replace("b", "12").replace("c", "13").replace("d", "21").replace("e", "22").replace("f", "23").replace("g", "31").replace("h", "32").replace("i", "33").replace("j", "41").replace("k", "42").replace("l", "43").replace("m", "51").replace("n", "52").replace("ñ", "53").replace("o", "61").replace("p", "62").replace("q", "63").replace("r", "71").replace("s", "72").replace("t", "73").replace("u", "81").replace("v", "82").replace("w", "83").replace("x", "91").replace("y", "92").replace("z", "93").replace(" ", "0")
    print("> " + x.replace("A", "11").replace("B", "12").replace("C", "13").replace("D", "21").replace("E", "22").replace("F", "23").replace("G", "31").replace("H", "32").replace("I", "33").replace("J", "41").replace("K", "42").replace("L", "43").replace("M", "51").replace("N", "52").replace("Ñ", "53").replace("O", "61").replace("P", "62").replace("Q", "63").replace("R", "71").replace("S", "72").replace("T", "73").replace("U", "81").replace("V", "82").replace("W", "83").replace("X", "91").replace("Y", "92").replace("Z", "93").replace(".", "/").replace(",", "."))
    q = input("\nDo you want to close the program? [Y/N]: ")
    if q == "Yes" or q == "yes" or q == "Y" or q == "y" or q == "yeah" or q == "Yeah" or q == "Close" or q == "close":
        break

# Someday I'll do the translation of the numbers
#If you think you can help me in the project, I invite you to modify the code or write to my twitter: www.twitter.com/garlok_dev