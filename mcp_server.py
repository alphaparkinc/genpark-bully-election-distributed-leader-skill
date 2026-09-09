import sys
import json
from client import BullyElectionSystem

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "elect":
        sys_obj = BullyElectionSystem(params.get("nodes", [1, 2, 3, 4, 5]))
        for c in params.get("crashed", []):
            sys_obj.crash_node(c)
        return sys_obj.trigger_election(params.get("initiator", 1))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
