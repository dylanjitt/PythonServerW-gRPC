# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicio_tecnologico.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservicio_tecnologico.proto\"h\n\rsolic_usuario\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x16\n\x0enumero_cliente\x18\x03 \x01(\x05\x12#\n\x0ctipoServicio\x18\x04 \x01(\x0e\x32\r.TipoServicio\":\n\x0e\x64\x65talles_solic\x12\x13\n\x0bid_servicio\x18\x01 \x01(\x05\x12\x13\n\x0b\x63osto_total\x18\x02 \x01(\x01*5\n\x0cTipoServicio\x12\n\n\x06NORMAL\x10\x00\x12\x0b\n\x07\x45XPRESS\x10\x01\x12\x0c\n\x08NEXT_DAY\x10\x02\x32\x43\n\x0frespuesta_solic\x12\x30\n\rcalcularCosto\x12\x0e.solic_usuario\x1a\x0f.detalles_solicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'servicio_tecnologico_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TIPOSERVICIO']._serialized_start=196
  _globals['_TIPOSERVICIO']._serialized_end=249
  _globals['_SOLIC_USUARIO']._serialized_start=30
  _globals['_SOLIC_USUARIO']._serialized_end=134
  _globals['_DETALLES_SOLIC']._serialized_start=136
  _globals['_DETALLES_SOLIC']._serialized_end=194
  _globals['_RESPUESTA_SOLIC']._serialized_start=251
  _globals['_RESPUESTA_SOLIC']._serialized_end=318
# @@protoc_insertion_point(module_scope)
