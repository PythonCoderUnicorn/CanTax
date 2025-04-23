
"""
==================================
     CANADIAN INCOME TAXATION
   planning and decision making
        2022-2023 edition
 Buckwold | Kitunen | Roman | Iqbal
        McGraw Hill
=================================
"""


primary_types_of_income = ['Business','Property','Employment','Capital Gains'] 

entities_subject_to_taxation_income = ['Individuals','Corporations','Trusts']


# alternative forms of business & investing structures used by taxable entities
alt_structures_taxable_entities = [
    'Proprietorship',
    'Corporation',
    'Partnership',
    'Limited partnership',
    'Joint venture',
    'Income trust'
]

tax_jurisdictions = [
    'Provincial',
    'Territorial',
    'Federal',
    'Foreign'
]




"""
====== FUNDAMENTALS OF TAX PLANNING

Tax Planning
    legitimate arranging of financial activities in a way that reduces or defers the related tax cost
    'legitimate' = tax authorities that do not attempt to prevent certain transactions

GAAR = general anti-avoidance rule

Tax Evasion
    knowingly failing to report revenue, claiming the deduction of a false expense or both

Tax Avoidance
    transactions planned and carried out mainly to avoid, reduce or defer tax payable under the law

Types of Tax Planning

1. shifting income from one time period to another
2. transferring income to another entity or alternatie taxpaper
3. converting the nature of income from one type to another

necessary to determine:
    a) future tax rates or income levels that will cause those tax rates or both
    b) discretionary opportunities iwthin the tax system
    c) time value of money




"""



def tax_planning_example():

    corporate_profit_yr_1 = 150e3
    # included in profit calculation is accounts receivable (bad debts)
    accounts_receivable = 20e3
    # new contract deal, projected profits for year 2
    corporate_profit_yr_2 = 550e3
    # option 1 = deducting | not deducting a reserve for bad debts in any year
    # option 2 = corporation pays tax at rate of 13% on first $550,000 of annual business income 
    #           and 27% on income above that amount (bracket and rates assumed)

    tax_rate_1 = 0.13
    tax_rate_2 = 0.27

    option1 = (accounts_receivable * tax_rate_1)
    option2 = (accounts_receivable * tax_rate_2)
    tax_reduction = option2 - option1


    deduction_claimed = str(input("claim deduction ? y/n: ")).lower()

    if deduction_claimed =='n':
        profits = corporate_profit_yr_1 + accounts_receivable
        option1 = (accounts_receivable * tax_rate_1)
        
        print(f"Profits ......... ${profits:,.2f}")
        print(f"Tax increase .... ${option1:,.2f} \n")

    elif deduction_claimed=='y':
        
        tax_deduct = corporate_profit_yr_1 - accounts_receivable
        print(f"Year 1\nProfits .......... ${tax_deduct:,.2f} ")
        print(f"Tax increase ..... ${option1:,.2f} \n")

        profits2 = corporate_profit_yr_2 - accounts_receivable
        option2 = (accounts_receivable * tax_rate_2)
        
        
        print(f"Year 2\nProfits ......... ${profits2:,.2f}")
        print(f"Tax increase .... ${option2:,.2f}")
        
        tax_reduction = option2 - option1
        tax_reduction2 = option1 - option2 
        if tax_reduction > tax_reduction2:
            print(f"\n(deduct in year 1)\nOverall tax reduction .... ${tax_reduction:,.2f}\n")
        else:
            print(f"\n(deduct in year 2)\nOverall tax reduction .... ${tax_reduction2:,.2f}\n")


    else:
        print("error")


# ==== benefits of shifting income tax from 1 period to another
def tax_defer_example():
    taxpaper_investment = 100e3 # 3 yrs
    invest_option_1 = {"type": "corporate bond", "annual interest": 0.10}
    invest_option_2 = {"type": "secure corporate share", "annual growth rate": 0.10}

    annual_aftertax_cashflow_earning = 0.06
    taxpayer_tax_rate = 0.50

    aftertax_annual_return = invest_option_1['annual interest'] - (taxpayer_tax_rate * invest_option_1['annual interest'])
    # print( aftertax_annual_return )

    bond_interest_received = aftertax_annual_return * taxpaper_investment
    reinvestment_securities_annual_return = annual_aftertax_cashflow_earning - (taxpayer_tax_rate * annual_aftertax_cashflow_earning)
    reinvestment_interest = reinvestment_securities_annual_return * bond_interest_received

    subtotal = bond_interest_received + reinvestment_interest + bond_interest_received
    reinvestment_interest2 = reinvestment_securities_annual_return * subtotal

    subtotal2 = subtotal + reinvestment_interest2 + bond_interest_received
    total_bond_value = taxpaper_investment + subtotal2

    print(f"Initial investment ........... ${taxpaper_investment:,.2f}")
    print("End of Year 1")
    print(f"Bond investment received ..... ${bond_interest_received:,.2f}")
    print("End of Year 2")
    print(f"Reinvestment interest ........ ${reinvestment_interest:,.2f}")
    print(f"Bond investment received ..... ${bond_interest_received:,.2f}")
    print(f".............................. ${subtotal:,.2f}")
    print("End of Year 3")
    print(f"Reinvestment interest ........ ${reinvestment_interest2:,.2f}")
    print(f"Bond investment received ..... ${bond_interest_received:,.2f}")
    print(f".............................. ${subtotal2:,.2f}")
    print(f"Total value of bond investment ............. ${total_bond_value:,.2f} \n")


    growth_1 = invest_option_1['annual interest'] * taxpaper_investment
    subtotal3 = growth_1 + taxpaper_investment

    growth_2 = invest_option_1['annual interest'] * subtotal3
    subtotal4 =  growth_1 + growth_2 + taxpaper_investment 

    growth_3 = invest_option_1['annual interest'] * subtotal4
    subtotal5 =  growth_1 + growth_2 + taxpaper_investment + growth_3

    tax_end_of_year = (0.5 * 1/2) * (subtotal5 - taxpaper_investment)
    total_value_share_investment = subtotal5 - tax_end_of_year

    return_on_share = total_value_share_investment - total_bond_value

    income_tax_gain = return_on_share - tax_end_of_year


    print(f"Initial investment ........... ${taxpaper_investment:,.2f}")
    print("End of Year 1")
    print(f"Growth ....................... ${growth_1:,.2f}")
    print(f".............................. ${subtotal3:,.2f}")
    print("End of Year 2")
    print(f"Growth ....................... ${growth_2:,.2f}")
    print(f".............................. ${subtotal4:,.2f}")
    print("End of Year 3")
    print(f"Growth ....................... ${growth_3:,.2f}")
    print(f".............................. ${subtotal5:,.2f}")
    print("Tax Rate at End of Year 3")
    print(f"tax @ end ... ${tax_end_of_year :,.2f}")
    print(f"Total value of share investment ........... ${total_value_share_investment:,.2f}")

    print(f"return on share investment ...... ${return_on_share:,.2f}")
    print(f"tax advantage on income tax ..... ${income_tax_gain:,.2f} \n")


