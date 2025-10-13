"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user = input("Enter a number or Done to finish: ").strip().lower()
        if user == "done": 
            break 
        try: 
            number = float(user)
            numbers.append(number)
        except ValueError:
            print("Invalide input")
        
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {
        "count" : len(numbers),
        "sum" : sum(numbers),
        "average" : sum(numbers)/len(numbers),
        "minimum" : min(numbers),
        "maximum" : max(numbers),
        "even_count": len([n for n in numbers if n%2 == 0]),
        "odd_count" : len([n for n in numbers if n%2 != 0])
    }
        
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"count : {analysis ['count']}")
    print(f"sum : {analysis ['sum']}")
    print(f"Average : {analysis ['average']}")
    print(f"Minimum : {analysis ['minimum']}")
    print(f"Maximumt : {analysis ["maximum"]}")
    print(f"Even_numbers : {analysis ['even_count']}")
    print(f"Odd_numbers : {analysis ['odd_count']}")



def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()