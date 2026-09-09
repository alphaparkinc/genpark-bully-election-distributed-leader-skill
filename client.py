class BullyElectionSystem:
    """Bully Leader Election Algorithm."""
    def __init__(self, node_ids: list[int]):
        self.node_ids = sorted(node_ids)
        self.failed_nodes = set()
        self.current_coordinator = max(self.node_ids) if self.node_ids else None

    def crash_node(self, node_id: int):
        self.failed_nodes.add(node_id)
        if self.current_coordinator == node_id:
            self.current_coordinator = None

    def recover_node(self, node_id: int):
        self.failed_nodes.discard(node_id)

    def trigger_election(self, initiator_id: int) -> dict:
        if initiator_id in self.failed_nodes:
            return {"error": "Initiator is crashed"}

        # Initiator sends ELECTION to all higher-ranked nodes
        higher_nodes = [nid for nid in self.node_ids if nid > initiator_id and nid not in self.failed_nodes]
        if not higher_nodes:
            # No higher alive node exists, initiator becomes coordinator
            self.current_coordinator = initiator_id
            return {
                "coordinator": initiator_id,
                "rounds": 1,
                "winner_is_initiator": True
            }

        # The highest alive node in the network will become coordinator
        alive_nodes = [nid for nid in self.node_ids if nid not in self.failed_nodes]
        self.current_coordinator = max(alive_nodes)

        return {
            "initiator": initiator_id,
            "coordinator": self.current_coordinator,
            "highest_alive_node": self.current_coordinator,
            "winner_is_initiator": (self.current_coordinator == initiator_id)
        }
