a_string_literal = "foo"
print(a_string_literal)

a_string_literal = """foo"""
print(a_string_literal)

a_string_literal = 'foo'
print(a_string_literal)

a_string_literal = '''foo'''
print(a_string_literal)

a_quote_in_a_triple_quote_literal = """ " ' """
print(a_quote_in_a_triple_quote_literal)

a_quote_newline_in_a_triple_quote_literal = """ \n """
print(a_quote_newline_in_a_triple_quote_literal)

# immutable
course = "Python for beginngers"
print(course.find("d"))
print(course.find("for"))

print("for" in course)

print(course.replace("for", "4"))

print(5 * "*")
print(course[9])
print(course[-1])  # last character. -index (negative index) := start at the end
print(
    """
    A very long string:
    print(course.find("d"))
    print(course.find("for"))

    print('for' in course)
"""
)
