# Publisher-Subscriber Notification System

## Overview

This project implements a basic Publisher-Subscriber Notification System using Flask.

## API Endpoints

1. **Subscribe**
   - **URL**: `/subscribe`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1",
         "subscriberId": "subscriber1"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Subscriber subscriber1 subscribed to topic topic1"
     }
     ```

2. **Notify**
   - **URL**: `/notify`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1"
     }
     ```
   - **Response**:
     ```json
     {
         "notifications": [
             "Notification sent to subscriber subscriber1 for topic topic1"
         ]
     }
     ```

3. **Unsubscribe**
   - **URL**: `/unsubscribe`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1",
         "subscriberId": "subscriber1"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Subscriber subscriber1 unsubscribed from topic topic1"
     }
     ```

## Postman Collection

The Postman collection can be found in the repository as `PubSubSystem.postman_collection.json`.

## Running Locally

To run the application locally:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python DEVDYNAMICSFLASK.py`
4. Access the endpoints at `http://localhost:5000`

## Output

1. Subscribe
![Alt Text](https://github.com/ShrutiGhodake/PubSubSystem/blob/main/subscribe.jpg)

2. Notify
![Alt Text](https://github.com/ShrutiGhodake/PubSubSystem/blob/main/Notify.jpg)

1. Unsubscribe
![Alt Text](https://github.com/ShrutiGhodake/PubSubSystem/blob/main/unsubscribe.jpg)

