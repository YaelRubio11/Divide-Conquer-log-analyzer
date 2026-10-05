from concurrent.futures import ProcessPoolExecutor 

from src.sequential import analyze_sequential
from src.divide_conquer import combine_results


def analyze_parallel(logs, workers=2):
         if not logs:
                  return analyze_sequential(logs)
         
         chunk_size = (len(logs) + workers -1) // workers
         
         chunks = [
                  logs[i:i + chunk_size]
                  for i in range(0, len(logs), chunk_size)
         ]
         
         with ProcessPoolExecutor(max_workers=workers) as executor:
                  results = list(
                           executor.map(analyze_sequential, chunks)
                  )
         final_result = results[0]
         
         for result in results [1:]:
                  final_result = combine_results(final_result, result)
         
         return final_result
                  
                  