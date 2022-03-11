# -*- coding: utf-8 -*-

from src.core.config import Config


ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
    + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
)

proxies = {
    "http": "",
    "https": "",
}

proxiesURI = "http://127.0.0.1:8889"


def test_get_ua():
    config = Config()
    assert config.get_headers()["User-Agent"] == ua


def test_set_cookie_into_headers():
    config = Config()
    config.set_headers("cookie", "12345678")
    assert config.get_headers()["cookie"] == "12345678"


def test_del_cookie():
    config = Config()
    config.del_headers("cookie")
    assert "cookie" not in config.get_headers()


def test_get_proxies():
    config = Config()
    assert config.get_proxies() == proxies


def test_set_proxies():
    config = Config()
    config.set_proxies("http", proxiesURI)
    assert config.get_proxies()["http"] == proxiesURI
    config.set_proxies("http", "")


def test_do_get():
    config = Config()
    res = config.do_get(
        "https://www.google.com",
        proxies={
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        },
    )
    assert res.status_code == 200


def test_do_post():
    config = Config()
    res = config.do_post(
        "https://reqbin.com/sample/post/json",
        headers={
            "User-Agent": ua,
        },
        proxies={
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        },
    )
    assert res.status_code == 200
