test_str = '{"showpassword":"no","bgcolor":"#ffffff"}'
  
# printing original string 
print("The original string is : " + str(test_str))
  
# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)
  
# printing result 
print("The string after binary conversion : " + str(res))



test_str = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxZZaAw="

# printing original string
print("The original string is : " + str(test_str))

# using join() + ord() + format()
# Converting String to binary
res2 = ''.join(format(ord(i), '08b') for i in test_str)

# printing result
print("The string after binary conversion : " + str(res2))

print("Xor the string")
print(res^res2);
