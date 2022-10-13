import color
from tabulate import tabulate



def ListenerHelper():
    listenerhelper = [
        [color.red('Start Listener'), color.green('The Command That Will Start One Of The Listeners You Have')],
        [color.red('List Listeners'), color.green('The Command That Will List The Listeners You Have')],
        [color.red('Delete Listener'), color.green('The Command That Delete One Of The Listeners You Have')],
        [color.red('Create Listener'), color.green('The Command That Will Create A Listener \n')]
    ]
    print("\n", tabulate(listenerhelper, headers=[color.blue("Options"), color.yellow("Description")]))

def DatabaseHelper():
    Databasehelper = [
        [color.red('Delete Database'), color.green('The Command That Will Clear The Entire Database For You \n')]
    ]
    print("\n", tabulate(Databasehelper, headers=[color.blue("Options"), color.yellow("Description")]))

def PayloadHelper():
    PayloadHelper = [
        [color.red('Generate Payload'), color.green('The Command That Will Generate A Payload To Deliver \n')]
    ]
    print("\n", tabulate(PayloadHelper, headers=[color.blue("Options"), color.yellow("Description")]))

def ImplantsHelper():
    Implantshelper = [
        [color.red('back'), color.green('The Command That Will Leave The Implant You Are Interacting With So You Return To Normal CLI')],
        [color.red('powershell [Command]'), color.green('Run A Powershell Command By Simply Typing Powershell & The Command After')],
        [color.red('cmd [Command]'), color.green('Run A CMD Command By Simply Typing CMD & The Command After \n')]
    ]
    print("\n", tabulate(Implantshelper, headers=[color.blue("Options"), color.yellow("Description")]))

def InteractHelper():
    Implantshelper = [
        [color.red('back'), color.green('The Command That Will Leave The Implant You Are Interacting With So You Return To Normal CLI')],
        [color.red('interact'), color.green('Simply Type Interact And It Will Prompt You For The Implant You Want To Interact With! \n')]
    ]
    print("\n", tabulate(Implantshelper, headers=[color.blue("Options"), color.yellow("Description")]))

def CommandHelper():
    Commandhelper = [
        [color.red('clear'), color.green('The Command That Will Clear The CLI For You If It Starts To Get Very Messy.')],
        [color.red('exit'), color.green('Simply Type Exit And It Will Close The CLI Rather Than Using Control C. \n')]
    ]
    print("\n", tabulate(Commandhelper, headers=[color.blue("Options"), color.yellow("Description")]))