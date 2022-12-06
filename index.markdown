---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Guide
---
# Before You Start
This quickstart guide assumes the following:
1. You use and understand Discord.
2. You own your own Discord server or hold administrator privledges for a Discord server.
3. You understand the basics of Python or a similar programming language.
4. You have the latest version of Python installed on your computer.

For guidance with the above, respectively refer to the following resources:
1. [Beginner's Guide to Discord](https://support.discord.com/hc/en-us/articles/360045138571-Beginner-s-Guide-to-Discord)
2. [Discord Support: How do I create a server?](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)
3. [W3 Schools Python Tutorial](https://www.w3schools.com/python/)
4. [Python Download](https://www.python.org/downloads/)

# Set Up Your Discord Developer Portal
Navigate to the [Discord Developer Portal](https://discord.com/developers/) and log in with your Discord account. You may need to confirm your email address when you first connect your account to the Developer Portal. When you've successfully linked your account, you'll see the main Developer Portal page:

![Discord Developer Portal page](/images/dev-portal-home.png)
## Create a Bot Application
Click the **New Application** button on the top-right of the page.

![Creating and naming a Discord App](/images/create-app.png){: width="50%"}

Give your bot application a name, and review and agree to the Discord Developer Terms of Service and Developer Policy. Click **Create** on the bottom-right of the window. You should see the following page:

![Discord App General Information Page](/images/gen-info.png)

Optionally, add additional information about your bot in the description and add tags to describe the content and functionality. You may also complete this later.

![Creating a Bot from Discord application settings](/images/bot-settings.png)

Select **Bot** from the **Settings** menu on the left side of the page, then **Add Bot**. When prompted to add a bot to this app, select **Yes, do it!!** After creation, you'll see your bot's settings:

![Build-A-Bot settings page](/images/build-a-bot.png)

You may optionally add an icon for your bot or change its username.

## Link Your Bot to Your Server
You'll need your bot's unique API token to connect it with your server and perform fun commands.

><sup>Note: Keep your API token private (otherwise other people can control your bot) and save it to a secure location. Keep this in mind if you plan to host your code publicly, such as on GitHub. [Black Tech Divas offers a tutorial](https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c) on this. You can reset your token at anytime if it is accidentally shared, but you'll need to update it in your code.</sup>

Click **Reset Token**, then **Yes, do it!** A long string of text, your API token, will appear:

![Copy API token](/images/copy-token.png){: width="75%"}

(I have reset my API token since creating this guide. Your API token will be different!)
Click **Copy**. Open a text editor, paste the token, and save this text to a secure location. We'll use it soon.

Next you'll need to set the permissions, what your bot is able to do, and scope, where your bot can access information. We'll first set the scope.

Under **Settings** on the left-side of the page, select **OAuth2**.

><sup>Note:OAuth2 is a common tool that allows an application or website to access information from another host. In our case, it will allow our bot to access resources from Discord.</sup>

Under **Scopes**, select **bot**.

![Setting the scope of the Discord Bot](/images/bot-scope.png)

You'll now see various **Permissions** appear. For now, select **Send Messages** only.

![Setting the permissions of the Discord Bot](/images/bot-perms.png)

Locate the **Generate URL** section at the bottom of the page. Select **Copy**, and paste this URL into a new tab in your web browser.

![Linking your bot to a server](/images/add-to-server.png){: width="50%"}

Select the server you'd like to host your bot under the **Add-to-Server** drop-down, then click **Continue**. Finally, select **Authorize** to confirm. You may need to complete a CAPTCHA.

You should see a message in your server's main text channel confirming that your bot joined your server. It will also be listed in the server members on the right.

![Success! The bot has joined your server.](/images/joined-server.png)

><sup>Note: If you want to enable more functions in your bot, you'll need to come back to the Permissions section in the Developer Portal and select the relevant permissions. You will also need to copy the new URL and repeat the above steps to connect and authorize your bot to perform certain actions in your server. It is best practice to only select the permissions you actually use. Refer to the [Discord Documentation](https://discord.com/developers/docs/topics/permissions) to learn more about what each permission does.</sup>

# Set Up Python
## Access Command Line
Computer operating systems allow command line access in different ways. Follow the instructions for your operating system below.  

<details>
<summary>Mac</summary>
On your keyboard, press <b>Command</b> and the <b>space bar</b> to open <b>Spotlight</b> search. Type <i>terminal</i> and press the <b>enter</b> key on your keyboard. This will open a new Terminal window which acts as a way to access the command line on a Mac.
</details>

<details>
<summary>Windows</summary>
In your Windows search bar, search for <b>command prompt</b>. Click on the application icon to open it.
</details>

## Install discord.py Library
We will use <i>pip</i>, the preferred installer program for Python, to download the discord.py Python library. This is required to write Python code that allows us to interact with Discord.

In your command line window, type the following command and press the **enter** key:

{% include codeHeader.html %}
```pip install -U discord.py```

## Install dotenv library
While this step is optional, it is best practice to install this Library to help us keep our private API token separate from our Python code.

In your command line window, type the following command and press the **enter** key:

{% include codeHeader.html %}
```pip install -U python-dotenv```

# Write Code!
We finally get to code!

## Edit Initial Templates
We'll create two files: an .env file that will store our API token, and a .py file into which we'll write our Python code. You could store your API token directly in the .py file, but separating it into a different file enables you to share your Python code without sharing your private API token. Create one folder that will hold both of these files.

### Create .env file
Create a text file named __.env__ in the folder of your choice. Add the following two lines to this file:

{% include codeHeader.html %}
```
# Private API token generated from Discord Developer Portal:
DISCORD_TOKEN=<paste-your-token-here>
```
Replace `<paste-your-token-here>` with your unique API token string that you copied and saved in a secure location earlier.

### Create .py file

Next, create a Python file named hello_world.py in the same folder. Add the following code to this file:

{% include codeHeader.html %}
```
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("The bot has logged in!") # outputs to local command line
    server = client.guilds[0] # gets your server
    first_channel = server.text_channels[0] # gets first text channel
    await first_channel.send("Hello, World!") # outputs to Discord

client.run(TOKEN)
```

><sup>Note: The code requires the first three import lines. The next two lines support in hiding your personal token from this file by pulling it from the env file created earlier. The next three lines link to the Discord client with specific permissions. @client.event is a decorator function, meaning it takes other functions, like on_ready, as arguments. This is how Discord handles events. Finally, the client runs with your token.</sup>

Run your code by typing the following into your command line and pressing the **enter** key:

<details markdown="1">
<summary>Mac</summary>
{% include codeHeader.html %}
```python3 hello_world.py```
</details>
<details markdown="1">
<summary>Windows</summary>
{% include codeHeader.html %}
```py -3 hello_world.py```
</details>


Successful code will display the message "The bot has logged in!" on your command line, and your bot will post a message in your Discord server:

![The Discord Bot successfully posts "Hello, World!" in the server.](/images/success.png)

# Bot Suggestions
Looking for more ideas for your bot? More basic examples are below. Note that you will need to update your bot permissions in the Discord Developer Portal for some.

## Respond to Message
To have your bot respond to messages, ensure both <b>send messages</b> and <b>read message history</b> permissions are allowed. Then, add the following code to your Python file:

{% include codeHeader.html %}
```
@client.event
async def on_message(message):
    if message.content == "Hello":
        await message.channel.send("Hi there!")
```
If a user sends the message <i>Hello</i> in the server, the bot will reply with <i>Hi there!</i>. You can add to this code so your bot responds to multiple messages with distinct responses.

## Use @everyone Tag
You can code your bot to send a message that tags @everyone on the server, which can be useful for annoucements. This requires enabling an additional permission, <b>mention_everyone</b>, but otherwise works similarly to sending a normal message. The following example shows this tag added to our original message:

{% include codeHeader.html %}
```
@client.event
async def on_ready():
    server = client.guilds[0] # gets your server
    first_channel = server.text_channels[0] # gets first text channel
    await first_channel.send("Hello, @everyone!") # tags everyone
```

## Another example
details

For more examples, refer to the [discord.py documenation](https://discordpy.readthedocs.io/en/latest/faq.html#general).

{% include post.html %}
