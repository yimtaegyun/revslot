import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"backend"))
import revslot.app as module
from revslot.storage import Store


@pytest.fixture
def client(tmp_path,monkeypatch):
    monkeypatch.delenv("NEBIUS_API_KEY",raising=False)
    monkeypatch.delenv("TAVILY_API_KEY",raising=False)
    monkeypatch.delenv("DATABASE_URL",raising=False)
    monkeypatch.setattr(module,"store",Store(str(tmp_path/"test.sqlite")))
    with TestClient(module.app) as c:
        assert c.post("/api/session").status_code==200
        yield c
