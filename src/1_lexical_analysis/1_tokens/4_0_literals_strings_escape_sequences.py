an_escaped_newline_string_literal = "\\n"
print(an_escaped_newline_string_literal)

an_escaped_backslash_string_literal = "\\"
print(an_escaped_backslash_string_literal)

an_escaped_ascii_bell_string_literal = "\a"
print(an_escaped_ascii_bell_string_literal) 

an_escaped_octal_value_string_literal = "\0o377"
print(an_escaped_octal_value_string_literal)

an_escape_sequence_only_for_string_literals = b"\N{BLACK SPADE SUIT}"
print(an_escape_sequence_only_for_string_literals)

an_escaped_hex_value_only_for_string_literals = "\fu032f"
print(f"uxxxx: {an_escaped_hex_value_only_for_string_literals}")
