from collections import deque

class ShortTermMemory:
    def __init__(self,max_turns=5):
        self.max_turns=max_turns
        self.memory = deque(maxlen=max_turns)
    
    def add(self,user,assistant):
        self.memory.append({
            "user":user,
            "assistant":assistant
        })
    
    def get_context(self):
        context = ""
        for turn in self.memory:
             context+=f"user: {turn['user']}\n"
             context+=f"assistant: {turn['assistant']}\n"
        return context.strip()
    
    def clear(self):
        self.memory.clear()