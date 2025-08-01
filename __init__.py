"""
@author: Dr.Lt.Data
@title: Inspire Pack
@nickname: Inspire Pack
@description: This extension provides various nodes to support Lora Block Weight, Regional Nodes, Backend Cache, Prompt Utils, List Utils and the Impact Pack.
"""

import importlib
import logging

version_code = [1, 20]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
logging.info(f"### Loading: ComfyUI-Inspire-Pack ({version_str})")

node_list = [
    "lora_block_weight",
    "segs_support",
    "a1111_compat",
    "prompt_support",
    "inspire_server",
    "image_util",
    "regional_nodes",
    "sampler_nodes",
    "backend_support",
    "list_nodes",
    "conditioning_nodes",
    "model_nodes",
    "util_nodes"
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    imported_module = importlib.import_module(".inspire.{}".format(module_name), __name__)

    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
