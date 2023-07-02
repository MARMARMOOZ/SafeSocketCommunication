#Passwordable Encryption Standard
#the encrypt function for proccesing, Encrypting, Show.
def Encrypt(word, password):
	#Eword var, Encrypted word
	Eword = ""
	#Bword var, Beter word
	Bword = list(word)
	#char list, list of a,...0
	charlist = list("ضصثقفغعهخحشسیبلاتنمکگظطزرذدپqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]{};:'\"\\|,<.>/?1234567890=_+()*&^%$#@!~` ")
	#for(for detecting all chars in Bword)
	for i in range(len(Bword)):
		#li var, current word has it
		li = Bword[i]
		#rli var, has numerical char
		rli =  0
		#for(for detecting char in charlist and get numerical number)
		for j in range(len(charlist)):
			#check if this char in charlist[j]
			if charlist[j] ==  li:
				#save in rli
				rli = j
		#Encrypting
		rli = rli * (password * 25000256009)
		#saving rli to Eword with str format
		Eword += str(rli)
		#- for space
		Eword += "-"
	#returning the encrypted
	return Eword
