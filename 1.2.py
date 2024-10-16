def filter_strings(filter_func, string_array):
    # Use a list comprehension to apply the filter function to each element in the array
    return [s for s in string_array if filter_func(s)]

# Define the filtering criteria as lambda functions
filter_out_spaces = lambda s: ' ' not in s
filter_out_starting_with_a = lambda s: not s.startswith('a')
filter_out_shorter_than_five = lambda s: len(s) >= 5

# Example array of strings
strings = ["apple", "banana", "cat", "adventure", "ant", "alpha", "bat", "echo", "delta"]

# Call the function with different filters
no_spaces = filter_strings(filter_out_spaces, strings)
not_starting_with_a = filter_strings(filter_out_starting_with_a, strings)
longer_than_or_equal_five = filter_strings(filter_out_shorter_than_five, strings)

# Print the results
print("Strings without spaces:", no_spaces)
print("Strings not starting with 'a':", not_starting_with_a)
print("Strings longer than or equal to 5 characters:", longer_than_or_equal_five)