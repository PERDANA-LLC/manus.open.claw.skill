---
name: oc-canvas
description: >
  Display local HTML content in a web browser. Use this skill to render generated
  HTML files, create interactive web-based demos, or present data visualizations.

---

## When to Use

Use this skill when you need to display HTML content that you have generated or have stored locally in the sandbox. It is particularly useful for:

-   Presenting reports or documents formatted in HTML.
-   Running interactive applications or games built with HTML, CSS, and JavaScript.
-   Displaying dashboards or data visualizations created with libraries like Chart.js or D3.js.

## When NOT to Use

-   Do not use this skill for accessing public websites; use the `browser` tool directly for that purpose.
-   This skill is for viewing content, not for web development. For building websites, use the appropriate web development skills and tools.

## Workflow

The general workflow involves serving your HTML files with a local web server and then using the `browser` tool to view them.

### 1. Create a Project Directory

It is best practice to keep your HTML files organized in a dedicated directory. You can create one using the `shell` tool.

```bash
mkdir -p /home/ubuntu/my-canvas-project
```

### 2. Place Your HTML Files

Ensure your HTML, CSS, and JavaScript files are located within the project directory you created. You can use the `file` tool to write your content.

```python
default_api.file(
    action="write",
    path="/home/ubuntu/my-canvas-project/index.html",
    text="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Canvas Test</title>
</head>
<body>
    <h1>Hello from the Canvas!</h1>
</body>
</html>"""
)
```

### 3. Start a Local Web Server

To view your HTML files, you need to serve them using a local HTTP server. The simplest way to do this is with Python's built-in `http.server` module. Run the server in the background from your project directory.

```bash
cd /home/ubuntu/my-canvas-project && python3.11 -m http.server 8000 &
```

This command starts a web server on port 8000, serving files from the `/home/ubuntu/my-canvas-project` directory. The `&` at the end runs the process in the background.

### 4. View in Browser

Once the server is running, you can use the `browser` tool to open and display your HTML file. The URL will be `http://localhost:8000` followed by the name of your file.

```python
default_api.browser(
    url="http://localhost:8000/index.html",
    intent="informational",
    focus="Displaying the test HTML page."
)
```

### 5. Clean Up (Optional)

When you are finished, you can stop the background web server process. First, find its Process ID (PID) and then use the `kill` command.

```bash
# Find the PID of the Python HTTP server
pgrep -f "python3.11 -m http.server"

# Kill the process using its PID (replace 12345 with the actual PID)
kill 12345
```
