from enum import Enum

class Status(Enum):
    # General states
    READY = "Machine is ready to begin cycle."
    SET = "User has set chamfer mode."
    TRAY_FULL = "Part placed correctly. Loading tray is full."
    IN_USE = "Part placed correctly. Loading tray is not full."
    EMERGENCY = "Emergency stop is activated."
    FIXED = "Issue was addressed."
    PAUSE = "Pause is activated."

    # Warnings and errors for rolling
    EMPTY = "No ball seats in the machine"

    # Warnings and errors for vision system and pick and place
    IVALID_PART = "Warning: No part detected."
    INVALID_CHAMFER = "Warning: No chamfer detected."
    CAMERA_FATAL = "Error: Camera visualization malfunction."

    # Warnings and errors for orienting
    #Ian 's machine
    #Ball seats can get stuck
    #Ball seats are not introduced to it properly
    #Gustavo's machine is less likely to experience errors

