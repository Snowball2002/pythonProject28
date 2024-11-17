# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



api_key= 'PK6KYD7FSKKVCE10V1Y4'
secret_key='vyWmMTohB5cVuN3WYMRTcNSuth7oXhbdzkUJsp43'
import config
{"action": "authenticate", "data": {"key_id": "'PK6KYD7FSKKVCE10V1Y4", "secret_key":
    "vyWmMTohB5cVuN3WYMRTcNSuth7oXhbdzkUJsp43"}}

{"action": "listen", "data": {"streams": ["T.SPY"]}}
import json
import websocket
import config

def authenticate_and_listen(api_key, secret_key, symbol):
    socket = "wss://data.alpaca.markets/stream" #is it cause its not the https paper treadeing socket endpoint

    def on_open(ws):
        print("opened")
        auth_data = {
            "action": "authenticate",
            "data": {"key_id": config.api, "secret_key": config.secret_key}
        }

        ws.send(json.dumps(auth_data))
#json string
        listen_message = {"action": "listen", "data": {"streams": [f"AM.{symbol}"]}}

        ws.send(json.dumps(listen_message))

    def on_message(ws, message):
        print("received a message")
        print(message)

    def on_close(ws):
        print("closed connection")

    ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
    ws.run_forever()

if __name__ == '__main__':
    api_key = 'PK6KYD7FSKKVCE10V1Y4'
    secret_key = 'vyWmMTohB5cVuN3WYMRTcNSuth7oXhbdzkUJsp43'
    symbol = 'TSLA'

    authenticate_and_listen(api_key, secret_key, symbol)

    import json
    from websocket import create_connection

    ws = create_connection("wss://data.alpaca.markets/stream")
    ws.send(json.dumps({"action": "authenticate", "data": {"key_id": "'PK6KYD7FSKKVCE10V1Y4", "secret_key":
    "vyWmMTohB5cVuN3WYMRTcNSuth7oXhbdzkUJsp43"}}))
    result = ws.recv()
    print(result)
    ws.close()

