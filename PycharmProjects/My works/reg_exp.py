# import re
# pattern=r'avodha'
# # if re.match(pattern,'avodha, hello avodha'):
# # if re.search(pattern,'hello avodha how are you'):
# #     print('matched')
# # else:
# #     print('not matched')
# print(re.findall(pattern,'avodha hello avodha how avodha are you avodha'))

# import re
# str='hai avodha how are you'
# pattern=r'avodha'
# new1=re.sub(pattern,'AMAL',str)
# print(new1)

# import re
# pattern=r'av.d.ha'
# if re.search(pattern,'avodkha'):
#     print('matched')
# else:
#     print('not matched')

import re
pattern=r'[A-Z][a-z][0-9]'
if re.search(pattern,'Av3'):
    print('correct')
else:
    print('not matched')