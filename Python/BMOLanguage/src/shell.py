import bmo

while True:
    text = input('$bmo> ')
    result, error = bmo.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)