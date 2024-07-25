import torch

def test_torch():
    try:
        print("Testing PyTorch tensor operations...")
        x = torch.rand(5, 3)
        print("Random tensor:", x)
    except Exception as e:
        print(f"Error during PyTorch test: {e}")

if __name__ == "__main__":
    test_torch()

