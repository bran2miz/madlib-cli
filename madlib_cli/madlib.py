def welcome():
    wlcMsg = """
        ****************************************
        ******Welcome to the Madlib Game! ******
        *****Add Words Based on the Prompt!***
        *****To quit at any time, type "quit"***
        ****************************************
    """
    print(wlcMsg)

def read_template(path):
  try:
    with open(path) as f:
      return f.read()
  except FileNotFoundError:
    raise FileNotFoundError('File cannot be found')
  except Exception as e:
    return "There is a problem : "+ e

def 