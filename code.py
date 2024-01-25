store = []

def create_subsequence(s, temp="", index=0):
    if index == len(s):
        store.append(temp)
        return

    # Include the current character in the subsequence
    create_subsequence(s, temp + s[index], index + 1)

    # Exclude the current character from the subsequence
    create_subsequence(s, temp, index + 1)

# Example usage:
input_string = "Haider"
create_subsequence(input_string)
print(store)
