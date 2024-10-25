import numpy as np
from numba import cuda
import time
from robometrics.lib.register import Register

# Define the CUDA kernel


@cuda.jit
def vector_add(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

# Function to perform vector addition continuously


def run_continuously():
    Register.async_auto_register()
    N = 1000
    a = np.ones(N, dtype=np.float32)
    b = np.ones(N, dtype=np.float32)
    c = np.zeros(N, dtype=np.float32)

    # Allocate device memory
    a_device = cuda.to_device(a)
    b_device = cuda.to_device(b)
    c_device = cuda.to_device(c)

    # Define the number of threads and blocks
    threads_per_block = 256
    blocks_per_grid = (a.size + (threads_per_block - 1)) // threads_per_block

    try:
        while True:
            vector_add, blocks_per_grid, threads_per_block
            c = c_device.copy_to_host()
            print("Result:", c)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Process interrupted and stopped.")
    Register.auto_unregister()


if __name__ == "__main__":
    run_continuously()
