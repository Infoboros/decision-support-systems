import pytest
from algorithm.analytical_network_process import AnalyticalNetworkProcessor


@pytest.fixture
def macro_clusters():
    return [
        {
            "matr": [
                [1.0, 3.0, 1./3.0],
                [1./3., 1.0, 1. / 3.],
                [3, 3., 1.0],
            ],
            "cluster": 0,
            "directs": [1, 2, 3]
        },
        {
            "matr": [
                [1.0, 1./3.0],
                [3, 1.0],
            ],
            "cluster": 1,
            "directs": [2, 3]
        },
        {
            "matr": [
                [1.0],
            ],
            "cluster": 2,
            "directs": [3]
        },
        {
            "matr": [
                [1.0],
            ],
            "cluster": 3,
            "directs": [0]
        }
    ]


@pytest.fixture
def micro_clusters():
    return [
        {
            "cluster": 0,
            "elements": [
                {
                    "element": 0,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 1/4.0, 6.0],
                            [4, 1.0, 5.0],
                            [1./6., 1./5, 1.0],
                        ],
                        [
                            [1.0, 2.0, 4.0],
                            [2., 1.0, 1./2.0],
                            [0.25, 2.0, 1.0],
                        ],
                        [
                            [1.0, 3.0, 3],
                            [1./3., 1.0, 3.0],
                            [1./3., 1./3., 1.0],
                        ],
                    ]
                },
                {
                    "element": 1,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 1./2.0, 4.],
                            [2., 1.0, 4.],
                            [1./4.0, 1./4.0, 1.0],
                        ],
                        [
                            [1.0, 3., 3.],
                            [1/3.0, 1.0, 1./3.0],
                            [1./3.0, 3., 1.0],
                        ],
                        [
                            [1.0, 3.0, 3.0],
                            [1.0 / 3.0, 1.0, 4.0],
                            [1.0 / 3.0, 1.0 / 4.0, 1.0],
                        ],
                    ]
                },
                {
                    "element": 2,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 1./2., 5.0],
                            [2.0, 1.0, 6.0],
                            [1./5, 1./6., 1.0],
                        ],
                        [
                            [1.0, 1./4.0, 1./6.],
                            [4., 1.0, 4.],
                            [6.0, 1/4., 1.0],
                        ],
                        [
                            [1.0, 3., 3.],
                            [1./3., 1.0, 3.0],
                            [1./3., 1./3., 1.0],
                        ],
                    ]
                },
            ]
        },
        {
            "cluster": 1,
            "elements": [
                {
                    "element": 0,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 2., 1./2.],
                            [1./2., 1.0, 2.0],
                            [2., 1./2., 1.0],
                        ],
                        [
                            [1.0, 3.0, 3.0],
                            [1./3., 1.0, 1./2.],
                            [1./3., 2.0, 1.0],
                        ],
                    ]
                },
                {
                    "element": 1,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 3., 3.],
                            [1./3., 1.0, 2.0],
                            [1./3., 1./2.0, 1.0],
                        ],
                        [
                            [1.0, 3.0, 3.0],
                            [1./3., 1.0, 1./3.],
                            [1./3., 3., 1.0],
                        ],
                    ]
                },
                {
                    "element": 2,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 1./5., 1./6.],
                            [5., 1.0, 3.],
                            [6., 1./3., 1.0],
                        ],
                        [
                            [1.0, 3.0, 3.0],
                            [1./3., 1.0, 2.0],
                            [1./3., 1./2., 1.0],
                        ],
                    ]
                },
            ]
        },
        {
            "cluster": 2,
            "elements": [
                {
                    "element": 0,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 3.0, 3.],
                            [1./3., 1.0, 1./3.],
                            [1./3., 3.0, 1.0],
                        ],
                    ]
                },
                {
                    "element": 1,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 1./4., 3.0],
                            [4., 1.0, 3.0],
                            [1./3., 1./3., 1.0],
                        ],
                    ]
                },
                {
                    "element": 2,
                    "directs": [
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [1.0, 2.0, 1./3.],
                            [1./2., 1.0, 1./3.],
                            [3., 3., 1.0],
                        ],
                    ]
                },
            ]
        },
        {
            "cluster": 3,
            "elements": [
                {
                    "element": 0,
                    "directs": [
                        [
                            [1.0, 2.0, 2.],
                            [1./2., 1.0, 2.],
                            [1./2.0, 1./2., 1.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                    ]
                },
                {
                    "element": 1,
                    "directs": [
                        [
                            [1.0, 3., 3.],
                            [1./3., 1.0, 3.],
                            [1./3., 1./3., 1.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                    ]
                },
                {
                    "element": 2,
                    "directs": [
                        [
                            [1.0, 1./2., 2.],
                            [2., 1.0, 1.0],
                            [1./2., 1., 1.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                        [
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0],
                        ],
                    ]
                },
            ]
        }
    ]


@pytest.fixture
def elements():
    return {
        "names": [
            "1.1 Word2Vec",
            "1.2 GloVe",
            "1.3 fastText",
            "2.1 Интерпретируемость",
            "2.2 Качество",
            "2.3 Скорость работы",
            "3.1 Количество параметров",
            "3.2 Сложность устройства",
            "3.3 Объем занимаемой памяти",
            "4.1 Качество стихотворного текста",
            "4.2 Количество предлагаемых вариантов",
            "4.3 Подготовка корпуса данных",
        ],
        "counts": [3, 3, 3, 3]
    }

def test_calculate(macro_clusters, micro_clusters, elements):
    processor = AnalyticalNetworkProcessor(macro_clusters, micro_clusters)
    processor.calculate(elements)
