# PALINDROME TEKSHIRISH (so‘zlar)**

# **Vazifa:** Foydalanuvchi gap kiritadi. Siz gapdagi so‘zlarni alohida qilib, har bir so‘z palindrom (teskari o‘qilganda o‘zi bilan bir xil) ekanligini aniqlang.
# **Masalan:**

# ```text
# Input: "olol radar makka non"  
# Output: ['olol', 'radar', 'non']
# ```
 
texts  = input("So'zlarni birin ketin vergul bilan kiriitng: ")
text = texts.split(",")

palindrom = []

for i in text:
    if i == i[::-1]:   # bunda takrorlangan so'zimiz uzini teskarisiga teng bulsa palindrom so'zga qo'shiladi
        palindrom.append(i)
    else:
        print("Palindrom so'z emas.")
print(palindrom)
