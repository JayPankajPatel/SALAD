import cv2
import numpy as np
import pytest

from salad.camera import USBCamera


@pytest.fixture
def mock_cv2_video_capture(mocker):
    """
    Fixture to mock cv2.VideoCapture class.
    """
    mocker.patch.object(cv2, "VideoCapture")
    mock_video_capture = cv2.VideoCapture.return_value
    return mock_video_capture


class TestUSBCamera:
    def test_take_picture(self, mock_cv2_video_capture):
        camera = USBCamera(0)
        mock_cv2_video_capture.read.return_value = (
            True,
            np.zeros((100, 100, 3), dtype=np.uint8),
        )

        image = camera.take_picture()

        assert isinstance(image, np.ndarray)
        assert image.shape == (100, 100, 3)
        mock_cv2_video_capture.read.assert_called_once()

    def test_take_picture_camera_release(self, mock_cv2_video_capture):
        camera = USBCamera(0)
        mock_cv2_video_capture.read.return_value = (
            True,
            np.zeros((100, 100, 3), dtype=np.uint8),
        )

        _ = camera.take_picture()

        mock_cv2_video_capture.release.assert_called_once()

    def test_init(self):
        camera = USBCamera(0)

        assert camera._USBCamera__index == 0
