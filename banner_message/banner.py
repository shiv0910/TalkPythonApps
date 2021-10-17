# default argument values usage:
# banner function takes 2 arguments here, the 2nd one is the default value n
# it must come after the arguments without default values
def banner(message, border="*"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("HAPPY BIRTHDAY SHAUNIT")
# now if we provide optional argument "*" instead of the default one.. it will b used
banner("happy new year", "-")

# now here message is the positional argument n border state is the keyword argument
# all keyword arguments should b provided after the positional arguments
banner(" dentist, devops", border="*")

# both keyword arguments
banner(border="*", message="good luck")




