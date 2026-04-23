from pydantic import BaseModel
from typing import Any

from ..utils import create_ui_path, BASE_URL

class IconAsset(BaseModel):
    filename: str = ""
    url: str = ""

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        if data.get("use_enka"):
            self.url = BASE_URL.format(PATH=f"ui/{self.filename}.png")
        else:
            self.url = create_ui_path(self.filename)
