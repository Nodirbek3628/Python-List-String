#  EMAIL DOMENLARINI AJRATISH**

# **Vazifa:** Foydalanuvchi bir nechta email adreslarini vergul bilan kiritadi. Siz har bir emaildan faqat domen (`@gmail.com`, `@mail.ru` va hokazo) qismini ajratib, takrorlanmas qilib ro‘yxatda qaytaring.
# **Masalan:**

# ```text
# Input: "ali@gmail.com,vali@mail.ru,karim@gmail.com"  
# Output: ['@gmail.com', '@mail.ru']
# ```

email_adress = input("Email manzillarini vergul bilan kiriting: ")
email = email_adress.split(",")



print(email)
