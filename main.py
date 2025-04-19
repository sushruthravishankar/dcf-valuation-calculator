#  DCF Valuation Calculator in Python

def dcf_valuation(fcf_list, wacc, terminal_growth_rate):
    discounted_fcfs = []
    wacc_decimal = wacc / 100
    g_decimal = terminal_growth_rate / 100

    # Discount each year's FCF
    for year, fcf in enumerate(fcf_list, start=1):
        discounted_fcf = fcf / (1 + wacc_decimal) ** year
        discounted_fcfs.append(discounted_fcf)

    # Terminal Value at end of Year 5
    terminal_value = (fcf_list[-1] * (1 + g_decimal)) / (wacc_decimal - g_decimal)

    # Discount Terminal Value back to present
    discounted_terminal_value = terminal_value / (1 + wacc_decimal) ** len(fcf_list)

    # Sum up all discounted FCFs and Terminal Value
    enterprise_value = sum(discounted_fcfs) + discounted_terminal_value

    # Print results
    print("\n--- DCF Valuation Summary ---")
    for i, dfcf in enumerate(discounted_fcfs, start=1):
        print(f"Year {i} Discounted FCF: ${dfcf:,.2f}")
    print(f"\nDiscounted Terminal Value: ${discounted_terminal_value:,.2f}")
    print(f"\nEnterprise Value: ${enterprise_value:,.2f}")

# Example Usage
if __name__ == "__main__":
    # Example input
    projected_fcfs = [10000, 10500, 11000, 11500, 12000]  # FCFs for 5 years
    wacc = 8  # in %
    terminal_growth_rate = 2.5  # in %

    dcf_valuation(projected_fcfs, wacc, terminal_growth_rate)
