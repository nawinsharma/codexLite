# codexLite - Your Intelligent Full-Stack Development Companion in the cli

codexLite is an intelligent, interactive development assistant that transforms your natural language requests into complete, production-ready applications. Whether you're building a simple todo app or a complex microservices architecture, codexLite guides you through every step of the development process with expert-level precision in the cli.

### ✨ Key Features

- **🤖 AI-Powered Development**: uses openai key for intelligent code generation and problem-solving
- **🏗️ Full-Stack Capabilities**: Build complete applications with frontend, backend, and database
- **🔄 Interactive Workflow**: Step-by-step planning, execution, and iteration
- **🛠️ Comprehensive Toolset**: File operations, server management, and system utilities
- **🧠 Smart Context Management**: Automatic conversation summarization for optimal performance


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Basic familiarity with terminal commands

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/codexLite.git
   cd codexLite
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

4. **Launch codexLite**
   ```bash
   python main.py
   ```

## 💬 How to Use

### Basic Commands

```bash
# Start codexLite
python main.py

# Available commands in the interactive session:
help          # Show example commands
quit/exit     # Exit the application
```

### Real Terminal Example

Here's exactly how codexLite works in practice:

```bash
$ python main.py

🚀 Enhanced Terminal Assistant Ready!
Available commands: build apps, modify code, manage servers, debug issues
Type 'help' for examples or 'quit' to exit

📬 User > create a basic todo app in html css and js with all crud functionality , make the ui beautiful
🔄 Summarizing context to improve performance...

🤖 Assistant: {"step": "plan", "content": "Creating a basic Todo app with HTML, CSS, and JavaScript that includes all CRUD (Create, Read, Update, Delete) functionalities. The UI will be designed to be visually appealing with modern styling techniques."}

🔠 PLAN: Creating a basic Todo app with HTML, CSS, and JavaScript that includes all CRUD (Create, Read, Update, Delete) functionalities. The UI will be designed to be visually appealing with modern styling techniques.

🤖 Assistant: {"step": "action", "tool": "create_folder", "input": "todo-app"}

⚙️ ACTION: create_folder → todo-app
📤 OUTPUT: Folder created: /home/nawin/mini-cursor/todo-app

🤖 Assistant: {"step": "action", "tool": "write_file", "input": {"path": "todo-app/index.html", "content": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Todo App</title>\n    <link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n    <div class=\"app-container\">\n        <h1>Todo List</h1>\n        <div class=\"input-container\">\n            <input type=\"text\" id=\"todo-input\" placeholder=\"Add a new task...\">\n            <button id=\"add-btn\">Add</button>\n        </div>\n        <ul id=\"todo-list\"></ul>\n    </div>\n    <script src=\"script.js\"></script>\n</body>\n</html>"}}

⚙️ ACTION: write_file → {'path': 'todo-app/index.html', 'content': '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Todo App</title>\n    <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n    <div class="app-container">\n        <h1>Todo List</h1>\n        <div class="input-container">\n            <input type="text" id="todo-input" placeholder="Add a new task...">\n            <button id="add-btn">Add</button>\n        </div>\n        <ul id="todo-list"></ul>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>'}
📤 OUTPUT: File written: /home/nawin/mini-cursor/todo-app/index.html

🤖 Assistant: {"step": "action", "tool": "write_file", "input": {"path": "todo-app/styles.css", "content": "body {\n    font-family: Arial, sans-serif;\n    background-color: #f4f4f9;\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n    margin: 0;\n}\n\n.app-container {\n    background-color: #fff;\n    padding: 20px;\n    border-radius: 8px;\n    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n    width: 300px;\n}\n\nh1 {\n    text-align: center;\n    color: #333;\n}\n\n.input-container {\n    display: flex;\n    margin-bottom: 20px;\n}\n\n#todo-input {\n    flex: 1;\n    padding: 10px;\n    border: 1px solid #ddd;\n    border-radius: 4px 0 0 4px;\n    outline: none;\n}\n\n#add-btn {\n    padding: 10px;\n    border: none;\n    background-color: #007bff;\n    color: white;\n    border-radius: 0 4px 4px 0;\n    cursor: pointer;\n}\n\n#add-btn:hover {\n    background-color: #0056b3;\n}\n\n#todo-list {\n    list-style-type: none;\n    padding: 0;\n}\n\n#todo-list li {\n    background-color: #f9f9f9;\n    padding: 10px;\n    margin-bottom: 10px;\n    border-radius: 4px;\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n}\n\n.todo-text {\n    flex: 1;\n}\n\n.todo-actions {\n    display: flex;\n    gap: 5px;\n}\n\n.todo-actions button {\n    border: none;\n    background-color: transparent;\n    cursor: pointer;\n    color: #007bff;\n}\n\n.todo-actions button:hover {\n    color: #0056b3;\n}"}}

⚙️ ACTION: write_file → {'path': 'todo-app/styles.css', 'content': 'body {\n    font-family: Arial, sans-serif;\n    background-color: #f4f4f9;\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n    margin: 0;\n}\n\n.app-container {\n    background-color: #fff;\n    padding: 20px;\n    border-radius: 8px;\n    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n    width: 300px;\n}\n\nh1 {\n    text-align: center;\n    color: #333;\n}\n\n.input-container {\n    display: flex;\n    margin-bottom: 20px;\n}\n\n#todo-input {\n    flex: 1;\n    padding: 10px;\n    border: 1px solid #ddd;\n    border-radius: 4px 0 0 4px;\n    outline: none;\n}\n\n#add-btn {\n    padding: 10px;\n    border: none;\n    background-color: #007bff;\n    color: white;\n    border-radius: 0 4px 4px 0;\n    cursor: pointer;\n}\n\n#add-btn:hover {\n    background-color: #0056b3;\n}\n\n#todo-list {\n    list-style-type: none;\n    padding: 0;\n}\n\n#todo-list li {\n    background-color: #f9f9f9;\n    padding: 10px;\n    margin-bottom: 10px;\n    border-radius: 4px;\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n}\n\n.todo-text {\n    flex: 1;\n}\n\n.todo-actions {\n    display: flex;\n    gap: 5px;\n}\n\n.todo-actions button {\n    border: none;\n    background-color: transparent;\n    cursor: pointer;\n    color: #007bff;\n}\n\n.todo-actions button:hover {\n    color: #0056b3;\n}'}
📤 OUTPUT: File written: /home/nawin/mini-cursor/todo-app/styles.css

🤖 Assistant: {"step": "action", "tool": "write_file", "input": {"path": "todo-app/script.js", "content": "document.addEventListener('DOMContentLoaded', () => {\n    const todoInput = document.getElementById('todo-input');\n    const addBtn = document.getElementById('add-btn');\n    const todoList = document.getElementById('todo-list');\n\n    addBtn.addEventListener('click', addTodo);\n\n    function addTodo() {\n        const todoText = todoInput.value.trim();\n        if (todoText === '') return;\n\n        const li = document.createElement('li');\n        const span = document.createElement('span');\n        span.className = 'todo-text';\n        span.textContent = todoText;\n\n        const actions = document.createElement('div');\n        actions.className = 'todo-actions';\n\n        const editBtn = document.createElement('button');\n        editBtn.textContent = 'Edit';\n        editBtn.addEventListener('click', () => editTodo(span));\n\n        const deleteBtn = document.createElement('button');\n        deleteBtn.textContent = 'Delete';\n        deleteBtn.addEventListener('click', () => deleteTodo(li));\n\n        actions.appendChild(editBtn);\n        actions.appendChild(deleteBtn);\n\n        li.appendChild(span);\n        li.appendChild(actions);\n        todoList.appendChild(li);\n\n        todoInput.value = '';\n    }\n\n    function editTodo(span) {\n        const newText = prompt('Edit your todo:', span.textContent);\n        if (newText !== null) {\n            span.textContent = newText.trim();\n        }\n    }\n\n    function deleteTodo(li) {\n        todoList.removeChild(li);\n    }\n});"}}

⚙️ ACTION: write_file → {'path': 'todo-app/script.js', 'content': "document.addEventListener('DOMContentLoaded', () => {\n    const todoInput = document.getElementById('todo-input');\n    const addBtn = document.getElementById('add-btn');\n    const todoList = document.getElementById('todo-list');\n\n    addBtn.addEventListener('click', addTodo);\n\n    function addTodo() {\n        const todoText = todoInput.value.trim();\n        if (todoText === '') return;\n\n        const li = document.createElement('li');\n        const span = document.createElement('span');\n        span.className = 'todo-text';\n        span.textContent = todoText;\n\n        const actions = document.createElement('div');\n        actions.className = 'todo-actions';\n\n        const editBtn = document.createElement('button');\n        editBtn.textContent = 'Edit';\n        editBtn.addEventListener('click', () => editTodo(span));\n\n        const deleteBtn = document.createElement('button');\n        deleteBtn.textContent = 'Delete';\n        deleteBtn.addEventListener('click', () => deleteTodo(li));\n\n        actions.appendChild(editBtn);\n        actions.appendChild(deleteBtn);\n\n        li.appendChild(span);\n        li.appendChild(actions);\n        todoList.appendChild(li);\n\n        todoInput.value = '';\n    }\n\n    function editTodo(span) {\n        const newText = prompt('Edit your todo:', span.textContent);\n        if (newText !== null) {\n            span.textContent = newText.trim();\n        }\n    }\n\n    function deleteTodo(li) {\n        todoList.removeChild(li);\n    }\n});"}
📤 OUTPUT: File written: /home/nawin/mini-cursor/todo-app/script.js

🤖 Assistant: {"step": "complete", "content": "The basic Todo app with CRUD functionality has been successfully created. The app includes a visually appealing UI with modern styling. You can open the `index.html` file in your browser to start using the app. The app allows you to add, edit, and delete tasks, providing a simple and effective task management solution."}

✅ COMPLETE: The basic Todo app with CRUD functionality has been successfully created. The app includes a visually appealing UI with modern styling. You can open the `index.html` file in your browser to start using the app. The app allows you to add, edit, and delete tasks, providing a simple and effective task management solution.
============================================================
🛠️ Continue development? (yes/no/status): 
```


