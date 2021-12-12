import re

print("""
    ****************************************
             Welcome to madlib            
     This is a phrasal template word game 
     where one player prompts others for  
     a list of words to substitute for    
     blanks in a story before reading it.                            
    ****************************************
    """)

def read_template(path):
    try:
        with open(path) as file:
            return  file.read()
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')
    except Exception as e:
        return "Something's Going Wrong : "+ e

 

def parse_template(text):
    parse= re.findall(r'\{(.*?)\}', text)
    for item in parse:    
        text=text.replace((item),'',1)
    return text, tuple(parse)




def merge(text,parse):
 
    newtxt=text.format(*parse)

    with open('assets/dark_and_stormy_night_template.text','w') as output:
        output.write(newtxt)
    return newtxt


def midlab():


    text_origin=read_template('assets/make_me_a_video_game_template.text')

    text,parse= parse_template(text_origin)
    array_word=[]
    for s in parse:
        words=input(f'Enter a {s} ')
        array_word.append(words)
    
    new_text=merge(text,array_word)
    
    return new_text


if __name__=='__main__':
  print (midlab())