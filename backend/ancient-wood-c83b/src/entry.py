from workers import Response, WorkerEntrypoint
import json

# fake database to storage the latest event send by SNSA
latest_event = {}


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        global latest_event

        # extract the request into url, method and path
        url = request.url
        method = request.method
        path = url.split(".workers.dev")[-1]

        if path == "/event" and method == "POST":
            # expect the request body to be a json object and store it in the latest_event variable
            body = await request.json()
            latest_event = body

            # here the response confirming correct reception of the event is sent back to the client
            return Response(
                json.dumps({"success": True}),
                headers={"Content-Type": "application/json"},
            )
        if path == "/latest-event" and method == "GET":
            return Response(
                json.dumps(latest_event), headers={"Content-Type": "application/json"}
            )
        return Response("Not Found", status=404)