#==== Transferring income to another entity
def transfer_tax_entity_example():

    unincorporated_business_annual_profits = 100e3
    personal_financial_obligations = 40e3
    tax_rates = {
        # personal tax = federal + provincial
        "first 50k": 0.20,
        "next 50k": 0.30,
        "next 56k": 0.40,
        "next 66k": 0.45,
        "over 222k": 0.50
    }
    private_corporate_tax_rate = {"first 500k": 0.13, "profits": 0.27}


    if unincorporated_business_annual_profits >= 100e3:
        # split the amount into half then tax based on 1st and 2nd halves
        tr1 = tax_rates['first 50k'] * (unincorporated_business_annual_profits/2)
        tr2 = tax_rates['next 50k'] * (unincorporated_business_annual_profits/2)
        subtotal_tax_rate = tr1+tr2
        subtotal_1 = unincorporated_business_annual_profits - subtotal_tax_rate
        total = subtotal_1 - personal_financial_obligations

        print(f"\nBusiness profits ................ ${unincorporated_business_annual_profits:,.2f}")
        print(f"Tax {tax_rates['first 50k']*100}% ..... ${tr1:,.2f}")
        print(f"Tax {tax_rates['next 50k']*100}% ..... ${tr2:,.2f}")
        print(f"total tax rates .......... ${subtotal_tax_rate:,.2f}")
        print(f".......................... ${subtotal_1:,.2f}")
        print(f"Personal expenditures .... ${personal_financial_obligations:,.2f}")
        print(f"Total ............................ ${total:,.2f}\n")

    # created separate corporation business: a shareholder, employed @ corporation and earning a salary
    salary = 50e3
    less_tax = tax_rates['first 50k'] * salary
    personal_req = salary - less_tax

    business_profits = unincorporated_business_annual_profits
    salary_to_shareholder = business_profits - salary
    corporate_business_profit = business_profits - salary_to_shareholder
    corporate_tax = private_corporate_tax_rate['first 500k'] * corporate_business_profit
    available_for_expansion = corporate_business_profit - corporate_tax
    cashflow_enhancement = available_for_expansion - total

    print(f"\n-- Corporation Employee & shareholder")
    print(f"Salary ................... ${salary:,.2f}")
    print(f"Tax rate {tax_rates['first 50k']*100}% ..... {less_tax:,.2f}")
    print(f"Personal requirements .... ${personal_req:,.2f}")
    print("-------")
    print(f"Business profits ............... ${business_profits:,.2f}")
    print(f"Salary to shareholder .......... ${salary_to_shareholder:,.2f}")
    print(f"Corporate business profit ...... ${corporate_business_profit:,.2f}")
    print(f"Corporate tax .................. ${corporate_tax:,.2f}")
    print(f"Available for expansion ........ ${available_for_expansion:,.2f}")
    print(f"Cash flow enhancement .......... ${cashflow_enhancement:,.2f}")


#==== converting income from 1 type to another
def income_type_conversion_example():
    company_shares_value = 410e3
    individual_share_cost = 10e3
    dividend = 40e3
    share_sales_incurred_loss = 500e3
    tax_rate_yr_1 = 0.5
    company_tax_rate = 0.43

    share_price = company_shares_value - dividend
    tax_cost = (company_tax_rate * dividend)
    capital_gain = share_price - individual_share_cost
    taxable_portion = (capital_gain * 1/2)

    print(f"\nDividend ................ ${dividend:,.2f}")
    print(f"Share price ............. ${share_price:,.2f}")
    print(f"Tax cost ................ ${tax_cost:,.2f}")
    print(f"Capital Gain ............ ${capital_gain:,.2f}")
    print(f"Taxable portion ......... ${taxable_portion:,.2f}\n")



















