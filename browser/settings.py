from PyQt6.QtWebEngineCore import QWebEngineProfile


def create_private_profile():
    profile = QWebEngineProfile()

    profile.setHttpCacheType(
        QWebEngineProfile.HttpCacheType.MemoryHttpCache
    )

    profile.setPersistentCookiesPolicy(
        QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies
    )

    return profile