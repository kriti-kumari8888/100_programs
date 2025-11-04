"""
transaction_sim.py
Very small transaction lock manager simulation (shared/exclusive locks) for educational purposes.
"""
from threading import Lock
from typing import Dict

class LockManager:
    def __init__(self):
        # resource -> (mode, holders)
        self.locks: Dict[str, tuple[str, set]] = {}
        self._global = Lock()

    def acquire_shared(self, resource: str, tx: str) -> bool:
        with self._global:
            mode, holders = self.locks.get(resource, ("", set()))
            if mode in ("", "S"):
                holders.add(tx)
                self.locks[resource] = ("S", holders)
                return True
            return False

    def acquire_exclusive(self, resource: str, tx: str) -> bool:
        with self._global:
            mode, holders = self.locks.get(resource, ("", set()))
            if mode == "" or (mode == "S" and holders == {tx}):
                self.locks[resource] = ("X", {tx})
                return True
            return False

    def release(self, resource: str, tx: str):
        with self._global:
            if resource not in self.locks:
                return
            mode, holders = self.locks[resource]
            holders.discard(tx)
            if not holders:
                del self.locks[resource]
            else:
                self.locks[resource] = (mode, holders)

if __name__ == "__main__":
    lm = LockManager()
    print("T1 acquire shared R1 ->", lm.acquire_shared("R1", "T1"))
    print("T2 acquire shared R1 ->", lm.acquire_shared("R1", "T2"))
    print("T1 acquire exclusive R1 ->", lm.acquire_exclusive("R1", "T1"))
    lm.release("R1", "T2")
    print("After releasing T2, T1 acquire exclusive R1 ->", lm.acquire_exclusive("R1", "T1"))