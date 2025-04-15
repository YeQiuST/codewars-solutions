# 🥋 Kata: Alias Gen
# 🔗 URL: https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f
# 🎯 Difficulty: 7 kyu
# ✍️ Language: Python

def alias_gen(f_name, l_name):
    if f_name[0].isdigit() or l_name[0].isdigit():
        return 'Your name must start with a letter from A - Z.'
    else:
        Keyf_name = f_name[0].upper()
        Keyl_name = l_name[0].upper()
        return f'{FIRST_NAME[Keyf_name]} {SURNAME[Keyl_name]}'
