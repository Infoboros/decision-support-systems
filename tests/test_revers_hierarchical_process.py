import pytest

from algorithm.revers_hierarchical_process import ReversHierarchicalProcessor
from algorithm.utility_analysis import UtilityAnalysis
from algorithm.utils import print_matrix


@pytest.fixture()
def alternatives():
    return [
        {
            'name': 'Одежда',
            'cost': 10
        },
        {
            'name': 'Ремонт',
            'cost': 25
        },
        {
            'name': 'Отдых',
            'cost': 30
        },
        {
            'name': 'Телефон',
            'cost': 7
        },
        {
            'name': 'Мебель',
            'cost': 18
        },
        {
            'name': 'Банк',
            'cost': 22
        },
        {
            'name': 'Образование',
            'cost': 27
        },
    ]


@pytest.fixture()
def hierarchia():
    return [
        [
            [0.13, 0.06, 0.9, 0.1, 0.13, 0.26],
            [0.26, 0.13, 0.1, 0.1, 0.13, 0.13],
            [0.51, 0.13, 0.9, 0.1, 0.51, 0.26],
            [0.13, 0.26, 0.1, 0.9, 0.13, 0.13],
            [0.13, 0.06, 0.9, 0.1, 0.03, 0.13],
            [0.06, 0.13, 0.1, 0.9, 0.13, 0.03],
            [0.13, 0.26, 0.1, 0.9, 0.06, 0.13],

        ],
        [
            [
                [1, 5, 1, 3, 5, 1. / 3.],
                [1. / 5., 1, 1. / 5., 1. / 3., 1, 1. / 7.],
                [1, 5, 1, 3, 5, 1. / 3.],
                [1. / 3., 3, 1. / 3., 1, 3, 1. / 5.],
                [1. / 5., 1, 1. / 5., 1. / 3., 1, 1. / 7.],
                [3, 7, 3, 5, 7, 1],

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
