from jarvis.memory.long_term import LongTermMemory

memory = LongTermMemory()

memory.store_fact(
    mem_type="user_profile",
    key="name",
    value="Utsav",
    confidence=0.95
)

print(memory.retrieve_by_key("name"))
