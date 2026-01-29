import json
from pathlib import Path
from datetime import datetime
import uuid

class LongTermMemory:
    
    def __init__(self,store_path="modular_agent/memory/store.json"):
        self.store_path = Path(store_path)
        self._load()
    
    def _load(self):
        if not self.store_path.exists():
            self.memory={
                "user_profile":[],
                "user_preferences":[],
                "system_facts":[]
            }
            self._save()
        else:
            with open(self.store_path,"r") as f:
                self.memory = json.load(f)
    
    def _save(self):
        with open(self.store_path,"w") as f:
            json.dump(self.memory,f,indent=2)
    
    def store_fact(self,mem_type,key,value,confidence=0.8,source="explicit"):
        
        if mem_type not in self.memory:
            raise ValueError(f"Invalid memory type: {mem_type}")

        fact={
            "id":str(uuid.uuid4()),
            "type":mem_type,
            "key":key,
            "value":value,
            "confidence":confidence,
            "source":source,
            "timestamp":datetime.utcnow().isoformat()
            
        }
        self.memory[mem_type].append(fact)
        self._save()
    
    def retrieve_by_key(self,key,min_confidence=0.7):
        results=[]
        for records in self.memory.values():
            for record in records:
                if record["key"]==key and record["confidence"]>=min_confidence:
                    results.append(record)
        results.sort(key=lambda x: x["timestamp"],reverse=True)
                    
        return results
    
    def has_facts(self,key,min_confidence=0.7):
        return len(self.retrieve_by_key(key,min_confidence))>0
            
    def answer_from_memory(self, query: str):
        query = query.lower()

        # 1. NAME
        if "my name" in query or "who am i" in query:
            records = self.retrieve_by_key("name")
            if records:
                return f"Your name is {records[0]['value']}."

        # 2. LOCATION
        if "where do i live" in query or "where am i" in query or "my location" in query:
            records = self.retrieve_by_key("location")
            if records:
                return f"You live in {records[0]['value']}."

        # 3. JOB
        if "what do i do" in query or "my job" in query:
            records = self.retrieve_by_key("job")
            if records:
                return f"You work as a {records[0]['value']}."

        # 4. Preferences
        if "what do i like" in query:
            # For likes, we might want to list ALL of them, not just the last one
            records = self.retrieve_by_key("likes")
            if records:
                # Get unique likes
                unique_likes = set([r['value'] for r in records])
                likes_str = ", ".join(unique_likes)
                return f"You have mentioned that you like: {likes_str}."

        return None