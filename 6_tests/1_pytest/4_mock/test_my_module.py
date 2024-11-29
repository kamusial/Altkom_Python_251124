import pytest
from unittest.mock import patch
from my_module import get_user_data

# przygotowanie fałszywej odpowiedzi
def test_get_user_data_success():
    mock_response = {
        'id': 1,
        'name': 'Kamil Musial',
        'email': 'kamil@altkom.pl'
    }
# mockowanie metody request.get
    with patch('my_module.requests.get') as mock_get:
        # konfiguracja mocka
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # wywołanie funkcji do przetestowania
        result = get_user_data(1)

        # Asercja
        assert result == mock_response
        mock_get.assert_called_once_with('http://example/users/1')

def test_get_user_data_not_found():
    with patch('my_module.requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        with pytest.raises(ValueError):
            get_user_data(2)

        mock_get.assert_called_once_with('http://example/users/2')

