# Foydalanuvchi bir nechta xabarlarni `|` bilan ajratib kiritadi. Siz har birini alohida qatorda ko‘rsating.
# **Masalan:**

# ```text
# Input: "Salom|Qalesiz?|Yaxshi o‘tdimi bugun?"  
# Output:  
# Salom  
# Qalesiz?  
# Yaxshi o‘tdimi bugun?
text = "Salom|Qalesiz?|Yaxshi o‘tdimi bugun?"

result = text.split("|")

for i in result:
    print(i)