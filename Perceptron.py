def AND_gate(x1, x2):
    # Initialize weights and bias
    w1 = 1
    w2 = 1
    b = -1
    
    # Compute the weighted sum
    weighted_sum = w1 * x1 + w2 * x2 + b
    
    # Apply the perceptron rule
    if weighted_sum <= 0:
        return 0
    else:
        return 1

# Dry run with sample inputs
print("Input (0, 0):", AND_gate(0, 0)) 
print("Input (0, 1):", AND_gate(0, 1)) 
print("Input (1, 0):", AND_gate(1, 0))   
print("Input (1, 1):", AND_gate(1, 1)) 
