# python build stubs for package ghetty
# File is generated by gopy. Do not edit.
# gopy.exe build -output=engine -vm=python3 .

from pybindgen import retval, param, Function, Module
import sys

class CheckedFunction(Function):
    def __init__(self, *a, **kw):
        super(CheckedFunction, self).__init__(*a, **kw)
        self._failure_expression = kw.get('failure_expression', '')
        self._failure_cleanup = kw.get('failure_cleanup', '')

    def set_failure_expression(self, expr):
        self._failure_expression = expr

    def set_failure_cleanup(self, expr):
        self._failure_cleanup = expr

    def generate_call(self):
        super(CheckedFunction, self).generate_call()
        check = "PyErr_Occurred()"
        if self._failure_expression:
            check = "{} && {}".format(self._failure_expression, check)
        failure_cleanup = self._failure_cleanup or None
        self.before_call.write_error_check(check, failure_cleanup)

def add_checked_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

def add_checked_string_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_cleanup('if (retval != NULL) free(retval);')
    fn.after_call.add_cleanup_code('free(retval);')
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

mod = Module('_ghetty')
mod.add_include('"ghetty_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_error_CTor', retval('int64_t'), [])
mod.add_function('Slice_error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_error_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_error_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_error_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Array_3_ghetty_Vertex_CTor', retval('int64_t'), [])
mod.add_function('Array_3_ghetty_Vertex_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Array_3_ghetty_Vertex_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Array_3_ghetty_Vertex_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Array_4_Ptr_ebiten_Image_CTor', retval('int64_t'), [])
mod.add_function('Array_4_Ptr_ebiten_Image_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Array_4_Ptr_ebiten_Image_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Array_4_Ptr_ebiten_Image_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_ghetty_Matrix_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_ghetty_Matrix_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_ghetty_Matrix_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_ghetty_Matrix_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Ptr_ghetty_Matrix_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_ghetty_Matrix_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_ghetty_ProcessedTriangle_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_ebiten_Vertex_CTor', retval('int64_t'), [])
mod.add_function('Slice_ebiten_Vertex_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_ebiten_Vertex_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_ebiten_Vertex_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_ebiten_Vertex_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_ebiten_Vertex_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_fs_DirEntry_CTor', retval('int64_t'), [])
mod.add_function('Slice_fs_DirEntry_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_fs_DirEntry_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_fs_DirEntry_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_fs_DirEntry_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_fs_DirEntry_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_fs_FileInfo_CTor', retval('int64_t'), [])
mod.add_function('Slice_fs_FileInfo_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_fs_FileInfo_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_fs_FileInfo_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_fs_FileInfo_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_fs_FileInfo_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_ghetty_Tile_CTor', retval('int64_t'), [])
mod.add_function('Slice_ghetty_Tile_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_ghetty_Tile_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_ghetty_Tile_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_ghetty_Tile_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_ghetty_Tile_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_ghetty_Triangle_CTor', retval('int64_t'), [])
mod.add_function('Slice_ghetty_Triangle_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_ghetty_Triangle_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_ghetty_Triangle_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_ghetty_Triangle_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_ghetty_Triangle_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Map_string_any_CTor', retval('int64_t'), [])
mod.add_function('Map_string_any_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_string_any_elem', retval('int64_t'), [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_any_contains', retval('bool'), [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_any_set', None, [param('int64_t', 'handle'), param('char*', 'key'), param('int64_t', 'value')])
mod.add_function('Map_string_any_delete', None, [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_any_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_AlgorithmUsed', retval('int64_t'), [])
mod.add_function('ghetty_Set_AlgorithmUsed', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Basic', retval('int64_t'), [])
mod.add_function('ghetty_Set_Basic', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Brick', retval('int64_t'), [])
mod.add_function('ghetty_Set_Brick', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Buffer', retval('int64_t'), [])
mod.add_function('ghetty_Set_Buffer', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Bunny', retval('int64_t'), [])
mod.add_function('ghetty_Set_Bunny', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Cobble', retval('int64_t'), [])
mod.add_function('ghetty_Set_Cobble', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Cores', retval('int64_t'), [])
mod.add_function('ghetty_Set_Cores', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Depth', retval('int64_t'), [])
mod.add_function('ghetty_Set_Depth', None, [param('int64_t', 'val')])
mod.add_function('ghetty_EncodedImage', retval('char*'), [])
mod.add_function('ghetty_Set_EncodedImage', None, [param('char*', 'val')])
mod.add_function('ghetty_Log', retval('int64_t'), [])
mod.add_function('ghetty_Set_Log', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Mutex', retval('int64_t'), [])
mod.add_function('ghetty_Set_Mutex', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Position', retval('int64_t'), [])
mod.add_function('ghetty_Set_Position', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Projection', retval('int64_t'), [])
mod.add_function('ghetty_Set_Projection', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Scale', retval('int64_t'), [])
mod.add_function('ghetty_Set_Scale', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Scene', retval('int64_t'), [])
mod.add_function('ghetty_Set_Scene', None, [param('int64_t', 'val')])
mod.add_function('ghetty_TileXSize', retval('int64_t'), [])
mod.add_function('ghetty_Set_TileXSize', None, [param('int64_t', 'val')])
mod.add_function('ghetty_TileYSize', retval('int64_t'), [])
mod.add_function('ghetty_Set_TileYSize', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Tiles', retval('int64_t'), [])
mod.add_function('ghetty_Set_Tiles', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Time', retval('float'), [])
mod.add_function('ghetty_Set_Time', None, [param('float', 'val')])
mod.add_function('ghetty_Triangles', retval('int64_t'), [])
mod.add_function('ghetty_Set_Triangles', None, [param('int64_t', 'val')])
mod.add_function('ghetty_UpscaledBuffer', retval('int64_t'), [])
mod.add_function('ghetty_Set_UpscaledBuffer', None, [param('int64_t', 'val')])
mod.add_function('ghetty_Upscaler', retval('char*'), [])
mod.add_function('ghetty_Set_Upscaler', None, [param('char*', 'val')])
mod.add_function('ghetty_WaitGroup', retval('int64_t'), [])
mod.add_function('ghetty_Set_WaitGroup', None, [param('int64_t', 'val')])
mod.add_function('ghetty_ProcessedTriangle_CTor', retval('int64_t'), [])
mod.add_function('ghetty_ProcessedTriangle_Triangle_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_Triangle_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_ProcessedTriangle_Bounds_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_Bounds_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_ProcessedTriangle_VS1_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_VS1_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_ProcessedTriangle_VS2_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_VS2_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_ProcessedTriangle_Span_Get', retval('float'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_Span_Set', None, [param('int64_t', 'handle'), param('float', 'val')])
mod.add_function('ghetty_ProcessedTriangle_Split_Get', retval('float'), [param('int64_t', 'handle')])
mod.add_function('ghetty_ProcessedTriangle_Split_Set', None, [param('int64_t', 'handle'), param('float', 'val')])
mod.add_function('ghetty_Shader_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Texture_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Texture_Width_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Texture_Width_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Texture_Height_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Texture_Height_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Texture_Data_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Texture_Data_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'ghetty_Texture_ConvertPosition', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'uv')])
mod.add_function('ghetty_Tile_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Tile_Frame_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Tile_Frame_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Tile_Depth_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Tile_Depth_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Tile_Triangles_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Tile_Triangles_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Tile_X_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Tile_X_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Tile_Y_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Tile_Y_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'ghetty_Tile_Barycentric', None, [param('int64_t', '_handle'), param('int64_t', 'triangle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_EdgeTest', None, [param('int64_t', '_handle'), param('int64_t', 'triangle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_SweepLine', None, [param('int64_t', '_handle'), param('int64_t', 'triangle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_Rasterize', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_Reset', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_Add', None, [param('int64_t', '_handle'), param('int64_t', 'triangle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_ConvertPosition', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'x'), param('int64_t', 'y')])
add_checked_function(mod, 'ghetty_Tile_Set', None, [param('int64_t', '_handle'), param('int64_t', 'position'), param('uint8_t', 'r'), param('uint8_t', 'g'), param('uint8_t', 'b'), param('float', 'depth'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Tile_Clear', None, [param('int64_t', '_handle'), param('uint8_t', 'r'), param('uint8_t', 'g'), param('uint8_t', 'b'), param('bool', 'goRun')])
mod.add_function('ghetty_Triangle_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Triangle_UV_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Vertices_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Color_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Normals_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Texture_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Texture_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Triangle_Shader_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Triangle_Shader_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'ghetty_Triangle_Transform', None, [param('int64_t', '_handle'), param('int64_t', 'm2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Triangle_ScreenSpace', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Triangle_Normalize', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Triangle_Sort', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Triangle_Bounds', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'ghetty_Triangle_Copy', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('ghetty_Game_CTor', retval('int64_t'), [])
add_checked_function(mod, 'ghetty_Game_Update', retval('char*'), [param('int64_t', '_handle')])
add_checked_function(mod, 'ghetty_Game_Draw', None, [param('int64_t', '_handle'), param('int64_t', 'screen'), param('bool', 'goRun')])
mod.add_function('ghetty_Logger_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Logger_File_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Logger_File_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('ghetty_Logger_CurrentFPS_Get', retval('double'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Logger_CurrentFPS_Set', None, [param('int64_t', 'handle'), param('double', 'val')])
mod.add_function('ghetty_Logger_ShouldWrite_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Logger_ShouldWrite_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
add_checked_function(mod, 'ghetty_Logger_Log', None, [param('int64_t', '_handle'), param('double', 'framerate'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Logger_Close', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
mod.add_function('ghetty_Matrix_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Matrix_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Matrix_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('ghetty_Matrix_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('ghetty_Matrix_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('ghetty_Matrix_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
add_checked_function(mod, 'ghetty_Matrix_Multiply', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'm2')])
add_checked_function(mod, 'ghetty_Matrix_Vertex', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('ghetty_Model_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Model_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Model_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('ghetty_Model_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('ghetty_Model_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('ghetty_Model_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('ghetty_Vertex_CTor', retval('int64_t'), [])
mod.add_function('ghetty_Vertex_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('ghetty_Vertex_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('ghetty_Vertex_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('ghetty_Vertex_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('ghetty_Vertex_append', None, [param('int64_t', 'handle'), param('float', 'value')])
add_checked_function(mod, 'ghetty_Vertex_Sum', None, [param('int64_t', '_handle'), param('int64_t', 'v2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Sub', None, [param('int64_t', '_handle'), param('int64_t', 'v2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Multiply', None, [param('int64_t', '_handle'), param('int64_t', 'v2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Transform', None, [param('int64_t', '_handle'), param('int64_t', 'm2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Dot', retval('float'), [param('int64_t', '_handle'), param('int64_t', 'v2')])
add_checked_function(mod, 'ghetty_Vertex_Cross', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'v2')])
add_checked_function(mod, 'ghetty_Vertex_CrossProduct', retval('float'), [param('int64_t', '_handle'), param('int64_t', 'v2')])
add_checked_function(mod, 'ghetty_Vertex_Interpolate', None, [param('int64_t', '_handle'), param('int64_t', 'v2'), param('float', 'factor'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_InsideClipSpace', retval('bool'), [param('int64_t', '_handle')])
add_checked_function(mod, 'ghetty_Vertex_ScreenSpace', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Normalize', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Matrix', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'ghetty_Vertex_Swap', None, [param('int64_t', '_handle'), param('int64_t', 'v2'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_Vertex_Copy', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'ghetty_Process', retval('int64_t'), [param('int64_t', 'triangle')])
add_checked_function(mod, 'ghetty_LoadTexture', retval('int64_t'), [param('char*', 'directory')])
add_checked_function(mod, 'ghetty_NewLogger', retval('int64_t'), [param('char*', 'directory')])
add_checked_function(mod, 'ghetty_NewLoggerCNN', retval('int64_t'), [param('char*', 'directory')])
add_checked_function(mod, 'ghetty_Clamp', retval('float'), [param('float', 'value'), param('int64_t', 'min'), param('int64_t', 'max')])
add_checked_function(mod, 'ghetty_Launch', None, [param('PyObject*', 'renderCallback', transfer_ownership=False), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_BuildAndProcess', None, [param('int64_t', 'triangle'), param('int64_t', 'tiles'), param('bool', 'goRun')])
add_checked_function(mod, 'ghetty_LoadModel', retval('int64_t'), [param('char*', 'directory')])
add_checked_function(mod, 'ghetty_ProjectionMatrix', retval('int64_t'), [])
add_checked_function(mod, 'ghetty_TransformationMatrix', retval('int64_t'), [param('int64_t', 'p'), param('int64_t', 'r')])
add_checked_function(mod, 'ghetty_BasicVertex', None, [param('int64_t', 'vertex'), param('int64_t', 'uv'), param('int64_t', 'normal'), param('int64_t', 'color'), param('int64_t', 'matrices'), param('bool', 'goRun')])

mod.generate(open('ghetty.c', 'w'))

