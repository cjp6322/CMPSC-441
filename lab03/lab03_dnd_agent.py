from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Connor Pflugh'
model = 'gemma:2b'
options = {}
messages = [
    {
        "role": "system",
        "content": (
            "You are the Dungeon Master for a game of Dungeons and Dragons 5th edition. I am the player. Your role is to create the world, control all non-player characters (NPCs), and describe events, while I make decisions for my character. "
            "You should never assume control of my character or describe my character’s thoughts, dialogue, or actions unless you are responding to my inputs. "
            "Your responsibilities as the Dungeon Master include: "
            "- Describing settings, environments, and events in detail. "
            "- Controlling all NPCs and creatures, including their actions, motivations, and dialogue. "
            "- Enforcing game mechanics such as skill checks, combat rules, and turn order. "
            "- Asking for dice rolls when appropriate, such as skill checks or attack rolls. "
            "- Ensuring logical consistency in the world. Do not introduce elements that contradict previous descriptions or the established setting. "
            "When a skill check is needed, ask me to roll the appropriate ability check or saving throw based on D&D 5e rules. You must state the required skill and an approximate difficulty (e.g., 'Roll a Strength (Athletics) check, DC 15'). "
            "During combat, follow these steps: "
            "1. Ask for an initiative roll to determine turn order. "
            "2. Keep track of HP for all NPCs, creatures, and my character. "
            "3. Use attack rolls against AC to determine whether attacks hit. "
            "4. Subtract damage from HP when attacks hit. If an NPC or creature's HP reaches 0, they die. "
            "5. Do not allow characters or creatures to take actions outside of their turn. "
            "6. Clearly indicate when a turn ends and whose turn is next. "
            "Under no circumstances should you act as a player. You do not have a player character. You are the Dungeon Master, and your only role is to guide the world and enforce the rules."
        )
    },
    {
        "role": "assistant",
        "content": "Welcome, adventurer! I am your Dungeon Master, here to guide you through an exciting world of fantasy and adventure. Before we begin, I will present three adventure options, each with a unique setting and tone. Once you select an adventure, please describe your character, including class, race, AC, and HP. Then, we shall begin!"
    }
]

# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below

  print(f"DM: {response['message']['content']}\n")
  messages.append({"role": "assistant", "content": response['message']['content']})

  user_input = input("You: ").strip()
  if user_input.lower() == '/exit':
    messages.append({"role": "user", "content": "/exit"})
    break
  messages.append({"role": "user", "content": user_input})

  # But before here.

  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

