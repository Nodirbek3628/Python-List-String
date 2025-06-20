# Foydalanuvchi FISH (Ism Familiya Sharif) ni kiritadi. Siz uni `'Familiya, Ism Sharif'` shaklida qaytaring.
# **Masalan:**

# ```text
# Input: "Aliyev Vali G'ani o‘g‘li"  
# Output: "Vali G'ani o‘g‘li, Aliyev"
# ```

name = input("Ismingizni kiriting>>")
last_name = input("Faamiliya kiriting>>")
patronymic = input("Otasini ismi>>")

print(f"{name} {patronymic} ,{last_name} .".title())
