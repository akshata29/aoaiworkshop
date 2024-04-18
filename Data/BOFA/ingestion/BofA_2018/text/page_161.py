
# START OF CODE BLOCK be904743

# Summary of the TEXT EXTRACT:
# Total income tax expense does not reflect the tax effects of items that are included in OCI each period.
# Other tax effects included in OCI each period resulted in a benefit of $1.2 billion, $1.2 billion and $498 million in 2018, 2017 and 2016, respectively.
# Prior to 2017, total income tax expense did not reflect tax effects associated with the Corporation's employee stock plans which decreased common stock and additional paid-in capital $41 million in 2016.
# Income tax expense for 2018, 2017 and 2016 varied from the amount computed by applying the statutory income tax rate to income before income taxes.
# The Corporation's federal statutory tax rate was 21 percent for 2018 and 35 percent for 2017 and 2016.
# On December 22, 2017, the President signed into law the Tax Act which made significant changes to federal income tax law including, among other things, reducing the statutory corporate income tax rate to 21 percent from 35 percent and changing the taxation of the Corporation's non-U.S. business activities.
# The impact on net income in 2017 was $2.9 billion, driven by $2.3 billion in income tax expense, largely from a lower valuation of certain U.S. deferred tax assets and liabilities.
# The change in the statutory tax rate also impacted the Corporation's tax- advantaged energy investments, resulting in a downward valuation adjustment of $946 million recorded in other income and a related income tax benefit of$347 million, which when netted against the $2.3 billion, resulted in a net impact on income tax expense of $1.9 billion.
# The Corporation has completed its analysis and accounting under Staff Accounting Bulletin No. 118 for the effects of the Tax Act.
# The reconciliation of the expected U.S. federal income tax expense, calculated by applying the federal statutory tax rate, to the Corporation's actual income tax expense, and the effective tax rates for 2018, 2017 and 2016 are presented in the table below.
# The Corporation files income tax returns in more than100 state and non-U.S. jurisdictions each year.
# The IRS and other tax authorities in countries and states in which the Corporation has significant business operations examine tax returns periodically (continuously in some jurisdictions).

# Variables:
# var_other_tax_effects_2018_498: Other tax effects in 2018 ($498 million)
# var_other_tax_effects_2017_1200: Other tax effects in 2017 ($1.2 billion)
# var_other_tax_effects_2016_1200: Other tax effects in 2016 ($1.2 billion)
# var_employee_stock_plans_2016_41: Employee stock plans in 2016 ($41 million)
# var_income_tax_expense_2018: Income tax expense in 2018
# var_income_tax_expense_2017: Income tax expense in 2017
# var_income_tax_expense_2016: Income tax expense in 2016
# var_federal_statutory_tax_rate_2018: Federal statutory tax rate in 2018 (21%)
# var_federal_statutory_tax_rate_2017: Federal statutory tax rate in 2017 (35%)
# var_federal_statutory_tax_rate_2016: Federal statutory tax rate in 2016 (35%)
# var_tax_act_impact_2017: Impact of Tax Act in 2017 ($2.9 billion)
# var_valuation_adjustment_2017: Valuation adjustment in 2017 ($946 million)
# var_income_tax_benefit_2017: Income tax benefit in 2017 ($347 million)
# var_net_impact_2017: Net impact on income tax expense in 2017 ($1.9 billion)
# var_expected_tax_expense_2018: Expected U.S. federal income tax expense in 2018
# var_expected_tax_expense_2017: Expected U.S. federal income tax expense in 2017
# var_expected_tax_expense_2016: Expected U.S. federal income tax expense in 2016
# var_state_tax_expense_2018: State tax expense in 2018
# var_state_tax_expense_2017: State tax expense in 2017
# var_state_tax_expense_2016: State tax expense in 2016
# var_affordable_housing_credits_2018: Affordable housing credits in 2018
# var_affordable_housing_credits_2017: Affordable housing credits in 2017
# var_affordable_housing_credits_2016: Affordable housing credits in 2016
# var_tax_exempt_income_2018: Tax-exempt income in 2018
# var_tax_exempt_income_2017: Tax-exempt income in 2017
# var_tax_exempt_income_2016: Tax-exempt income in 2016
# var_share_based_compensation_2018: Share-based compensation in 2018
# var_share_based_compensation_2017: Share-based compensation in 2017
# var_nondeductible_expenses_2018: Nondeductible expenses in 2018
# var_nondeductible_expenses_2017: Nondeductible expenses in 2017
# var_nondeductible_expenses_2016: Nondeductible expenses in 2016
# var_prior_period_UTBs_2018: Changes in prior-period UTBs in 2018
# var_prior_period_UTBs_2017: Changes in prior-period UTBs in 2017
# var_prior_period_UTBs_2016: Changes in prior-period UTBs in 2016
# var_rate_differential_2018: Rate differential on non-US earnings in 2018
# var_rate_differential_2017: Rate differential on non-US earnings in 2017
# var_rate_differential_2016: Rate differential on non-US earnings in 2016
# var_tax_law_changes_2017: Tax law changes in 2017 ($2.3 billion)
# var_other_2018: Other in 2018
# var_other_2017: Other in 2017
# var_other_2016: Other in 2016
# var_total_income_tax_expense_2018: Total income tax expense in 2018
# var_total_income_tax_expense_2017: Total income tax expense in 2017
# var_total_income_tax_expense_2016: Total income tax expense in 2016
# var_UTB_balance_2018: UTB balance in 2018
# var_UTB_balance_2017: UTB balance in 2017
# var_UTB_balance_2016: UTB balance in 2016
# var_UTB_balance_effective_tax_rate_2018: UTB balance affecting effective tax rate in 2018
# var_UTB_balance_effective_tax_rate_2017: UTB balance affecting effective tax rate in 2017
# var_UTB_balance_effective_tax_rate_2016: UTB balance affecting effective tax rate in 2016
# var_UTB_balance_other_items_2018: UTB balance including other items in 2018
# var_UTB_balance_other_items_2017: UTB balance including other items in 2017
# var_UTB_balance_other_items_2016: UTB balance including other items in 2016
# var_UTB_balance_gross_state_UTBs_2018: UTB balance including gross state UTBs in 2018
# var_UTB_balance_gross_state_UTBs_2017: UTB balance including gross state UTBs in 2017
# var_UTB_balance_gross_state_UTBs_2016: UTB balance including gross state UTBs in 2016
# var_UTB_balance_gross_non_US_UTBs_2018: UTB balance including gross non-U.S. UTBs in 2018
# var_UTB_balance_gross_non_US_UTBs_2017: UTB balance including gross non-U.S. UTBs in 2017
# var_UTB_balance_gross_non_US_UTBs_2016: UTB balance including gross non-U.S. UTBs in 2016
# var_number_of_state_and_non_US_jurisdictions: Number of state and non-U.S. jurisdictions

