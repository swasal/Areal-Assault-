'''OpenGL extension EXT.texture_format_BGRA8888

This module customises the behaviour of the 
OpenGL.raw.GLES1.EXT.texture_format_BGRA8888 to provide a more 
Python-friendly API

Overview (from the spec)
	
	 This extension provides an additional format and type combination
	 for use when specifying texture data.  The current allowed combinations
	 are:
	
	 Internal Format     External Format Type                    Bytes per Pixel
	 ---------------     --------------- ----                    ---------------
	 RGBA                RGBA             UNSIGNED_BYTE          4
	 RGB                 RGB              UNSIGNED_BYTE          3
	 RGBA                RGBA             UNSIGNED_SHORT_4_4_4_4 2
	 RGBA                RGBA             UNSIGNED_SHORT_5_5_5_1 2
	 RGB                 RGB              UNSIGNED_SHORT_5_6_5   2
	 LUMINANCE_ALPHA     LUMINANCE_ALPHA  UNSIGNED_BYTE          2
	 LUMINANCE           LUMINANCE        UNSIGNED_BYTE          1
	 ALPHA               ALPHA            UNSIGNED_BYTE          1
	
	
	This table is extended to include format BGRA_EXT and type UNSIGNED_BYTE:
	
	 Internal Format     External Format Type                    Bytes per Pixel
	 ---------------     --------------- ----                    ---------------
	 BGRA_EXT            BGRA_EXT        UNSIGNED_BYTE           4
	 RGBA                RGBA            UNSIGNED_BYTE           4
	 RGB                 RGB             UNSIGNED_BYTE           3
	 RGBA                RGBA            UNSIGNED_SHORT_4_4_4_4  2
	 RGBA                RGBA            UNSIGNED_SHORT_5_5_5_1  2
	 RGB                 RGB             UNSIGNED_SHORT_5_6_5    2
	 LUMINANCE_ALPHA     LUMINANCE_ALPHA UNSIGNED_BYTE           2
	 LUMINANCE           LUMINANCE       UNSIGNED_BYTE           1
	 ALPHA               ALPHA           UNSIGNED_BYTE           1
	
	 This format is renderable in versions of OpenGL ES from 2.0 onwards.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_format_BGRA8888.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.EXT.texture_format_BGRA8888 import *
from OpenGL.raw.GLES1.EXT.texture_format_BGRA8888 import _EXTENSION_NAME

def glInitTextureFormatBgra8888EXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION