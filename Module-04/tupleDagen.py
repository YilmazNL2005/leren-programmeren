# Alle dagen van de week zijn: ma t/m zo
# De werkdagen zijn: ma t/m vr
# Weekenddagen zijn: za en zo
# Omgekeerd de dagen van de week is: zo t/m ma
# Omgekeerd werkdagen: vr t/m ma
# Omgekeerd weekenddagen is: zo en za

WEEK = ("ma", "di", "wo", "do", "vr", "za", "zo")

# Alle dagen van de week
for x in range(0,len(WEEK)):
    print(WEEK[x])
print("\n")

# Werkdagen van de week
for x in range(0, len(WEEK) -2, 1):
    print(WEEK[x])
print("\n")

# Weekenddagen
for x in range(5, len(WEEK)):
    print(WEEK[x])
print("\n")

# Omgekeerd alle dagen van de week
for x in range(len(WEEK)-1, -1, -1):
    print(WEEK[x])
print("\n")

# Omgekeerd alle werkdagen van de week
for x in range(len(WEEK)-3, -1, -1):
    print(WEEK[x])
print("\n")

# Omgekeerd alle weekenddagen van de week
for x in range(len(WEEK)-1, 4, -1):
    print(WEEK[x])
print("\n")
