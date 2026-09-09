from src.sequential import analyze_sequential
from src.divide_conquer import analyze_divide_conquer


def sample_logs():
         return[
                  "INTO Server started susccessfully",
                  "ERROR Failed login for user admin",
                  "ERROR Failed login for user root",
                  "WARNING Unauthorized access attempt",
                  "INFO User login successful",
                  "ERROR SQL error while executing query",
                  "CRITICAL Database unavailable",
                  "ERROR Connection refused",
                  "INFO Request completed",
                  "INFO Server healthy",
         ]
         
def test_sequential_analysis():
         logs = sample_logs()
         
         
         #print(logs)
         #print(len(logs))
         
         result = analyze_sequential(logs)
         
         assert result["total_lines"] == 10
         assert result["errors"] == 4
         assert result["critical"] == 1
         assert result["failed_logins"] == 2
         assert result["unauthorized"] == 1
         assert result["sql_errors"] == 1
         assert result["connection_refused"] == 1
         

def test_divide_conquer_analysis():
         logs = sample_logs()
         
         result = analyze_divide_conquer(logs)
         
         assert result["total_lines"] == 10
         assert result["errors"] == 4
         assert result["critical"] == 1
         assert result["failed_logins"] == 2
         assert result["unauthorized"] == 1
         assert result["sql_errors"] == 1
         assert result["connection_refused"] == 1
         

def test_both_algorithms_return_same_result():
         logs = sample_logs()
         
         senquential_result = analyze_sequential(logs)
         divide_conquer_result = analyze_divide_conquer(logs)
         
         assert senquential_result == divide_conquer_result
         
