import signal
import json
import time
from dotenv import load_dotenv
from openai import OpenAI

from tools import (
    run_command, create_folder, write_file, read_file, list_files,
    run_server, stop_servers, get_current_directory, find_files, check_port
)
from context_manager import should_summarize_context, summarize_context
from prompts import SYSTEM_PROMPT

load_dotenv()
client = OpenAI()

def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    print("\n🚀 Enhanced Terminal Assistant Ready!")
    print("Available commands: build apps, modify code, manage servers, debug issues")
    print("Type 'help' for examples or 'quit' to exit")

    def signal_handler(sig, frame):
        print("\n🛑 Shutting down gracefully...")
        stop_servers()
        exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            user_input = input("\n📬 User > ").strip()
            
            if user_input.lower() in ["exit", "quit"]:
                stop_servers()
                print("👋 Goodbye!")
                break
            
            if user_input.lower() == "help":
                print("""
🔧 **EXAMPLE COMMANDS:**
• "Create a React todo app"
• "Add authentication to my Express server"  
• "Build a dashboard with charts"
• "Fix my server that won't start"
• "Add a new feature to my existing app"
• "Show me the current project structure"
                """)
                continue

            # Check if context should be summarized
            if should_summarize_context(messages):
                print("🔄 Summarizing context to improve performance...")
                messages = summarize_context(messages)

            messages.append({"role": "user", "content": user_input})

            while True:
                for attempt in range(3):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            response_format={"type": "json_object"},
                            messages=messages,
                            temperature=0.3,
                            max_tokens=2000
                        )
                        reply = response.choices[0].message.content
                        parsed = json.loads(reply)
                        break
                    except json.JSONDecodeError as e:
                        print(f"⚠️ JSON parsing error (attempt {attempt + 1}): {e}")
                        if attempt == 2:
                            print("❌ Failed to get valid JSON after 3 attempts")
                            break
                        time.sleep(1)
                    except Exception as e:
                        print(f"⚠️ API error (attempt {attempt + 1}): {e}")
                        if attempt == 2:
                            print("❌ Failed to get response after 3 attempts")
                            break
                        time.sleep(2)
                else:
                    break

                print(f"\n🤖 Assistant: {reply}")
                messages.append({"role": "assistant", "content": reply})

                step = parsed.get("step")

                if step == "plan":
                    print(f"🔠 PLAN: {parsed['content']}")
                    continue

                elif step == "action":
                    tool_name = parsed.get("tool")
                    tool_input = parsed.get("input")
                    print(f"⚙️ ACTION: {tool_name} → {tool_input}")
                    
                    # Map tool names to functions
                    available_tools = {
                        "run_command": run_command,
                        "create_folder": create_folder,
                        "write_file": write_file,
                        "read_file": read_file,
                        "list_files": list_files,
                        "run_server": run_server,
                        "stop_servers": stop_servers,
                        "get_current_directory": get_current_directory,
                        "find_files": find_files,
                        "check_port": check_port,
                    }
                    
                    if tool_name not in available_tools:
                        print(f"❌ Unknown tool: {tool_name}")
                        break

                    result = available_tools[tool_name](tool_input)
                    print(f"📤 OUTPUT: {result}")
                    
                    messages.append({
                        "role": "user",
                        "content": json.dumps({
                            "step": "tool_output",
                            "tool": tool_name,
                            "input": tool_input,
                            "output": result
                        })
                    })
                    continue

                elif step == "observe":
                    print(f"👁️ OBSERVE: {parsed['content']}")
                    continue

                elif step == "complete":
                    print(f"✅ COMPLETE: {parsed['content']}")
                    print("=" * 60)

                    while True:
                        follow_up = input("🛠️ Continue development? (yes/no/status): ").strip().lower()
                        if follow_up in ["no", "n", "done", "finished", "exit"]:
                            print("🎉 Project finalized.")
                            return
                        elif follow_up in ["yes", "y", "sure", "okay", "ok"]:
                            next_change = input("📬 What would you like to add/modify? > ").strip()
                            messages.append({"role": "user", "content": next_change})
                            break
                        elif follow_up == "status":
                            print(f"📁 Current directory: {get_current_directory()}")
                            # Note: We can't directly access running_processes from here
                            # but the stop_servers function handles the process management
                            continue
                        else:
                            print("❓ Please answer 'yes', 'no', or 'status'.")
                    break

                else:
                    print(f"❓ Unknown step: {step}")
                    break

        except KeyboardInterrupt:
            print("\n🛑 Interrupted. Stopping servers...")
            stop_servers()
            break
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            continue

if __name__ == "__main__":
    main()