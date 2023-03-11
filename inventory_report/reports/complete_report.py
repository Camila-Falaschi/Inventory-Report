from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        simple_report = super().generate(dict_list)
        company_counter = Counter(
            [item["nome_da_empresa"] for item in dict_list]
        ).most_common()
        companies_counter = ""
        for company, quantity in company_counter:
            companies_counter += f"- {company}: {quantity}\n"

        return f"""{simple_report}
Produtos estocados por empresa:
{companies_counter}"""
