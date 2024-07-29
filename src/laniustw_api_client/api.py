import httpx
import uuid
from pydantic import validate_call
from laniustw_api_client import PROJECT_API_URL
import pathlib


@validate_call
def test(identifier: uuid.UUID | None) -> httpx.Response:
    api_url = f"{PROJECT_API_URL}/api/test"
    print(api_url)
    params = {"identifier": identifier}
    return httpx.get(url=api_url, params=params)


@validate_call
def speech_recogn(speech_file: pathlib.Path) -> httpx.Response:
    api_url = f"{PROJECT_API_URL}/api/speech_recognition"
    files = {"file": (speech_file.name, speech_file.open(mode="rb"))}
    return httpx.post(url=api_url, files=files)


@validate_call
def image_recognition(file: pathlib.Path) -> httpx.Response:
    api_url = f"{PROJECT_API_URL}/api/Image_recognition"
    files = {"file": (file.name, file.open("rb"))}
    return httpx.post(url=api_url, files=files)


@validate_call
def chat_RAG(question: str, identifier: uuid.UUID | None) -> httpx.Response:
    api_url = f"{PROJECT_API_URL}/api/chat/RAG"
    params = {
        "question": question,
        "identifier": identifier,
    }
    return httpx.get(url=api_url, params=params)


@validate_call
def chat_Recommendation(
    question: str, identifier: uuid.UUID | None, Recommended_num: int | None
) -> httpx.Response:
    api_url = f"{PROJECT_API_URL}/api/chat/Recommendation"
    params = {
        "question": question,
        "identifier": identifier,
        "Recommended_num": Recommended_num,
    }
    return httpx.get(url=api_url, params=params)


@validate_call
def chat_Experience(question: str, identifier: uuid.UUID | None):
    api_url = f"{PROJECT_API_URL}/api/chat/Experience"
    params = {
        "question": question,
        "identifier": identifier,
    }
    return httpx.get(url=api_url, params=params)
