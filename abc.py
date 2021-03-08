name = "my_var" # This has to be a string, variables like my_var1, my_var2 will be created.
value = "[]" # This also has to be a string, even when you want to assign integers! When you want to assign a string "3", you'd do this: value = "'3'"
amount = 5 # This must be an integer. This many variables will be created (my_var1, my_var2 ... my_var5).

for i in range(1, amount+1):
    command_variable = ""
    command_variable = name + str(i) + " = " + value
    exec(command_variable)