## 🛠️ Available Tools

### Command Tools
- **`run_command(cmd)`** - Execute terminal commands with timeout protection
- **`run_server(cmd)`** - Start development servers in background
- **`stop_servers()`** - Gracefully terminate all running processes

### File Tools
- **`create_folder(path)`** - Create directory structures
- **`write_file({path, content})`** - Write files with automatic backup
- **`read_file(path)`** - Read and analyze file contents
- **`list_files(path)`** - Explore directory structures
- **`find_files(pattern)`** - Search for files by pattern

### System Tools
- **`get_current_directory()`** - Get current working directory
- **`check_port(port)`** - Verify port availability

## 🧠 Intelligent Features

### Context Management
- **Automatic Summarization**: Long conversations are intelligently summarized
- **Token Optimization**: Efficient use of API tokens for cost management
- **Conversation History**: Maintains context across development sessions

### Error Handling
- **Graceful Degradation**: Handles failures with helpful error messages
- **Timeout Protection**: Prevents hanging processes
- **Resource Cleanup**: Ensures proper cleanup of processes and files

### Development Workflow
- **Planning Phase**: Comprehensive analysis and strategy development
- **Execution Phase**: Step-by-step implementation with real-time feedback
- **Observation Phase**: Result analysis and strategy adaptation
- **Iteration Phase**: Continuous improvement based on outcomes

## 🔧 Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
OPENAI_MODEL=gpt-4o                    # Default: gpt-4o
OPENAI_TEMPERATURE=0.3                 # Default: 0.3
OPENAI_MAX_TOKENS=2000                 # Default: 2000
```

### Customization
- **System Prompts**: Modify `prompts.py` to customize AI behavior
- **Tool Extensions**: Add new tools in the `tools/` directory
- **Context Management**: Adjust summarization thresholds in `context_manager.py`
