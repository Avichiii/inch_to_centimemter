'''this program converts inch to centimemers'''
def inch_to_cent(convert):
    return  convert * 2.54


convert= int(input("enter in inch: "))

result = inch_to_cent(convert)

print(result)