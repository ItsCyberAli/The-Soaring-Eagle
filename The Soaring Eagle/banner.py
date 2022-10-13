from os import terminal_size
from tkinter import N
from turtle import width
import pyfiglet
from tabulate import tabulate
import color

def PrintBanner():
    asciibanner = pyfiglet.figlet_format("Soaring Eagle C2")
    print(color.red(asciibanner))
    print(color.cyan("\t\t\t\tAuthors Twitter: @ItsCyberAli"))
    print(color.yellow("I developed this tool for whoever wants to learn the basics regarding C2 and Malware Development, it is not intended to be used in real world scenarios and engagements you will get caught guaranteed, \nI developed it for learning not evasion. However I am working on something very sophisticated and if you have any questions feel free to reach me on my twitter above or even improve the code and \nCollaborate to help others learn!\n"))

def HelpBanner():
    helpbanner = [
        [color.red('Help {option}'), color.green('The Command That Will Display The Help Menu Of One Of The 4 Below')],
        [color.red('Listeners'), color.green('The Command That Will Show You The Help Menu Of The Listeners')],
        [color.red('Implants'), color.green('The Command That Will Show You The Help Menu Of The Implants')],
        [color.red('Interact'), color.green('The Command That Will Show You The Help Menu Of Interact')],
        [color.red('Database'), color.green('The Command That Will Show You The Help Menu Of The Database')],
        [color.red('Commands'), color.green('The Command That Will Show You The Small Commands For The CLI')],
        [color.red('Payloads'), color.green('The Command That Will Show You The Help Menu Of The Payloads \n')]
    ]
    print(tabulate(helpbanner, headers=[color.blue("Options"), color.yellow("Description")]))