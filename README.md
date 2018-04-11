# WrapIt
Simple HTTP POST API wrapper for Python classes.

# Example:

```python
#!/usr/bin/env python

from wrapit.api_wrapper import create_app

# The class to be wrapped
class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

# Create an instance of the class
calculator = Calculator()

# Create an app by wrapping this instance
app = create_app(calculator)

# Main program
if __name__ == "__main__":
    # Start the app accepting connections from arbitraty hosts on a port
    app.run(host="0.0.0.0", port=5555)
```
