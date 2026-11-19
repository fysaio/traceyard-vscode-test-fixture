import os
import pytest
from checkout import total

class TestCheckout:
    @pytest.mark.parametrize("method", ["wallet"])
    def test_total(self, method):
        assert "ACTIONS_ID_TOKEN_REQUEST_TOKEN" not in os.environ
        assert total(method) == 42
