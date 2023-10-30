"""
CP1404 Practical - Client code to use the ProgrammingLanguage class.
Expected time = 30 minutes
Actual time = 20 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# print(python)
# print(ruby)
# print(visual_basic)

programming_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in programming_languages:
    if ProgrammingLanguage.is_dynamic(language):
        print(language.field)
