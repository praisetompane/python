from types import GenericAlias

print("Creating GenericAlias by subscripting a generic type")
subscription_generic_alias_creation = list[int]
print(f"{subscription_generic_alias_creation=}\n")

print("Creating GenericAlias directly")
direct_generic_alias_creation = GenericAlias(list, (int))
print(f"{direct_generic_alias_creation=}\n")


assert subscription_generic_alias_creation == direct_generic_alias_creation
