# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/motion_analysis_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.util.tracking import motion_analysis_pb2 as mediapipe_dot_util_dot_tracking_dot_motion__analysis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<mediapipe/calculators/video/motion_analysis_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a-mediapipe/util/tracking/motion_analysis.proto\"\xe5\x05\n\x1fMotionAnalysisCalculatorOptions\x12:\n\x10\x61nalysis_options\x18\x01 \x01(\x0b\x32 .mediapipe.MotionAnalysisOptions\x12l\n\x12selection_analysis\x18\x04 \x01(\x0e\x32<.mediapipe.MotionAnalysisCalculatorOptions.SelectionAnalysis:\x12\x41NALYSIS_WITH_SEED\x12&\n\x17hybrid_selection_camera\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x66\n\rmeta_analysis\x18\x08 \x01(\x0e\x32\x37.mediapipe.MotionAnalysisCalculatorOptions.MetaAnalysis:\x16META_ANALYSIS_USE_META\x12 \n\x15meta_models_per_frame\x18\x06 \x01(\x05:\x01\x31\x12)\n\x19meta_outlier_domain_ratio\x18\t \x01(\x02:\x06\x30.0015\x12\x1a\n\x0b\x62ypass_mode\x18\x07 \x01(\x08:\x05\x66\x61lse\"~\n\x11SelectionAnalysis\x12\x16\n\x12\x41NALYSIS_RECOMPUTE\x10\x01\x12\x1d\n\x19NO_ANALYSIS_USE_SELECTION\x10\x02\x12\x1a\n\x16\x41NALYSIS_FROM_FEATURES\x10\x03\x12\x16\n\x12\x41NALYSIS_WITH_SEED\x10\x04\"D\n\x0cMetaAnalysis\x12\x1a\n\x16META_ANALYSIS_USE_META\x10\x01\x12\x18\n\x14META_ANALYSIS_HYBRID\x10\x02\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8f\x8e\x8a\x81\x01 \x01(\x0b\x32*.mediapipe.MotionAnalysisCalculatorOptions\"\x81\x01\n\x0eHomographyData\x12\"\n\x16motion_homography_data\x18\x01 \x03(\x02\x42\x02\x10\x01\x12 \n\x14histogram_count_data\x18\x02 \x03(\rB\x02\x10\x01\x12\x13\n\x0b\x66rame_width\x18\x03 \x01(\x05\x12\x14\n\x0c\x66rame_height\x18\x04 \x01(\x05')



_MOTIONANALYSISCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['MotionAnalysisCalculatorOptions']
_HOMOGRAPHYDATA = DESCRIPTOR.message_types_by_name['HomographyData']
_MOTIONANALYSISCALCULATOROPTIONS_SELECTIONANALYSIS = _MOTIONANALYSISCALCULATOROPTIONS.enum_types_by_name['SelectionAnalysis']
_MOTIONANALYSISCALCULATOROPTIONS_METAANALYSIS = _MOTIONANALYSISCALCULATOROPTIONS.enum_types_by_name['MetaAnalysis']
MotionAnalysisCalculatorOptions = _reflection.GeneratedProtocolMessageType('MotionAnalysisCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONANALYSISCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.video.motion_analysis_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MotionAnalysisCalculatorOptions)
  })
_sym_db.RegisterMessage(MotionAnalysisCalculatorOptions)

HomographyData = _reflection.GeneratedProtocolMessageType('HomographyData', (_message.Message,), {
  'DESCRIPTOR' : _HOMOGRAPHYDATA,
  '__module__' : 'mediapipe.calculators.video.motion_analysis_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.HomographyData)
  })
_sym_db.RegisterMessage(HomographyData)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_MOTIONANALYSISCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _HOMOGRAPHYDATA.fields_by_name['motion_homography_data']._options = None
  _HOMOGRAPHYDATA.fields_by_name['motion_homography_data']._serialized_options = b'\020\001'
  _HOMOGRAPHYDATA.fields_by_name['histogram_count_data']._options = None
  _HOMOGRAPHYDATA.fields_by_name['histogram_count_data']._serialized_options = b'\020\001'
  _MOTIONANALYSISCALCULATOROPTIONS._serialized_start=161
  _MOTIONANALYSISCALCULATOROPTIONS._serialized_end=902
  _MOTIONANALYSISCALCULATOROPTIONS_SELECTIONANALYSIS._serialized_start=615
  _MOTIONANALYSISCALCULATOROPTIONS_SELECTIONANALYSIS._serialized_end=741
  _MOTIONANALYSISCALCULATOROPTIONS_METAANALYSIS._serialized_start=743
  _MOTIONANALYSISCALCULATOROPTIONS_METAANALYSIS._serialized_end=811
  _HOMOGRAPHYDATA._serialized_start=905
  _HOMOGRAPHYDATA._serialized_end=1034
# @@protoc_insertion_point(module_scope)
