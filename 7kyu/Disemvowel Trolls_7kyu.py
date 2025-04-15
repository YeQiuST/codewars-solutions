# 🥋 Kata: Disemvowel Trolls
# 🔗 URL: https://www.codewars.com/kata/52fba66badcd10859f00097e
# 🎯 Difficulty: 7 kyu
# ✍️ Language: Python

def disemvowel(string_):
    return ''.join([char for char in string_ if char.lower() not in 'aeiou'])
