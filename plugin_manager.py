import os
import importlib

PLUGINS_DIR = "plugins"

def create_plugins_directory():
    """Create the plugins directory if it doesn't exist."""
    if not os.path.exists(PLUGINS_DIR):
        os.makedirs(PLUGINS_DIR)
        print("Plugins directory created.")

def create_plugin(name):
    """Create a new plugin with the given name."""
    sample_code = f"""\
def run():
    print("Hello from the {name} plugin!")
"""
    with open(os.path.join(PLUGINS_DIR, f"{name}.py"), "w") as f:
        f.write(sample_code)
    print(f"Plugin '{name}' created. Edit it to add your functionality.")

def delete_plugin(name):
    """Delete a plugin with the given name."""
    try:
        os.remove(os.path.join(PLUGINS_DIR, f"{name}.py"))
        print(f"Plugin '{name}' deleted.")
    except FileNotFoundError:
        print(f"Plugin '{name}' not found.")

def list_plugins():
    """List all plugins in the plugins directory."""
    plugins = [f[:-3] for f in os.listdir(PLUGINS_DIR) if f.endswith(".py")]
    print("Available plugins:", plugins)
    return plugins

def load_plugins(load_order=None, omit_files=None):
    """Load plugins based on specified load order and omitted files."""
    plugins = []
    for filename in os.listdir(PLUGINS_DIR):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            if omit_files and module_name in omit_files:
                continue
            try:
                module = importlib.import_module(f"{PLUGINS_DIR.replace('/', '.')}.{module_name}")
                plugins.append(module)
                print(f"Loaded plugin: {module_name}")
            except Exception as e:
                print(f"Failed to load plugin {module_name}: {e}")

    # Sort plugins if a load order is specified
    if load_order:
        plugins.sort(key=lambda x: load_order.index(x.__name__) if x.__name__ in load_order else len(load_order))
    return plugins

def run_plugins(plugins, function_name="run"):
    """Run a specified function from each loaded plugin."""
    for plugin in plugins:
        if hasattr(plugin, function_name):
            func = getattr(plugin, function_name)
            func()
        else:
            print(f"Plugin '{plugin.__name__}' does not have a function '{function_name}'.")

def main():
    create_plugins_directory()
    while True:
        print("\nPlugin Manager")
        print("1. Create Plugin")
        print("2. Delete Plugin")
        print("3. List Plugins")
        print("4. Load and Run Plugins")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter the plugin name: ")
            create_plugin(name)
        elif choice == "2":
            name = input("Enter the plugin name to delete: ")
            delete_plugin(name)
        elif choice == "3":
            list_plugins()
        elif choice == "4":
            load_order_input = input("Enter a comma-separated list of plugins to load in order (leave empty for default): ")
            load_order = load_order_input.split(",") if load_order_input else None
            omit_files_input = input("Enter a comma-separated list of plugins to omit (leave empty for none): ")
            omit_files = omit_files_input.split(",") if omit_files_input else None
            plugins = load_plugins(load_order=load_order, omit_files=omit_files)
            run_plugins(plugins)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
