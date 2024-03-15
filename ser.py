from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize global model parameters
global_weights = {'weights': [], 'biases': []}

@app.route('/update_model', methods=['POST'])
def update_model():
    global global_weights
    
    # Receive model parameters from client
    client_data = request.json
    client_weights = client_data['weights']
    client_biases = client_data['biases']
    
    # Aggregate model parameters
    aggregated_weights = aggregate_weights(global_weights['weights'], client_weights)
    aggregated_biases = aggregate_biases(global_weights['biases'], client_biases)
    
    # Update global model parameters
    global_weights['weights'] = aggregated_weights
    global_weights['biases'] = aggregated_biases
    
    # Send updated model parameters back to client
    return jsonify(global_weights)

def aggregate_weights(global_weights, client_weights):
    # Implement aggregation logic (e.g., averaging)
    # This is a simple averaging example
    aggregated_weights = [(gw + cw) / 2 for gw, cw in zip(global_weights, client_weights)]
    return aggregated_weights

def aggregate_biases(global_biases, client_biases):
    # Implement aggregation logic for biases
    # This is a simple averaging example
    aggregated_biases = [(gb + cb) / 2 for gb, cb in zip(global_biases, client_biases)]
    return aggregated_biases

if __name__ == '__main__':
    app.run(debug=True)  # You can set debug to False in production
