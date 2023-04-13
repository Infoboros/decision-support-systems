import pytest

from algorithm.revers_hierarchical_process import ReversHierarchicalProcessor
from algorithm.utility_analysis import UtilityAnalysis
from algorithm.utils import print_matrix


@pytest.fixture()
def alternatives():
    return [
        {
            'name': 'Honda Civic',
            'cost': 600
        },
        {
            'name': 'Toyota Celica',
            'cost': 500
        },
        {
            'name': 'Toyota Supra',
            'cost': 5000
        },
        {
            'name': 'Nissan Skyline',
            'cost': 800
        },
        {
            'name': 'Subaru Impreza',
            'cost': 600
        },
        {
            'name': 'Toyota Camry',
            'cost': 1600
        },
        {
            'name': 'Mazda RX-7',
            'cost': 2000
        },
    ]


@pytest.fixture()
def hierarchia():
    return [
        [
            [0.13,    0.13,    0.26,    0.13,    0.13,    0.9],
            [0.26,    0.26,    0.51,    0.26,    0.26,    0.9],
            [0.51,    0.26,    0.51,    0.51,    0.51,    0.9],
            [0.51,    0.26,    0.13,    0.26,    0.51,    0.9],
            [0.03,    0.06,    0.06,    0.06,    0.13,    0.1],
            [0.06,    0.13,    0.06,    0.13,    0.13,    0.1],
            [0.13,    0.03,    0.13,    0.13,    0.26,    0.9],

        ],
        [
            [
                [1, 1./3., 1./5., 1./3., 1./2., 1./3.],
                [3,     1,     2,     3,     1, 1./4.],
                [5, 1./2.,     1,     2, 1./2., 1./3.],
                [3, 1./3., 1./2.,     1, 1./3., 1./5.],
                [2,     1,     2,     3,     1,     1],
                [3,     4,     3,     5,     1,     1]
            ]
        ]
    ]


def test_rever_hierarchical_process(hierarchia, alternatives):
    print()
    Za, *hierarchic = hierarchia
    processor = ReversHierarchicalProcessor(Za, hierarchic)
    Zs = processor.get_Zs()
    for level, Z in enumerate(Zs):
        print(f'LEVEL {level + 1}')
        print_matrix(Z)

    utilitys = [z[0] for z in Zs[-1]]

    utility_analysis = UtilityAnalysis(alternatives, utilitys)

    print('Альтернативы отсортированные по убыванию полезности')
    utility_analysis.sort_by('utility')
    utility_analysis.print_table()
    print()

    print('Альтернативы отсортированные по убыванию полезность/стоимость')
    utility_analysis.sort_by('utility_cost')
    utility_analysis.print_table()
    print()

    utility_analysis.print_chart_analisys()
