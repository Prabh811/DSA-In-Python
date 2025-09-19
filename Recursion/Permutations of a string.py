def permute(s_list, i):
  """
  Generates all permutations of a string using backtracking.

  Args:
    s_list: A list of characters from the string.
    i: The starting index for the current permutation.
  """
  # Base case: if we have reached the end of the string,
  # a full permutation has been formed.
  if i == len(s_list) - 1:
    print("".join(s_list))
    return

  # Recursive step: iterate through the rest of the string
  for j in range(i, len(s_list)):
    # Swap the characters at indices i and j
    s_list[i], s_list[j] = s_list[j], s_list[i]
    
    # Recursively call permute for the next starting index
    permute(s_list, i + 1)
    
    # Backtrack: swap the characters back to their original positions
    # to explore other possibilities.
    s_list[i], s_list[j] = s_list[j], s_list[i]


# --- Main Execution ---
try:
  input_string = input("Enter a string: ")
  if input_string:
    print("--- Permutations ---")
    # Strings in Python are immutable, so we convert it to a list
    # to allow for in-place swapping of characters.
    permute(list(input_string), 0)
  else:
    print("Input string is empty.")
except (EOFError, KeyboardInterrupt):
  print("\nNo input provided. Exiting.")
