# assignBot
Proof of concept. Role assignment concept bot made for Invictus Intergalactic Federation aka INVFED.

Step-by-Step to start the bot on a new server:
1. verify .env contains the correct keys
2. verify that role names are correct for the server that you are now in
3. create the embed message with !embed in the text channel of your choice
4. get the message id of that new embed and copy/paste it into the code on line 77 (if message_id == <your message id>)
5. restart the bot to save the changes made
6. test bot by selecting the reactions and seeing if role is assigned

Proper .env format:
DISCORD_TOKEN = <bot token here>
DISCORD_GUILD = Turtle-12 Bot Test Server 
CHOICE_1 = Starfighter Corps 
CHOICE_2 = Armored Corps 
CHOICE_3 = Operations Corps 
CHECKER_ROLE = Enlisted
