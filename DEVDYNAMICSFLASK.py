from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to hold topics and their subscribers
topics = {}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    topicId = data.get('topicId')
    subscriberId = data.get('subscriberId')
    
    if not topicId or not subscriberId:
        return jsonify({"error": "Missing topicId or subscriberId"}), 400
    
    if topicId not in topics:
        topics[topicId] = set()
    
    topics[topicId].add(subscriberId)
    return jsonify({"message": f"Subscriber {subscriberId} subscribed to topic {topicId}"}), 200

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    topicId = data.get('topicId')
    
    if not topicId:
        return jsonify({"error": "Missing topicId"}), 400
    
    if topicId not in topics:
        return jsonify({"message": f"Topic {topicId} does not exist"}), 200
    
    subscribers = topics[topicId]
    notifications = [f"Notification sent to subscriber {subscriber} for topic {topicId}" for subscriber in subscribers]
    return jsonify({"notifications": notifications}), 200

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    topicId = data.get('topicId')
    subscriberId = data.get('subscriberId')
    
    if not topicId or not subscriberId:
        return jsonify({"error": "Missing topicId or subscriberId"}), 400
    
    if topicId not in topics or subscriberId not in topics[topicId]:
        return jsonify({"message": f"Subscriber {subscriberId} is not subscribed to topic {topicId}"}), 200
    
    topics[topicId].remove(subscriberId)
    return jsonify({"message": f"Subscriber {subscriberId} unsubscribed from topic {topicId}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
