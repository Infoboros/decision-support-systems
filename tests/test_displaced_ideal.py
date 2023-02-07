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
def criteria_sign():
    return [1, 1, 1, -1]


@pytest.fixture
def controller(video_card_alternative, weights_video_cards, criteria_sign):
    return DisplacedIdeal(video_card_alternative, weights_video_cards, criteria_sign)


def test_init(video_card_alternative, weights_video_cards, criteria_sign):
    controller = DisplacedIdeal(video_card_alternative, weights_video_cards, criteria_sign)
    logger = controller.logger

    assert equal_list(logger.get_step(2).data, [0.25, 0.25, 0.125, 0.375])


def test_dmm(controller, video_card_alternative):
    dmm = controller.get_decision_making_matrix()
    assert equal_list(dmm, video_card_alternative)


def test_major(controller):
    major = controller.get_major()
    assert equal_list(major, [1050, 5500, 6144, 8400])


def test_minor(controller):
    minor = controller.get_minor()
    assert equal_list(minor, [1000, 4500, 1024, 15629])


def test_get_relative_alternatives(controller):
    relative = controller.get_relative_alternatives(
        controller.get_minor(),
        controller.get_major()
    )
    assert equal_list(
        relative,
        [
            [1, 0.7, 0.8, 0.018007663],
            [1, 1, 1, 0.0076756066],
            [0, 0, 0, 1],
            [0.6, 0.1, 0.8, 0]
        ]
    )


def test_algorithm(controller):
    while len(controller.alternatives) > 1:
        new_iteration = controller.execute()
        print(controller.logger)
        controller = new_iteration

    print('Решение')
    print(controller.alternatives)

