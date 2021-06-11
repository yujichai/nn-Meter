# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import os
import json
from nn_meter.utils.grapher_tool import Grapher
from nn_meter.kerneldetection.utils.ir_tools import convert_nodes


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_fusion_unit(name):
    filename = os.path.join(BASE_DIR, f"{name}_fusionunit.json")
    with open(filename, "r") as fp:
        graph = json.load(fp)

    if not isinstance(graph, list):
        graph = [graph]

    return [Grapher(graph=convert_nodes(g)) for g in graph]
