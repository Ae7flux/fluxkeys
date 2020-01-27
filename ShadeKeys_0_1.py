bl_info = {
    "name" : "Shading type keys",
    "description" : "Allows assigng shading types to individual keys",
    "author" : "Francis Boyle",
    "blender" : (2, 80,1),
    "location" : "Properties > Utilities > Shading Type Keys",
    "versoin" : (0,1),
    "category" : "Utilities"
    }
    
import bpy


class Set_Wireframe(bpy.types.Operator):
    """Sets wireframe mode"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "scene.setwireframe"        # Unique identifier for buttons and menu items to reference.
    bl_label = "set wireframe mode"         # Display name in the interface.
    total: bpy.props.IntProperty(name="Total", default=4)  

    def execute(self, context):        # execute() is called when running the operator.

        for area in bpy.context.screen.areas: 
            if area.type == 'VIEW_3D':
                space = area.spaces.active
                space.shading.type = 'WIREFRAME' 

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.
        
class Set_Material(bpy.types.Operator):
    """Sets material mode"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "scene.setmaterial"        # Unique identifier for buttons and menu items to reference.
    bl_label = "set material mode"         # Display name in the interface.
    total: bpy.props.IntProperty(name="Total", default=4)  



    def execute(self, context):        # execute() is called when running the operator.

        for area in bpy.context.screen.areas: 
            if area.type == 'VIEW_3D':
                space = area.spaces.active
                space.shading.type = 'MATERIAL' 

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.        
        
        
class Set_Rendered(bpy.types.Operator):
    """Sets rendered mode"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "scene.rendered"        # Unique identifier for buttons and menu items to reference.
    bl_label = "set rendered mode"         # Display name in the interface.
    total: bpy.props.IntProperty(name="Total", default=4)  

    def execute(self, context):        # execute() is called when running the operator.

        for area in bpy.context.screen.areas: 
            if area.type == 'VIEW_3D':
                space = area.spaces.active
                space.shading.type = 'RENDERED' 

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.    
    
def menu_func(self, context):
    self.layout.operator(SetWireframe.bl_idname)    
    self.layout.operator(SetMaterial.bl_idname)     
    self.layout.operator(SetRendered.bl_idname)   
        
addon_keymaps = []        
 
def register():

    bpy.utils.register_class(SetWireframe)
    
  
    bpy.utils.register_class(SetMaterial)    
    bpy.utils.register_class(SetRendered)   
 

    

    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type='VIEW_3D', region_type='WINDOW')
        kmi = km.keymap_items.new(SetWireframe.bl_idname, 'W', 'PRESS' , ctrl=True, shift=True, alt=True)
        kmi.properties.total = 5
        addon_keymaps.append((km, kmi))
        
        km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type='VIEW_3D', region_type='WINDOW')
        kmi = km.keymap_items.new(SetMaterial.bl_idname, 'M', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi.properties.total = 5
        addon_keymaps.append((km, kmi)) 
               
        km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type='VIEW_3D', region_type='WINDOW')
        kmi = km.keymap_items.new(SetRendered.bl_idname, 'R', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi.properties.total = 5
        addon_keymaps.append((km, kmi))                
 

def unregister():

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    


    bpy.utils.unregister_class(SetRendered)   
    bpy.utils.unregister_class(SetMaterial)
    bpy.utils.unregister_class(SetWireframe)    
    
    bpy.types.VIEW3D_MT_object.remove(menu_func)

    
if __name__ == "__main__":
    register()
    
    
    
    
    
   

