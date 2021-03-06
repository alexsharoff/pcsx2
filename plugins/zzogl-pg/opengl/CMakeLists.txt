# Check that people use the good file
if(NOT TOP_CMAKE_WAS_SOURCED)
    message(FATAL_ERROR "
    You did not 'cmake' the good CMakeLists.txt file. Use the one in the top dir.
    It is advice to delete all wrongly generated cmake stuff => CMakeFiles & CMakeCache.txt")
endif(NOT TOP_CMAKE_WAS_SOURCED)


# plugin name
set(Output zzogl-0.3.0)

set(CommonFlags
    -pthread
    -DZEROGS_SSE2
    -fno-regmove
    -fno-strict-aliasing
    -Wstrict-aliasing # Allow to track strict aliasing issue.
    -Wunused-variable
    )

set(OptimizationFlags
    -O2
    -DNDEBUG
    )

# Debug - Build
if(CMAKE_BUILD_TYPE STREQUAL Debug)
    # add defines
    add_definitions(${CommonFlags} -g -Wall -D_DEBUG)
endif(CMAKE_BUILD_TYPE STREQUAL Debug)

# Devel - Build
if(CMAKE_BUILD_TYPE STREQUAL Devel)
    # add defines
    add_definitions(${CommonFlags} ${OptimizationFlags} -g -W -DZEROGS_DEVBUILD)
endif(CMAKE_BUILD_TYPE STREQUAL Devel)

# Release - Build
if(CMAKE_BUILD_TYPE STREQUAL Release)
    # add defines
    add_definitions(${CommonFlags} ${OptimizationFlags} -W)
endif(CMAKE_BUILD_TYPE STREQUAL Release)

# zzogl sources
set(zzoglSources
    GifTransfer.cpp
    GLWin32.cpp
    GLWinX11.cpp
    GSmain.cpp
    HostMemory.cpp
    Mem.cpp
    # memcpy_amd.cpp
    Mem_Swizzle.cpp
    Mem_Tables.cpp
    Profile.cpp
    rasterfont.cpp
    NewRegs.cpp
    Regs.cpp
    targets.cpp
    x86.cpp
    zerogs.cpp
    zpipe.cpp
    ZZClut.cpp
    ZZHacks.cpp
    ZZKeyboard.cpp
    ZZoglDrawing.cpp
    ZZLog.cpp
    ZZoglCreate.cpp
    ZZoglCRTC.cpp
    ZZoglFlush.cpp
    ZZoglFlushHack.cpp
    ZZoglSave.cpp
    ZZoglShaders.cpp
    ZZoglShoots.cpp
    ZZoglVB.cpp
    )

# zzogl headers
set(zzoglHeaders
    common.h
    CRC.h
    GifTransfer.h
    # glprocs.h
    GS.h
    HostMemory.h
    Mem.h
    Mem_Swizzle.h
    Mem_Transmit.h
    Profile.h
    rasterfont.h
    NewRegs.h
    Regs.h
    targets.h
    Util.h
    x86.h
    zerogs.h
    zpipe.h
    ZZClut.h
    ZZGl.h
    ZZHacks.h
    ZZoglDrawing.h
    ZZLog.h
    ZZoglCRTC.h
    ZZoglMath.h
    ZZoglShaders.h
    ZZoglShoots.h
    ZZoglVB.h
    )

# zzogl S sources
set(zzoglSSources
    x86-32.S)

# zzogl shader sources
set(zzoglShaderSources
    ctx0/ps2hw_ctx.fx
    ctx1/ps2hw_ctx.fx)

# zzogl Linux sources
set(zzoglLinuxSources
    Linux/Conf.cpp
    Linux/Linux.cpp)

# zzogl Linux headers
set(zzoglLinuxHeaders
    Linux/Linux.h)

# change language of .S-files to c++
set_source_files_properties(${zzoglSSources} PROPERTIES LANGUAGE CXX)

# add additional include directories
include_directories(.
    Linux)

# add library
add_library(${Output} SHARED
    ${zzoglSources}
    ${zzoglHeaders}
    ${zzoglSSources}
    ${zzoglShaderSources}
    ${zzoglLinuxSources}
    ${zzoglLinuxHeaders})

# link target with project internal libraries
target_link_libraries(${Output} Utilities)

# link target with Cg
target_link_libraries(${Output} ${CG_LIBRARIES})

# link target with glew
target_link_libraries(${Output} ${GLEW_LIBRARY})

# link target with opengl
target_link_libraries(${Output} ${OPENGL_LIBRARIES})

# link target with X11
target_link_libraries(${Output} ${X11_LIBRARIES})

# link target with jpeg
target_link_libraries(${Output} ${JPEG_LIBRARIES})

# User flags options
if(NOT USER_CMAKE_LD_FLAGS STREQUAL "")
    target_link_libraries(${Output} "${USER_CMAKE_LD_FLAGS}")
endif(NOT USER_CMAKE_LD_FLAGS STREQUAL "")

if(PACKAGE_MODE)
    install(TARGETS ${Output} DESTINATION ${PLUGIN_DIR})
    install(FILES ${PROJECT_SOURCE_DIR}/plugins/zzogl-pg/opengl/ps2hw.dat DESTINATION ${PLUGIN_DIR})
else(PACKAGE_MODE)
    install(TARGETS ${Output} DESTINATION ${CMAKE_SOURCE_DIR}/bin/plugins)
    install(FILES ${PROJECT_SOURCE_DIR}/plugins/zzogl-pg/opengl/ps2hw.dat DESTINATION ${CMAKE_SOURCE_DIR}/bin/plugins)
endif(PACKAGE_MODE)
