from jarvis.controller import handle_query
print("Welcome to Jarvis! Type your query below (type 'exit' to quit).")
while True:
    prompt = input("User: ")
    if prompt.lower() == "exit":
        break
    response = handle_query(prompt)
    print("Jarvis:", response)