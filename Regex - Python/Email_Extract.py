import re
import datetime
import os


f1 = open('Email_Extract_Unmodified.txt', 'r', encoding='utf8')
    

content = f1.read()
res_content = re.sub(r'\r',"",content,flags=re.M)
res_content = re.sub(r'Do you agree to the group rules from the admin\?\n.*\n(.*)',r'zxc\1',res_content,flags=re.M)
res_content = re.sub(r'(.*)@(.*)\n',r'zxc\1@\2\n',res_content,flags=re.M)
res_content = re.sub(r'^(?!zxc).*\n',"",res_content,flags=re.M)
res_content = re.sub(r'\n\n',r'\n',res_content,flags=re.M)
res_content = re.sub(r'^zxc',"",res_content,flags=re.M)
res_content = re.sub(r'\n^(.*)@(.*)\n',r',\1@\2\n',res_content,flags=re.M)

print(str(datetime.date.today()))
i = 0

path = str(datetime.date.today()) + '-allieTask-'+ str('%03d'%i) +'.txt'
is_path = os.path.exists(path)
while is_path is True:
    i += 1
    path = str(datetime.date.today()) + '-allieTask-'+ str('%03d'%i) +'.txt'
    is_path = os.path.exists(path)
    print(is_path)
with open(str(datetime.date.today())+'-allieTask-'+str('%03d' % i)+'.txt','w', encoding='utf8') as f2:
    f2.write(res_content)
        