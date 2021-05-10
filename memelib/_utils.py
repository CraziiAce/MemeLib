import discord

def _format(data, embed_color):
    embed = discord.Embed(
        title=data["title"],
        url=data["post_url"],
        color=embed_color,
        description=f"{data['author']} | Can't see the image? [Click Here.]({data['img_url']})",
    )
    embed.set_image(url=data["image_url"])
    embed.set_footer(text=f"{data['upvotes']} 👍 | {data['comments']} 💬")
    return embed