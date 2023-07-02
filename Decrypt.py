#Passwordable Encryption Standard
#the decrypt function for proccesing, decrypting, Show.
def Decrypt(Eword, password):
	#word var, saving result
	word = ""
	#BEword var, beter Eword
	BEword = list(Eword)
	#char list
	charlist = list("ضصثقفغعهخحشسیبلاتنمکگظطزرذدپqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]{};:'\"\\|,<.>/?1234567890=_+()*&^%$#@!~` ")
	#token var, lexer char saving in this
	token = ""
	#for(lexer)
	for i in range(len(Eword)):
		#if current char is - ...
		if BEword[i] == "-":
			#saving the current token to ie
			ie = int(token)
			#Encrypting
			DN = (ie) / (password * 25000256009)
			#add word the char of the number
			word += charlist[int(DN%len(charlist))]
			#clear token
			token = ""
		#if current char is'n - ...
		elif BEword[i] != "-":
			#add char to token
			token += BEword[i]
	#returnnig the word
	return word
