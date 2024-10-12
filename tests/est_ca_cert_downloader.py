import os
import pytest
from unittest.mock import patch, mock_open
from modules.ca_cert_downloader import download_ca_cert

@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open)
@patch('requests.get')
def test_download_ca_cert_exists(mock_get, mock_open, mock_exists):
    # Simulate certificate already exists
    mock_exists.return_value = True
    download_ca_cert()
    mock_get.assert_not_called()

@patch('os.path.exists')
@patch('builtins.open', new_callable=mock_open)
@patch('requests.get')
def test_download_ca_cert_not_exists(mock_get, mock_open, mock_exists):
    # Simulate certificate does not exist, then download
    mock_exists.return_value = False
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'Test Cert Content'
    
    download_ca_cert()

    mock_get.assert_called_once()
    mock_open.assert_called_once_with('ca-stage.crt', 'wb')
    mock_open().write.assert_called_once_with(b'Test Cert Content')

@patch('os.path.exists')
@patch('requests.get')
def test_download_ca_cert_failure(mock_get, mock_exists):
    # Simulate download failure
    mock_exists.return_value = False
    mock_get.side_effect = Exception("Download failed")
    
    with pytest.raises(Exception):
        download_ca_cert()
    mock_get.assert_called_once()