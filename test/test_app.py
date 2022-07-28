import pytest
import sys
import io
sys.path.insert(0, "src")

from app import app

# module to use app for testing
@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()
    yield testing_client


def test_indexpage(test_client):
    # test case if no files are uploaded
    response = test_client.get('/')
    # status code
    assert response.status_code == 200
    assert b'<h1>Upload fundus photography images </h1>' in response.data

def test_upload_nofiles(test_client):
    # test case if no files are uploaded
    response = test_client.post('/', content_type='multipart/form-data')
    # status code
    assert response.status_code == 201
    assert b'<h1>Upload fundus photography images </h1>' in response.data


def test_upload_1files(test_client):
    # test case if 1 file is uploaded
    #'test.jpg'
    image = "fakeimage1.png"
    data={}
    data['images'] = (open(image, 'rb'), image)

    rv = test_client.post('/', data=data, follow_redirects=True, content_type='multipart/form-data')
    assert rv.status_code == 201
    assert b'<h1> fundus photography images result </h1>' in rv.data


