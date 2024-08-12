import pytest
from pydantic import ValidationError

from app.schemas.pagination_query_params.schema import PaginationQueryParams


def test_pagination_query_params_valid():
    # Test with default values
    params = PaginationQueryParams()
    assert params.limit == 10
    assert params.offset == 0

    # Test with custom valid values
    params = PaginationQueryParams(limit=20, offset=5)
    assert params.limit == 20
    assert params.offset == 5


def test_pagination_query_params_invalid_limit():
    # Test with limit of 0 (invalid)
    with pytest.raises(ValidationError) as exc_info:
        PaginationQueryParams(limit=0)
    assert "limit must be greater than 0" in str(exc_info.value)

    # Test with limit of -1 (invalid)
    with pytest.raises(ValidationError) as exc_info:
        PaginationQueryParams(limit=-1)
    assert "limit must be greater than 0" in str(exc_info.value)


def test_pagination_query_params_invalid_offset():
    # Test with offset of -1 (invalid)
    with pytest.raises(ValidationError) as exc_info:
        PaginationQueryParams(offset=-1)
    assert "offset must be greater than or equal to 0" in str(exc_info.value)
