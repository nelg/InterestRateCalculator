#!/bin/env python3
import argparse
from tabulate import tabulate
from terminalcolor import ctext, cprint


def calculate_after_tax_return(principal, interest_rate, tax_rate):
    return (principal * interest_rate) * (1 - tax_rate)


def calculate_interest_rate_from_after_tax_return(principal, after_tax_return, tax_rate):
    total_return_before_taxes = after_tax_return / (1 - tax_rate)
    return (total_return_before_taxes / principal) 


def parse_interest_rates(interest_rates):
    parsed_rates = []
    for rate in interest_rates:
        if rate > 1:
            rate /= 100
        parsed_rates.append(rate)
    return sorted(parsed_rates)

def parse_input_percentage(input):
   if input > 1:
      return input / 100
   return input

def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def RGB_to_hex(RGB):
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])

def create_color_string(rgb):
    return f"24bit-{rgb[0]};{rgb[1]};{rgb[2]}"

def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
  ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
  # Starting and ending colors in RGB form
  s = hex_to_RGB(start_hex)
  f = hex_to_RGB(finish_hex)
  # Initilize a list of the output colors with the starting color
  RGB_list = [create_color_string(s)]
  # Calcuate a color at each evenly spaced value of t from 1 to n
  for t in range(1, n):
    # Interpolate RGB vector for color at the current value of t
    curr_vector = [
      int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
      for j in range(3)
    ]
    # Add it to our list of output colors
    RGB_list.append(create_color_string(curr_vector))

  return RGB_list


parser = argparse.ArgumentParser(description='Calculate the after-tax return on investment at various interest rates.')
parser.add_argument('--principal', type=float, default=100000, help='the principal amount (default: %(default)s)')
parser.add_argument('--pir-tax-rate', dest='pir_tax_rate', type=float, default=0.28, help='the tax rate for the portfolio investment income (default: %(default)s)')
parser.add_argument('--personal-tax-rate', type=float, default=0.33, help='the personal tax rate for the after-tax return (default: %(default)s)')
parser.add_argument('interest_rates', nargs='*', type=float, default=[0.04, 0.05, 0.052, 0.055, 0.056, 0.058, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11], help='interest rates')
args = parser.parse_args()





principal = args.principal
pir_tax_rate = parse_input_percentage(args.pir_tax_rate)
personal_tax_rate = parse_input_percentage(args.personal_tax_rate)
interest_rates = parse_interest_rates(args.interest_rates)

print(ctext(f"-------- INPUTS --------- ",color="24bit-213;94;245", text_type="bold"))
print(ctext(f"Principal: $ {principal:.2f}",color="24bit-253;74;215", text_type="bold"))
print(ctext(f"PIR Tax Rate: {pir_tax_rate:.2%}",color="24bit-253;74;225", text_type="bold"))
print(ctext(f"Personal Tax Rate: {personal_tax_rate:.2%}",color="24bit-253;74;255", text_type="bold"))    
print()

brightness = 230
gradient_steps = int(brightness / len(interest_rates))
linear_gradient_tax = iter(linear_gradient("#6aa3ff", "#a4ffe4",  len(interest_rates)))
linear_gradient_interest = iter(linear_gradient("#fbff19", "#ffb99e",  len(interest_rates)))
linear_gradient_return_before_tax = iter(linear_gradient("#ff3884", "#f8a7ff",  len(interest_rates)))

results = []
for interest_rate in interest_rates:
    return_before_taxes = principal * interest_rate
    tax_payable = return_before_taxes * pir_tax_rate
    after_tax_return = return_before_taxes - tax_payable

    interest_rate_from_after_tax_return = calculate_interest_rate_from_after_tax_return(principal, after_tax_return, personal_tax_rate)
    return_before_taxes_using_interest_rate_from_after_tax = principal * interest_rate_from_after_tax_return
    tax_payable_using_personal_tax_rate = return_before_taxes_using_interest_rate_from_after_tax * personal_tax_rate    
    tax_color = next(linear_gradient_tax)
    return_before_tax_color = next(linear_gradient_return_before_tax)
    results.append([
        ctext(f"{interest_rate:.2%}", color=f"24bit-255;{brightness};{brightness}"),
        ctext(f"$ {return_before_taxes:.2f}", color=return_before_tax_color),
        ctext(f"$ {tax_payable:.2f}", color=tax_color),
        ctext(f"{interest_rate_from_after_tax_return:.2%}", color=next(linear_gradient_interest)),
        ctext(f"$ {return_before_taxes_using_interest_rate_from_after_tax:.2f}", color=return_before_tax_color),
        ctext(f"$ {tax_payable_using_personal_tax_rate:.2f}", color=tax_color),
        ctext(f"$ {after_tax_return:.2f}", color=f"24bit-{brightness};255;{brightness}")
    ])
    brightness -= gradient_steps

headers = [
     ctext('PIR Interest Rate',color="24bit-53;234;255", text_type="bold"),
     ctext('Return Before Taxes\n(using input interest rate)',color="24bit-53;234;255", text_type="bold"),
     ctext('Tax Payable\n(using PIR tax rate)',color="24bit-53;234;255", text_type="bold"),
     ctext('Personal Interest Rate\n(Must be at least\nthis rate to match PIR)',color="24bit-53;234;255", text_type="bold"),
     ctext('Return Before Taxes\n(using calculated interest rate)',color="24bit-53;234;255", text_type="bold"),
     ctext('Tax Payable\n(using personal tax rate)',color="24bit-53;234;255", text_type="bold"),
     ctext('After-tax Return',color="24bit-53;234;255", text_type="bold")
]

print(tabulate(results, headers=headers, tablefmt='simple'))
