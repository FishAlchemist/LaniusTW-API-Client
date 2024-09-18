import httpx
import uuid
import laniustw_model.response
import pydantic
import laniustw_api_client
import typing
import pathlib

model_type = typing.TypeVar("model_type")


class ModelResponse(typing.Generic[model_type]):
    def __init__(self, response: httpx.Response, result_type: model_type) -> None:
        super().__init__()
        self.response: httpx.Response = response
        self.result_type: model_type = result_type

    @property
    def result(self) -> model_type:
        if issubclass(self.result_type, pydantic.BaseModel):
            return self.result_type.model_validate(self.response.json())
        return self.result_type(self.response.text)


@pydantic.validate_call
def health_check(token: str) -> ModelResponse[laniustw_model.response.HealthCheck]:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/health"
    response = httpx.get(url=api_url, params={"token": token})
    return ModelResponse[laniustw_model.response.HealthCheck](
        response=response, result_type=laniustw_model.response.HealthCheck
    )


@pydantic.validate_call
def integrate(
    Images: list[pathlib.Path], speech_file: pathlib.Path, token: str
) -> ModelResponse[str]:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/Integrate"
    files = [("Images", (image.name, image.read_bytes())) for image in Images]
    files.append(("speech_file", (speech_file.name, speech_file.read_bytes())))
    params = {"token": token}
    response = httpx.get(
        url=api_url, params=params, timeout=httpx.Timeout(20.0, read=None)
    )
    return ModelResponse[str](response=response, result_type=str)


@pydantic.validate_call
def chat_RAG(
    question: str, identifier: uuid.UUID | None, token: str
) -> ModelResponse[laniustw_model.response.ChatResponse[uuid.UUID]]:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/chat/RAG"
    params = {"question": question, "identifier": identifier, "token": token}
    response = httpx.get(
        url=api_url, params=params, timeout=httpx.Timeout(10.0, read=None)
    )
    return ModelResponse[laniustw_model.response.ChatResponse[uuid.UUID]](
        response=response, result_type=laniustw_model.response.ChatResponse[uuid.UUID]
    )


@pydantic.validate_call
def chat_Experience(
    question: str, identifier: uuid.UUID | None, token: str
) -> ModelResponse[laniustw_model.response.ChatResponse[uuid.UUID]]:
    api_url = f"{laniustw_api_client.PROJECT_API_URL}/api/chat/Experience"
    params = {"question": question, "identifier": identifier, "token": token}
    response = httpx.get(
        url=api_url, params=params, timeout=httpx.Timeout(10.0, read=None)
    )
    return ModelResponse[laniustw_model.response.ChatResponse[uuid.UUID]](
        response=response, result_type=laniustw_model.response.ChatResponse[uuid.UUID]
    )
