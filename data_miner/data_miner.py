import re 

def main():
    input_file_1 = "lvl1_bozuk_veri.txt"
    output_file_1 = "lvl1_temiz_rehber.txt"
    clear_file(input_file_1, output_file_1)
    input_file_2 = "lvl2_bozuk_veri.txt"
    output_file_2 = "lvl2_temiz_rehber.txt"
    clear_file(input_file_2, output_file_2)

def clear_file(input_file, output_file):
    mails = []
    numbers = []
    with open(input_file, "r") as file:
        for line in file:
            line = line.rstrip()
            if not line: 
                continue
            is_mail = re.search(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+?\.[a-z]+\b", line)
            is_number = re.search(r"(?<!\d)(?:(?:\+\d{1,3}|0)[ -]*)?\(?\d{3}\)?[ -]*\d{3}[ -]*\d{2}[ -]*\d{2}(?!\d)", line)
            if is_mail:
                mails.append(is_mail.group())
            if is_number:
                number = is_number.group()
                number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                numbers.append(number)
    with open(output_file, "w") as file:
        file.write("Mails:\n\n")
        for mail in mails:
            file.write(mail + "\n")
        file.write("\nNumbers:\n\n")
        for number in numbers:
            file.write(number + "\n")


if __name__ == "__main__":
    main()




