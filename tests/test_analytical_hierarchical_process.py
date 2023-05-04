import pytest

from algorithm.analytical_hierarchical_process import AnalyticalHierarchicalProcessor
from algorithm.matrix import Matrix


@pytest.fixture()
def hierarchia():
    return [
        {
            'nodes': ['1', '2'],
            'matrs': [
                [
                    [1, 1, 1. / 3., 1. / 5.],
                    [1, 1, 1. / 3., 1. / 5.],
                    [3, 3, 1, 1],
                    [5, 5, 1, 1],
                ],
                [
                    [1, 1. / 2., 1. / 2., 5.],
                    [2, 1, 1. / 2., 5.],
                    [2, 1. / 2., 1, 3],
                    [1. / 5., 1. / 5., 1. / 3., 1],
                ]
            ]
        },
        {
            'nodes': ['3', '4', '5', '6'],
            'matrs': [
                [
                    [1, 2, 1. / 2., 2],
                    [1. / 2., 1, 1. / 3., 1. / 2.],
                    [2, 3, 1, 2],
                    [1. / 2., 2, 1. / 2., 1],
                ],
                [
                    [1, 1. / 2., 1. / 2., 1. / 3.],
                    [2, 1, 1, 1. / 2.],
                    [2, 1, 1, 1. / 2.],
                    [3, 2, 2, 1],
                ],

                [
                    [1, 2, 1. / 2., 1. / 3.],
                    [1. / 2., 1, 1. / 2., 1. / 3.],
                    [2, 2, 1, 1. / 2.],
                    [3, 3, 2, 1],
                ],
                [
                    [1, 1. / 2., 1. / 3., 1. / 2.],
                    [2, 1, 1. / 2., 1],
                    [3, 2, 1, 1. / 2.],
                    [2, 1, 2, 1],
                ],
            ]
        },
    ]


@pytest.fixture
def matr():
    # return [
    #     [1, 1, 1],
    #     [1, 1, 1],
    #     [1, 1, 1],
    # ]
    return [
        [1, 1. / 3., 1. / 2.],
        [3, 1, 3],
        [2, 1. / 3., 1]
    ]


def test_matrix(matr):
    processor = Matrix(matr)
    eigenvalues, lmax = processor.get_eigenvalues_and_lmax()
    IS = processor.get_is(lmax)
    OS = processor.get_os(IS)

    print()
    print(eigenvalues)
    print(IS)
    print(OS)


def test_hierarchical_processor(hierarchia):
    AnalyticalHierarchicalProcessor(hierarchia).calculate()
