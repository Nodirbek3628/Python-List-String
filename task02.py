#  FAOLIYAT TURINI ENUMGA O‘XSHASH QILISH**

# **Vazifa:** Foydalanuvchi bir nechta sohalarni vergul bilan ajratib kiritadi. Siz ularni `snake_case` formatiga keltirib, `_` bilan ajratib yozing.
# **Masalan:**

# ```text
# Input: "Dasturlash, Sun'iy intellekt, Web dizayn"  
# Output: "dasturlash_sun'iy_intellekt_web_dizayn FAOLIYAT TURINI ENUMGA O‘XSHASH QILISH**

# a = "Dasturlash, Sun'iy intellekt, Web dizayn"

# b = a.lower()
# c = b.split(",")
# d = "_".join(c)

# print(d)

text = input("vergul bilan ajratib matn kiriitng.").lower().split(", ")
snake_case = " _ ".join(text)


print(snake_case)