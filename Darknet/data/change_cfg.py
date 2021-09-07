ori_cfg_file_url = "/home/yolo/project/train/src_repo/projects/cfg/yolov4-custom.cfg";
new_cfg_file_url = "/home/yolo/project/train/src_repo/projects/cfg/yolov4-custom_new.cfg";
anchor_file_url = "/home/yolo/project/train/src_repo/projects/anchors.txt";
ori_cfg_file = open(ori_cfg_file_url,"r");
new_cfg_file = open(new_cfg_file_url,"w");
anchor_file = open(anchor_file_url,"r");

anchor_info = anchor_file.read()

anchor_file.close()
for line in ori_cfg_file:
	new_cfg_file.seek(0,2)
	if line[0:7] != 'anchors':
		new_cfg_file.write(line)
	else:
		new_cfg_file.write("anchors = " + anchor_info + "\n")


ori_cfg_file.close()
new_cfg_file.close()

print("cfg is changed")
