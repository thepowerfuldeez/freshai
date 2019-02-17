# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Centralized catalog of paths."""

import os


class DatasetCatalog(object):
    DATA_DIR = "/home/georgiy/workspace/freshai/data"
    DATASETS = {
        "food_train": {
            "img_dir": "coco/images/train2017",
            "ann_file": "coco/annotations/filtered_instances_train2017.json"
        },
        "food_val": {
            "img_dir": "coco/images/val2017",
            "ann_file": "coco/annotations/filtered_instances_val2017.json"
        }
    }

    @staticmethod
    def get(name):
        if "food" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs["img_dir"]),
                ann_file=os.path.join(data_dir, attrs["ann_file"]),
            )
            return dict(
                factory="FoodDataset",
                args=args,
            )
        raise RuntimeError("Dataset not available: {}".format(name))


class ModelCatalog(object):
    C2_IMAGENET_MODELS = {
        "R-50": "/home/georgiy/workspace/freshai/models/mask_rcnn_R-50-FPN_1x_detectron_no_last_layers.pth"
    }

    @staticmethod
    def get(name):
        if name == "R-50":
            return ModelCatalog.C2_IMAGENET_MODELS[name]
        raise RuntimeError("model not present in the catalog {}".format(name))
