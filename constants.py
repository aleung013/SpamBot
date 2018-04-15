Prefix = '$'
Delim = ' '


#########################
###  Output Messages  ###
#########################
Message_Unknown_Command = 'I don\'t understand that command.'
Message_Help = 'My name is SpamBot... Here are some commands I can do:\n' + \
               '**{}help [command]** - Displays this message. If a command is given, displays detailed information on the given command.\n'.format(Prefix) + \
               '**{}rand [x] [y]** - Returns a random number within given range\n'.format(Prefix) + \
               '**{}flip [w]** - Flips a coin with given weight on heads'.format(Prefix)



Message_Help_Help = '**{}help [command]** Displays the help message, which contains a list of all possible commands that I can do.\n'.format(Prefix) + \
                    '\tIf a command is given, displays detailed information about the given command.'
Message_Help_Rand = '**{}rand [x] [y]** Returns a random number between x and y, inclusive.\n'.format(Prefix) + \
                    '\t If no range is given, returns a random number between 1 and 100.\n' + \
                    '\t If only one number is given, will return a number between 1 and that number.'
Message_Help_Flip = '**{}flip [w]** Flips a weighted coin with heads weighted w and tails weighted 1-w.\n'.format(Prefix) + \
                    '\t If no weight is given, the coin will be fair. (w = 0.5)'
