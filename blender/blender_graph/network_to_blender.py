# -*- coding:utf-8 -*-

import bpy,bmesh
from math import acos, degrees, pi
# from mathutils import Vector

import json
from random import choice

# 准备转成materials的colors的rgb值
colors = {"purple": (178, 132, 234), "gray": (11, 11, 11),
          "green": (114, 195, 0), "red": (255, 0, 75),
          "blue": (0, 131, 255), "clear": (0, 131, 255),
          "yellow": (255, 187, 0), "light_gray": (180, 180, 180)}

# 将颜色标准化为[0,1]之间，并且设定materials
for key, value in colors.items():
    value = [x / 255.0 for x in value]
    bpy.data.materials.new(name=key)
    bpy.data.materials[key].diffuse_color = value
    bpy.data.materials[key].specular_intensity = 0.5

    # 如果是这些颜色就不指定更多参数
    if key == "gray" or key == "light_gray":
        continue

    # 透明度参数
    bpy.data.materials[key].use_transparency = True
    bpy.data.materials[key].transparency_method = "RAYTRACE"
    bpy.data.materials[key].alpha = 0.1 if key == "clear" else 0.95
    bpy.data.materials[key].raytrace_transparency.fresnel = 0.1
    bpy.data.materials[key].raytrace_transparency.ior = 1.15


def draw_network(network):
    """ Takes assembled network/molecule data and draws to blender """

    # 增加原始网格
    bpy.ops.object.select_all(action='DESELECT')
    # bpy.ops.mesh.primitive_uv_sphere_add()
    # sphere = bpy.context.object
    # 以下设置圆柱体和圆锥体分别用来表示连接的边和箭头的，我们不需要箭头
    # bpy.ops.mesh.primitive_cylinder_add()
    # cylinder = bpy.context.object
    # cylinder.active_material = bpy.data.materials["light_gray"]
    # bpy.ops.mesh.primitive_cone_add()
    # cone = bpy.context.object
    # cone.active_material = bpy.data.materials["light_gray"]

    # 保存所有节点和边的引用
    shapes = []
    # 给要smoothed的形状保存单独的引用
    shapes_to_smooth = []

    # 生成结点
    for key, node in network["nodes"].items():

        # 结点的颜色设定
        col = node.get("color", choice(list(colors.keys())))

        # 复制原始网格并且生成新节点
        bpy.ops.mesh.primitive_uv_sphere_add()
        node_sphere = bpy.context.active_object
        node_sphere.name = key
        node_sphere.location = node["location"]
        # node_sphere.dimensions = [node_size] * 3
        node_sphere.active_material = bpy.data.materials[col]
        #bpy.context.scene.objects.link(node_sphere)
        shapes.append(node_sphere)
        shapes_to_smooth.append(node_sphere)

    # 生成边
    
    for edge in network["edges"]:

        # 通过遍历获取源和目标的位置
        source_name = edge["source"]
        target_name = edge["target"]
        bpy.context.scene.objects.active = bpy.data.objects[source_name]
        bpy.ops.object.mode_set(mode = 'EDIT')

        source_loc = network["nodes"][edge["source"]]["location"]
        target_loc = network["nodes"][edge["target"]]["location"]
        
        diff = [c1 - c2 for c2, c1 in zip(source_loc, target_loc)]

        obj = bpy.context.object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        vec_source = bm.verts.new([0,0,0])
        vec_target = bm.verts.new(diff)

        bm.edges.new((vec_source, vec_target))
        
        # bmesh.update_edit_mesh(bpy.context.object.data)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        # 设置父子关系
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[source_name]
        bpy.data.objects[target_name].select = True
        bpy.ops.object.parent_set()
        #bpy.data.objects[target_name].parent = bpy.data.objects[source_name]
        # cent = [(c2 + c1) / 2 for c2, c1 in zip(source_loc, target_loc)]
        # mag = sum([(c2 - c1) ** 2
        #           for c1, c2 in zip(source_loc, target_loc)]) ** 0.5

        # # 复制原始网格来创建边
        # edge_cylinder = cylinder.copy()
        # edge_cylinder.data = cylinder.data.copy()
        # edge_cylinder.dimensions = [edge_thickness] * 2 + [mag - node_size]
        # edge_cylinder.location = cent
        # edge_cylinder.rotation_mode = "AXIS_ANGLE"
        # edge_cylinder.rotation_axis_angle = [angle] + list(v_rot)
        # bpy.context.scene.objects.link(edge_cylinder)
        # shapes.append(edge_cylinder)
        # shapes_to_smooth.append(edge_cylinder)

        

    # 删除原始网格
    bpy.ops.object.select_all(action='DESELECT')
    # sphere.select = True
    # cylinder.select = True
    # cone.select = True

    # 删除启动时的小方块
    if "Cube" in bpy.data.objects.keys():
        bpy.data.objects.get("Cube").select = True
    bpy.ops.object.delete()

    # Smooth指定的形状
    for shape in shapes_to_smooth:
        shape.select = True
    bpy.context.scene.objects.active = shapes_to_smooth[0]
    bpy.ops.object.shade_smooth()

    # 我们不需要合并，通过设置父子关系来看
    # # 将生成的多个物体合并成一个，方便旋转等操作
    # for shape in shapes:
    #     shape.select = True
    # bpy.context.scene.objects.active = shapes[0]
    # bpy.ops.object.join()

    # 将整个物体居中对齐
    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="MEDIAN")

    # 刷新场景
    bpy.context.scene.update()

def draw_my_properties(self, context):
    scene = context.scene
    layout = self.layout

    col = layout.column(align = True)
    col.label("Process name:")
    col.prop(scene, "frame_start",text="default")
    col.separator()
    col.label("Process ID:")
    col.prop(scene, "frame_start",text="default")

def register():
    bpy.types.VIEW3D_PT_view3d_properties.prepend(draw_my_properties)

def unregister():
    bpy.types.VIEW3D_PT_view3d_properties.remove(draw_my_properties)

if __name__ == "__main__":
    with open("network.json") as network_file:
        network = json.load(network_file)
    draw_network(network)
    register()
