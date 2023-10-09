from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from pytube import YouTube
import argparse
from aiogram.types.input_file import FSInputFile, URLInputFile

router = Router()

    
@router.message()
async def downloader_handler(message: Message):
    await message.answer("Загрузка...")
    
    video = YouTube(message.text)
    audio = video.streams.filter(only_audio=True).first()
    try:
        audio.download("audio", "audio.mp3")
    except:
        await message.answer("Произошла ошибки при загрузке аудио, попробуйще еще раз"); return
    thumbnail = URLInputFile(video.embed_url)
    file = FSInputFile("./audio/audio.mp3")
    await message.answer_audio(file, title=video.title, thumbnail=thumbnail, performer=video.author,
                               duration=video.length)
    
    