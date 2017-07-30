import bpy

from .operators.align_camera import AlignCamera
from .operators.audio_to_vse import AudioToVSE
from .operators.generate_visualizer import GenerateVisualizer
from .operators.remove_bz_audio import RemoveBZAudio

bl_info = {
    "name": "Bizualizer",
    "description": "Create a simple visualizer for audio",
    "author": "doakey3",
    "version": (1, 2, 0),
    "blender": (2, 7, 8),
    "wiki_url": "https://github.com/doakey3/Bizualizer",
    "tracker_url": "https://github.com/doakey3/Bizualizer/issues",
    "category": "Animation",
    "location": "Properties > Scene"}


class BizualizerUI(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Bizualizer"
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        row = layout.row()
        row.prop(scene, "bz_audiofile", icon="SOUND")
        row = layout.row()
        row.prop(scene, "bz_audio_channel")
        row = layout.row()
        row.operator("sequencerextra.bz_audio_to_sequencer",
                     icon="SEQ_SEQUENCER")
        row.operator("sequencerextra.bz_audio_remove", icon="CANCEL")
        row = layout.row()
        row.prop(scene, "bz_bar_count")
        row.prop(scene, "bz_bar_width")
        row = layout.row()
        row.prop(scene, "bz_amplitude")
        row.prop(scene, "bz_spacing")
        row = layout.row()
        split = row.split()
        col_a = split.column(align=True)
        col_a.prop(scene, "bz_use_radial")
        col_b = split.column(align=True)
        col_b.prop(scene, "bz_radius")
        if scene.bz_use_radial:
            col_b.enabled = True
        else:
            col_b.enabled = False
        row = layout.row()
        row.operator("object.bz_generate", icon="RADIO")
        row = layout.row()
        row.operator("object.bz_align_camera", icon="CAMERA_DATA")


def initprop():
    bpy.types.Scene.bz_audiofile = bpy.props.StringProperty(
        description="Define path of the audio file",
        subtype="FILE_PATH",
        )

    bpy.types.Scene.bz_audio_channel = bpy.props.IntProperty(
        name="Audio Channel",
        description="Channel where audio will be added",
        default=1,
        min=1
        )

    bpy.types.Scene.bz_bar_count = bpy.props.IntProperty(
        name="Bar Count",
        description="The number of bars to make",
        default=64,
        min=1
        )

    bpy.types.Scene.bz_bar_width = bpy.props.FloatProperty(
        name="Bar Width",
        description="The width of the bars",
        default=0.8,
        min=0
        )

    bpy.types.Scene.bz_amplitude = bpy.props.FloatProperty(
        name="Amplitude",
        description="Amplitude of visualizer bars",
        default=24.0,
        min=0
        )

    bpy.types.Scene.bz_use_radial = bpy.props.BoolProperty(
        name="Use Radial",
        description="Use a circular visualizer",
        default=False
        )

    bpy.types.Scene.bz_radius = bpy.props.FloatProperty(
        name="Radius",
        description="Radius of the radial visualizer",
        default=20,
        min=0
        )

    bpy.types.Scene.bz_spacing = bpy.props.FloatProperty(
        name="Spacing",
        description="Spacing between bars",
        default=2.25,
        min=0
        )


def register():
    bpy.utils.register_module(__name__)

    initprop()


def unregister():
    bpy.utils.unregister_module(__name__)

    del bpy.types.Scene.bz_audiofile
    del bpy.types.Scene.bz_bar_count
    del bpy.types.Scene.bz_bar_width
    del bpy.types.Scene.bz_amplitude
    del bpy.types.Scene.bz_spacing
    del bpy.types.Scene.bz_use_radial
    del bpy.types.Scene.bz_radius