var_other_tax_effects_2018_498 = 498
var_other_tax_effects_2017_1200 = 1200
var_other_tax_effects_2016_1200 = 1200
var_employee_stock_plans_2016_41 = 41
var_income_tax_expense_2018 = None
var_income_tax_expense_2017 = None
var_income_tax_expense_2016 = None
var_federal_statutory_tax_rate_2018 = 21
var_federal_statutory_tax_rate_2017 = 35
var_federal_statutory_tax_rate_2016 = 35
var_tax_act_impact_2017 = 2900
var_valuation_adjustment_2017 = 946
var_income_tax_benefit_2017 = 347
var_net_impact_2017 = 1900
var_expected_tax_expense_2018 = None
var_expected_tax_expense_2017 = None
var_expected_tax_expense_2016 = None
var_state_tax_expense_2018 = None
var_state_tax_expense_2017 = None
var_state_tax_expense_2016 = None
var_affordable_housing_credits_2018 = None
var_affordable_housing_credits_2017 = None
var_affordable_housing_credits_2016 = None
var_tax_exempt_income_2018 = None
var_tax_exempt_income_2017 = None
var_tax_exempt_income_2016 = None
var_share_based_compensation_2018 = None
var_share_based_compensation_2017 = None
var_nondeductible_expenses_2018 = None
var_nondeductible_expenses_2017 = None
var_nondeductible_expenses_2016 = None
var_prior_period_UTBs_2018 = None
var_prior_period_UTBs_2017 = None
var_prior_period_UTBs_2016 = None
var_rate_differential_2018 = None
var_rate_differential_2017 = None
var_rate_differential_2016 = None
var_tax_law_changes_2017 = 2300
var_other_2018 = None
var_other_2017 = None
var_other_2016 = None
var_total_income_tax_expense_2018 = None
var_total_income_tax_expense_2017 = None
var_total_income_tax_expense_2016 = None
var_UTB_balance_2018 = None
var_UTB_balance_2017 = None
var_UTB_balance_2016 = None
var_UTB_balance_effective_tax_rate_2018 = None
var_UTB_balance_effective_tax_rate_2017 = None
var_UTB_balance_effective_tax_rate_2016 = None
var_UTB_balance_other_items_2018 = None
var_UTB_balance_other_items_2017 = None
var_UTB_balance_other_items_2016 = None
var_UTB_balance_gross_state_UTBs_2018 = None
var_UTB_balance_gross_state_UTBs_2017 = None
var_UTB_balance_gross_state_UTBs_2016 = None
var_UTB_balance_gross_non_US_UTBs_2018 = None
var_UTB_balance_gross_non_US_UTBs_2017 = None
var_UTB_balance_gross_non_US_UTBs_2016 = None
var_number_of_state_and_non_US_jurisdictions = None

# END OF CODE BLOCK be904743
