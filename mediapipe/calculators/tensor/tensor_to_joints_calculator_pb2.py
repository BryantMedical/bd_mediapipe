# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensor_to_joints_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>mediapipe/calculators/tensor/tensor_to_joints_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa8\x01\n\x1fTensorToJointsCalculatorOptions\x12\x12\n\nnum_joints\x18\x01 \x01(\x05\x12\x16\n\x0bstart_index\x18\x02 \x01(\x05:\x01\x30\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf1\x91\xe7\xc1\x01 \x01(\x0b\x32*.mediapipe.TensorToJointsCalculatorOptions')



_TENSORTOJOINTSCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['TensorToJointsCalculatorOptions']
TensorToJointsCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorToJointsCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TENSORTOJOINTSCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensor.tensor_to_joints_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorToJointsCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorToJointsCalculatorOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORTOJOINTSCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _TENSORTOJOINTSCALCULATOROPTIONS._serialized_start=116
  _TENSORTOJOINTSCALCULATOROPTIONS._serialized_end=284
# @@protoc_insertion_point(module_scope)
