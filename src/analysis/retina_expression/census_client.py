"""Proxy-aware CZ CELLxGENE Census connection.

The sandboxed environment routes all egress through an HTTP proxy advertised as
``localhost:<port>``.  ``localhost`` does not resolve inside the sandbox, so both
``requests`` (used by cellxgene_census for the release directory) and TileDB's S3
VFS (used for the actual SOMA reads) have to be pointed at ``127.0.0.1`` instead.
TileDB does not read ``HTTPS_PROXY``; it needs explicit ``vfs.s3.proxy_*`` config.
"""

import os
import urllib.parse as _up

CENSUS_VERSION = "2025-11-08"  # pinned: "stable" as of 2026-11-02


def _proxy_url() -> str | None:
    raw = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not raw:
        return None
    return raw.replace("@localhost:", "@127.0.0.1:").replace(
        "//localhost:", "//127.0.0.1:"
    )


def fix_proxy_env() -> None:
    """Point every proxy variable at 127.0.0.1.

    The sandbox advertises its egress proxy as ``localhost:<port>``, which does
    not resolve inside the sandbox.  curl survives this; ``urllib`` and
    ``requests`` do not.  Call this before any stdlib HTTP request.
    """
    url = _proxy_url()
    if not url:
        return
    for k in (
        "HTTPS_PROXY",
        "https_proxy",
        "HTTP_PROXY",
        "http_proxy",
        "ALL_PROXY",
        "all_proxy",
    ):
        if os.environ.get(k):
            os.environ[k] = url


def tiledb_config() -> dict:
    cfg = {"vfs.s3.no_sign_request": "true", "vfs.s3.region": "us-west-2"}
    url = _proxy_url()
    if url:
        u = _up.urlparse(url)
        cfg.update(
            {
                "vfs.s3.proxy_scheme": "http",
                "vfs.s3.proxy_host": u.hostname,
                "vfs.s3.proxy_port": str(u.port),
                "vfs.s3.proxy_username": _up.unquote(u.username or ""),
                "vfs.s3.proxy_password": _up.unquote(u.password or ""),
            }
        )
    return cfg


def open_census(version: str = CENSUS_VERSION):
    import cellxgene_census

    fix_proxy_env()
    # An AWS profile in the environment can override anonymous access to the
    # public census bucket.
    os.environ.pop("AWS_PROFILE", None)
    return cellxgene_census.open_soma(
        census_version=version, tiledb_config=tiledb_config()
    )
