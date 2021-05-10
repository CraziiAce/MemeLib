import pytest
import memelib


def get_meme():
    client = memelib.DankMemeClient()
    return client.meme()


def test_answer():
    assert str(get_meme) is True