# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import argparse

hashType = "sha256"
myFile = ""

def hash(file, method):
	if not os.path.isdir(file):
		f = open(file, 'rb')
		sum = ""
		if method == "sha1":
			sum = hashlib.sha1(f.read()).hexdigest()
		elif method == "sha224":
			sum = hashlib.sha224(f.read()).hexdigest()
		elif method == "sha256":
			sum = hashlib.sha256(f.read()).hexdigest()
		elif method == "sha384":
			sum = hashlib.sha384(f.read()).hexdigest()
		elif method == "sha512":
			sum = hashlib.sha512(f.read()).hexdigest()
		elif method == "md5":
			sum = hashlib.md5(f.read()).hexdigest()
		f.close()
		return sum
	else:
		return "dir"

def findMyFile (path):
	myHash = hash(myFile, hashType)

	unsorted = os.listdir(path)
	filelist = sorted(unsorted, key=len)
	for file in filelist:
		sum = hash(path + "\\" + file, hashType)
		try:
			if sum != "dir":                                        # 非文件夹
				if myHash == sum:
					return path + "\\" + file
			else:                                                   # 如果到了这里说明非文件夹且指定文件不存在
				tmp = findMyFile(path + "\\" + file)
				if tmp != "":
					return tmp
		except Exception as e:
			print("Error displaying file name.")
		print("")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='you need to input hash type and directory path')
	parser.add_argument("--file", type = str, required = True, help = "your file path")
	parser.add_argument("--type", type = str, help = "hash type, like md5 sha256, default is sha256")
	parser.add_argument("--dir", type = str, required = True, help = "Directory path")                 #必要参数
	args = parser.parse_args()
	
	#
	# 参数解析和保存
	#
	if args.type != None:
		hashType = args.type
	myFile = args.file
	filePath = ""
	
	if os.path.exists(myFile):
		filePath = findMyFile(args.dir)
	else:
		print("input file not exists")
		exit()
	
	if filePath != "":
		print(filePath)
	else:
		print("Not find...")

