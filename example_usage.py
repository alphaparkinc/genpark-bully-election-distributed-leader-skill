from client import BullyElectionSystem

def main():
    print("=== Bully Distributed Leader Election ===")
    system = BullyElectionSystem([1, 2, 3, 4, 5])
    assert system.current_coordinator == 5

    # Coordinator 5 crashes
    system.crash_node(5)
    print("Node 5 crashed.")

    # Node 2 detects failure and triggers election
    res = system.trigger_election(initiator_id=2)
    print("Election Result:", res)
    assert res["coordinator"] == 4

    print("Bully Election System verified successfully!")

if __name__ == "__main__":
    main()
