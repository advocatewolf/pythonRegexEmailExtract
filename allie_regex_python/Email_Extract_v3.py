import re
import datetime
import os


def process_content(content):
    content = re.sub(r'\r', "", content, flags=re.M)
    content = re.sub(r'Do you agree to the group rules from the admin\?\n.*\n(.*)', r'zxc\1', content, flags=re.M)
    content = re.sub(r'(.*)@(.*)\n', r'zxc\1@\2\n', content, flags=re.M)
    content = re.sub(r'^(?!zxc).*\n', "", content, flags=re.M)
    content = re.sub(r'\n\n', r'\n', content, flags=re.M)
    content = re.sub(r'^zxc', "", content, flags=re.M)
    content = re.sub(r'\n^(.*)@(.*)\n', r',\1@\2\n', content, flags=re.M)
    content = re.sub(r'^I agree', r'', content, flags=re.M)
    content = re.sub(r'\.con$', r'\.com', content, flags=re.M)
    return content


def save_processed_content(content):
    i = 0
    number_of_lines = content.count("\n")
    number_of_email = content.count('@')
    file_path = f"{datetime.date.today()}-allieTask-{number_of_email:03d}email-{number_of_lines:03d}-members-{i:03d}.txt"

    while os.path.exists(file_path):
        i += 1
        file_path = f"{datetime.date.today()}-allieTask-{number_of_email:03d}email-{number_of_lines:03d}-members-{i:03d}.txt"

    with open(file_path, "w", encoding='utf-8') as f:
        f.write(content)



def main():
    with open('Email_Extract_Unmodified.txt', 'r', encoding='utf-8') as f1:
        content = f1.read()

    processed_content = process_content(content)
    save_processed_content(processed_content)


if __name__ == "__main__":
    main()
