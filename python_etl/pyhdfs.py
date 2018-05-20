#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class pyhdfs:

    def mkdir(self,dir_path):
        command = 'hdfs dfs -mkdir '+dir_path
        res= os.popen(command,'r')
        print (res)

    def put(self,file_path,dir_path):
        command = 'hdfs dfs -put ' + file_path + ' ' + dir_path
        res = os.popen(command,'r')
        print (res)

    def list(self,dir_path):
        command = 'hdfs dfs -ls ' + dir_path
        res = os.popen(command, 'r')
        result = res.read()
        for line in result.splitlines():
            print(line)

