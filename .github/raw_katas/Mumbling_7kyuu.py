# 🥋 Kata: Mumbling
# 🔗 URL: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# 🎯 Difficulty: 7 kyu
# ✍️ Language: Python

def accum(st):
    return '-'.join(j.upper() + j.lower()*i for i, j in enumerate(st))
