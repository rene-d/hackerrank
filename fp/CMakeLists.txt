project(fp Haskell)

add_executable(fp-solve-me-first fp-solve-me-first.hs)
add_executable(fp-hello-world fp-hello-world.hs)
add_executable(fp-hello-world-n-times fp-hello-world-n-times.hs)


add_test_hackerrank(fp-solve-me-first)
add_test_hackerrank(fp-hello-world)
add_test_hackerrank(fp-hello-world-n-times)
