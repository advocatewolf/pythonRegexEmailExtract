import re
import datetime
import os
import pandas as pd

def main():
    f1 = open('fb_member_request_details.txt', 'r', encoding='utf-8')
        

    content = f1.read()
    delimiter = r"Do you agree to the group rules from th.*\n.*\n"
    list_of_elements = re.split(delimiter, content)
    final_list = []
    # for element in list_of_elements:
    #     if "Hasn't answered membership questions" in element:
    #         list_of_elements.remove(element)
    for element in list_of_elements:
        temp_list = element.split("\n")
        print(temp_list[0])
        try:
            temp_why = temp_list[temp_list.index("Why do you want to join the Virtual Assistant Inner Circle?")+1]
        except ValueError:
            temp_why = None
        try:
            temp_how = temp_list[temp_list.index("How did you find this group?")+1]
        except ValueError:
            temp_how = None
        try:
            temp_email = temp_list[temp_list.index("Would you like us to send you the Ultimate Virtual Assistant Business Plan to help you get started? If so, what’s your e-mail address?")+1]
            temp_email_try = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', temp_email)
        except ValueError:
            temp_email = None
            temp_email_try = None
        try:
            temp_email_try = temp_email_try[0]
        except IndexError:
            temp_email_try = None
        except TypeError:
            temp_email_try = None
        temp_dict = {
            "name":temp_list[0],
            "why":temp_why,
            "how":temp_how,
            "email_try":temp_email_try,
            "email":temp_email
        }
        final_list.append(temp_dict)
    final_df = pd.DataFrame(final_list, columns = final_list[0].keys())
    
    i = 0

    file_path = f"{str(datetime.date.today())}-jacintaTask-{len(final_list):03d}member-{str('%03d'%i)}.txt"
    is_path = os.path.exists(file_path)
    while is_path is True:
        i += 1
        file_path = f"{str(datetime.date.today())}-jacintaTask-{len(final_list):03d}member-{str('%03d'%i)}.txt"
        is_path = os.path.exists(file_path)
    # with open(file_path, "w") as f2:
    #     f2.write(final_df)

    final_df.to_csv(file_path, index=False, encoding='utf-8')
    # print(final_df)
if __name__ == "__main__":
    main()