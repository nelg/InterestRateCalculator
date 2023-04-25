This tools is for calculating the after-tax return and various other related values for a given principal amount and a set of interest rates, personal tax rate, and portfolio investment income tax rate. It uses the argparse library to parse command line arguments for the principal, pir_tax_rate, personal_tax_rate, and interest_rates. It then iterates over the interest rates, calculates various values for each rate, and appends the results to a list. Finally, it prints the results in a table using the tabulate library, with various values colored using the terminalcolor library.

The code also includes some helper functions for converting between RGB and hex color codes and generating color gradients.


# Requirements:
pip install -r requirements.txt -t .

# Example output:
<code>
-------- INPUTS --------- 
Principal: $ 100000.00
PIR Tax Rate: 28.00%
Personal Tax Rate: 33.00%

Interest Rate    Return Before Taxes            Tax Payable             Interest Rate              Return Before Taxes                 Tax Payable                  After-tax Return
                 (using input interest rate)    (using PIR tax rate)    (from After-tax Return)    (using calculated interest rate)    (using personal tax rate)
---------------  -----------------------------  ----------------------  -------------------------  ----------------------------------  ---------------------------  ------------------
4.00%            $ 4000.00                      $ 1120.00               4.30%                      $ 4298.51                           $ 1418.51                    $ 2880.00
5.00%            $ 5000.00                      $ 1400.00               5.37%                      $ 5373.13                           $ 1773.13                    $ 3600.00
5.20%            $ 5200.00                      $ 1456.00               5.59%                      $ 5588.06                           $ 1844.06                    $ 3744.00
5.50%            $ 5500.00                      $ 1540.00               5.91%                      $ 5910.45                           $ 1950.45                    $ 3960.00
5.60%            $ 5600.00                      $ 1568.00               6.02%                      $ 6017.91                           $ 1985.91                    $ 4032.00
5.80%            $ 5800.00                      $ 1624.00               6.23%                      $ 6232.84                           $ 2056.84                    $ 4176.00
6.00%            $ 6000.00                      $ 1680.00               6.45%                      $ 6447.76                           $ 2127.76                    $ 4320.00
7.00%            $ 7000.00                      $ 1960.00               7.52%                      $ 7522.39                           $ 2482.39                    $ 5040.00
8.00%            $ 8000.00                      $ 2240.00               8.60%                      $ 8597.01                           $ 2837.01                    $ 5760.00
9.00%            $ 9000.00                      $ 2520.00               9.67%                      $ 9671.64                           $ 3191.64                    $ 6480.00
10.00%           $ 10000.00                     $ 2800.00               10.75%                     $ 10746.27                          $ 3546.27                    $ 7200.00
11.00%           $ 11000.00                     $ 3080.00               11.82%                     $ 11820.90                          $ 3900.90                    $ 7920.00

</code>

# Example use:
<code>
python3 InterestRateCalculator.py --principal 50000 0.06 0.07 

seq 1 .2 40 | xargs python3 InterestRateCalculator.py
</code>
## lolcat output
<code bash>
./InterestRateCalculator.py  | lolcat
</code>

## HTML output:
<code bash>
yay python-ansi2html
python3 InterestRateCalculator.py --principal 500000 4 4.2 4.4 4.6 4.7 4.8 30 33 | ansi2html  > InterestRates.html
</code>
