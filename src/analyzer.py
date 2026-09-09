from src.sequential import analyze_sequential
from src.divide_conquer import analyze_divide_conquer

def load_logs(file_path):
         with open(file_path, "r", encoding="utf-8") as file:
                  return file.readlines()


def print_report(result):
    print("\nSecurity Log Analysis")
    print("=" * 30)
    
    print(f"Total lines:        {result['total_lines']}")
    print(f"Errors:             {result['errors']}")
    print(f"Critical events:    {result['critical']}")
    print(f"Failed logins:      {result['failed_logins']}")
    print(f"Unauthorized:       {result['unauthorized']}")
    print(f"SQL errors:         {result['sql_errors']}")
    print(f"Connection refused: {result['connection_refused']}")
         
         
def main():
         file_path = "examples/sample.log"
         
         logs = load_logs(file_path)
         
         sequential_result = analyze_sequential(logs)
         divide_conquer_result = analyze_divide_conquer(logs)
         
         
         print("\nSequential Analysis")
         print_report(sequential_result)
         
         print("\nDivide & Conquer Analysis")
         print_report(divide_conquer_result)
         
if __name__ == "__main__":
         main()
         