# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/processors/proto/image_preprocessing_graph_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.calculators.tensor import image_to_tensor_calculator_pb2 as mediapipe_dot_calculators_dot_tensor_dot_image__to__tensor__calculator__pb2
from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nVmediapipe/tasks/cc/components/processors/proto/image_preprocessing_graph_options.proto\x12+mediapipe.tasks.components.processors.proto\x1a=mediapipe/calculators/tensor/image_to_tensor_calculator.proto\x1a$mediapipe/framework/calculator.proto\"\x91\x03\n\x1eImagePreprocessingGraphOptions\x12J\n\x17image_to_tensor_options\x18\x01 \x01(\x0b\x32).mediapipe.ImageToTensorCalculatorOptions\x12m\n\x07\x62\x61\x63kend\x18\x02 \x01(\x0e\x32S.mediapipe.tasks.components.processors.proto.ImagePreprocessingGraphOptions.Backend:\x07\x44\x45\x46\x41ULT\"8\n\x07\x42\x61\x63kend\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0b\x43PU_BACKEND\x10\x01\x12\x0f\n\x0bGPU_BACKEND\x10\x02\x32z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x84\xf2\xed\xd9\x01 \x01(\x0b\x32K.mediapipe.tasks.components.processors.proto.ImagePreprocessingGraphOptions')



_IMAGEPREPROCESSINGGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['ImagePreprocessingGraphOptions']
_IMAGEPREPROCESSINGGRAPHOPTIONS_BACKEND = _IMAGEPREPROCESSINGGRAPHOPTIONS.enum_types_by_name['Backend']
ImagePreprocessingGraphOptions = _reflection.GeneratedProtocolMessageType('ImagePreprocessingGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPREPROCESSINGGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.components.processors.proto.image_preprocessing_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.processors.proto.ImagePreprocessingGraphOptions)
  })
_sym_db.RegisterMessage(ImagePreprocessingGraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGEPREPROCESSINGGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _IMAGEPREPROCESSINGGRAPHOPTIONS._serialized_start=237
  _IMAGEPREPROCESSINGGRAPHOPTIONS._serialized_end=638
  _IMAGEPREPROCESSINGGRAPHOPTIONS_BACKEND._serialized_start=458
  _IMAGEPREPROCESSINGGRAPHOPTIONS_BACKEND._serialized_end=514
# @@protoc_insertion_point(module_scope)
