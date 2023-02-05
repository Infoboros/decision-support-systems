import pytest

from algorithm.displaced_ideal import DisplacedIdeal
from tests.utils import equal_list


@pytest.fixture
def video_card_alternative():
    return [
        [1000, 4800, 2048, 9940],
        [1000, 4500, 1024, 8400],
        [1050, 5500, 6144, 15629],
        [1020, 5400, 2048, 10799]
    ]


@pytest.fixture
def weights_video_cards():
    return [4, 4, 2, 6]


@pytest.fixture
def controller(video_card_alternative, weights_video_cards):
    return DisplacedIdeal(video_card_alternative, weights_video_cards)


def test_init(video_card_alternative, weights_video_cards):
    controller = DisplacedIdeal(video_card_alternative, weights_video_cards)
    logger = controller.logger

    assert equal_list(logger.get_step(2).data, [0.25, 0.25, 0.125, 0.375])


def test_algorithm(controller, video_card_alternative):
    dmm = controller.get_decision_making_matrix()
    assert equal_list(dmm, video_card_alternative)
    print(controller.logger)