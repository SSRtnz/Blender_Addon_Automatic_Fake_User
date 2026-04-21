bl_info = {
    "name": "[Project Resistance] Lets Turn On Auto Fake User",
    "author": "Theiyn tnz",
    "version": (1, 0 ,0),
    "blender": (3, 0, 0),
    "location": "Below this message(Only Enable / Disable)",
    "description": "Automatically enables Fake User for all data blocks",
    "category": "System" ,
    "warning" : "First Public Version. Some function maybe has bug" ,
    "doc_url": "https://github.com/SSRtnz/Blender_Addon_Automatic_Fake_User/blob/main/%5BPDF%5DLets%20turn%20on%20auto%20Fake%20User%20manual.pdf" ,
    "tracker_url": "https://www.facebook.com/profile.php?id=61577688574948" ,
    "support" : "TESTING" ,
}

import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty

# --- 1. Setting Part (Preferences) ---
class AutoFakeUserPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    # Make button for enable
    
    use_actions: BoolProperty(name = "Actions (Animation)", default = True) #1
    use_armatures: BoolProperty(name = "Armatures", default = True) #2
    use_brushes : BoolProperty(name = "Brushes", default = True) #3
    use_cameras : BoolProperty(name = "Cameras", default = True) #4
    use_curves : BoolProperty(name = "Curves", default = True) #5
    use_images: BoolProperty(name = "Images", default = True) #6
    use_lights : BoolProperty(name = "Lights", default = True) #7
    use_materials: BoolProperty(name = "Materials", default = True) #8
    use_meshes: BoolProperty(name = "Meshes", default = True) #9
    use_node_groups: BoolProperty(name = "Node Groups", default = True) #10
    use_particles : BoolProperty(name = "Particles", default = True) #11
    use_texts : BoolProperty(name = "Texts", default = True) #12
    use_textures : BoolProperty(name = "Textures", default = True) #13
    use_worlds : BoolProperty(name = "Worlds", default = True) # 14

    def draw(self, context):
        layout = self.layout
        layout.label(text="Enable Auto Fake User for:")
        column = layout.column_flow(columns=2)
        column.prop(self, "use_actions") #1
        column.prop(self, "use_armatures") #2
        column.prop(self, "use_brushes") #3
        column.prop(self, "use_cameras") #4
        column.prop(self, "use_curves") #5
        column.prop(self, "use_images") #6
        column.prop(self, "use_lights") #7
        column.prop(self, "use_materials")#8
        column.prop(self, "use_meshes") #9
        column.prop(self, "use_node_groups") #10
        column.prop(self, "use_particles") #11
        column.prop(self, "use_texts") #12
        column.prop(self, "use_textures") #13
        column.prop(self, "use_worlds") #14

# -----------------------------

# --- 2. Main system ---
@persistent
def auto_set_fake_user(scene):
    # Use variable in Preferences button for use function
    prefs = bpy.context.preferences.addons[__name__].preferences
    
    # match `UI` and `Data` on Blender
    mapping = [
        (prefs.use_actions, bpy.data.actions), #1 -
        (prefs.use_armatures, bpy.data.armatures), #2
        (prefs.use_brushes, bpy.data.brushes), #3
        (prefs.use_cameras, bpy.data.cameras), #4
        (prefs.use_curves, bpy.data.curves), #5 -
        (prefs.use_images, bpy.data.images), #6
        (prefs.use_lights, bpy.data.lights), #7
        (prefs.use_materials, bpy.data.materials), #8
        (prefs.use_meshes, bpy.data.meshes), #9
        (prefs.use_node_groups, bpy.data.node_groups), #10 -
        (prefs.use_particles, bpy.data.particles), #11
        (prefs.use_texts, bpy.data.texts), #12
        (prefs.use_textures, bpy.data.textures), #13
        (prefs.use_worlds, bpy.data.worlds) #14
    ]
    
    for should_run, collection in mapping:
        if should_run:
            for item in collection:
                if hasattr(item, "use_fake_user") and not item.use_fake_user:
                    item.use_fake_user = True

# -----------------------------

def register():
    # Add function to Event when update anything in Scene (Make or Copy)
    bpy.utils.register_class(AutoFakeUserPreferences)
    if auto_set_fake_user not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(auto_set_fake_user)

def unregister():
    # Delete this function in Event
    bpy.utils.unregister_class(AutoFakeUserPreferences)
    if auto_set_fake_user in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(auto_set_fake_user)

if __name__ == "__main__":
    register()