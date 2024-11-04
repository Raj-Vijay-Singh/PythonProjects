dict1 = {"emp":
             {"details":
                  {"age": 50,
                   "gender": "Male"},
              "dept": "Psychology",
              "scores":
                  {"Testing": 50,
                   "Practical": 80}
              }
         }

print(f"Value of the key 'Practical' in the dictionary: {dict1["emp"]["scores"]["Practical"]}")
