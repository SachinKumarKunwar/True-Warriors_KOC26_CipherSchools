#take user input (string)
#if the len of string is a greater than 3 
#add "ing" as a suffix in the original string
#else print the same string given by user

from platformdirs import user_cache_dir


user =  input("Give me word")


length = len(user)


def main():
    if length> 3:
        print(user+"ing")
    else:
        print(user)

main()