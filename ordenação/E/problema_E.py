
log_entries = []
while True:
    try:
        log_entry = input()
       
        log_entries.append(log_entry)
    except EOFError:
        break


sorted_entries = sorted(log_entries, key=lambda x: x[:19][::-1])


for entry in sorted_entries:
    print(entry)

