# -*- coding: utf-8 -*-

import os,sys

print os.path.abspath('.')
print sys.path[0]

json_path = os.path.join(sys.path[0], 'json')

print json_path

# 一种输出当前目录下所有文件的方法
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件

json_files = os.listdir(json_path)

json_files_num = len(json_files)

# i = 1

# diff_path = os.path.join(json_path, 'diff'+str(i)+'.json' )

# print diff_path

count = 0

def add():
    global count
    count += 1
    diff_path = os.path.join(json_path, 'diff'+str(count)+'.json' )

    return diff_path

print add()

nodes = [
    {
        "group": 1,
        "name": "1492:imjpmig.exe"
    },
    {
        "group": 2,
        "name": "1491:iasdfmig.exe"
    },
     {
        "group": 1,
        "name": "1492:imjpmig.exe"
    },
    {
        "group": 2,
        "name": "1492:iasdfmig.exe"
    },
    {
        "group": 1,
        "name": "1492:imjpmig.exe"
    }
]

res = {
    "links": [
        {
            "source": "492:winlogon.exe",
            "target_group": 1,
            "target": "548:lsass.exe",
            "source_group": 1
        },
        {
            "source": "492:winlogon.exe",
            "target_group": 2,
            "target": "536:services.exe",
            "source_group": 1
        },
        {
            "source": "1204:explorer.exe",
            "target_group": 1,
            "target": "1492:imjpmig.exe",
            "source_group": 1
        },
        {
            "source": "1492:imjpmig.exe",
            "target_group": 6,
            "target": "1492:privileges",
            "source_group": 1
        }]
}

diff = {
    "links_add": [
        {
            "source": "rachel.amber",
            "target_group": 1,
            "target": "chole.price",
            "source_group": 1
        }
    ],
    "nodes_remove": [
        {
            "group": 1,
            "name": "1492:imjpmig.exe"
        },
        {
            "group": 6,
            "name": "1492:privileges"
        }],
        "nodes_add": [
            {
                "group": 1,
                "name": "1492:chloe.price"
            },
            {
                "group": 2,
                "name": "1492:max.coffeild"
            }
        ],
        "links_remove": [
        {
            "source": "1204:explorer.exe",
            "target_group": 1,
            "target": "1492:imjpmig.exe",
            "source_group": 1
        },
        {
            "source": "1492:imjpmig.exe",
            "target_group": 6,
            "target": "1492:privileges",
            "source_group": 1
        }]   
}
def rm_nodes():
    global nodes
    if diff['nodes_remove'] != []:
        lnr = len(diff['nodes_remove'])
        for i in range(0, lnr):
            for node in nodes:
                if node['name'] == diff['nodes_remove'][i]['name']:
                    nodes.remove(node)

def add_nodes():
    global nodes
    if diff['nodes_add'] != []:
        lna = len(diff['nodes_add'])
        for i in range(0, lna):
            nodes.append(diff['nodes_add'][i])
    # nodes = sorted(nodes, key = lambda node: node['group'])
        nodes.sort(key = lambda node: node['group'])
rm_nodes()
print nodes
add_nodes()
print nodes

def remove_res():
    global res
    if diff['links_remove'] != []:
        llr = len(diff['links_remove'])
        for i in range(0, llr):
            for link in res['links']:
                if link['source'] == diff['links_remove'][i]['source'] and \
                    link['target'] == diff['links_remove'][i]['target'] and \
                    link['source_group'] == diff['links_remove'][i]['source_group'] and \
                    link['target_group'] == diff['links_remove'][i]['target_group']:
                    res['links'].remove(link)

remove_res()
print res

def add_res():
    global res
    if diff['links_add'] != []:
        for newLink in diff['links_add']:
            res['links'].append(newLink)
    res['links'].sort(key = lambda link: link['target_group'])

add_res()
print res

c = []

def pr():
    print 'this is pr'
    for i in range(0,9):
        c.append(i)

def an():
    global c
    pr()
    print c

an()

