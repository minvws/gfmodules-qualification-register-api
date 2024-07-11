from typing import Any


def api_version_header() -> dict[str, dict[str, Any]]:
    return {
        "API-Version": {
            "description": "API version in SemVer format",
            "schema": {
                "type": "string"
            }
        }
    }


def api_version_header_responses(response_codes: list[int]) -> dict[int | str, dict[str, Any]]:
    responses: dict[int | str, dict[str, Any]] = {}

    for code in response_codes:
        responses[code] = {
            "headers": {
                **api_version_header()
            }
        }

    return responses

