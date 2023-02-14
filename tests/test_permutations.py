import pytest
from algorithm.permutations import Permutations


@pytest.fixture
def video_card_alternative():
    return [
        [10, 3, 7, 3],
        [12, 2.5, 6, 4],
        [9, 2.5, 8, 5],
        [11, 2, 9, 4]
    ]


@pytest.fixture
def weights_video_cards():
    return [3, 1, 3, 4]


@pytest.fixture
def criteria_sign():
    return [-1, -1, 1, 1]


@pytest.fixture
def controller(video_card_alternative, weights_video_cards, criteria_sign):
    return Permutations(video_card_alternative, weights_video_cards, criteria_sign)


def test_permutations(controller):
    controller.execute()

    print(controller.logger)
