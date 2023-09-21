import glob

read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        total_lines = 0
        with open(f, "r", encoding="utf-8", errors="ignore") as infile:
            for line in infile:
                total_lines += 1
            outfile.write(f"{f} - {total_lines}\n".encode())
