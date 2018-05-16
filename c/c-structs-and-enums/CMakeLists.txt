add_hackerrank(small-triangles-large-triangles small-triangles-large-triangles.c)
add_hackerrank(post-transition post-transition.c)
add_hackerrank(too-high-boxes too-high-boxes.c)
add_hackerrank(structuring-the-document structuring-the-document.c)


target_compile_options(small-triangles-large-triangles PRIVATE "-Wno-conversion")
target_compile_options(post-transition PRIVATE "-Wno-conversion")
target_compile_options(structuring-the-document PRIVATE "-Wno-conversion" "-Wno-unused-variable")

target_link_libraries(small-triangles-large-triangles m)
