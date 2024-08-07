import httpx
import uuid
from pydantic import validate_call
import laniustw_api_client
import pathlib


@validate_call
def health_check(token: str) -> httpx.Response:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/health"
    return httpx.get(url=api_url, params={"token": token})


@validate_call
def speech_recogn(speech_file: pathlib.Path | str, token: str) -> httpx.Response:
    if isinstance(speech_file, str):
        speech_file = pathlib.Path(speech_file)
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/speech_recognition"
    files = {"speech_file": (speech_file.name, speech_file.read_bytes())}
    return httpx.post(
        url=api_url,
        files=files,
        timeout=httpx.Timeout(10.0, read=None),
        params={"token": token},
    )


@validate_call
def image_recognition(file: pathlib.Path | str, token: str) -> httpx.Response:
    if isinstance(file, str):
        file = pathlib.Path(file)
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/Image_recognition"
    files = {"file": (file.name, file.read_bytes())}
    return httpx.post(
        url=api_url,
        files=files,
        timeout=httpx.Timeout(10.0, read=None),
        params={"token": token},
    )


@validate_call
def chat_RAG(question: str, identifier: uuid.UUID | None, token: str) -> httpx.Response:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/chat/RAG"
    params = {"question": question, "identifier": identifier, "token": token}
    return httpx.get(url=api_url, params=params, timeout=httpx.Timeout(10.0, read=None))


@validate_call
def chat_Recommendation(
    question: str, Recommended_num: int | None, token: str
) -> httpx.Response:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/chat/Recommendation"
    params = {
        "question": question,
        "Recommended_num": Recommended_num,
        "token": token,
    }
    return httpx.get(url=api_url, params=params, timeout=httpx.Timeout(10.0, read=None))


@validate_call
def chat_Experience(question: str, identifier: uuid.UUID | None, token: str):
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/chat/Experience"
    params = {"question": question, "identifier": identifier, "token": token}
    return httpx.get(url=api_url, params=params, timeout=httpx.Timeout(10.0, read=None))
