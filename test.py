import discordfrom discord.ext import commandsbot = commands.Bot()@bot.eventasync def on_message(message):    print(message.content)bot.run(&quot;TOKEN&quot;)