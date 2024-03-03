import time
import random

heart = [
    "          |",
    "          ||",
    "      --\\ \\||",
    "       --\\ \\||",
    "        --\\ \\||",
    "         --\\ \\|",
    "          --\\ \\",
    "             \\ \\",
    "              \\ \\",
    "               \\ \\",
    "              MM\\ \\MMMM                         MMMMMMMMM",
    "          MMMMMMM\\ \\MMMMMMMM               MMMMMMMMMMMMMMMMMM",
    "       MMMMMMMXXXX\\ \\XXXMMMMMMM         MMMMMMMXXXXXXXXXXMMMMMMM",
    "    MMMMMMXXXXXXXXX\\ \\XXXXXMMMMMM     MMMMMMXXXXXX:::::XXXXXXMMMMMM",
    "   MMMMMXXXXXXXX::::\\ \\:XXXXXXMMMM   MMMMXXXXXX:::::::::::XXXXXMMMMM",
    "  MMMMXXXXXXX::::::::\\ \\::::XXXXMMM MMMXXXX::::::::::::::::::XXXXMMMM",
    " MMMMXXXXXX:::::::::::\\ :::::::XXXMMMXXX:::::::::::.....:::::::XXXMMMM",
    " MMMXXXXX::::::::::::::::::::::::XXXXX:::::::::...........::::::XXXMMM",
    "MMMXXXXX:::::::::::.......:::::::::X::::::::......    ......::::XXXXMMM",
    "MMMXXXX:::::::::..............:::::::::::.......         ....::::XXXMMM",
    "MMMXXXX::::::::..................:::::.......             ...::::XXXMMM",
    "MMMXXXX:::::::.....................:............         ....::::XXXMMM",
    "MMMXXXX:::::::....................................       ....::::XXXMMM",
    "MMMXXXX:::::::......................................    .....::::XXXMMM",
    "MMMXXXXX::::::....................................... ......::::XXXXMMM",
    "MMMMXXXX:::::::.............................................::::XXXMMMM",
    " MMMXXXX::::::::............................................::::XXXMMM",
    " MMMMXXXX::::::::..........................................::::XXXMMMM",
    "  MMMXXXX::::::::::.......................................:::::XXXMMM",
    "  MMMMXXXX:::::::::::...................................::::::XXXMMMM",
    "   MMMXXXXX::::::::::::..............................::::::::XXXXMMM",
    "   MMMMXXXXX:::::::::::::.........................::::::::::XXXXMMMM",
    "    MMMMXXXXX:::::::::::::::...................::::::::::::XXXXMMMM",
    "     MMMMXXXXX:::::::::::::::::.............::::::::::::::XXXXMMMM",
    "      MMMMXXXXXX::::::::::::::::::.......::::::::::::::XXXXXXMMMM",
    "       MMMMXXXXXXXX::::::::::::::::...::::::::::::::XXXXXXXXMMMM",
    "         MMMMXXXXXXXXX::::::::::::::::::::::\\::::XXXXXXXXXMMMM",
    "           MMMMMXXXXXXXXXX:::::::::::::::::\\ \\XXXXXXXXXMMMMM",
    "              MMMMMMXXXXXXXXXXX:::::::::XXXX\\ \\XXXXMMMMMM",
    "                  MMMMMMXXXXXXXXXXX:XXXXXXXXX\\ \\MMMMM",
    "                      MMMMMMXXXXXXXXXXXXXXXMMM\\ \\",
    "                          MMMMMXMMMMM       \\ \\",
    "                              MMMMM           \\ \\   \\",
    "                               MMM             \\ \\ \\",
    "                                M             \\\\\\\\\\",
    "                                               \\\\\\\\",
    "                                                 \\\\",
    "                                                   \\"
]
love = "                         I love you"
for line in heart:
    for char in line:
        if char == ' ':
            print(' ', end='', flush=True)
        else:
            print(char, end='', flush=True)
            time.sleep(0.001)

    print()
for brra in love:
    print(brra, end='', flush=True)
    time.sleep(random.uniform(0.07, 0.19))
