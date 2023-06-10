import os
import csv

def analyze_budget_data():
    # Set the path for the budget_data.csv file
    budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    profit_loss_changes = []
    months = []

    # Read the CSV file
    with open(budget_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        csv_header = next(csvreader)

        # Loop through the rows in the CSV file
        for row in csvreader:
            # Calculate the total number of months
            total_months += 1

            # Calculate the net total amount of "Profit/Losses"
            net_total += int(row[1])

            # Calculate the changes in "Profit/Losses"
            if total_months > 1:
                profit_loss_changes.append(int(row[1]) - previous_profit_loss)
                months.append(row[0])

            previous_profit_loss = int(row[1])

    # Calculate the average of the changes in "Profit/Losses"
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    # Find the greatest increase and decrease in profits
    greatest_increase = max(profit_loss_changes)
    greatest_increase_index = profit_loss_changes.index(greatest_increase)
    greatest_increase_month = months[greatest_increase_index]

    greatest_decrease = min(profit_loss_changes)
    greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
    greatest_decrease_month = months[greatest_decrease_index]

    # Print the analysis to the terminal
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    # Export the analysis to a text file
    output_path = os.path.join("PyBank", "Analysis", "financial_analysis.txt")
    with open(output_path, "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_total}\n")
        txtfile.write(f"Average Change: ${average_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

def analyze_election_data():
    # Set the path for the election_data.csv file
    election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    max_votes = 0

    # Read the CSV file
    with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        csv_header = next(csvreader)

        # Loop through the rows in the CSV file
        for row in csvreader:
            # Calculate the total number of votes
            total_votes += 1

            # Count the votes for each candidate
            candidate = row[2]
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export the analysis to a text file
    output_path = os.path.join("PyPoll", "Analysis", "election_results.txt")
    with open(output_path, "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")

def main():
    analyze_budget_data()
    analyze_election_data()

if __name__ == "__main__":
    main()
