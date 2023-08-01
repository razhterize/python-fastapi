import fastapi

class API():
    def __init__(self, name: str) -> None:
        self.name = name
        self.router = fastapi.APIRouter()
        self.router.add_api_route("/hello", self.hello, methods=['GET'])

    def hello(self):
        return {"content": self.name}

app = fastapi.FastAPI()
hello = API("hello")
app.include_router(hello.router)