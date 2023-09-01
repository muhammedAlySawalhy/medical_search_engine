
from pydantic import BaseModel
from fastapi import APIRouter
from utils import extract_data_from_html
from utils import fetch_html_content
from utils import save_data_to_json


router = APIRouter()


class RequestUrls(BaseModel):
    urls: list[str]


@router.post("/api/v1/request_urls")
def fetchData(Urls: RequestUrls):
    for url in Urls.urls:
        try:
            html_content = extract_data_from_html(url)
            paragraphs, anchors = extract_data_from_html(html_content)
            save_data_to_json(url, paragraphs, anchors)
        except:
            print("Error in fetching data")
    return {"message": "Data fetched successfully"}
