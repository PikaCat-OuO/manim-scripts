from pathlib import Path

from manim import logger
from manim_voiceover.helper import prompt_ask_missing_package, remove_bookmarks
from manim_voiceover.services.base import SpeechService
import asyncio

try:
    import edge_tts
except ImportError:
    logger.error("Missing packages. Run `pip install edge-tts` to use EdgeService.")

VOICE = "zh-CN-YunxiaNeural"


async def generate(text, output_file) -> None:
    """Edge TTS Main function"""
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)


class EdgeService(SpeechService):
    """Speech service for Edge TTS.
    Default voice: ``zh-CN-YunxiaNeural``.
    """

    def __init__(
            self, **kwargs
    ):
        self.init_kwargs = kwargs
        prompt_ask_missing_package("TTS", "TTS>=0.13.3")
        SpeechService.__init__(self, **kwargs)

    def generate_from_text(
            self, text: str, cache_dir: str = None, path: str = None, **kwargs
    ) -> dict:
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_text = remove_bookmarks(text)
        input_data = {"input_text": text, "service": "edge"}

        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path

        if not kwargs:
            kwargs = self.init_kwargs

        output_path = str(Path(cache_dir) / audio_path)
        mp3_path = Path(output_path).with_suffix(".mp3")

        # Text to speech to a file
        loop = asyncio.get_event_loop_policy().get_event_loop()
        loop.run_until_complete(generate(input_text, mp3_path))

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
            # "word_boundaries": word_boundaries,
        }

        return json_dict
