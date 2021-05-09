#this is the file for any universal declarations or defines or whatever that will be imported into other files
#just do "from constants import {function_name}" to get iter


#DEFINES BOT COLOR TO BE USED IN EMBEDS
#import into other files for use
bot_color = 0xff0000


#REQUESTED BY FOOTER FOR EMBEDS
def requested_by(ctx, embed):
    author_name = ctx.author.display_name
    embed.set_footer(text = f"Requested by {author_name}")
