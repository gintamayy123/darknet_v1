python /home/yolo/project/train/src_repo/projects/data/gene_labels.py

/home/yolo/project/train/src_repo/projects/darknet detector calc_anchors /home/yolo/project/train/src_repo/projects/data/custom-data.data -num_of_clusters 9 -width 416 -height 416



python /home/yolo/project/train/src_repo/projects/data/change_cfg.py


/home/yolo/project/train/src_repo/projects/darknet detector train /home/yolo/project/train/src_repo/projects/data/custom-data.data /home/yolo/project/train/src_repo/projects/cfg/yolov4-custom_new.cfg /home/yolo/project/train/src_repo/projects/weights/yolov4.conv.137 -map





