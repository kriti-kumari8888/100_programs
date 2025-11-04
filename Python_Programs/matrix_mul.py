import numpy as np

def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Multiply two matrices using NumPy."""
    try:
        return np.dot(A, B)
    except ValueError as e:
        raise ValueError(f"Matrix multiplication error: {e}")

def main():
    # Example matrices
    A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
    B = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    try:
        C = matrix_multiply(A, B)
        print("\nResult (A × B):")
        print(C)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()