from workers import Response, WorkerEntrypoint
from urllib.parse import urlparse
import json

# fake database to storage the latest event send by SNSA
latest_event = {}


# helper function for json response
def json_response(data, status=200):
    return Response(
        json.dumps(data),
        status=status,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        global latest_event

        # extract the request into url, method and path
        url = request.url
        method = request.method
        path = urlparse(url).path

        # Handle CORS preflight
        if method == "OPTIONS":
            return Response(
                "",
                status=204,
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type",
                },
            )

        if path == "/event" and method == "POST":
            # expect the request body to be a json object and store it in the latest_event variable
            body = await request.json()
            latest_event = body

            # here the response confirming correct reception of the event is sent back to the client
            return json_response(
                {"success": True, "message": "Event received successfully"}
            )
        if path == "/latest-event" and method == "GET":
            return json_response(latest_event)
        return Response("Not Found", status=404)
