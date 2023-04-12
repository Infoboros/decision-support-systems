from matplotlib import pyplot as plt
from tabulate import tabulate


class UtilityAnalysis:
    def __init__(self, alternatives: list, utilitys: list):
        self.alternatives = [
            {
                **alternative,
                'utility': utilitys[index]
            }
            for index, alternative in enumerate(alternatives)
        ]
        self.calculate_utility_cost()

    def calculate_utility_cost(self):
        self.alternatives = [
            {
                **alternative,
                'utility_cost': alternative['utility'] / alternative['cost']
            }
            for alternative in self.alternatives
        ]

    def print_table(self):
        print(
            tabulate(
                [
                    [alternative["name"], alternative["utility"], alternative["cost"], alternative["utility_cost"]]
                    for alternative in self.alternatives
                ],
                headers=['Наименование', 'Полезность', 'Стоимость', 'Полезность/Стоимость']
            )
        )

    def sort_by(self, field: str):
        self.alternatives.sort(key=lambda alternative: alternative[field], reverse=True)

    def get_selected(self, cost: float) -> (list, float, float):
        remains = cost
        selected = []
        for alternative in self.alternatives:
            if (remains - alternative['cost']) >= 0:
                selected.append(alternative)
                remains -= alternative['cost']

        utilitys = sum(alternative['utility'] for alternative in selected)

        return selected, utilitys, remains

    def get_chart_analisys(self) -> list:
        chart = []
        max_cost_sum = sum(alternative['cost'] for alternative in self.alternatives)
        for cost in range(max_cost_sum + 1):
            _, utility, remains = self.get_selected(cost)
            chart.append({
                'cost': cost,
                'utility': utility,
                'remains': remains
            })

        return chart

    def print_chart_analisys(self):
        self.sort_by('utility')
        max_utility_chart = self.get_chart_analisys()

        self.sort_by('utility_cost')
        max_utility_cost_chart = self.get_chart_analisys()

        fig, host = plt.subplots(layout='constrained')

        ax2 = host.twinx()

        host.set_xlabel("Стоимость (руб)")
        host.set_ylabel("Полезность")
        # ax2.set_ylabel("Остаток (руб)")

        def get_plot_data(data, field):
            return [
                [row['cost'] for row in data],
                [row[field] for row in data]
            ]
        #
        # r1 = ax2.plot(*get_plot_data(max_utility_chart, 'remains'), color='orange',
        #               label="Остаток (Максимизация полезности)")
        # r2 = ax2.plot(*get_plot_data(max_utility_cost_chart, 'remains'), color='cyan',
        #               label="Остаток (Максимизация полезность/стоимость)")

        l1 = host.plot(*get_plot_data(max_utility_chart, 'utility'), color='red', label="Полезность (Максимизация полезности)")
        l2 = host.plot(*get_plot_data(max_utility_cost_chart, 'utility'), color='blue',
                       label="Полезность (Максимизация полезность/стоимость)")

        host.legend(handles=l1 + l2, loc='best')
        plt.title("Зависимость Полезности от Cтоимости")
        plt.show()
