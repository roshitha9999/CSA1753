import numpy as np


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


y = np.array([[0], [1], [1], [0]])


weights = np.random.rand(2, 1)
bias = np.random.rand(1)


lr = 0.1


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


for epoch in range(0, 2000, 100):
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)

    
    loss = np.mean((y - y_pred) ** 2)

    
    d_pred = y_pred - y
    d_weights = np.dot(X.T, d_pred) / len(X)
    d_bias = np.mean(d_pred)

    
    weights -= lr * d_weights
    bias -= lr * d_bias

    print(f"Epoch {epoch}, Loss = {loss:.4f}")


print("\nPredictions:")
print(sigmoid(np.dot(X, weights) + bias))
