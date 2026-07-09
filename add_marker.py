bl_info = {
    "name": "Marker Creator",
    "author": "AI",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Add > Mesh > Marker",
    "description": "Add Marker",
    "category": "Mesh",
}

import bpy

class MESH_OT_create_marker(bpy.types.Operator):
    bl_idname = "mesh.create_marker"
    bl_label = "Marker"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cursor_loc = context.scene.cursor.location
        cursor_rot = context.scene.cursor.rotation_euler
        bpy.ops.mesh.primitive_cube_add(
            size=0.2, 
            enter_editmode=False, 
            align='CURSOR', 
            location=cursor_loc, 
            rotation=cursor_rot
        )    
        marker_obj = context.active_object
        marker_obj.name = "Marker"
        mat_name = "default"
        mat = bpy.data.materials.get(mat_name)        
        if mat is None:
            mat = bpy.data.materials.new(name=mat_name)
            mat.use_nodes = True            
        if marker_obj.data.materials:
            marker_obj.data.materials[0] = mat
        else:
            marker_obj.data.materials.append(mat)            
        return {'FINISHED'}
def menu_func(self, context):
    self.layout.operator(MESH_OT_create_marker.bl_idname, icon='MESH_CUBE')
def register():
    bpy.utils.register_class(MESH_OT_create_marker)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
def unregister():
    bpy.utils.unregister_class(MESH_OT_create_marker)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
if __name__ == "__main__":
    register()