cmake_minimum_required(VERSION 3.18...3.30)
project(ElaWidgetToolsPython LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(Shiboken6 REQUIRED)
find_package(PySide6 REQUIRED)

set(BINDINGS_MODULE_TARGET "ElaWidgetToolsPython")
set(BINDINGS_LIBRARY_NAME "ElaWidgetTools")

set(WRAPPED_HEADER ${CMAKE_CURRENT_SOURCE_DIR}/global.h)
set(TYPESYSTEM_FILE ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)

get_target_property(PYSIDE6_INCLUDE_DIRS PySide6::pyside6 INTERFACE_INCLUDE_DIRECTORIES)
get_target_property(SHIBOKEN6_INCLUDE_DIRS Shiboken6::libshiboken INTERFACE_INCLUDE_DIRECTORIES)
get_target_property(QT6_CORE_INCLUDE_DIRS Qt6::Core INTERFACE_INCLUDE_DIRECTORIES)
get_target_property(QT6_GUI_INCLUDE_DIRS Qt6::Gui INTERFACE_INCLUDE_DIRECTORIES)
get_target_property(QT6_WIDGETS_INCLUDE_DIRS Qt6::Widgets INTERFACE_INCLUDE_DIRECTORIES)
get_filename_component(QT6_PREFIX_DIR "${Qt6_DIR}/../../.." ABSOLUTE)

set(SHIBOKEN_OPTIONS
    --generator-set=shiboken
    --enable-parent-ctor-heuristic
    --enable-return-value-heuristic
    --use-isnull-as-nb-bool
    --avoid-protected-hack
    --enable-pyside-extensions
)

set(GENERATED_SOURCES_DIR ${CMAKE_CURRENT_BINARY_DIR}/ElaWidgetTools)

file(STRINGS ${TYPESYSTEM_FILE} TYPESYSTEM_TYPE_LINES
    REGEX "^[ \t]*<(object|namespace)-type name=\"[^\"]+\""
)
set(GENERATED_SOURCES ${GENERATED_SOURCES_DIR}/elawidgettools_module_wrapper.cpp)
foreach(TYPE_LINE IN LISTS TYPESYSTEM_TYPE_LINES)
    string(REGEX REPLACE ".*name=\"([^\"]+)\".*" "\\1" TYPE_NAME "${TYPE_LINE}")
    string(TOLOWER "${TYPE_NAME}" TYPE_WRAPPER_NAME)
    list(APPEND GENERATED_SOURCES
        ${GENERATED_SOURCES_DIR}/${TYPE_WRAPPER_NAME}_wrapper.cpp
    )
endforeach()

execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "
import shiboken6_generator
import os
print(os.path.join(os.path.dirname(shiboken6_generator.__file__), 'shiboken6'))
"
    OUTPUT_VARIABLE SHIBOKEN6_GENERATOR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(NOT SHIBOKEN6_GENERATOR)
    find_program(SHIBOKEN6_GENERATOR shiboken6)
endif()

execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "
import PySide6
import os
print(os.path.join(os.path.dirname(PySide6.__file__), 'typesystems'))
"
    OUTPUT_VARIABLE PYSIDE6_TYPESYSTEMS
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

set(SHIBOKEN_INCLUDE_DIRS
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/ElaWidgetTools
    ${QT6_PREFIX_DIR}/include
    ${QT6_CORE_INCLUDE_DIRS}
    ${QT6_GUI_INCLUDE_DIRS}
    ${QT6_WIDGETS_INCLUDE_DIRS}
    ${PYSIDE6_INCLUDE_DIRS}
    ${PYSIDE6_INCLUDE_DIRS}/QtCore
    ${PYSIDE6_INCLUDE_DIRS}/QtGui
    ${PYSIDE6_INCLUDE_DIRS}/QtWidgets
)

set(PATH_SEP ":")
if(WIN32)
    set(PATH_SEP ";")
endif()

list(JOIN SHIBOKEN_INCLUDE_DIRS "${PATH_SEP}" SHIBOKEN_INCLUDE_DIRS_STR)

add_custom_command(
    OUTPUT ${GENERATED_SOURCES}
    COMMAND ${SHIBOKEN6_GENERATOR}
        ${SHIBOKEN_OPTIONS}
        --typesystem-paths=${PYSIDE6_TYPESYSTEMS}
        --include-paths=${SHIBOKEN_INCLUDE_DIRS_STR}
        --output-directory=${CMAKE_CURRENT_BINARY_DIR}
        ${WRAPPED_HEADER}
        ${TYPESYSTEM_FILE}
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/fix_class_name.py ${GENERATED_SOURCES_DIR}
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/fix_out_params.py ${GENERATED_SOURCES_DIR}
    DEPENDS ${WRAPPED_HEADER} ${TYPESYSTEM_FILE} ${CMAKE_CURRENT_SOURCE_DIR}/fix_class_name.py ${CMAKE_CURRENT_SOURCE_DIR}/fix_out_params.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Running Shiboken6 generator..."
)

Python3_add_library(${BINDINGS_MODULE_TARGET} MODULE ${GENERATED_SOURCES})

target_include_directories(${BINDINGS_MODULE_TARGET} PRIVATE
    ${CMAKE_SOURCE_DIR}/ElaWidgetTools
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${GENERATED_SOURCES_DIR}
    ${Python3_INCLUDE_DIRS}
    ${SHIBOKEN6_INCLUDE_DIRS}
    ${QT6_PREFIX_DIR}/include
    ${QT6_CORE_INCLUDE_DIRS}
    ${QT6_GUI_INCLUDE_DIRS}
    ${QT6_WIDGETS_INCLUDE_DIRS}
    ${PYSIDE6_INCLUDE_DIRS}
    ${PYSIDE6_INCLUDE_DIRS}/QtCore
    ${PYSIDE6_INCLUDE_DIRS}/QtGui
    ${PYSIDE6_INCLUDE_DIRS}/QtWidgets
)

target_link_libraries(${BINDINGS_MODULE_TARGET} PRIVATE
    ElaWidgetTools
    Qt6::Widgets
    Shiboken6::libshiboken
    PySide6::pyside6
)

set_target_properties(${BINDINGS_MODULE_TARGET} PROPERTIES
    PREFIX ""
    SUFFIX ".${Python3_SOABI}.so"
    OUTPUT_NAME "ElaWidgetTools"
)

# On macOS the extension must bind to the same Qt that PySide6 ships at runtime
# (PySide6 bundles its own Qt under site-packages/PySide6/Qt/lib), not the Qt
# used for compilation. Rewrite the Qt framework references to @rpath and set
# @loader_path-based rpaths so the module resolves Qt/PySide6/shiboken6
# relative to its install location inside site-packages.
if(APPLE)
    add_custom_command(TARGET ${BINDINGS_MODULE_TARGET} POST_BUILD
        COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/fix_install_names.py
                $<TARGET_FILE:${BINDINGS_MODULE_TARGET}>
        COMMENT "Rewriting Qt install names to @rpath for PySide6 compatibility"
    )
endif()

# Install directly into the target interpreter's site-packages so that
# `import ElaWidgetTools` works out of the box for that Python.
execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "import site; print(site.getsitepackages()[0])"
    OUTPUT_VARIABLE Python3_SITEPACKAGES
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
install(
    TARGETS ${BINDINGS_MODULE_TARGET}
    LIBRARY DESTINATION ${Python3_SITEPACKAGES}
)
