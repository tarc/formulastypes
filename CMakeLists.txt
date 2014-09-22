cmake_minimum_required (VERSION 2.8)

project (fac-tmp)

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    add_definitions ("-DNOVARIADIC")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions ("-std=c++11")
endif ()

file (GLOB sources ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

list (REMOVE_ITEM sources "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp")
list (REMOVE_ITEM sources "${CMAKE_CURRENT_SOURCE_DIR}/moveconstr.cpp")

add_executable (main ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
add_executable (moveconstr ${CMAKE_CURRENT_SOURCE_DIR}/moveconstr.cpp)

foreach (filesrc ${sources})
	get_filename_component (filesrcwe ${filesrc} NAME_WE)
	add_library (${filesrcwe} ${filesrc})
	target_link_libraries (main ${filesrcwe})
endforeach ()
