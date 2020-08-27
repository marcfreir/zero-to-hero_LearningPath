#############
### SHELL ###
#############

# BMO
import bmo

while True:
    text = input('$bmo> ')
    result, error = bmo.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)