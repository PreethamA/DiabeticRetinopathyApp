import pytest
import sys

sys.path.insert(0, "src")

from app import app

# module to use app for testing
@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

def test_upload_nofiles(test_client):
    # test case if no files are uploaded
    response = test_client.get('/')
    # status code
    assert response.status_code == 200
    assert b'<h1>Upload fundus photography images </h1>' in response.data



def test_upload_1files(test_client):
    # test case if 1 file is uploaded
    image = "fakeimage1.png"
    data = {
        'image': (open(image, 'rb'), image),
        'filename': image
    }
    rv = test_client.post('/', data=data, content_type='multipart/form-data')
    assert rv.status_code == 201



