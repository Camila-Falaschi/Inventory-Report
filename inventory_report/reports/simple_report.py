from datetime import datetime, date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cla, dict_list):
        today = date.today()
        mfg_date_list = [item["data_de_fabricacao"] for item in dict_list]
        mfg_str_to_date_list = [
            datetime.strptime(date, "%Y-%m-%d").date()
            for date in mfg_date_list
        ]
        oldest_mfg_date = min(mfg_str_to_date_list)

        exp_date_list = [item["data_de_validade"] for item in dict_list]
        exp_str_to_date_list = [
            datetime.strptime(date, "%Y-%m-%d").date()
            for date in exp_date_list
        ]
        exp_dates_higher_than_today = []
        for product_exp_date in exp_str_to_date_list:
            if product_exp_date >= today:
                exp_dates_higher_than_today.append(product_exp_date)
        closest_exp_date = min(exp_dates_higher_than_today)

        company_counter = Counter(
            [item["nome_da_empresa"] for item in dict_list]
        )

        return f"""Data de fabricação mais antiga: {oldest_mfg_date}
Data de validade mais próxima: {closest_exp_date}
Empresa com mais produtos: {company_counter.most_common()[0][0]}"""
