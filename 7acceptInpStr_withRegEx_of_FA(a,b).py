def FA(s):
    # Check if the length is less than 3
    if len(s) < 3:
        return "Rejected"
    
    # Check the first three characters
    if s[0] == '1' and s[1] == '0' and s[2] == '1':
        # After the first three characters, only '1' should appear
        for i in range(3, len(s)):
            if s[i] != '1':
                return "Rejected"
        return "Accepted"
    else:
        return "Rejected"

# Test cases
inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))
