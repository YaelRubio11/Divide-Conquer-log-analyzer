import random
import time

from src.sequential import analyze_sequential
from src.divide_conquer import analyze_divide_conquer
from src.parallel import analyze_parallel


SAMPLE_MESSAGES = [
         "INFO Server started succesfully",
         "ERROR Failed login for user admin",
         "ERROR Failed login for user root",
         "WARNING Unauthorized acces attempt",
         "INFO User login succesful",
         "ERROR SQL error while executing query", 
         "CRITICAL Database unavailable",
         "ERROR Connection refused",
         "INFO Request completed",
         "INFO Server healthy", 
]

def generate_logs(amount):
         return [random.choice(SAMPLE_MESSAGES) for _ in range(amount)]

def benchmark(function, logs):
         start = time.perf_counter()
         
         result = function(logs)
         
         end = time.perf_counter()
         
         return end - start, result

def main():
    sizes = [10_000, 100_000, 500_000, 1_000_000]

    print("\nPerformance Benchmark")
    print("=" * 55)

    for log_count in sizes:
        print(f"\nGenerating {log_count:,} logs...")
        logs = generate_logs(log_count)

        sequential_time, sequential_result = benchmark(
            analyze_sequential,
            logs,
        )

        divide_time, divide_result = benchmark(
            analyze_divide_conquer,
            logs,
        )
        
        parallel_time, parallel_result = benchmark(
                 analyze_parallel,
                 logs,
        )

        print(f"Dataset size:       {log_count:,} logs")
        print(f"Sequential:         {sequential_time:.6f} seconds")
        print(f"Divide & Conquer:   {divide_time:.6f} seconds")
        print(f"Parallel:           {parallel_time:.6f} seconds")
        print(
            "Results identical:",
            sequential_result == divide_result ==parallel_result,
        )        
if __name__ == "__main__":
         main()


