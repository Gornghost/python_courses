def salary_net_uah(salary_usd, currency, taxes, esv):
    # What salary in UAH after paying taxes
    salary_uah = salary_usd*currency
    salary_minus_taxes = salary_uah - salary_uah*taxes/100
    result_uah = salary_minus_taxes - esv
    return result_uah


def salary_net_usd(salary_usd, currency, taxes, esv):
    # What salary in USD after paying taxes
    esv_usd = esv/currency
    salary_minus_esv = salary_usd - salary_usd*taxes/100
    result_usd = salary_minus_esv - esv_usd
    return result_usd


def print_salary(salary_usd, currency, taxes, esv):
    result_usd = str(round(salary_net_usd(salary_usd, currency, taxes, esv), 2))
    result_uah = str(round(salary_net_uah(salary_usd, currency, taxes, esv), 2))
    print("Your salary after paying taxes is " + result_usd + " USD " + "(" + result_uah + " UAH)")


print_salary(salary_usd=2100, currency=27, taxes=5, esv=1039.06)