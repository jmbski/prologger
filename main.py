import os
from datetime import datetime
from warskald import utils, AttrDict, cmdx

PROLOGUE_END = '#' * 80
PROLOGUE_END = f'{PROLOGUE_END.strip()}\n'

def get_prologue(file_path: str) -> str:
    if(os.path.exists(file_path)):
        text: list[str] = utils.load_data(file_path, use_global_data_path=False, text_lines=True)
        prologue_lines: list[str] = []
        if(text[0].startswith('#')):
            for line in text:
                if(line.startswith('#')):
                    prologue_lines.append(line)
                else:
                    break
        elif(text[0].startswith('"""') or text[0].startswith("'''")):
            for line in text:
                prologue_lines.append(line)
                if('"""' in line or "'''" in line):
                    break
                
        return ''.join(prologue_lines)
    return ''

def build_prologue(args: AttrDict) -> str:
    author = args.author or args.a
    description = args.description or args.d
    version = args.version or args.v
    ticket_id = args.ticket_id or args.t
    date_format = args.date_format or args.f or '%Y-%m-%d'
    date = datetime.now().strftime(date_format)
    user_id = args.user_id or args.U or cmdx('whoami', print_out=False)
    auto_format_desc = args.auto_format or args.af
    update = args.update or args.u
    file_path = args.file_path or args.f
    prologue = f'''# Author: {author}
# Description: {description}
# Version: {version}
# Ticket ID: {ticket_id}
# Date: {date}
# User ID: {user_id}{PROLOGUE_END}
'''
    open('prologue.txt', 'w').write(prologue)
    return prologue
    

def main():
    args = utils.get_inputs()
    print(args)
    if(isinstance(args, str)):
        prologue = get_prologue(args)
        print(prologue)
    elif(isinstance(args, AttrDict)):
        prologue = build_prologue(args)
        

if(__name__ == '__main__'):
    main()