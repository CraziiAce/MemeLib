import aiohttp
import random
import requests

from memelib.errors import *
from memelib._utils import _format


class DankMemeClient:
    """The client to get memes from"""

    def __init__(
        self,
        use_reddit_for_memes: bool = True,
        reddit_user_agent: str = "MemeLib",
        return_embed: bool = False,
        embed_color=None,
    ):
        """Initialize a client. The embed color must be on 0xFFFFFF format"""
        self.memes = {"random": "meme()"}
        self.meme_subreddits = ["/dankmemes", "/memes", "/wholesomememes"]
        self.agent = reddit_user_agent
        self.usereddit = use_reddit_for_memes
        self.return_embed = return_embed
        self.embed_color = embed_color

    async def async_meme(self, subreddit=None):
        if self.usereddit and subreddit:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://reddit.com/r/{subreddit}/random.json",
                    headers={"user-agent": self.agent},
                ) as r:
                    res = await r.json()
            if r.status != 200:
                if r.status == 429:
                    raise RateLimitError(
                        "Uh-oh, it looks like you were ratelimited! Try changing your user agent by passing it in the `DankMemeClient` call."
                    )
                    return None
                elif r.status == 404:
                    raise SubredditNotFoundError(
                        "Reddit's API returned a 404 error. Make sure the subreddit that you passed does not include the `r/` in front of it."
                    )
                    return None
                else:
                    raise RedditApiError(
                        f"Reddit's API returned status code {r.status_code}"
                    )
                    return None
            data = {
                "title": res[0]["data"]["children"][0]["data"]["title"],
                "author": f"u/{res[0]['data']['children'][0]['data']['author']}",
                "subreddit": res[0]["data"]["children"][0]["data"][
                    "subreddit_name_prefixed"
                ],
                "upvotes": res[0]["data"]["children"][0]["data"]["ups"],
                "comments": res[0]["data"]["children"][0]["data"]["num_comments"],
                "img_url": res[0]["data"]["children"][0]["data"]["url"],
                "post_url": f"https://reddit.com{res[0]['data']['children'][0]['data']['permalink']}",
            }
            if not self.return_embed:
                return data
            else:
                return _format(data, self.embed_color)
        elif self.usereddit and not subreddit:
            subreddit = random.choice(self.meme_subreddits)
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://reddit.com/r/{subreddit}/random.json",
                    headers={"user-agent": self.agent},
                ) as r:
                    res = await r.json()
                data = {
                    "title": res[0]["data"]["children"][0]["data"]["title"],
                    "author": f"u/{res[0]['data']['children'][0]['data']['author']}",
                    "subreddit": res[0]["data"]["children"][0]["data"][
                        "subreddit_name_prefixed"
                    ],
                    "upvotes": res[0]["data"]["children"][0]["data"]["ups"],
                    "comments": res[0]["data"]["children"][0]["data"]["num_comments"],
                    "img_url": res[0]["data"]["children"][0]["data"]["url"],
                    "post_url": f"https://reddit.com{res[0]['data']['children'][0]['data']['permalink']}",
                }
                if not self.return_embed:
                    return data
                else:
                    return _format(data, self.embed_color)
        elif not self.usereddit:
            return "Still in progress"
            raise SubredditNotFoundError("You didn't specify a subreddit")

    def meme(self, subreddit=None):
        if self.usereddit and subreddit:
            r = requests.get(
                "https://reddit.com/r/{subreddit}/random.json",
                headers={"user-agent": self.agent},
            )
            res = r.json()
            if r.status_code != 200:
                if r.status_code == 429:
                    raise RateLimitError(
                        "Uh-oh, it looks like you were ratelimited! Try changing your user agent by passing it in the `DankMemeClient` call."
                    )
                    return None
                elif r.status == 404:
                    raise SubredditNotFoundError(
                        "Reddit's API returned a 404 error. Make sure the subreddit that you passed does not include the `r/` in front of it."
                    )
                    return None
                else:
                    raise RedditApiError(
                        f"Reddit's API returned status code {r.status_code}"
                    )
                    return None
            data = {
                "title": res[0]["data"]["children"][0]["data"]["title"],
                "author": f"u/{res[0]['data']['children'][0]['data']['author']}",
                "subreddit": res[0]["data"]["children"][0]["data"][
                    "subreddit_name_prefixed"
                ],
                "upvotes": res[0]["data"]["children"][0]["data"]["ups"],
                "comments": res[0]["data"]["children"][0]["data"]["num_comments"],
                "img_url": res[0]["data"]["children"][0]["data"]["url"],
                "post_url": f"https://reddit.com{res[0]['data']['children'][0]['data']['permalink']}",
            }
            if not self.return_embed:
                return data
            else:
                return _format(data, self.embed_color)
        elif self.usereddit and not subreddit:
            subreddit = random.choice(self.meme_subreddits)
            r = requests.get(
                "https://reddit.com/r/{subreddit}/random.json",
                headers={"user-agent": self.agent},
            )
            res = r.json()
            data = {
                "title": res[0]["data"]["children"][0]["data"]["title"],
                "author": f"u/{res[0]['data']['children'][0]['data']['author']}",
                "subreddit": res[0]["data"]["children"][0]["data"][
                    "subreddit_name_prefixed"
                ],
                "upvotes": res[0]["data"]["children"][0]["data"]["ups"],
                "comments": res[0]["data"]["children"][0]["data"]["num_comments"],
                "img_url": res[0]["data"]["children"][0]["data"]["url"],
                "post_url": f"https://reddit.com{res[0]['data']['children'][0]['data']['permalink']}",
            }
            if not self.return_embed:
                return data
            else:
                return _format(data, self.embed_color)
        elif not self.usereddit:
            return "Still in progress"
            raise SubredditNotFoundError("You didn't specify a subreddit")
