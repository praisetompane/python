from datetime import date

string_variable = "i am a variable"
numeric_variable = 1

print("\n")
print("example of basic format string substitution")
a_formatted_string_literal = f"a formatted with a {string_variable}"
print(a_formatted_string_literal)
print("\n")

a_formatted_string_literal = f"a formatted with a {numeric_variable}"
print(a_formatted_string_literal)
print("\n")

print(
    """example using a conversion modifier '!r'.
      notice the "''" around the value showing it is a string"""
)
a_conversion_field_format_string = f"a formatted with a {string_variable!r}"
print(a_conversion_field_format_string)
print("\n")

print("example using a format spec ':'")
today = date(year=2023, month=1, day=27)
a_formatted_string_with_format_modifier = f"today's date is {today:%Y %B %d}"
print(a_formatted_string_with_format_modifier)
print("\n")

print("""example using '=' .
      notice the expression 'today ='  is in the printed output.""")

a_formatted_string_with_variable_included = f"{today =: %Y %B %d}"
print(a_formatted_string_with_variable_included)
print("\n")

a_formatted_string_with_variable_included_2 = f"{today = }"
print(a_formatted_string_with_variable_included_2)
print("\n")

print("example using a '' in format expression")
backlash_literal = "\t"
print(f"{ord(backlash_literal)}")
print("\n")

print("example using a decimal/float number")
decimal_number = 100/3
print(f"{decimal_number:.2f}")
print("\n")
