def load_kernel_context():
    return {
        "ethos": "truth_over_comfort",
        "authority": "aria_command_center",
        "stop_conditions": "always_leave_forward_path"
    }

def load_boot_context():
    return {
        "primary_goal": "bring_system_online",
        "mode": "operate",
        "priorities": ["responsiveness", "safety", "cost"],
        "scope": "system"
    }
