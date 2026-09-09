from src.sequential import analyze_sequential, empty_result

def combine_results(left, right):
         result = empty_result()
         
         for key in result:
                  result[key] = left[key] + right[key]
                  
         return result

def analyze_divide_conquer(logs, threshold=2):
         if len(logs) <= threshold:
                  return analyze_sequential(logs)
         
         middle = len(logs) // 2
         
         left_logs = logs[:middle]
         right_logs = logs[middle:]
         
         left_result = analyze_divide_conquer(left_logs, threshold)
         right_result = analyze_divide_conquer(right_logs, threshold)
         
         return combine_results(left_result, right_result) 

         
                 
                  
         
         