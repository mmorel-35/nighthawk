resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/home/vscode/.cache/bazel/_bazel_vscode/install/20da5ab742b8d3d499c34fdafcd3c8b8/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository envoy instantiated at:\n  /workspaces/nighthawk/WORKSPACE:5:23: in <toplevel>\n  /workspaces/nighthawk/bazel/repositories.bzl:10:17: in nighthawk_dependencies\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "envoy",
               "generator_name": "envoy",
               "generator_function": "nighthawk_dependencies",
               "generator_location": None,
               "url": "https://github.com/envoyproxy/envoy/archive/c11574972860a40de36acf3ab8d930273f5ece65.tar.gz",
               "sha256": "a61e3e912d9b18034045ca347ac1f205cc2b878d6ea370f8c8e58ceb32b23f26",
               "strip_prefix": "envoy-c11574972860a40de36acf3ab8d930273f5ece65"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/envoyproxy/envoy/archive/c11574972860a40de36acf3ab8d930273f5ece65.tar.gz",
                         "urls": [],
                         "sha256": "a61e3e912d9b18034045ca347ac1f205cc2b878d6ea370f8c8e58ceb32b23f26",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "envoy-c11574972860a40de36acf3ab8d930273f5ece65",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "envoy"
                    },
                    "output_tree_hash": "3596c5a2f1237f0180e6f702d5a1dad68c7a1cb571613cf2e5e0bfe359b7abc7"
               }
          ]
     },
     {
          "original_rule_class": "@envoy//bazel:api_binding.bzl%_default_envoy_api",
          "definition_information": "Repository envoy_api instantiated at:\n  /workspaces/nighthawk/WORKSPACE:14:18: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_binding.bzl:29:27: in envoy_api_binding\nRepository rule _default_envoy_api defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_binding.bzl:17:37: in <toplevel>\n",
          "original_attributes": {
               "name": "envoy_api",
               "generator_name": "envoy_api",
               "generator_function": "envoy_api_binding",
               "generator_location": None,
               "reldir": "api"
          },
          "repositories": [
               {
                    "rule_class": "@envoy//bazel:api_binding.bzl%_default_envoy_api",
                    "attributes": {
                         "name": "envoy_api",
                         "generator_name": "envoy_api",
                         "generator_function": "envoy_api_binding",
                         "generator_location": None,
                         "reldir": "api"
                    },
                    "output_tree_hash": "309d29a3c86d821a29aa0f7bb0643b7916cb5befea4e66b2e52861388941b83a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_googleapis instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:24:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_googleapis",
               "generator_name": "com_google_googleapis",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/googleapis/googleapis/archive/114a745b2841a044e98cdbb19358ed29fcf4a5f1.tar.gz"
               ],
               "sha256": "9b4e0d0a04a217c06b426aefd03b82581a9510ca766d2d1c70e52bb2ad4a0703",
               "strip_prefix": "googleapis-114a745b2841a044e98cdbb19358ed29fcf4a5f1"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/googleapis/googleapis/archive/114a745b2841a044e98cdbb19358ed29fcf4a5f1.tar.gz"
                         ],
                         "sha256": "9b4e0d0a04a217c06b426aefd03b82581a9510ca766d2d1c70e52bb2ad4a0703",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "googleapis-114a745b2841a044e98cdbb19358ed29fcf4a5f1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_googleapis"
                    },
                    "output_tree_hash": "d1d4b8a2a2c6d7fe1b06bd7196289a1d17d75108cab8245a1fa8e3838ec4c4cb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository aspect_bazel_lib instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:367:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_bazel_lib",
               "generator_name": "aspect_bazel_lib",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/aspect-build/bazel-lib/archive/v2.4.1.tar.gz"
               ],
               "sha256": "38c5bf333ae70d1bb3a18da6053084ce5f475f0ed0a8f04eed415186d5a7b04b",
               "strip_prefix": "bazel-lib-2.4.1",
               "patches": [
                    "@envoy//bazel:aspect.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/aspect-build/bazel-lib/archive/v2.4.1.tar.gz"
                         ],
                         "sha256": "38c5bf333ae70d1bb3a18da6053084ce5f475f0ed0a8f04eed415186d5a7b04b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "bazel-lib-2.4.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:aspect.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "aspect_bazel_lib"
                    },
                    "output_tree_hash": "1e5807b604cee37786923848899b6aa99146412e6d706ae46b9894e684d005d6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository emsdk instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:352:11: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1270:26: in _emsdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "emsdk",
               "generator_name": "emsdk",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/emscripten-core/emsdk/archive/0ea8f8a8707070e9a7c83fbb4a3065683bcf1799.tar.gz"
               ],
               "sha256": "1ca0ff918d476c55707bb99bc0452be28ac5fb8f22a9260a8aae8a38d1bc0e27",
               "strip_prefix": "emsdk-0ea8f8a8707070e9a7c83fbb4a3065683bcf1799/bazel",
               "patches": [
                    "@envoy//bazel:emsdk.patch"
               ],
               "patch_args": [
                    "-p2"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/emscripten-core/emsdk/archive/0ea8f8a8707070e9a7c83fbb4a3065683bcf1799.tar.gz"
                         ],
                         "sha256": "1ca0ff918d476c55707bb99bc0452be28ac5fb8f22a9260a8aae8a38d1bc0e27",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "emsdk-0ea8f8a8707070e9a7c83fbb4a3065683bcf1799/bazel",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:emsdk.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p2"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "emsdk"
                    },
                    "output_tree_hash": "cfb0ac45c103c5a98c2aafaf0e4b46de7a51293c59f232e6baf1bd806f532f05"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository proxy_wasm_cpp_host instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:351:25: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1261:26: in _proxy_wasm_cpp_host\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "proxy_wasm_cpp_host",
               "generator_name": "proxy_wasm_cpp_host",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/proxy-wasm/proxy-wasm-cpp-host/archive/e200fee8af40918c41f3275cff090993e3b26940.tar.gz"
               ],
               "sha256": "9711411b3b8d48a3ee9278f44824ce569c1fdd491183255f568f2b938360e964",
               "strip_prefix": "proxy-wasm-cpp-host-e200fee8af40918c41f3275cff090993e3b26940",
               "patches": [
                    "@envoy//bazel:proxy_wasm_cpp_host.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/proxy-wasm/proxy-wasm-cpp-host/archive/e200fee8af40918c41f3275cff090993e3b26940.tar.gz"
                         ],
                         "sha256": "9711411b3b8d48a3ee9278f44824ce569c1fdd491183255f568f2b938360e964",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "proxy-wasm-cpp-host-e200fee8af40918c41f3275cff090993e3b26940",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:proxy_wasm_cpp_host.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "proxy_wasm_cpp_host"
                    },
                    "output_tree_hash": "9ee2f31a36906de9e7ba46fd566208c401425ae4cc48f4f2d60fe4b5cddb8518"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:329:25: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:964:26: in _com_google_protobuf\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python",
               "generator_name": "rules_python",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_python/archive/0.31.0.tar.gz"
               ],
               "sha256": "c68bdc4fbec25de5b5493b8819cfc877c4ea299c0dcb15c244c5a00208cde311",
               "strip_prefix": "rules_python-0.31.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_python/archive/0.31.0.tar.gz"
                         ],
                         "sha256": "c68bdc4fbec25de5b5493b8819cfc877c4ea299c0dcb15c244c5a00208cde311",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_python-0.31.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_python"
                    },
                    "output_tree_hash": "63a74ef74b45a21f2060ce17374d4c00fedcad9f88095a2ea9d7346d62ca67c6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_rules_proto_grpc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:310:33: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1235:26: in _com_github_rules_proto_grpc\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_rules_proto_grpc",
               "generator_name": "com_github_rules_proto_grpc",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/rules-proto-grpc/rules_proto_grpc/releases/download/4.6.0/rules_proto_grpc-4.6.0.tar.gz"
               ],
               "sha256": "2a0860a336ae836b54671cbbe0710eec17c64ef70c4c5a88ccfd47ea6e3739bd",
               "strip_prefix": "rules_proto_grpc-4.6.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/rules-proto-grpc/rules_proto_grpc/releases/download/4.6.0/rules_proto_grpc-4.6.0.tar.gz"
                         ],
                         "sha256": "2a0860a336ae836b54671cbbe0710eec17c64ef70c4c5a88ccfd47ea6e3739bd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto_grpc-4.6.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_rules_proto_grpc"
                    },
                    "output_tree_hash": "4154826927cd2adc39d57115effa4c7cb588209e20cd0286560816eb94121b1f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
          "definition_information": "Repository rules_python_internal instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:53:10: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule internal_config_repo defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/private/internal_config_repo.bzl:93:39: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python_internal",
               "generator_name": "rules_python_internal",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
                    "attributes": {
                         "name": "rules_python_internal",
                         "generator_name": "rules_python_internal",
                         "generator_function": "envoy_dependencies_extra",
                         "generator_location": None
                    },
                    "output_tree_hash": "e3cdc1dc7ccd575c9f96009b8b405a42d410026808c2f3cf4bd64bd0cf62fe2c"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
          "definition_information": "Repository python3_11 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:26:31: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:615:22: in python_register_toolchains\nRepository rule toolchain_aliases defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/private/toolchains_repo.bzl:211:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_11",
               "generator_name": "python3_11",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "platforms": [
                    "aarch64-apple-darwin",
                    "aarch64-unknown-linux-gnu",
                    "ppc64le-unknown-linux-gnu",
                    "x86_64-apple-darwin",
                    "x86_64-pc-windows-msvc",
                    "x86_64-unknown-linux-gnu"
               ],
               "python_version": "3.11.3",
               "user_repository_name": "python3_11"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
                    "attributes": {
                         "name": "python3_11",
                         "generator_name": "python3_11",
                         "generator_function": "envoy_dependencies_extra",
                         "generator_location": None,
                         "platforms": [
                              "aarch64-apple-darwin",
                              "aarch64-unknown-linux-gnu",
                              "ppc64le-unknown-linux-gnu",
                              "x86_64-apple-darwin",
                              "x86_64-pc-windows-msvc",
                              "x86_64-unknown-linux-gnu"
                         ],
                         "python_version": "3.11.3",
                         "user_repository_name": "python3_11"
                    },
                    "output_tree_hash": "2d330034cdd6f2624a6430a5c614bfe87874a68e36e03d8cd7a05167d6203536"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:16:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.5.0/bazel-skylib-1.5.0.tar.gz"
               ],
               "sha256": "cd55a062e763b9349921f0f5db8c3933288dc8ba4f76dd9416aac68acee3cb94",
               "strip_prefix": ""
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.5.0/bazel-skylib-1.5.0.tar.gz"
                         ],
                         "sha256": "cd55a062e763b9349921f0f5db8c3933288dc8ba4f76dd9416aac68acee3cb94",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "f917c8b406ba8ed7853be3a016c9c60f1825c38e0685c1a1bd6efe75edf33257"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository envoy_toolshed instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:66:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "envoy_toolshed",
               "generator_name": "envoy_toolshed",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/envoyproxy/toolshed/archive/bazel-v0.1.1.tar.gz"
               ],
               "sha256": "ee759b57270a2747f3f2a3d6ecaad63b834dd9887505a9f1c919d72429dbeffd",
               "strip_prefix": "toolshed-bazel-v0.1.1/bazel"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/envoyproxy/toolshed/archive/bazel-v0.1.1.tar.gz"
                         ],
                         "sha256": "ee759b57270a2747f3f2a3d6ecaad63b834dd9887505a9f1c919d72429dbeffd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "toolshed-bazel-v0.1.1/bazel",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "envoy_toolshed"
                    },
                    "output_tree_hash": "0b29d70fabbe97e5a501c65e1b4fd1745871b376cab94e8223af588d1e80ad3c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_foreign_cc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:274:29: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1474:26: in _foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc",
               "generator_name": "rules_foreign_cc",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_foreign_cc/archive/0.9.0.tar.gz"
               ],
               "sha256": "2a4d07cd64b0719b39a7c12218a3e507672b82a97b98c6a89d38565894cf7c51",
               "strip_prefix": "rules_foreign_cc-0.9.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_foreign_cc/archive/0.9.0.tar.gz"
                         ],
                         "sha256": "2a4d07cd64b0719b39a7c12218a3e507672b82a97b98c6a89d38565894cf7c51",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_foreign_cc-0.9.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_foreign_cc"
                    },
                    "output_tree_hash": "b9eb5e3fa6e896c9e79dfa97d54aba8ac201a24be6c549a30d5b5704d0e69bbb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_fuzzing instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:353:19: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1401:26: in _rules_fuzzing\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_fuzzing",
               "generator_name": "rules_fuzzing",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_fuzzing/archive/v0.4.1.tar.gz"
               ],
               "sha256": "f6f3f42c48576acd5653bf07637deee2ae4ebb77ccdb0dacc67c184508bedc8c",
               "strip_prefix": "rules_fuzzing-0.4.1",
               "patches": [
                    "@envoy//bazel:rules_fuzzing.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_fuzzing/archive/v0.4.1.tar.gz"
                         ],
                         "sha256": "f6f3f42c48576acd5653bf07637deee2ae4ebb77ccdb0dacc67c184508bedc8c",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_fuzzing-0.4.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:rules_fuzzing.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_fuzzing"
                    },
                    "output_tree_hash": "5dfdd3cb7874b96eddefdd6462cdd3a3ab0300d3dc4c514ba1ecbd021161c2e5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_chrusty_protoc_gen_jsonschema instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:62:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_chrusty_protoc_gen_jsonschema",
               "generator_name": "com_github_chrusty_protoc_gen_jsonschema",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/norbjd/protoc-gen-jsonschema/archive/7680e4998426e62b6896995ff73d4d91cc5fb13c.zip"
               ],
               "sha256": "ba3e313b10a1b50a6c1232d994c13f6e23d3669be4ae7fea13762f42bb3b2abc",
               "strip_prefix": "protoc-gen-jsonschema-7680e4998426e62b6896995ff73d4d91cc5fb13c"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/norbjd/protoc-gen-jsonschema/archive/7680e4998426e62b6896995ff73d4d91cc5fb13c.zip"
                         ],
                         "sha256": "ba3e313b10a1b50a6c1232d994c13f6e23d3669be4ae7fea13762f42bb3b2abc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "protoc-gen-jsonschema-7680e4998426e62b6896995ff73d4d91cc5fb13c",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_chrusty_protoc_gen_jsonschema"
                    },
                    "output_tree_hash": "4fc53d80e1ff25a40dba22d45c30edfc2f8f452350da8b8fa487590dd2c81462"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_aignas_rules_shellcheck instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:366:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_aignas_rules_shellcheck",
               "generator_name": "com_github_aignas_rules_shellcheck",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/aignas/rules_shellcheck/archive/0.3.2.tar.gz"
               ],
               "sha256": "798c7ff488a949e51d7d41d853d79164ce5c5335364ba32f972b79df8dd6be62",
               "strip_prefix": "rules_shellcheck-0.3.2"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/aignas/rules_shellcheck/archive/0.3.2.tar.gz"
                         ],
                         "sha256": "798c7ff488a949e51d7d41d853d79164ce5c5335364ba32f972b79df8dd6be62",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_shellcheck-0.3.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_aignas_rules_shellcheck"
                    },
                    "output_tree_hash": "d66055ea743bf9ddab0df396a4fee338a1d08eeebfea01348f745d08cfffbec3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_pkg instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:365:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_pkg",
               "generator_name": "rules_pkg",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_pkg/archive/0.10.1.tar.gz"
               ],
               "sha256": "d330dbe3e3004241ddb9b377416ffc5c823e3e2c08c0d56a7e1935499e7f8577",
               "strip_prefix": "rules_pkg-0.10.1"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_pkg/archive/0.10.1.tar.gz"
                         ],
                         "sha256": "d330dbe3e3004241ddb9b377416ffc5c823e3e2c08c0d56a7e1935499e7f8577",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_pkg-0.10.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_pkg"
                    },
                    "output_tree_hash": "795c7faa36d19caacc5633cc8694eaa443db5d7060cb294f8f7867fd2b7eb7f3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository proxy_wasm_rust_sdk instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:354:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "proxy_wasm_rust_sdk",
               "generator_name": "proxy_wasm_rust_sdk",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/proxy-wasm/proxy-wasm-rust-sdk/archive/v0.2.1.tar.gz"
               ],
               "sha256": "23f3f2d8c4c8069a2e72693b350d7442b7722d334f73169eea78804ff70cde20",
               "strip_prefix": "proxy-wasm-rust-sdk-0.2.1"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/proxy-wasm/proxy-wasm-rust-sdk/archive/v0.2.1.tar.gz"
                         ],
                         "sha256": "23f3f2d8c4c8069a2e72693b350d7442b7722d334f73169eea78804ff70cde20",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "proxy-wasm-rust-sdk-0.2.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "proxy_wasm_rust_sdk"
                    },
                    "output_tree_hash": "b8de92255520d22894c4da6d0283dbbcc648ba171ff4cc3e4025886e94b83816"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository build_bazel_rules_nodejs instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:19:15: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/emsdk/deps.bzl:7:21: in deps\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_rules_nodejs",
               "generator_name": "build_bazel_rules_nodejs",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_nodejs/releases/download/4.4.1/rules_nodejs-4.4.1.tar.gz"
               ],
               "sha256": "4501158976b9da216295ac65d872b1be51e3eeb805273e68c516d2eb36ae1fbb"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_nodejs/releases/download/4.4.1/rules_nodejs-4.4.1.tar.gz"
                         ],
                         "sha256": "4501158976b9da216295ac65d872b1be51e3eeb805273e68c516d2eb36ae1fbb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "build_bazel_rules_nodejs"
                    },
                    "output_tree_hash": "0d10a1e108b7c7f3d98ede8993e2919d39eecaa078bdd483362f734a3e1e7666"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository upb instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:349:9: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1246:26: in _upb\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "upb",
               "generator_name": "upb",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/protocolbuffers/upb/archive/e074c038c35e781a1876f8eb52b14f822ae2db66.tar.gz"
               ],
               "sha256": "8608c15b5612c6154d4ee0c23910afe6c283985e1d368ea71704dcd8684135d4",
               "strip_prefix": "upb-e074c038c35e781a1876f8eb52b14f822ae2db66",
               "patches": [
                    "@envoy//bazel:upb.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/protocolbuffers/upb/archive/e074c038c35e781a1876f8eb52b14f822ae2db66.tar.gz"
                         ],
                         "sha256": "8608c15b5612c6154d4ee0c23910afe6c283985e1d368ea71704dcd8684135d4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "upb-e074c038c35e781a1876f8eb52b14f822ae2db66",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:upb.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "upb"
                    },
                    "output_tree_hash": "10776e73eb72a16d9dbb000713ff3aa575cb453ba98294f05f8ada70b5f09b7b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository io_bazel_rules_go instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:379:13: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:247:30: in _go_deps\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_go",
               "generator_name": "io_bazel_rules_go",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_go/releases/download/v0.39.1/rules_go-v0.39.1.zip"
               ],
               "sha256": "6dc2da7ab4cf5d7bfc7c949776b1b7c733f05e56edc4bcd9022bb249d2e2a996",
               "strip_prefix": "",
               "patches": [
                    "@envoy//bazel:rules_go.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_go/releases/download/v0.39.1/rules_go-v0.39.1.zip"
                         ],
                         "sha256": "6dc2da7ab4cf5d7bfc7c949776b1b7c733f05e56edc4bcd9022bb249d2e2a996",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:rules_go.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "io_bazel_rules_go"
                    },
                    "output_tree_hash": "804d41db8466a06a039ac1dfa4c146ed7c4f3abcc3b44e21390f8fb5ef969211"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_cel_cpp instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:355:24: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:704:26: in _com_google_cel_cpp\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_cel_cpp",
               "generator_name": "com_google_cel_cpp",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/cel-cpp/archive/0abd738f9f54388452e6ebb0955eb039f9162b3d.tar.gz"
               ],
               "sha256": "d163805320a782c5194b7496cdd5e8c9d9604eeffc1e531770cf6b130bc182fd",
               "strip_prefix": "cel-cpp-0abd738f9f54388452e6ebb0955eb039f9162b3d",
               "patches": [
                    "@envoy//bazel:cel-cpp.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/cel-cpp/archive/0abd738f9f54388452e6ebb0955eb039f9162b3d.tar.gz"
                         ],
                         "sha256": "d163805320a782c5194b7496cdd5e8c9d9604eeffc1e531770cf6b130bc182fd",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "cel-cpp-0abd738f9f54388452e6ebb0955eb039f9162b3d",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:cel-cpp.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_cel_cpp"
                    },
                    "output_tree_hash": "3b0a7c108b56c9586b6f5b4bf70587c529e1549ced0ea2615bfe4c564fe7174a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository build_bazel_rules_apple instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:309:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1154:26: in _com_github_grpc_grpc\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_rules_apple",
               "generator_name": "build_bazel_rules_apple",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_apple/releases/download/3.1.1/rules_apple.3.1.1.tar.gz"
               ],
               "sha256": "34c41bfb59cdaea29ac2df5a2fa79e5add609c71bb303b2ebb10985f93fa20e7",
               "strip_prefix": ""
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_apple/releases/download/3.1.1/rules_apple.3.1.1.tar.gz"
                         ],
                         "sha256": "34c41bfb59cdaea29ac2df5a2fa79e5add609c71bb303b2ebb10985f93fa20e7",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "build_bazel_rules_apple"
                    },
                    "output_tree_hash": "7e73ab2fff840dbd672268ff2099d326a19cac817f6fe2e810b6717b538c7035"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_gazelle instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:379:13: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:253:30: in _go_deps\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle",
               "generator_name": "bazel_gazelle",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.31.1/bazel-gazelle-v0.31.1.tar.gz"
               ],
               "sha256": "b8b6d75de6e4bf7c41b7737b183523085f56283f6db929b86c5e7e1f09cf59c9",
               "strip_prefix": ""
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.31.1/bazel-gazelle-v0.31.1.tar.gz"
                         ],
                         "sha256": "b8b6d75de6e4bf7c41b7737b183523085f56283f6db929b86c5e7e1f09cf59c9",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_gazelle"
                    },
                    "output_tree_hash": "a1c2acff524f770b968adaf51e3585e7ab26c86ec39086a4db2404e63aab2510"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_rust instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:380:15: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:256:26: in _rust_deps\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_rust",
               "generator_name": "rules_rust",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_rust/archive/0.35.0.tar.gz"
               ],
               "sha256": "3120c7aa3a146dfe6be8d5f23f4cf10af7d0f74a5aed8b94a818f88643bd24c3",
               "strip_prefix": "rules_rust-0.35.0",
               "patches": [
                    "@envoy//bazel:rules_rust.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_rust/archive/0.35.0.tar.gz"
                         ],
                         "sha256": "3120c7aa3a146dfe6be8d5f23f4cf10af7d0f74a5aed8b94a818f88643bd24c3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_rust-0.35.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:rules_rust.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_rust"
                    },
                    "output_tree_hash": "7237e0fb7e7ba09aa1b6525d5f4491a7cec7eb02170e4f7b8c3b578b882be446"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python:repositories.bzl%python_repository",
          "definition_information": "Repository python3_11_x86_64-unknown-linux-gnu instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:26:31: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:581:26: in python_register_toolchains\nRepository rule python_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:402:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_11_x86_64-unknown-linux-gnu",
               "generator_name": "python3_11_x86_64-unknown-linux-gnu",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "ignore_root_user_error": False,
               "patches": [],
               "platform": "x86_64-unknown-linux-gnu",
               "python_version": "3.11.3",
               "release_filename": "20230507/cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz",
               "sha256": "da50b87d1ec42b3cb577dfd22a3655e43a53150f4f98a4bfb40757c9d7839ab5",
               "strip_prefix": "python",
               "urls": [
                    "https://github.com/indygreg/python-build-standalone/releases/download/20230507/cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python:repositories.bzl%python_repository",
                    "attributes": {
                         "auth_patterns": {},
                         "coverage_tool": "",
                         "distutils": None,
                         "distutils_content": "",
                         "ignore_root_user_error": False,
                         "name": "python3_11_x86_64-unknown-linux-gnu",
                         "netrc": "",
                         "patches": [],
                         "platform": "x86_64-unknown-linux-gnu",
                         "python_version": "3.11.3",
                         "release_filename": "20230507/cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz",
                         "sha256": "da50b87d1ec42b3cb577dfd22a3655e43a53150f4f98a4bfb40757c9d7839ab5",
                         "strip_prefix": "python",
                         "urls": [
                              "https://github.com/indygreg/python-build-standalone/releases/download/20230507/cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz"
                         ]
                    },
                    "output_tree_hash": "3962010c2f61c86936dbefabf2caf166df9a3ddeb9d2d7f888f0b9cef05c0723"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
          "definition_information": "Repository dev_pip3 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:30:26: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/python_dependencies.bzl:15:14: in envoy_python_dependencies\nRepository rule pip_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:640:33: in <toplevel>\n",
          "original_attributes": {
               "name": "dev_pip3",
               "generator_name": "dev_pip3",
               "generator_function": "envoy_python_dependencies",
               "generator_location": None,
               "requirements_lock": "@envoy//tools/dev:requirements.txt",
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "dev_pip3",
                         "generator_name": "dev_pip3",
                         "generator_function": "envoy_python_dependencies",
                         "generator_location": None,
                         "requirements_lock": "@envoy//tools/dev:requirements.txt",
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "ed6fe60b7cc4c69921615f5bcfde9a9206cc5d0d459bb6a57017984ce2da436a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
          "definition_information": "Repository fuzzing_pip3 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:30:26: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/python_dependencies.bzl:22:14: in envoy_python_dependencies\nRepository rule pip_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:640:33: in <toplevel>\n",
          "original_attributes": {
               "name": "fuzzing_pip3",
               "generator_name": "fuzzing_pip3",
               "generator_function": "envoy_python_dependencies",
               "generator_location": None,
               "requirements_lock": "@rules_fuzzing//fuzzing:requirements.txt",
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "fuzzing_pip3",
                         "generator_name": "fuzzing_pip3",
                         "generator_function": "envoy_python_dependencies",
                         "generator_location": None,
                         "requirements_lock": "@rules_fuzzing//fuzzing:requirements.txt",
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "82dfa33443724e9cd9d5b213b49a500f3345ab2f99e40f9fe56c7c67f7780d07"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
          "definition_information": "Repository base_pip3 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:30:26: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/python_dependencies.bzl:8:14: in envoy_python_dependencies\nRepository rule pip_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:640:33: in <toplevel>\n",
          "original_attributes": {
               "name": "base_pip3",
               "generator_name": "base_pip3",
               "generator_function": "envoy_python_dependencies",
               "generator_location": None,
               "requirements_lock": "@envoy//tools/base:requirements.txt",
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "base_pip3",
                         "generator_name": "base_pip3",
                         "generator_function": "envoy_python_dependencies",
                         "generator_location": None,
                         "requirements_lock": "@envoy//tools/base:requirements.txt",
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "ce15603c448329472e985b83cec0ea8ae70ff0f9dd99893ddc2ccafe244b8219"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
          "definition_information": "Repository nh_pip3 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:38:30: in <toplevel>\n  /workspaces/nighthawk/bazel/python_dependencies.bzl:5:14: in nighthawk_python_dependencies\nRepository rule pip_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:640:33: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3",
               "generator_name": "nh_pip3",
               "generator_function": "nighthawk_python_dependencies",
               "generator_location": None,
               "requirements_lock": "//tools/base:requirements.txt",
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "nh_pip3",
                         "generator_name": "nh_pip3",
                         "generator_function": "nighthawk_python_dependencies",
                         "generator_location": None,
                         "requirements_lock": "//tools/base:requirements.txt",
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "49482030b78248c6d2d374dee60f8e5cad2677fe9d262798c0b608e20378acf3"
               }
          ]
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "envoy_build_config",
               "path": "."
          },
          "native": "local_repository(name = \"envoy_build_config\", path = \".\")"
     },
     {
          "original_rule_class": "@rules_fuzzing//fuzzing/private/oss_fuzz:repository.bzl%oss_fuzz_repository",
          "definition_information": "Repository rules_fuzzing_oss_fuzz instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:57:31: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_fuzzing/fuzzing/repositories.bzl:64:14: in rules_fuzzing_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule oss_fuzz_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_fuzzing/fuzzing/private/oss_fuzz/repository.bzl:123:38: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_fuzzing_oss_fuzz",
               "generator_name": "rules_fuzzing_oss_fuzz",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@rules_fuzzing//fuzzing/private/oss_fuzz:repository.bzl%oss_fuzz_repository",
                    "attributes": {
                         "name": "rules_fuzzing_oss_fuzz",
                         "generator_name": "rules_fuzzing_oss_fuzz",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None
                    },
                    "output_tree_hash": "01d5c852d5e6ad0fe07c9bf569ccbc242e1690ad634876716337f449b475783a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:46:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_proto/archive/refs/tags/4.0.0.tar.gz"
               ],
               "sha256": "66bfdf8782796239d3875d37e7de19b1d94301e8972b3cbd2446b332429b4df1",
               "strip_prefix": "rules_proto-4.0.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_proto/archive/refs/tags/4.0.0.tar.gz"
                         ],
                         "sha256": "66bfdf8782796239d3875d37e7de19b1d94301e8972b3cbd2446b332429b4df1",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-4.0.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "b023cb39c4ffadad4f3dfed69c5e2106c3867742f898fd631f33658c86523034"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:47:28: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:60:10: in rules_rust_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "generator_name": "rules_cc",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.0.9/rules_cc-0.0.9.tar.gz"
               ],
               "sha256": "2037875b9a4456dce4a79d112a8ae885bbc4aad968e6587dca6e64f3a0900cdf",
               "strip_prefix": "rules_cc-0.0.9"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.0.9/rules_cc-0.0.9.tar.gz"
                         ],
                         "sha256": "2037875b9a4456dce4a79d112a8ae885bbc4aad968e6587dca6e64f3a0900cdf",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_cc-0.0.9",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "eefc332fe980e25b58e7a4bd9fccd9e1a06dcb06f81423ce66248b4f1e7f8f74"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_envoyproxy_protoc_gen_validate instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:19:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_envoyproxy_protoc_gen_validate",
               "generator_name": "com_envoyproxy_protoc_gen_validate",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bufbuild/protoc-gen-validate/archive/refs/tags/v1.0.4.zip"
               ],
               "sha256": "9372f9ecde8fbadf83c8c7de3dbb49b11067aa26fb608c501106d0b4bf06c28f",
               "strip_prefix": "protoc-gen-validate-1.0.4",
               "patches": [
                    "@envoy//bazel:pgv.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bufbuild/protoc-gen-validate/archive/refs/tags/v1.0.4.zip"
                         ],
                         "sha256": "9372f9ecde8fbadf83c8c7de3dbb49b11067aa26fb608c501106d0b4bf06c28f",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "protoc-gen-validate-1.0.4",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:pgv.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_envoyproxy_protoc_gen_validate"
                    },
                    "output_tree_hash": "09773e71c26ef7169d5dc5137e1dc3258ea2aec101389acc7651740ae71d5c54"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_grpc_grpc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:309:26: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1149:26: in _com_github_grpc_grpc\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_grpc_grpc",
               "generator_name": "com_github_grpc_grpc",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/grpc/grpc/archive/v1.59.4.tar.gz"
               ],
               "sha256": "6edc67c2ad200c5b618c421f6e8c1b734a4aa3e741975e683491da03390ebf63",
               "strip_prefix": "grpc-1.59.4",
               "patches": [
                    "@envoy//bazel:grpc.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/grpc/grpc/archive/v1.59.4.tar.gz"
                         ],
                         "sha256": "6edc67c2ad200c5b618c421f6e8c1b734a4aa3e741975e683491da03390ebf63",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "grpc-1.59.4",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:grpc.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_grpc_grpc"
                    },
                    "output_tree_hash": "aaec29f5b250ea63c98338788489be505af4238a766df14ed0106b3299bba5f9"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository platforms instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:33:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:130:15: in apple_rules_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:86:14: in _maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms",
               "generator_name": "platforms",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.7/platforms-0.0.7.tar.gz",
                    "https://github.com/bazelbuild/platforms/releases/download/0.0.7/platforms-0.0.7.tar.gz"
               ],
               "sha256": "3a561c99e7bdbe9173aa653fd579fe849f1d8d67395780ab4770b1f381431d51"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.7/platforms-0.0.7.tar.gz",
                              "https://github.com/bazelbuild/platforms/releases/download/0.0.7/platforms-0.0.7.tar.gz"
                         ],
                         "sha256": "3a561c99e7bdbe9173aa653fd579fe849f1d8d67395780ab4770b1f381431d51",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "platforms"
                    },
                    "output_tree_hash": "ea31ba2d06afba6fdbef3c4bec658c7bfc0ae458200a42bd03cc60ad8c90dd99"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:526:13: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bf5ba89669bcdf4526f821bc9f1f9f49409ae9c61c4e8f21c9f17e06c475127"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository python3_11_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:26:31: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:626:20: in python_register_toolchains\nRepository rule toolchains_repo defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/private/toolchains_repo.bzl:104:34: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_11_toolchains",
               "generator_name": "python3_11_toolchains",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "python_version": "3.11.3",
               "set_python_version_constraint": False,
               "user_repository_name": "python3_11"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "python3_11_toolchains",
                         "generator_name": "python3_11_toolchains",
                         "generator_function": "envoy_dependencies_extra",
                         "generator_location": None,
                         "python_version": "3.11.3",
                         "set_python_version_constraint": False,
                         "user_repository_name": "python3_11"
                    },
                    "output_tree_hash": "88854676ce0681e5c46b0ddd70f5fa024672f389bb0444190cd56e7fdb27f0e9"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
          "definition_information": "Repository rules_foreign_cc_framework_toolchain_linux instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:49:34: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:84:39: in register_framework_toolchains\nRepository rule framework_toolchain_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc_framework_toolchain_linux",
               "generator_name": "rules_foreign_cc_framework_toolchain_linux",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:linux_commands.bzl",
               "exec_compatible_with": [
                    "@platforms//os:linux"
               ],
               "target_compatible_with": []
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
                    "attributes": {
                         "name": "rules_foreign_cc_framework_toolchain_linux",
                         "generator_name": "rules_foreign_cc_framework_toolchain_linux",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:linux_commands.bzl",
                         "exec_compatible_with": [
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": []
                    },
                    "output_tree_hash": "261428dd85e2b4f519dc0a4fb8f7d075dd79c7f757956c0c62c2dc8df33b12b2"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
          "definition_information": "Repository rules_foreign_cc_framework_toolchain_freebsd instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:49:34: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:84:39: in register_framework_toolchains\nRepository rule framework_toolchain_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc_framework_toolchain_freebsd",
               "generator_name": "rules_foreign_cc_framework_toolchain_freebsd",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:freebsd_commands.bzl",
               "exec_compatible_with": [
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": []
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
                    "attributes": {
                         "name": "rules_foreign_cc_framework_toolchain_freebsd",
                         "generator_name": "rules_foreign_cc_framework_toolchain_freebsd",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:freebsd_commands.bzl",
                         "exec_compatible_with": [
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": []
                    },
                    "output_tree_hash": "ab50e87df2604a634bd06712e0784d5fed103beb57b0e5931b05f5c55600a7a4"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
          "definition_information": "Repository rules_foreign_cc_framework_toolchain_windows instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:49:34: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:84:39: in register_framework_toolchains\nRepository rule framework_toolchain_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc_framework_toolchain_windows",
               "generator_name": "rules_foreign_cc_framework_toolchain_windows",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:windows_commands.bzl",
               "exec_compatible_with": [
                    "@platforms//os:windows"
               ],
               "target_compatible_with": []
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
                    "attributes": {
                         "name": "rules_foreign_cc_framework_toolchain_windows",
                         "generator_name": "rules_foreign_cc_framework_toolchain_windows",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:windows_commands.bzl",
                         "exec_compatible_with": [
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": []
                    },
                    "output_tree_hash": "90802060bac987d5016fc653ee8bb86d3c16e1b03fefb0874fd9c4e54bd1bcc2"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
          "definition_information": "Repository rules_foreign_cc_framework_toolchain_macos instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:49:34: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:84:39: in register_framework_toolchains\nRepository rule framework_toolchain_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/private/framework/toolchain.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc_framework_toolchain_macos",
               "generator_name": "rules_foreign_cc_framework_toolchain_macos",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:macos_commands.bzl",
               "exec_compatible_with": [
                    "@platforms//os:macos"
               ],
               "target_compatible_with": []
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository",
                    "attributes": {
                         "name": "rules_foreign_cc_framework_toolchain_macos",
                         "generator_name": "rules_foreign_cc_framework_toolchain_macos",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "commands_src": "@rules_foreign_cc//foreign_cc/private/framework/toolchains:macos_commands.bzl",
                         "exec_compatible_with": [
                              "@platforms//os:macos"
                         ],
                         "target_compatible_with": []
                    },
                    "output_tree_hash": "5a89df2a83cd2bbd85023a8482aca73ae081acdf11bce6a01df2d0e874974af0"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:520:13: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/cpp/cc_configure.bzl:183:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/cpp/cc_configure.bzl:77:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "f95f3d84ac75b4a4d9817af803f1d998a755bd9c20c700c79fa82cb159e98cfc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:349:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb8b23eb4ea8b42cec8fd2e3752c459811f8944d1b9c66b71d53f693f71c52c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:333:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_toolchain_config_repo",
               "generator_name": "remotejdk18_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0fbe406ef93edfa2dd63ecbec5eb91b55150360ebda0981365494b89015f6d4e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
          "definition_information": "Repository cmake_3.23.2_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:62:28: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:65:22: in prebuilt_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:142:14: in _cmake_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule prebuilt_toolchains_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains_repository.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "cmake_3.23.2_toolchains",
               "generator_name": "cmake_3.23.2_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "repos": {
                    "cmake-3.23.2-linux-aarch64": [
                         "@platforms//cpu:aarch64",
                         "@platforms//os:linux"
                    ],
                    "cmake-3.23.2-linux-x86_64": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:linux"
                    ],
                    "cmake-3.23.2-macos-universal": [
                         "@platforms//os:macos"
                    ],
                    "cmake-3.23.2-windows-i386": [
                         "@platforms//cpu:x86_32",
                         "@platforms//os:windows"
                    ],
                    "cmake-3.23.2-windows-x86_64": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:windows"
                    ]
               },
               "tool": "cmake"
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
                    "attributes": {
                         "name": "cmake_3.23.2_toolchains",
                         "generator_name": "cmake_3.23.2_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "repos": {
                              "cmake-3.23.2-linux-aarch64": [
                                   "@platforms//cpu:aarch64",
                                   "@platforms//os:linux"
                              ],
                              "cmake-3.23.2-linux-x86_64": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:linux"
                              ],
                              "cmake-3.23.2-macos-universal": [
                                   "@platforms//os:macos"
                              ],
                              "cmake-3.23.2-windows-i386": [
                                   "@platforms//cpu:x86_32",
                                   "@platforms//os:windows"
                              ],
                              "cmake-3.23.2-windows-x86_64": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:windows"
                              ]
                         },
                         "tool": "cmake"
                    },
                    "output_tree_hash": "5de74eaf9e27159469a57518e4b88c4cbe0175f02281f21bd1263a84a6b5ad47"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:317:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d088fdffd2f9c3a6cdefd249980df8b6b1ac0240cb5a1e7c67655ed2f181d0fb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:301:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "195ddef2a390e6ceebe003a0f2ede89a2962723d5e89c88fc6f1203d84eec1c5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:285:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0492adccec49cb7fafa99a8da0a43c1ecf77d62d15c2213ced41f7dd06d2a40f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:269:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7b4e118acc67f0ab2e764a34c9081459f46ecf83ede0abcb03fdbe4959b9033e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:253:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "78dfb0f7dab651cbc675d9dfe42e28b363ec26c3e5dc9a57b94833852f91deda"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:238:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "224a8c9f9e2f5e5cbb9efff01aa2555019675d3e1c9b93a7b4a83dfd7f5b69d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:222:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f698cb98820064a11248ba634c70c6df5b57382ee5f8a1b589007e5b73bfc6f8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:206:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8fc6087c6e654d2ff8ce626db7d0902fcf08d111f3c9f737ab19355b67d59c80"
               }
          ]
     },
     {
          "original_rule_class": "@rules_foreign_cc//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
          "definition_information": "Repository ninja_1.11.0_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:62:28: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:66:22: in prebuilt_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:4243:14: in _ninja_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule prebuilt_toolchains_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains_repository.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "ninja_1.11.0_toolchains",
               "generator_name": "ninja_1.11.0_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "repos": {
                    "ninja_1.11.0_linux": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:linux"
                    ],
                    "ninja_1.11.0_mac": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:macos"
                    ],
                    "ninja_1.11.0_win": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:windows"
                    ]
               },
               "tool": "ninja"
          },
          "repositories": [
               {
                    "rule_class": "@rules_foreign_cc//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
                    "attributes": {
                         "name": "ninja_1.11.0_toolchains",
                         "generator_name": "ninja_1.11.0_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "repos": {
                              "ninja_1.11.0_linux": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:linux"
                              ],
                              "ninja_1.11.0_mac": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:macos"
                              ],
                              "ninja_1.11.0_win": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:windows"
                              ]
                         },
                         "tool": "ninja"
                    },
                    "output_tree_hash": "cbebb2ebfa8541edd5ef7e25a25f71a37d93fbd9a58bf79a3ab84342cea26518"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:190:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "57763b4c6342c2729b70ccf1676a75726a4775a6e6468c86462f7247c968ecd7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:174:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9cd805ebc7702094002f5373bee54fb0b9bba1ece881b83ff48c0586ddaa10d5"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_sdk_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:29:27: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:662:28: in go_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:304:19: in go_download_sdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:292:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:279:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk_toolchains",
               "generator_name": "go_sdk_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_sdk"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.20"
               ],
               "geese": [
                    ""
               ],
               "goarchs": [
                    ""
               ]
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_sdk_toolchains",
                         "generator_name": "go_sdk_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_sdk"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.20"
                         ],
                         "geese": [
                              ""
                         ],
                         "goarchs": [
                              ""
                         ]
                    },
                    "output_tree_hash": "0ba3eb58c5fa72f98b663aa84f396b54d1287021a9d2ec86082e0f74f679b0e7"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_linux_amd64_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:31:31: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:161:20: in envoy_download_go_sdks\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:304:19: in go_download_sdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:292:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:279:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_linux_amd64_toolchains",
               "generator_name": "go_linux_amd64_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_linux_amd64"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.20"
               ],
               "geese": [
                    "linux"
               ],
               "goarchs": [
                    "amd64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_linux_amd64_toolchains",
                         "generator_name": "go_linux_amd64_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_linux_amd64"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.20"
                         ],
                         "geese": [
                              "linux"
                         ],
                         "goarchs": [
                              "amd64"
                         ]
                    },
                    "output_tree_hash": "747e6f5a7478466c39a5bccf9055b8f6bcc10205858c42d4589c83d972003542"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_linux_arm64_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:31:31: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:167:20: in envoy_download_go_sdks\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:304:19: in go_download_sdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:292:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:279:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_linux_arm64_toolchains",
               "generator_name": "go_linux_arm64_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_linux_arm64"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.20"
               ],
               "geese": [
                    "linux"
               ],
               "goarchs": [
                    "arm64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_linux_arm64_toolchains",
                         "generator_name": "go_linux_arm64_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_linux_arm64"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.20"
                         ],
                         "geese": [
                              "linux"
                         ],
                         "goarchs": [
                              "arm64"
                         ]
                    },
                    "output_tree_hash": "39d3b8d2137e653104f9e343d1f1cb66dfb8d7e55d7c8879250f64dec6e0a14c"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_darwin_amd64_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:31:31: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:173:20: in envoy_download_go_sdks\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:304:19: in go_download_sdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:292:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:279:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_darwin_amd64_toolchains",
               "generator_name": "go_darwin_amd64_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_darwin_amd64"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.20"
               ],
               "geese": [
                    "darwin"
               ],
               "goarchs": [
                    "amd64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_darwin_amd64_toolchains",
                         "generator_name": "go_darwin_amd64_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_darwin_amd64"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.20"
                         ],
                         "geese": [
                              "darwin"
                         ],
                         "goarchs": [
                              "amd64"
                         ]
                    },
                    "output_tree_hash": "860097962c4c270bf96a58b98a71a8e285d9f5c363d3bb30092f530156c1389a"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository go_darwin_arm64_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:31:31: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:179:20: in envoy_download_go_sdks\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:304:19: in go_download_sdk\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:292:27: in _go_toolchains\nRepository rule go_multiple_toolchains defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:279:41: in <toplevel>\n",
          "original_attributes": {
               "name": "go_darwin_arm64_toolchains",
               "generator_name": "go_darwin_arm64_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "prefixes": [
                    ""
               ],
               "sdk_repos": [
                    "go_darwin_arm64"
               ],
               "sdk_types": [
                    "remote"
               ],
               "sdk_versions": [
                    "1.20"
               ],
               "geese": [
                    "darwin"
               ],
               "goarchs": [
                    "arm64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "go_darwin_arm64_toolchains",
                         "generator_name": "go_darwin_arm64_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "prefixes": [
                              ""
                         ],
                         "sdk_repos": [
                              "go_darwin_arm64"
                         ],
                         "sdk_types": [
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.20"
                         ],
                         "geese": [
                              "darwin"
                         ],
                         "goarchs": [
                              "arm64"
                         ]
                    },
                    "output_tree_hash": "30493f3462cbe45ea93ad7bfb72b4948b0e7fcc2a46614295f3ee59f9ca53216"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_s390x__s390x-unknown-linux-gnu__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:38:24: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_s390x__s390x-unknown-linux-gnu__stable",
               "generator_name": "rust_linux_s390x__s390x-unknown-linux-gnu__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:s390x",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:s390x",
                    "@platforms//os:linux"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_s390x__s390x-unknown-linux-gnu__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_s390x__s390x-unknown-linux-gnu__stable",
                         "generator_name": "rust_linux_s390x__s390x-unknown-linux-gnu__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:s390x",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:s390x",
                              "@platforms//os:linux"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_s390x__s390x-unknown-linux-gnu__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "6c0cff601f4fbd59ed1576ed7f5c4bf49d64e9155e863c3d3b1ab891db0fde79"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:158:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "383e78f7a5b828401c8b5a470bc3676797a189fe9641856f243c35e282e4384c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:142:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f6c7a48666a77c098017285e46d511074ce3de7ff4e9808bc592fd49228681b2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:126:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "a762e337f24b8b511c520c1101b81cc02082e3fd25e58140dfa47eb7342161ce"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:110:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4b40216fabc2f6c17810749b3bf713065a39e05ff547dac45c395be6391709af"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:94:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "10df692cd4259131687761221fcb989c660f1c6e9376feba066b4fdc80bdc048"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_s390x__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:38:24: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_s390x__wasm32-unknown-unknown__stable",
               "generator_name": "rust_linux_s390x__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:s390x",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_s390x__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_s390x__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_linux_s390x__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:s390x",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_s390x__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "dea9ac352ecd1637808d0cf2f5d2e24f66f84d9b63db8c022711d8ce9cf81f33"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:78:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b5938368c9f92a6f5045ffca11214afb8ec9256686bec9245714376aa66b67d1"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:62:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f817d64408c5484cf564d5fdc24f11c3f601835818645f6de7ab4c56eaf4056f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:46:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8e1033ec85367ff2067aa4aa175c76d9cab0f81b9d0d4f10b7743e953331b892"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_s390x__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:38:24: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_s390x__wasm32-wasi__stable",
               "generator_name": "rust_linux_s390x__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:s390x",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_s390x__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_s390x__wasm32-wasi__stable",
                         "generator_name": "rust_linux_s390x__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:s390x",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_s390x__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "fa56de0b75d6aeaebd4ba70dd500a75705bc044426b67fe2938bd575815d532e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_analyzer_1.74.1 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:193:10: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:692:31: in rust_analyzer_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_analyzer_1.74.1",
               "generator_name": "rust_analyzer_1.74.1",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [],
               "target_compatible_with": [],
               "toolchain": "@rust_analyzer_1.74.1_tools//:rust_analyzer_toolchain",
               "toolchain_type": "@rules_rust//rust/rust_analyzer:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_analyzer_1.74.1",
                         "generator_name": "rust_analyzer_1.74.1",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [],
                         "target_compatible_with": [],
                         "toolchain": "@rust_analyzer_1.74.1_tools//:rust_analyzer_toolchain",
                         "toolchain_type": "@rules_rust//rust/rust_analyzer:toolchain_type"
                    },
                    "output_tree_hash": "3b3c15608ded2a694d0e5371cb7bd5b95dd467235f9a5ca6ec32daefb5300428"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:32:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/local_java_repository.bzl:232:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/jdk/local_java_repository.bzl:201:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "java_home": "/home/vscode/.cache/bazel/_bazel_vscode/install/20da5ab742b8d3d499c34fdafcd3c8b8/embedded_tools/tools/jdk/nosystemjdk",
               "version": "",
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = ___RUNTIME_VERSION___,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "java_home": "/home/vscode/.cache/bazel/_bazel_vscode/install/20da5ab742b8d3d499c34fdafcd3c8b8/embedded_tools/tools/jdk/nosystemjdk",
                         "version": "",
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = ___RUNTIME_VERSION___,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n"
                    },
                    "output_tree_hash": "3c00464defe7f910e18c56f2a6f01b71f2fe7949218cf07eae50a06b7142a2ad"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_bazel_lib//lib/private:yq_toolchain.bzl%yq_toolchains_repo",
          "definition_information": "Repository yq_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:63:27: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/aspect_bazel_lib/lib/repositories.bzl:79:23: in register_yq_toolchains\nRepository rule yq_toolchains_repo defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/aspect_bazel_lib/lib/private/yq_toolchain.bzl:407:37: in <toplevel>\n",
          "original_attributes": {
               "name": "yq_toolchains",
               "generator_name": "yq_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "user_repository_name": "yq"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_bazel_lib//lib/private:yq_toolchain.bzl%yq_toolchains_repo",
                    "attributes": {
                         "name": "yq_toolchains",
                         "generator_name": "yq_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "user_repository_name": "yq"
                    },
                    "output_tree_hash": "3e5a936eb7cd675a13b00701f706f647e0ba597ff55fbf01df66cf9767a239f8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__aarch64-apple-darwin__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__aarch64-apple-darwin__stable",
               "generator_name": "rust_darwin_aarch64__aarch64-apple-darwin__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_aarch64__aarch64-apple-darwin__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__aarch64-apple-darwin__stable",
                         "generator_name": "rust_darwin_aarch64__aarch64-apple-darwin__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_aarch64__aarch64-apple-darwin__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "bab5bf9a446ff8881777de8fc151872c220e98ec3adf32e12670e3b2c0277755"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__aarch64-apple-darwin__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__aarch64-apple-darwin__nightly",
               "generator_name": "rust_darwin_aarch64__aarch64-apple-darwin__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_aarch64__aarch64-apple-darwin__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__aarch64-apple-darwin__nightly",
                         "generator_name": "rust_darwin_aarch64__aarch64-apple-darwin__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_aarch64__aarch64-apple-darwin__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "201642deeddafe1fe08d37612c489223abc4b7921911a627a8f60ee51e0fe6be"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_darwin_aarch64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_darwin_aarch64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "46213f0b32dff6fa137f9f37075a51fe6e61d16d42ee532848ac1325e123038a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_darwin_aarch64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_darwin_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "f20fa6f2148e0aba5b738e0f465c0d175fbebfe7b2cbd2ae8e9399760d529dd1"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__wasm32-wasi__stable",
               "generator_name": "rust_darwin_aarch64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__wasm32-wasi__stable",
                         "generator_name": "rust_darwin_aarch64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "0ae4424a3d167534491c353d6eb04c1437d8ecb324a05742e674e574a5720b59"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_aarch64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_aarch64__wasm32-wasi__nightly",
               "generator_name": "rust_darwin_aarch64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_aarch64__wasm32-wasi__nightly",
                         "generator_name": "rust_darwin_aarch64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "eb66a179d67618218973b402cc75a2a0f13d835baee0e37d771e32ba3d7fe97c"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__aarch64-apple-darwin instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__aarch64-apple-darwin",
               "generator_name": "rustfmt_nightly-2023-12-07__aarch64-apple-darwin",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:osx"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-apple-darwin_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__aarch64-apple-darwin",
                         "generator_name": "rustfmt_nightly-2023-12-07__aarch64-apple-darwin",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:osx"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-apple-darwin_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "60fdf5767ffa18dd29b8c7067dd281de4e779771cb4799c438823d0345144748"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_bazel_lib//lib/private:jq_toolchain.bzl%jq_toolchains_repo",
          "definition_information": "Repository jq_toolchains instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:62:27: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/aspect_bazel_lib/lib/repositories.bzl:51:23: in register_jq_toolchains\nRepository rule jq_toolchains_repo defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/aspect_bazel_lib/lib/private/jq_toolchain.bzl:158:37: in <toplevel>\n",
          "original_attributes": {
               "name": "jq_toolchains",
               "generator_name": "jq_toolchains",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "user_repository_name": "jq"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_bazel_lib//lib/private:jq_toolchain.bzl%jq_toolchains_repo",
                    "attributes": {
                         "name": "jq_toolchains",
                         "generator_name": "jq_toolchains",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "user_repository_name": "jq"
                    },
                    "output_tree_hash": "372ff19b7076ae4fd0acf82cdf5ef3fc4d769f6f3692094bd3d7c212557e3347"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu",
               "generator_name": "rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu",
                         "generator_name": "rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-unknown-linux-gnu_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "1c0efdd8a19ffed8a94c800896130455296fafb8441092e7e91f0f8f4ee00186"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__wasm32-wasi__nightly",
               "generator_name": "rust_linux_x86_64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__wasm32-wasi__nightly",
                         "generator_name": "rust_linux_x86_64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "5f968631c59cdcfde122f020dc2bf325e54b975b963196f6c99a66f8f6924843"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__wasm32-wasi__stable",
               "generator_name": "rust_linux_x86_64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__wasm32-wasi__stable",
                         "generator_name": "rust_linux_x86_64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "c5882086c4de904189ba28c249438c68a90990336ef92a237f3b1d24881ac002"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_linux_x86_64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_linux_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "8fda962e905a9095c19770f0cb01558dfec8177387fcb46e963f2c10d34345dc"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_linux_x86_64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_linux_x86_64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "7d3342a4df39d55e72b610b5792fcb984c37ed023e97317205b4e918f85aeddf"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly",
               "generator_name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly",
                         "generator_name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_x86_64__x86_64-unknown-linux-gnu__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "d3845aca421bcc9dbea201e8551f0c776cb2f5fb0ac771c531d61ff32f75f614"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_x86_64__x86_64-unknown-linux-gnu__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__stable",
               "generator_name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:linux"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_x86_64__x86_64-unknown-linux-gnu__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__stable",
                         "generator_name": "rust_linux_x86_64__x86_64-unknown-linux-gnu__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:linux"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_x86_64__x86_64-unknown-linux-gnu__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "05bbdf6b149cbbd643ec0bea693f8c735cbc83cf9613e87197d1adbe691cb698"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd",
               "generator_name": "rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd",
                         "generator_name": "rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-unknown-freebsd_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "ddf074158861b2169765e903a9de526787fa508a838f8556b571b347783da2c7"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__wasm32-wasi__nightly",
               "generator_name": "rust_freebsd_x86_64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_freebsd_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__wasm32-wasi__nightly",
                         "generator_name": "rust_freebsd_x86_64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "7c05a3a97c1f7a1f1f1f8c4fc8358340291c8113a677d91ea9ca37c1fe2d75e5"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__wasm32-wasi__stable",
               "generator_name": "rust_freebsd_x86_64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_freebsd_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__wasm32-wasi__stable",
                         "generator_name": "rust_freebsd_x86_64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "6c990145ff1175d534f900f743c97be980c1bcdcf8a9237302383d4e4e7efadd"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__aarch64-pc-windows-msvc__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__aarch64-pc-windows-msvc__stable",
               "generator_name": "rust_windows_aarch64__aarch64-pc-windows-msvc__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_aarch64__aarch64-pc-windows-msvc__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__aarch64-pc-windows-msvc__stable",
                         "generator_name": "rust_windows_aarch64__aarch64-pc-windows-msvc__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_aarch64__aarch64-pc-windows-msvc__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "ca084fd046926273b03189a6898cdf45f5fc94db23a7615e2681aa5ce063b8aa"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__aarch64-pc-windows-msvc__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__aarch64-pc-windows-msvc__nightly",
               "generator_name": "rust_windows_aarch64__aarch64-pc-windows-msvc__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_aarch64__aarch64-pc-windows-msvc__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__aarch64-pc-windows-msvc__nightly",
                         "generator_name": "rust_windows_aarch64__aarch64-pc-windows-msvc__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_aarch64__aarch64-pc-windows-msvc__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "9da3e99adeda4991ed0ce289d088d09b036701cc717227c74edf7fc39f618bc0"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_windows_aarch64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_windows_aarch64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "a4c6154326bb5d44e56c2917aabfac9ac723721b59880708ea571f1bac15f580"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_windows_aarch64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_windows_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "b591d1c79bc8a0ae6e2a8f257f714a56d1df9091d23dea010eb1583e8193ed5f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__wasm32-wasi__stable",
               "generator_name": "rust_windows_aarch64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__wasm32-wasi__stable",
                         "generator_name": "rust_windows_aarch64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "bf24fb0c9b2eeebc81bcf73ef958a4ded40f69d5f91a0c462c87a3699ba61164"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_aarch64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_aarch64__wasm32-wasi__nightly",
               "generator_name": "rust_windows_aarch64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_aarch64__wasm32-wasi__nightly",
                         "generator_name": "rust_windows_aarch64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "f27a5d27d7a7d3886e4a9222ba2ef36e7d5f1acd17582b2258e1a2a185de9bd1"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc",
               "generator_name": "rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:windows"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc",
                         "generator_name": "rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:windows"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-pc-windows-msvc_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "2e148393898c02dfc865d0437acd60542fb5b61abc2bf960d1690909928637a9"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_freebsd_x86_64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_freebsd_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_freebsd_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "43bdab62d01ceab58cd0b943fee25664e39bcd023676e401ef10095510b6b57d"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_freebsd_x86_64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_freebsd_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_freebsd_x86_64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "dbe2f256519f0c761d438b5a0412fd2231d1f0d886656233058be03c8dbc3966"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__aarch64-unknown-linux-gnu__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__stable",
               "generator_name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_aarch64__aarch64-unknown-linux-gnu__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__stable",
                         "generator_name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_aarch64__aarch64-unknown-linux-gnu__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "6f8b49acd9bf587adc29e88f682283961efbe7ea494c6ec4ab35c0d925a03b3b"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly",
               "generator_name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly",
                         "generator_name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__x86_64-unknown-freebsd__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "181715e34fe527370cd46c58b363e1bb3ac8e9e6ae86d76dcb972a47eaef6802"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_freebsd_x86_64__x86_64-unknown-freebsd__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__stable",
               "generator_name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:freebsd"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_freebsd_x86_64__x86_64-unknown-freebsd__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__stable",
                         "generator_name": "rust_freebsd_x86_64__x86_64-unknown-freebsd__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:freebsd"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_freebsd_x86_64__x86_64-unknown-freebsd__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "75dd987a2f82b067aabc71d5008192c7a84215d37ef617fd35400b73f0e42634"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc",
               "generator_name": "rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc",
                         "generator_name": "rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-pc-windows-msvc_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "ba4361db53e9375d3daf2dc2ed1a6763a7cd88a557df31fa76ab49f4edef2c0c"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__wasm32-wasi__nightly",
               "generator_name": "rust_windows_x86_64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__wasm32-wasi__nightly",
                         "generator_name": "rust_windows_x86_64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "e930e2f60bf17fa797414bdf6164d05909fe0735d669dd4abd363764808d0465"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly",
               "generator_name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly",
                         "generator_name": "rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_aarch64__aarch64-unknown-linux-gnu__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "7145a451a7b5ac6dcae3624f1ad349ec4b297e57df92883660668c11b5881f4a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_linux_aarch64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_linux_aarch64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_aarch64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "020bcc09e69e0a5967d65f87bbf04408f53f04e807535e7e04f072f702d3564f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_linux_aarch64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_linux_aarch64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_aarch64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "d0653fef91e683c3dd91d7250d7626aa16cd09abb66a14131944834f2cf585c8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__wasm32-wasi__stable",
               "generator_name": "rust_linux_aarch64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_linux_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__wasm32-wasi__stable",
                         "generator_name": "rust_linux_aarch64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_linux_aarch64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "d50ac493425e7113b8e5125b167d79b5de6140f52c791a1a704f48b912a3f266"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_linux_aarch64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_linux_aarch64__wasm32-wasi__nightly",
               "generator_name": "rust_linux_aarch64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_linux_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_linux_aarch64__wasm32-wasi__nightly",
                         "generator_name": "rust_linux_aarch64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_linux_aarch64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "b59c30939d421c0b3628d5da33ccd6c2fedd3135a65dd126e4535ad22b23476e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu",
               "generator_name": "rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:aarch64",
                    "@platforms//os:linux"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu",
                         "generator_name": "rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:aarch64",
                              "@platforms//os:linux"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__aarch64-unknown-linux-gnu_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "ea0d15249bf8645b6f2a1aaee69d0e90c1ad519537a8c9e1d9e8bb1c2f8f91d9"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__x86_64-apple-darwin__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__x86_64-apple-darwin__stable",
               "generator_name": "rust_darwin_x86_64__x86_64-apple-darwin__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_x86_64__x86_64-apple-darwin__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__x86_64-apple-darwin__stable",
                         "generator_name": "rust_darwin_x86_64__x86_64-apple-darwin__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_x86_64__x86_64-apple-darwin__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "504124ae838e8a54860c4c43bff0a618aa6dd2699126f9a3e4947c208272092c"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__x86_64-apple-darwin__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__x86_64-apple-darwin__nightly",
               "generator_name": "rust_darwin_x86_64__x86_64-apple-darwin__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_x86_64__x86_64-apple-darwin__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__x86_64-apple-darwin__nightly",
                         "generator_name": "rust_darwin_x86_64__x86_64-apple-darwin__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_x86_64__x86_64-apple-darwin__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "8549a2a8a5aa266d8ecb4474aae49ce8be2d7519e105a58b3be06d6eae29ab37"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__wasm32-wasi__stable",
               "generator_name": "rust_windows_x86_64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__wasm32-wasi__stable",
                         "generator_name": "rust_windows_x86_64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "3e55930520d3077bb9262cfdda218c694222ebf5888512a6e8b6d02703d8c6f8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_windows_x86_64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_windows_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "fef61cfa31bc7cff8dfeb299ad6aa8fcf306098d97ed8c0b671f1aaa15c55dbf"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_windows_x86_64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_windows_x86_64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "e96916ee129fce7c11ab84da7b17e52ad0a8ece23e5240ce505f501213693ee2"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__x86_64-pc-windows-msvc__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__x86_64-pc-windows-msvc__nightly",
               "generator_name": "rust_windows_x86_64__x86_64-pc-windows-msvc__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_windows_x86_64__x86_64-pc-windows-msvc__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__x86_64-pc-windows-msvc__nightly",
                         "generator_name": "rust_windows_x86_64__x86_64-pc-windows-msvc__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_windows_x86_64__x86_64-pc-windows-msvc__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "6f3edc30b7e69b5666f47a695e2db05a99f20a22828c50a3be526c479ad3bbc4"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_windows_x86_64__x86_64-pc-windows-msvc__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_windows_x86_64__x86_64-pc-windows-msvc__stable",
               "generator_name": "rust_windows_x86_64__x86_64-pc-windows-msvc__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:windows"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_windows_x86_64__x86_64-pc-windows-msvc__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_windows_x86_64__x86_64-pc-windows-msvc__stable",
                         "generator_name": "rust_windows_x86_64__x86_64-pc-windows-msvc__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:windows"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_windows_x86_64__x86_64-pc-windows-msvc__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "1b5be10bf235eb244a3a092805fc8106be3ace17d977950b07bf1290d4d118b6"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rustfmt_nightly-2023-12-07__x86_64-apple-darwin instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:243:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:815:31: in rustfmt_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rustfmt_nightly-2023-12-07__x86_64-apple-darwin",
               "generator_name": "rustfmt_nightly-2023-12-07__x86_64-apple-darwin",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-apple-darwin_tools//:rustfmt_toolchain",
               "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rustfmt_nightly-2023-12-07__x86_64-apple-darwin",
                         "generator_name": "rustfmt_nightly-2023-12-07__x86_64-apple-darwin",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "toolchain": "@rustfmt_nightly-2023-12-07__x86_64-apple-darwin_tools//:rustfmt_toolchain",
                         "toolchain_type": "@rules_rust//rust/rustfmt:toolchain_type"
                    },
                    "output_tree_hash": "5c61a8cda765712a4bcb1e23fd650537abcb538907e8c4a9c89488db0b602a5a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__wasm32-wasi__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__wasm32-wasi__nightly",
               "generator_name": "rust_darwin_x86_64__wasm32-wasi__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__wasm32-wasi__nightly",
                         "generator_name": "rust_darwin_x86_64__wasm32-wasi__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_x86_64__wasm32-wasi__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "e8c6a34db2949a7ef369ded87deade71f14bb3b38e61b61c2bc74cd9c42ce335"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__wasm32-wasi__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__wasm32-wasi__stable",
               "generator_name": "rust_darwin_x86_64__wasm32-wasi__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:wasi"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__wasm32-wasi__stable",
                         "generator_name": "rust_darwin_x86_64__wasm32-wasi__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:wasi"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_x86_64__wasm32-wasi__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "12ec4d991ec32fbe542e955b7178babfaef2b07a1eef3a919a4b4c61e26ec84b"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__wasm32-unknown-unknown__stable instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__wasm32-unknown-unknown__stable",
               "generator_name": "rust_darwin_x86_64__wasm32-unknown-unknown__stable",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:stable"
               ],
               "toolchain": "@rust_darwin_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__wasm32-unknown-unknown__stable",
                         "generator_name": "rust_darwin_x86_64__wasm32-unknown-unknown__stable",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:stable"
                         ],
                         "toolchain": "@rust_darwin_x86_64__wasm32-unknown-unknown__stable_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "964d86127a343e1edeb124c6c4df878c82ce68729e8dd9c6e990a90dcbc09e99"
               }
          ]
     },
     {
          "original_rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
          "definition_information": "Repository rust_darwin_x86_64__wasm32-unknown-unknown__nightly instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:48:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:221:14: in rust_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:975:61: in rust_repository_set\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:579:31: in rust_toolchain_repository\nRepository rule toolchain_repository_proxy defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_rust/rust/repositories.bzl:459:45: in <toplevel>\n",
          "original_attributes": {
               "name": "rust_darwin_x86_64__wasm32-unknown-unknown__nightly",
               "generator_name": "rust_darwin_x86_64__wasm32-unknown-unknown__nightly",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "exec_compatible_with": [
                    "@platforms//cpu:x86_64",
                    "@platforms//os:osx"
               ],
               "target_compatible_with": [
                    "@platforms//cpu:wasm32",
                    "@platforms//os:none"
               ],
               "target_settings": [
                    "@rules_rust//rust/toolchain/channel:nightly"
               ],
               "toolchain": "@rust_darwin_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
               "toolchain_type": "@rules_rust//rust:toolchain"
          },
          "repositories": [
               {
                    "rule_class": "@rules_rust//rust:repositories.bzl%toolchain_repository_proxy",
                    "attributes": {
                         "name": "rust_darwin_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_name": "rust_darwin_x86_64__wasm32-unknown-unknown__nightly",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "exec_compatible_with": [
                              "@platforms//cpu:x86_64",
                              "@platforms//os:osx"
                         ],
                         "target_compatible_with": [
                              "@platforms//cpu:wasm32",
                              "@platforms//os:none"
                         ],
                         "target_settings": [
                              "@rules_rust//rust/toolchain/channel:nightly"
                         ],
                         "toolchain": "@rust_darwin_x86_64__wasm32-unknown-unknown__nightly_tools//:rust_toolchain",
                         "toolchain_type": "@rules_rust//rust:toolchain"
                    },
                    "output_tree_hash": "3e55ec6e5a97c0c190b05c67b0bb13fa243c37484743fe54fb541db39d24fbbf"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_googlesource_code_re2 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:348:9: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1238:26: in _re2\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_googlesource_code_re2",
               "generator_name": "com_googlesource_code_re2",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/re2/archive/2023-11-01.tar.gz"
               ],
               "sha256": "4e6593ac3c71de1c0f322735bc8b0492a72f66ffccfad76e259fa21c41d27d8a",
               "strip_prefix": "re2-2023-11-01"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/re2/archive/2023-11-01.tar.gz"
                         ],
                         "sha256": "4e6593ac3c71de1c0f322735bc8b0492a72f66ffccfad76e259fa21c41d27d8a",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "re2-2023-11-01",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_googlesource_code_re2"
                    },
                    "output_tree_hash": "5f4d9907608f91d1ed7475f545c769113bf490d4f86f303c5be924f9af5779ad"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:414:6: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java",
               "generator_name": "rules_java",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_java/releases/download/5.5.1/rules_java-5.5.1.tar.gz"
               ],
               "sha256": "73b88f34dc251bce7bc6c472eb386a6c2b312ed5b473c81fe46855c248f792e0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_java/releases/download/5.5.1/rules_java-5.5.1.tar.gz"
                         ],
                         "sha256": "73b88f34dc251bce7bc6c472eb386a6c2b312ed5b473c81fe46855c248f792e0",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_java"
                    },
                    "output_tree_hash": "be23e9fc134c0d03298232e1e3d3f7b3fb5245cc1014f3c1ffb43550a0935fb0"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_protobuf instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:329:25: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:978:26: in _com_google_protobuf\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_protobuf",
               "generator_name": "com_google_protobuf",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/protocolbuffers/protobuf/releases/download/v24.4/protobuf-24.4.tar.gz"
               ],
               "sha256": "616bb3536ac1fff3fb1a141450fa28b875e985712170ea7f1bfe5e5fc41e2cd8",
               "strip_prefix": "protobuf-24.4",
               "patches": [
                    "@envoy//bazel:protobuf.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/protocolbuffers/protobuf/releases/download/v24.4/protobuf-24.4.tar.gz"
                         ],
                         "sha256": "616bb3536ac1fff3fb1a141450fa28b875e985712170ea7f1bfe5e5fc41e2cd8",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "protobuf-24.4",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:protobuf.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_protobuf"
                    },
                    "output_tree_hash": "0ac00badb105a3969271ad28382453753784e70c671ca62146016c8cbce119ee"
               }
          ]
     },
     {
          "original_rule_class": "@com_google_googleapis//:repository_rules.bzl%switched_rules",
          "definition_information": "Repository com_google_googleapis_imports instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:389:31: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_google_googleapis/repository_rules.bzl:299:19: in switched_rules_by_language\nRepository rule switched_rules defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_google_googleapis/repository_rules.bzl:45:33: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_googleapis_imports",
               "generator_name": "com_google_googleapis_imports",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "rules": {
                    "proto_library_with_info": [
                         "",
                         ""
                    ],
                    "moved_proto_library": [
                         "",
                         ""
                    ],
                    "java_proto_library": [
                         "",
                         ""
                    ],
                    "java_grpc_library": [
                         "",
                         ""
                    ],
                    "java_gapic_library": [
                         "",
                         ""
                    ],
                    "java_gapic_test": [
                         "",
                         ""
                    ],
                    "java_gapic_assembly_gradle_pkg": [
                         "",
                         ""
                    ],
                    "py_proto_library": [
                         "@com_github_grpc_grpc//bazel:python_rules.bzl",
                         ""
                    ],
                    "py_grpc_library": [
                         "@com_github_grpc_grpc//bazel:python_rules.bzl",
                         ""
                    ],
                    "py_gapic_library": [
                         "",
                         ""
                    ],
                    "py_test": [
                         "",
                         ""
                    ],
                    "py_gapic_assembly_pkg": [
                         "",
                         ""
                    ],
                    "go_proto_library": [
                         "@io_bazel_rules_go//proto:def.bzl",
                         ""
                    ],
                    "go_library": [
                         "@io_bazel_rules_go//go:def.bzl",
                         ""
                    ],
                    "go_test": [
                         "",
                         ""
                    ],
                    "go_gapic_library": [
                         "",
                         ""
                    ],
                    "go_gapic_assembly_pkg": [
                         "",
                         ""
                    ],
                    "cc_proto_library": [
                         "native.cc_proto_library",
                         ""
                    ],
                    "cc_grpc_library": [
                         "@com_github_grpc_grpc//bazel:cc_grpc_library.bzl",
                         ""
                    ],
                    "cc_gapic_library": [
                         "",
                         ""
                    ],
                    "php_proto_library": [
                         "",
                         "php_proto_library"
                    ],
                    "php_grpc_library": [
                         "",
                         "php_grpc_library"
                    ],
                    "php_gapic_library": [
                         "",
                         "php_gapic_library"
                    ],
                    "php_gapic_assembly_pkg": [
                         "",
                         "php_gapic_assembly_pkg"
                    ],
                    "nodejs_gapic_library": [
                         "",
                         "typescript_gapic_library"
                    ],
                    "nodejs_gapic_assembly_pkg": [
                         "",
                         "typescript_gapic_assembly_pkg"
                    ],
                    "ruby_proto_library": [
                         "",
                         ""
                    ],
                    "ruby_grpc_library": [
                         "",
                         ""
                    ],
                    "ruby_ads_gapic_library": [
                         "",
                         ""
                    ],
                    "ruby_cloud_gapic_library": [
                         "",
                         ""
                    ],
                    "ruby_gapic_assembly_pkg": [
                         "",
                         ""
                    ],
                    "csharp_proto_library": [
                         "",
                         ""
                    ],
                    "csharp_grpc_library": [
                         "",
                         ""
                    ],
                    "csharp_gapic_library": [
                         "",
                         ""
                    ],
                    "csharp_gapic_assembly_pkg": [
                         "",
                         ""
                    ]
               }
          },
          "repositories": [
               {
                    "rule_class": "@com_google_googleapis//:repository_rules.bzl%switched_rules",
                    "attributes": {
                         "name": "com_google_googleapis_imports",
                         "generator_name": "com_google_googleapis_imports",
                         "generator_function": "envoy_dependencies",
                         "generator_location": None,
                         "rules": {
                              "proto_library_with_info": [
                                   "",
                                   ""
                              ],
                              "moved_proto_library": [
                                   "",
                                   ""
                              ],
                              "java_proto_library": [
                                   "",
                                   ""
                              ],
                              "java_grpc_library": [
                                   "",
                                   ""
                              ],
                              "java_gapic_library": [
                                   "",
                                   ""
                              ],
                              "java_gapic_test": [
                                   "",
                                   ""
                              ],
                              "java_gapic_assembly_gradle_pkg": [
                                   "",
                                   ""
                              ],
                              "py_proto_library": [
                                   "@com_github_grpc_grpc//bazel:python_rules.bzl",
                                   ""
                              ],
                              "py_grpc_library": [
                                   "@com_github_grpc_grpc//bazel:python_rules.bzl",
                                   ""
                              ],
                              "py_gapic_library": [
                                   "",
                                   ""
                              ],
                              "py_test": [
                                   "",
                                   ""
                              ],
                              "py_gapic_assembly_pkg": [
                                   "",
                                   ""
                              ],
                              "go_proto_library": [
                                   "@io_bazel_rules_go//proto:def.bzl",
                                   ""
                              ],
                              "go_library": [
                                   "@io_bazel_rules_go//go:def.bzl",
                                   ""
                              ],
                              "go_test": [
                                   "",
                                   ""
                              ],
                              "go_gapic_library": [
                                   "",
                                   ""
                              ],
                              "go_gapic_assembly_pkg": [
                                   "",
                                   ""
                              ],
                              "cc_proto_library": [
                                   "native.cc_proto_library",
                                   ""
                              ],
                              "cc_grpc_library": [
                                   "@com_github_grpc_grpc//bazel:cc_grpc_library.bzl",
                                   ""
                              ],
                              "cc_gapic_library": [
                                   "",
                                   ""
                              ],
                              "php_proto_library": [
                                   "",
                                   "php_proto_library"
                              ],
                              "php_grpc_library": [
                                   "",
                                   "php_grpc_library"
                              ],
                              "php_gapic_library": [
                                   "",
                                   "php_gapic_library"
                              ],
                              "php_gapic_assembly_pkg": [
                                   "",
                                   "php_gapic_assembly_pkg"
                              ],
                              "nodejs_gapic_library": [
                                   "",
                                   "typescript_gapic_library"
                              ],
                              "nodejs_gapic_assembly_pkg": [
                                   "",
                                   "typescript_gapic_assembly_pkg"
                              ],
                              "ruby_proto_library": [
                                   "",
                                   ""
                              ],
                              "ruby_grpc_library": [
                                   "",
                                   ""
                              ],
                              "ruby_ads_gapic_library": [
                                   "",
                                   ""
                              ],
                              "ruby_cloud_gapic_library": [
                                   "",
                                   ""
                              ],
                              "ruby_gapic_assembly_pkg": [
                                   "",
                                   ""
                              ],
                              "csharp_proto_library": [
                                   "",
                                   ""
                              ],
                              "csharp_grpc_library": [
                                   "",
                                   ""
                              ],
                              "csharp_gapic_library": [
                                   "",
                                   ""
                              ],
                              "csharp_gapic_assembly_pkg": [
                                   "",
                                   ""
                              ]
                         }
                    },
                    "output_tree_hash": "2d78bb29808b86b0561c3d4b704cbcc772ca0ae4b559425349f9e97db1958c63"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository build_bazel_rules_swift instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:33:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:122:15: in apple_rules_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:86:14: in _maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_rules_swift",
               "generator_name": "build_bazel_rules_swift",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "url": "https://github.com/bazelbuild/rules_swift/releases/download/1.13.0/rules_swift.1.13.0.tar.gz",
               "sha256": "28a66ff5d97500f0304f4e8945d936fe0584e0d5b7a6f83258298007a93190ba"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_swift/releases/download/1.13.0/rules_swift.1.13.0.tar.gz",
                         "urls": [],
                         "sha256": "28a66ff5d97500f0304f4e8945d936fe0584e0d5b7a6f83258298007a93190ba",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "build_bazel_rules_swift"
                    },
                    "output_tree_hash": "9e6eb42278684bd709cd716863b02fab099ba6230c568e60e4cc0444457b9e8a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_ruby instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:358:16: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1471:26: in _rules_ruby\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_ruby",
               "generator_name": "rules_ruby",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/protocolbuffers/rules_ruby/archive/37cf5900d0b0e44fa379c0ea3f5fcee0035d77ca.tar.gz"
               ],
               "sha256": "24ed42b7e06907be993b21be603c130076c7d7e49d4f4d5bd228c5656a257f5e",
               "strip_prefix": "rules_ruby-37cf5900d0b0e44fa379c0ea3f5fcee0035d77ca"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/protocolbuffers/rules_ruby/archive/37cf5900d0b0e44fa379c0ea3f5fcee0035d77ca.tar.gz"
                         ],
                         "sha256": "24ed42b7e06907be993b21be603c130076c7d7e49d4f4d5bd228c5656a257f5e",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_ruby-37cf5900d0b0e44fa379c0ea3f5fcee0035d77ca",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_ruby"
                    },
                    "output_tree_hash": "adcba3091249b57fb851b5ff6fe3fec48d7cd0dc048b11b9b8aaa1ece2eb42b9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__zipp instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__zipp",
               "generator_name": "pypi__zipp",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/8c/08/d3006317aefe25ea79d3b76c9650afabaf6d63d1c8443b236e7405447503/zipp-3.16.2-py3-none-any.whl",
               "sha256": "679e51dd4403591b2d6838a48de3d283f3d188412a9782faadf845f298736ba0",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/8c/08/d3006317aefe25ea79d3b76c9650afabaf6d63d1c8443b236e7405447503/zipp-3.16.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "679e51dd4403591b2d6838a48de3d283f3d188412a9782faadf845f298736ba0",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__zipp"
                    },
                    "output_tree_hash": "cbbd66feba955df87dd3e2b41984f9952944c17d8454ac1078477c13d4e86695"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__wheel instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__wheel",
               "generator_name": "pypi__wheel",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/b8/8b/31273bf66016be6ad22bb7345c37ff350276cfd46e389a0c2ac5da9d9073/wheel-0.41.2-py3-none-any.whl",
               "sha256": "75909db2664838d015e3d9139004ee16711748a52c8f336b52882266540215d8",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/b8/8b/31273bf66016be6ad22bb7345c37ff350276cfd46e389a0c2ac5da9d9073/wheel-0.41.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "75909db2664838d015e3d9139004ee16711748a52c8f336b52882266540215d8",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__wheel"
                    },
                    "output_tree_hash": "ad24b5d7c08fae04832b31496db847058d9d7181bea4fe2a8a49e77644b59e2a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__tomli instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__tomli",
               "generator_name": "pypi__tomli",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
               "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__tomli"
                    },
                    "output_tree_hash": "f9a1c7504cb442c93fd0ba6fad73302a929d58fa4ec63d9e58722761310453f6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__setuptools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__setuptools",
               "generator_name": "pypi__setuptools",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/4f/ab/0bcfebdfc3bfa8554b2b2c97a555569c4c1ebc74ea288741ea8326c51906/setuptools-68.1.2-py3-none-any.whl",
               "sha256": "3d8083eed2d13afc9426f227b24fd1659489ec107c0e86cec2ffdde5c92e790b",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/4f/ab/0bcfebdfc3bfa8554b2b2c97a555569c4c1ebc74ea288741ea8326c51906/setuptools-68.1.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "3d8083eed2d13afc9426f227b24fd1659489ec107c0e86cec2ffdde5c92e790b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__setuptools"
                    },
                    "output_tree_hash": "1e403fa09bc264da438adf1ca6ded7c2b5da30ce829d74ca392e0686c358ab86"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pyproject_hooks instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pyproject_hooks",
               "generator_name": "pypi__pyproject_hooks",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d5/ea/9ae603de7fbb3df820b23a70f6aff92bf8c7770043254ad8d2dc9d6bcba4/pyproject_hooks-1.0.0-py3-none-any.whl",
               "sha256": "283c11acd6b928d2f6a7c73fa0d01cb2bdc5f07c57a2eeb6e83d5e56b97976f8",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d5/ea/9ae603de7fbb3df820b23a70f6aff92bf8c7770043254ad8d2dc9d6bcba4/pyproject_hooks-1.0.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "283c11acd6b928d2f6a7c73fa0d01cb2bdc5f07c57a2eeb6e83d5e56b97976f8",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pyproject_hooks"
                    },
                    "output_tree_hash": "f24d9c91fad41ab5a5d889d1a7b7406737c056a8a4f93e7eca8f8e34188f3487"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip_tools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip_tools",
               "generator_name": "pypi__pip_tools",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e8/df/47e6267c6b5cdae867adbdd84b437393e6202ce4322de0a5e0b92960e1d6/pip_tools-7.3.0-py3-none-any.whl",
               "sha256": "8717693288720a8c6ebd07149c93ab0be1fced0b5191df9e9decd3263e20d85e",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e8/df/47e6267c6b5cdae867adbdd84b437393e6202ce4322de0a5e0b92960e1d6/pip_tools-7.3.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "8717693288720a8c6ebd07149c93ab0be1fced0b5191df9e9decd3263e20d85e",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip_tools"
                    },
                    "output_tree_hash": "7ca9b21b0609bdcde4ab5eca317a7efb407cc27701d174791b1983c54be94101"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository build_bazel_apple_support instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:33:29: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:114:15: in apple_rules_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/build_bazel_rules_apple/apple/repositories.bzl:86:14: in _maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_apple_support",
               "generator_name": "build_bazel_apple_support",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "url": "https://github.com/bazelbuild/apple_support/releases/download/1.11.1/apple_support.1.11.1.tar.gz",
               "sha256": "cf4d63f39c7ba9059f70e995bf5fe1019267d3f77379c2028561a5d7645ef67c"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/apple_support/releases/download/1.11.1/apple_support.1.11.1.tar.gz",
                         "urls": [],
                         "sha256": "cf4d63f39c7ba9059f70e995bf5fe1019267d3f77379c2028561a5d7645ef67c",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "build_bazel_apple_support"
                    },
                    "output_tree_hash": "ebcc105aae2ceefe3bc84019a2ce9f88def6a7d4bc7806f43e4ddf5de5641922"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__build instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__build",
               "generator_name": "pypi__build",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/58/91/17b00d5fac63d3dca605f1b8269ba3c65e98059e1fd99d00283e42a454f0/build-0.10.0-py3-none-any.whl",
               "sha256": "af266720050a66c893a6096a2f410989eeac74ff9a68ba194b3f6473e8e26171",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/58/91/17b00d5fac63d3dca605f1b8269ba3c65e98059e1fd99d00283e42a454f0/build-0.10.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "af266720050a66c893a6096a2f410989eeac74ff9a68ba194b3f6473e8e26171",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__build"
                    },
                    "output_tree_hash": "f8420d837a49b784a1053ecfe18edfefc650babd40dc89e4c16ce1e28405f346"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__click instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__click",
               "generator_name": "pypi__click",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
               "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
                         "urls": [],
                         "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__click"
                    },
                    "output_tree_hash": "047fcc2ac986c4735231f85831ef0287d18d6a50ece4f6396880382e74816ca5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip",
               "generator_name": "pypi__pip",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/50/c2/e06851e8cc28dcad7c155f4753da8833ac06a5c704c109313b8d5a62968a/pip-23.2.1-py3-none-any.whl",
               "sha256": "7ccf472345f20d35bdc9d1841ff5f313260c2c33fe417f48c30ac46cccabf5be",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/50/c2/e06851e8cc28dcad7c155f4753da8833ac06a5c704c109313b8d5a62968a/pip-23.2.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "7ccf472345f20d35bdc9d1841ff5f313260c2c33fe417f48c30ac46cccabf5be",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip"
                    },
                    "output_tree_hash": "9f0c16c4495119f12c5b0216e7ffa593dd205861fd7a1e2b3e3161c2be1cd6d4"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__colorama instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__colorama",
               "generator_name": "pypi__colorama",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
               "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__colorama"
                    },
                    "output_tree_hash": "b4b748db844b7bd5ddd33b18b4c247920bee533f0c9317770ff8af88bd2e0b68"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__importlib_metadata instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__importlib_metadata",
               "generator_name": "pypi__importlib_metadata",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/cc/37/db7ba97e676af155f5fcb1a35466f446eadc9104e25b83366e8088c9c926/importlib_metadata-6.8.0-py3-none-any.whl",
               "sha256": "3ebb78df84a805d7698245025b975d9d67053cd94c79245ba4b3eb694abe68bb",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/cc/37/db7ba97e676af155f5fcb1a35466f446eadc9104e25b83366e8088c9c926/importlib_metadata-6.8.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "3ebb78df84a805d7698245025b975d9d67053cd94c79245ba4b3eb694abe68bb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__importlib_metadata"
                    },
                    "output_tree_hash": "68ada03376b21287724dd6aa4c41c70c8cfe84d577bd8feb29519df118201eda"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pep517 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pep517",
               "generator_name": "pypi__pep517",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
               "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pep517"
                    },
                    "output_tree_hash": "1363a557a4f8c410257bdcdd71176a058f243bd04cf881bc3a3028439e2f31e3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__packaging instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__packaging",
               "generator_name": "pypi__packaging",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ab/c3/57f0601a2d4fe15de7a553c00adbc901425661bf048f2a22dfc500caf121/packaging-23.1-py3-none-any.whl",
               "sha256": "994793af429502c4ea2ebf6bf664629d07c1a9fe974af92966e4b8d2df7edc61",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ab/c3/57f0601a2d4fe15de7a553c00adbc901425661bf048f2a22dfc500caf121/packaging-23.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "994793af429502c4ea2ebf6bf664629d07c1a9fe974af92966e4b8d2df7edc61",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__packaging"
                    },
                    "output_tree_hash": "e3f8328f3612caed62375fea5c319a07c4c5fd43fce351e8be027849fd817c27"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__installer instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__installer",
               "generator_name": "pypi__installer",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
               "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__installer"
                    },
                    "output_tree_hash": "4384d89d32a9ff4be9389762f11abe965b5d381906a1e3e3f76983907a3c908e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__more_itertools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:26:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories_extra.bzl:23:20: in envoy_dependencies_extra\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/repositories.bzl:65:29: in py_repositories\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/repositories.bzl:137:14: in pip_install_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__more_itertools",
               "generator_name": "pypi__more_itertools",
               "generator_function": "envoy_dependencies_extra",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/5a/cb/6dce742ea14e47d6f565589e859ad225f2a5de576d7696e0623b784e226b/more_itertools-10.1.0-py3-none-any.whl",
               "sha256": "64e0735fcfdc6f3464ea133afe8ea4483b1c5fe3a3d69852e6503b43a0b222e6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/5a/cb/6dce742ea14e47d6f565589e859ad225f2a5de576d7696e0623b784e226b/more_itertools-10.1.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "64e0735fcfdc6f3464ea133afe8ea4483b1c5fe3a3d69852e6503b43a0b222e6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__more_itertools"
                    },
                    "output_tree_hash": "c1b7c56059fa7fd3ba99306b2b6dbca15a4eea03cf742339ba2528254593c763"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_iniconfig instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_iniconfig",
               "generator_name": "nh_pip3_iniconfig",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "iniconfig==2.0.0     --hash=sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3     --hash=sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_iniconfig",
                         "generator_name": "nh_pip3_iniconfig",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "iniconfig==2.0.0     --hash=sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3     --hash=sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "4229be89f3e99db53407a55feb303dfa11b0b1bcddb3cebb30b70b88724f6f3d"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pyyaml instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pyyaml",
               "generator_name": "nh_pip3_pyyaml",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pyyaml==6.0.1     --hash=sha256:04ac92ad1925b2cff1db0cfebffb6ffc43457495c9b3c39d3fcae417d7125dc5     --hash=sha256:062582fca9fabdd2c8b54a3ef1c978d786e0f6b3a1510e0ac93ef59e0ddae2bc     --hash=sha256:0d3304d8c0adc42be59c5f8a4d9e3d7379e6955ad754aa9d6ab7a398b59dd1df     --hash=sha256:1635fd110e8d85d55237ab316b5b011de701ea0f29d07611174a1b42f1444741     --hash=sha256:184c5108a2aca3c5b3d3bf9395d50893a7ab82a38004c8f61c258d4428e80206     --hash=sha256:18aeb1bf9a78867dc38b259769503436b7c72f7a1f1f4c93ff9a17de54319b27     --hash=sha256:1d4c7e777c441b20e32f52bd377e0c409713e8bb1386e1099c2415f26e479595     --hash=sha256:1e2722cc9fbb45d9b87631ac70924c11d3a401b2d7f410cc0e3bbf249f2dca62     --hash=sha256:1fe35611261b29bd1de0070f0b2f47cb6ff71fa6595c077e42bd0c419fa27b98     --hash=sha256:28c119d996beec18c05208a8bd78cbe4007878c6dd15091efb73a30e90539696     --hash=sha256:326c013efe8048858a6d312ddd31d56e468118ad4cdeda36c719bf5bb6192290     --hash=sha256:40df9b996c2b73138957fe23a16a4f0ba614f4c0efce1e9406a184b6d07fa3a9     --hash=sha256:42f8152b8dbc4fe7d96729ec2b99c7097d656dc1213a3229ca5383f973a5ed6d     --hash=sha256:49a183be227561de579b4a36efbb21b3eab9651dd81b1858589f796549873dd6     --hash=sha256:4fb147e7a67ef577a588a0e2c17b6db51dda102c71de36f8549b6816a96e1867     --hash=sha256:50550eb667afee136e9a77d6dc71ae76a44df8b3e51e41b77f6de2932bfe0f47     --hash=sha256:510c9deebc5c0225e8c96813043e62b680ba2f9c50a08d3724c7f28a747d1486     --hash=sha256:5773183b6446b2c99bb77e77595dd486303b4faab2b086e7b17bc6bef28865f6     --hash=sha256:596106435fa6ad000c2991a98fa58eeb8656ef2325d7e158344fb33864ed87e3     --hash=sha256:6965a7bc3cf88e5a1c3bd2e0b5c22f8d677dc88a455344035f03399034eb3007     --hash=sha256:69b023b2b4daa7548bcfbd4aa3da05b3a74b772db9e23b982788168117739938     --hash=sha256:6c22bec3fbe2524cde73d7ada88f6566758a8f7227bfbf93a408a9d86bcc12a0     --hash=sha256:704219a11b772aea0d8ecd7058d0082713c3562b4e271b849ad7dc4a5c90c13c     --hash=sha256:7e07cbde391ba96ab58e532ff4803f79c4129397514e1413a7dc761ccd755735     --hash=sha256:81e0b275a9ecc9c0c0c07b4b90ba548307583c125f54d5b6946cfee6360c733d     --hash=sha256:855fb52b0dc35af121542a76b9a84f8d1cd886ea97c84703eaa6d88e37a2ad28     --hash=sha256:8d4e9c88387b0f5c7d5f281e55304de64cf7f9c0021a3525bd3b1c542da3b0e4     --hash=sha256:9046c58c4395dff28dd494285c82ba00b546adfc7ef001486fbf0324bc174fba     --hash=sha256:9eb6caa9a297fc2c2fb8862bc5370d0303ddba53ba97e71f08023b6cd73d16a8     --hash=sha256:a08c6f0fe150303c1c6b71ebcd7213c2858041a7e01975da3a99aed1e7a378ef     --hash=sha256:a0cd17c15d3bb3fa06978b4e8958dcdc6e0174ccea823003a106c7d4d7899ac5     --hash=sha256:afd7e57eddb1a54f0f1a974bc4391af8bcce0b444685d936840f125cf046d5bd     --hash=sha256:b1275ad35a5d18c62a7220633c913e1b42d44b46ee12554e5fd39c70a243d6a3     --hash=sha256:b786eecbdf8499b9ca1d697215862083bd6d2a99965554781d0d8d1ad31e13a0     --hash=sha256:ba336e390cd8e4d1739f42dfe9bb83a3cc2e80f567d8805e11b46f4a943f5515     --hash=sha256:baa90d3f661d43131ca170712d903e6295d1f7a0f595074f151c0aed377c9b9c     --hash=sha256:bc1bf2925a1ecd43da378f4db9e4f799775d6367bdb94671027b73b393a7c42c     --hash=sha256:bd4af7373a854424dabd882decdc5579653d7868b8fb26dc7d0e99f823aa5924     --hash=sha256:bf07ee2fef7014951eeb99f56f39c9bb4af143d8aa3c21b1677805985307da34     --hash=sha256:bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43     --hash=sha256:c8098ddcc2a85b61647b2590f825f3db38891662cfc2fc776415143f599bb859     --hash=sha256:d2b04aac4d386b172d5b9692e2d2da8de7bfb6c387fa4f801fbf6fb2e6ba4673     --hash=sha256:d483d2cdf104e7c9fa60c544d92981f12ad66a457afae824d146093b8c294c54     --hash=sha256:d858aa552c999bc8a8d57426ed01e40bef403cd8ccdd0fc5f6f04a00414cac2a     --hash=sha256:e7d73685e87afe9f3b36c799222440d6cf362062f78be1013661b00c5c6f678b     --hash=sha256:f003ed9ad21d6a4713f0a9b5a7a0a79e08dd0f221aff4525a2be4c346ee60aab     --hash=sha256:f22ac1c3cac4dbc50079e965eba2c1058622631e526bd9afd45fedd49ba781fa     --hash=sha256:faca3bdcf85b2fc05d06ff3fbc1f83e1391b3e724afa3feba7d13eeab355484c     --hash=sha256:fca0e3a251908a499833aa292323f32437106001d436eca0e6e7833256674585     --hash=sha256:fd1592b3fdf65fff2ad0004b5e363300ef59ced41c2e6b3a99d4089fa8c5435d     --hash=sha256:fd66fc5d0da6d9815ba2cebeb4205f95818ff4b79c3ebe268e75d961704af52f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pyyaml",
                         "generator_name": "nh_pip3_pyyaml",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pyyaml==6.0.1     --hash=sha256:04ac92ad1925b2cff1db0cfebffb6ffc43457495c9b3c39d3fcae417d7125dc5     --hash=sha256:062582fca9fabdd2c8b54a3ef1c978d786e0f6b3a1510e0ac93ef59e0ddae2bc     --hash=sha256:0d3304d8c0adc42be59c5f8a4d9e3d7379e6955ad754aa9d6ab7a398b59dd1df     --hash=sha256:1635fd110e8d85d55237ab316b5b011de701ea0f29d07611174a1b42f1444741     --hash=sha256:184c5108a2aca3c5b3d3bf9395d50893a7ab82a38004c8f61c258d4428e80206     --hash=sha256:18aeb1bf9a78867dc38b259769503436b7c72f7a1f1f4c93ff9a17de54319b27     --hash=sha256:1d4c7e777c441b20e32f52bd377e0c409713e8bb1386e1099c2415f26e479595     --hash=sha256:1e2722cc9fbb45d9b87631ac70924c11d3a401b2d7f410cc0e3bbf249f2dca62     --hash=sha256:1fe35611261b29bd1de0070f0b2f47cb6ff71fa6595c077e42bd0c419fa27b98     --hash=sha256:28c119d996beec18c05208a8bd78cbe4007878c6dd15091efb73a30e90539696     --hash=sha256:326c013efe8048858a6d312ddd31d56e468118ad4cdeda36c719bf5bb6192290     --hash=sha256:40df9b996c2b73138957fe23a16a4f0ba614f4c0efce1e9406a184b6d07fa3a9     --hash=sha256:42f8152b8dbc4fe7d96729ec2b99c7097d656dc1213a3229ca5383f973a5ed6d     --hash=sha256:49a183be227561de579b4a36efbb21b3eab9651dd81b1858589f796549873dd6     --hash=sha256:4fb147e7a67ef577a588a0e2c17b6db51dda102c71de36f8549b6816a96e1867     --hash=sha256:50550eb667afee136e9a77d6dc71ae76a44df8b3e51e41b77f6de2932bfe0f47     --hash=sha256:510c9deebc5c0225e8c96813043e62b680ba2f9c50a08d3724c7f28a747d1486     --hash=sha256:5773183b6446b2c99bb77e77595dd486303b4faab2b086e7b17bc6bef28865f6     --hash=sha256:596106435fa6ad000c2991a98fa58eeb8656ef2325d7e158344fb33864ed87e3     --hash=sha256:6965a7bc3cf88e5a1c3bd2e0b5c22f8d677dc88a455344035f03399034eb3007     --hash=sha256:69b023b2b4daa7548bcfbd4aa3da05b3a74b772db9e23b982788168117739938     --hash=sha256:6c22bec3fbe2524cde73d7ada88f6566758a8f7227bfbf93a408a9d86bcc12a0     --hash=sha256:704219a11b772aea0d8ecd7058d0082713c3562b4e271b849ad7dc4a5c90c13c     --hash=sha256:7e07cbde391ba96ab58e532ff4803f79c4129397514e1413a7dc761ccd755735     --hash=sha256:81e0b275a9ecc9c0c0c07b4b90ba548307583c125f54d5b6946cfee6360c733d     --hash=sha256:855fb52b0dc35af121542a76b9a84f8d1cd886ea97c84703eaa6d88e37a2ad28     --hash=sha256:8d4e9c88387b0f5c7d5f281e55304de64cf7f9c0021a3525bd3b1c542da3b0e4     --hash=sha256:9046c58c4395dff28dd494285c82ba00b546adfc7ef001486fbf0324bc174fba     --hash=sha256:9eb6caa9a297fc2c2fb8862bc5370d0303ddba53ba97e71f08023b6cd73d16a8     --hash=sha256:a08c6f0fe150303c1c6b71ebcd7213c2858041a7e01975da3a99aed1e7a378ef     --hash=sha256:a0cd17c15d3bb3fa06978b4e8958dcdc6e0174ccea823003a106c7d4d7899ac5     --hash=sha256:afd7e57eddb1a54f0f1a974bc4391af8bcce0b444685d936840f125cf046d5bd     --hash=sha256:b1275ad35a5d18c62a7220633c913e1b42d44b46ee12554e5fd39c70a243d6a3     --hash=sha256:b786eecbdf8499b9ca1d697215862083bd6d2a99965554781d0d8d1ad31e13a0     --hash=sha256:ba336e390cd8e4d1739f42dfe9bb83a3cc2e80f567d8805e11b46f4a943f5515     --hash=sha256:baa90d3f661d43131ca170712d903e6295d1f7a0f595074f151c0aed377c9b9c     --hash=sha256:bc1bf2925a1ecd43da378f4db9e4f799775d6367bdb94671027b73b393a7c42c     --hash=sha256:bd4af7373a854424dabd882decdc5579653d7868b8fb26dc7d0e99f823aa5924     --hash=sha256:bf07ee2fef7014951eeb99f56f39c9bb4af143d8aa3c21b1677805985307da34     --hash=sha256:bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43     --hash=sha256:c8098ddcc2a85b61647b2590f825f3db38891662cfc2fc776415143f599bb859     --hash=sha256:d2b04aac4d386b172d5b9692e2d2da8de7bfb6c387fa4f801fbf6fb2e6ba4673     --hash=sha256:d483d2cdf104e7c9fa60c544d92981f12ad66a457afae824d146093b8c294c54     --hash=sha256:d858aa552c999bc8a8d57426ed01e40bef403cd8ccdd0fc5f6f04a00414cac2a     --hash=sha256:e7d73685e87afe9f3b36c799222440d6cf362062f78be1013661b00c5c6f678b     --hash=sha256:f003ed9ad21d6a4713f0a9b5a7a0a79e08dd0f221aff4525a2be4c346ee60aab     --hash=sha256:f22ac1c3cac4dbc50079e965eba2c1058622631e526bd9afd45fedd49ba781fa     --hash=sha256:faca3bdcf85b2fc05d06ff3fbc1f83e1391b3e724afa3feba7d13eeab355484c     --hash=sha256:fca0e3a251908a499833aa292323f32437106001d436eca0e6e7833256674585     --hash=sha256:fd1592b3fdf65fff2ad0004b5e363300ef59ced41c2e6b3a99d4089fa8c5435d     --hash=sha256:fd66fc5d0da6d9815ba2cebeb4205f95818ff4b79c3ebe268e75d961704af52f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "e1db1c9960195aaa2c8304ee02a27850f1be88cc4557abbe05de309d58d1d21a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_execnet instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_execnet",
               "generator_name": "nh_pip3_execnet",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "execnet==2.0.2     --hash=sha256:88256416ae766bc9e8895c76a87928c0012183da3cc4fc18016e6f050e025f41     --hash=sha256:cc59bc4423742fd71ad227122eb0dd44db51efb3dc4095b45ac9a08c770096af",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_execnet",
                         "generator_name": "nh_pip3_execnet",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "execnet==2.0.2     --hash=sha256:88256416ae766bc9e8895c76a87928c0012183da3cc4fc18016e6f050e025f41     --hash=sha256:cc59bc4423742fd71ad227122eb0dd44db51efb3dc4095b45ac9a08c770096af",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "8821afe541f2c16b09b1183146d879dbb9d62ddb32cccc787f2e39fc8dcbf073"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_apipkg instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_apipkg",
               "generator_name": "nh_pip3_apipkg",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "apipkg==3.0.2     --hash=sha256:a16984c39de280701f3f6406ed3af658f2a1965011fe7bb5be34fbb48423b411     --hash=sha256:c7aa61a4f82697fdaa667e70af1505acf1f7428b1c27b891d204ba7a8a3c5e0d",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_apipkg",
                         "generator_name": "nh_pip3_apipkg",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "apipkg==3.0.2     --hash=sha256:a16984c39de280701f3f6406ed3af658f2a1965011fe7bb5be34fbb48423b411     --hash=sha256:c7aa61a4f82697fdaa667e70af1505acf1f7428b1c27b891d204ba7a8a3c5e0d",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "49685fa024a3a5b539bf56a15158730df3c8ab552ad06e62a23f776a103eaeed"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pytest_xdist instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pytest_xdist",
               "generator_name": "nh_pip3_pytest_xdist",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pytest-xdist==3.5.0     --hash=sha256:cbb36f3d67e0c478baa57fa4edc8843887e0f6cfc42d677530a36d7472b32d8a     --hash=sha256:d075629c7e00b611df89f490a5063944bee7a4362a5ff11c7cc7824a03dfce24",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pytest_xdist",
                         "generator_name": "nh_pip3_pytest_xdist",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pytest-xdist==3.5.0     --hash=sha256:cbb36f3d67e0c478baa57fa4edc8843887e0f6cfc42d677530a36d7472b32d8a     --hash=sha256:d075629c7e00b611df89f490a5063944bee7a4362a5ff11c7cc7824a03dfce24",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "e10f20787cd6842fc08af92f5d880d4d07d73fef2abe748e23475022413fc0d8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_packaging instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_packaging",
               "generator_name": "nh_pip3_packaging",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "packaging==23.2     --hash=sha256:048fb0e9405036518eaaf48a55953c750c11e1a1b68e0dd1a9d62ed0c092cfc5     --hash=sha256:8c491190033a9af7e1d931d0b5dacc2ef47509b34dd0de67ed209b5203fc88c7",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_packaging",
                         "generator_name": "nh_pip3_packaging",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "packaging==23.2     --hash=sha256:048fb0e9405036518eaaf48a55953c750c11e1a1b68e0dd1a9d62ed0c092cfc5     --hash=sha256:8c491190033a9af7e1d931d0b5dacc2ef47509b34dd0de67ed209b5203fc88c7",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "1e22f6ca93e4c599950e02da0297ef7a199eeba12c9c33e748bff75dc699d720"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_importlib_metadata instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_importlib_metadata",
               "generator_name": "nh_pip3_importlib_metadata",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "importlib-metadata==7.0.1     --hash=sha256:4805911c3a4ec7c3966410053e9ec6a1fecd629117df5adee56dfc9432a1081e     --hash=sha256:f238736bb06590ae52ac1fab06a3a9ef1d8dce2b7a35b5ab329371d6c8f5d2cc",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_importlib_metadata",
                         "generator_name": "nh_pip3_importlib_metadata",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "importlib-metadata==7.0.1     --hash=sha256:4805911c3a4ec7c3966410053e9ec6a1fecd629117df5adee56dfc9432a1081e     --hash=sha256:f238736bb06590ae52ac1fab06a3a9ef1d8dce2b7a35b5ab329371d6c8f5d2cc",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "6ad992e54778d750e586ee51cfec64060aae2fa1c26dfe5a257d7e2ec26f8ca6"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_more_itertools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_more_itertools",
               "generator_name": "nh_pip3_more_itertools",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "more-itertools==10.2.0     --hash=sha256:686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684     --hash=sha256:8fccb480c43d3e99a00087634c06dd02b0d50fbf088b380de5a41a015ec239e1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_more_itertools",
                         "generator_name": "nh_pip3_more_itertools",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "more-itertools==10.2.0     --hash=sha256:686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684     --hash=sha256:8fccb480c43d3e99a00087634c06dd02b0d50fbf088b380de5a41a015ec239e1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "ddfc8df1f232e5fc86c76ca1fad4f608c9121dae1923be414aba464664e788e1"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_six instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_six",
               "generator_name": "nh_pip3_six",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "six==1.16.0     --hash=sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926     --hash=sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_six",
                         "generator_name": "nh_pip3_six",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "six==1.16.0     --hash=sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926     --hash=sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "74596f215078a28efe417e8746c5e4bddcecc70d873095d416806c536fb44e5e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_py instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_py",
               "generator_name": "nh_pip3_py",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "py==1.11.0     --hash=sha256:51c75c4126074b472f746a24399ad32f6053d1b34b68d2fa41e558e6f4a98719     --hash=sha256:607c53218732647dff4acdfcd50cb62615cedf612e72d1724fb1a0cc6405b378",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_py",
                         "generator_name": "nh_pip3_py",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "py==1.11.0     --hash=sha256:51c75c4126074b472f746a24399ad32f6053d1b34b68d2fa41e558e6f4a98719     --hash=sha256:607c53218732647dff4acdfcd50cb62615cedf612e72d1724fb1a0cc6405b378",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "2383f7ad0668fb6d62eb5fa176cfa26f663c81a460d0368aad6722200ce3efa9"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pluggy instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pluggy",
               "generator_name": "nh_pip3_pluggy",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pluggy==1.4.0     --hash=sha256:7db9f7b503d67d1c5b95f59773ebb58a8c1c288129a88665838012cfb07b8981     --hash=sha256:8c85c2876142a764e5b7548e7d9a0e0ddb46f5185161049a79b7e974454223be",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pluggy",
                         "generator_name": "nh_pip3_pluggy",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pluggy==1.4.0     --hash=sha256:7db9f7b503d67d1c5b95f59773ebb58a8c1c288129a88665838012cfb07b8981     --hash=sha256:8c85c2876142a764e5b7548e7d9a0e0ddb46f5185161049a79b7e974454223be",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "6632ff68c3d9c8a8440a5594be48f42587d6366699341c641f3aa345ed5a9698"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_zipp instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_zipp",
               "generator_name": "nh_pip3_zipp",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "zipp==3.17.0     --hash=sha256:0e923e726174922dce09c53c59ad483ff7bbb8e572e00c7f7c46b88556409f31     --hash=sha256:84e64a1c28cf7e91ed2078bb8cc8c259cb19b76942096c8d7b84947690cabaf0",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_zipp",
                         "generator_name": "nh_pip3_zipp",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "zipp==3.17.0     --hash=sha256:0e923e726174922dce09c53c59ad483ff7bbb8e572e00c7f7c46b88556409f31     --hash=sha256:84e64a1c28cf7e91ed2078bb8cc8c259cb19b76942096c8d7b84947690cabaf0",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "475964d3884e110b897715e4e4515c2ee91874aae78837e83a5e5ee13515cee7"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_attrs instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_attrs",
               "generator_name": "nh_pip3_attrs",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "attrs==23.2.0     --hash=sha256:935dc3b529c262f6cf76e50877d35a4bd3c1de194fd41f47a2b7ae8f19971f30     --hash=sha256:99b87a485a5820b23b879f04c2305b44b951b502fd64be915879d77a7e8fc6f1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_attrs",
                         "generator_name": "nh_pip3_attrs",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "attrs==23.2.0     --hash=sha256:935dc3b529c262f6cf76e50877d35a4bd3c1de194fd41f47a2b7ae8f19971f30     --hash=sha256:99b87a485a5820b23b879f04c2305b44b951b502fd64be915879d77a7e8fc6f1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "56aa8f096536624c1e4ff0e27d260b4c88d924fee8319fe8bf1df612c7e196e1"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pytest_dependency instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pytest_dependency",
               "generator_name": "nh_pip3_pytest_dependency",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pytest-dependency==0.6.0     --hash=sha256:934b0e6a39d95995062c193f7eaeed8a8ffa06ff1bcef4b62b0dc74a708bacc1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pytest_dependency",
                         "generator_name": "nh_pip3_pytest_dependency",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pytest-dependency==0.6.0     --hash=sha256:934b0e6a39d95995062c193f7eaeed8a8ffa06ff1bcef4b62b0dc74a708bacc1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "165dca331790a9a1cdc46a2219c334fc63b40d392327237e00af1d02cb9e649e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pytest instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pytest",
               "generator_name": "nh_pip3_pytest",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pytest==8.0.0     --hash=sha256:249b1b0864530ba251b7438274c4d251c58d868edaaec8762893ad4a0d71c36c     --hash=sha256:50fb9cbe836c3f20f0dfa99c565201fb75dc54c8d76373cd1bde06b06657bdb6",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pytest",
                         "generator_name": "nh_pip3_pytest",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pytest==8.0.0     --hash=sha256:249b1b0864530ba251b7438274c4d251c58d868edaaec8762893ad4a0d71c36c     --hash=sha256:50fb9cbe836c3f20f0dfa99c565201fb75dc54c8d76373cd1bde06b06657bdb6",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "c791b052dc70d0b60a243646b4880dea19401deff6f343a8f77344386405aa56"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_idna instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_idna",
               "generator_name": "nh_pip3_idna",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "idna==3.6     --hash=sha256:9ecdbbd083b06798ae1e86adcbfe8ab1479cf864e4ee30fe4e46a003d12491ca     --hash=sha256:c05567e9c24a6b9faaa835c4821bad0590fbb9d5779e7caa6e1cc4978e7eb24f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_idna",
                         "generator_name": "nh_pip3_idna",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "idna==3.6     --hash=sha256:9ecdbbd083b06798ae1e86adcbfe8ab1479cf864e4ee30fe4e46a003d12491ca     --hash=sha256:c05567e9c24a6b9faaa835c4821bad0590fbb9d5779e7caa6e1cc4978e7eb24f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "5897633eca6987ddd3fa69ddacda927a07425708118c63892a149b56edefce6e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_certifi instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_certifi",
               "generator_name": "nh_pip3_certifi",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "certifi==2024.2.2     --hash=sha256:0569859f95fc761b18b45ef421b1290a0f65f147e92a1e5eb3e635f9a5e4e66f     --hash=sha256:dc383c07b76109f368f6106eee2b593b04a011ea4d55f652c6ca24a754d1cdd1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_certifi",
                         "generator_name": "nh_pip3_certifi",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "certifi==2024.2.2     --hash=sha256:0569859f95fc761b18b45ef421b1290a0f65f147e92a1e5eb3e635f9a5e4e66f     --hash=sha256:dc383c07b76109f368f6106eee2b593b04a011ea4d55f652c6ca24a754d1cdd1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "350d838cc318faec5b196e1a90c49420c3771d0a92fe769e4baf2226bf0017cc"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_chardet instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_chardet",
               "generator_name": "nh_pip3_chardet",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "chardet==5.2.0     --hash=sha256:1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7     --hash=sha256:e1cf59446890a00105fe7b7912492ea04b6e6f06d4b742b2c788469e34c82970",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_chardet",
                         "generator_name": "nh_pip3_chardet",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "chardet==5.2.0     --hash=sha256:1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7     --hash=sha256:e1cf59446890a00105fe7b7912492ea04b6e6f06d4b742b2c788469e34c82970",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "92fc2c49d281038a61a22c435c78da5f34f4b2189f3abbe2da10675baeda7f5f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_urllib3 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_urllib3",
               "generator_name": "nh_pip3_urllib3",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "urllib3==2.2.0     --hash=sha256:051d961ad0c62a94e50ecf1af379c3aba230c66c710493493560c0c223c49f20     --hash=sha256:ce3711610ddce217e6d113a2732fafad960a03fd0318c91faa79481e35c11224",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_urllib3",
                         "generator_name": "nh_pip3_urllib3",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "urllib3==2.2.0     --hash=sha256:051d961ad0c62a94e50ecf1af379c3aba230c66c710493493560c0c223c49f20     --hash=sha256:ce3711610ddce217e6d113a2732fafad960a03fd0318c91faa79481e35c11224",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "06c856a902f0229ecb0cd2b1bfe95745821710a8fbc291ab3c8897cdc270f63b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_protobuf_protoc_linux_x86_64 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:329:25: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:973:30: in _com_google_protobuf\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_protobuf_protoc_linux_x86_64",
               "generator_name": "com_google_protobuf_protoc_linux_x86_64",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/protocolbuffers/protobuf/releases/download/v24.4/protoc-24.4-linux-x86_64.zip"
               ],
               "sha256": "5871398dfd6ac954a6adebf41f1ae3a4de915a36a6ab2fd3e8f2c00d45b50dec",
               "strip_prefix": "",
               "build_file": "@rules_proto//proto/private:BUILD.protoc"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/protocolbuffers/protobuf/releases/download/v24.4/protoc-24.4-linux-x86_64.zip"
                         ],
                         "sha256": "5871398dfd6ac954a6adebf41f1ae3a4de915a36a6ab2fd3e8f2c00d45b50dec",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@rules_proto//proto/private:BUILD.protoc",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_protobuf_protoc_linux_x86_64"
                    },
                    "output_tree_hash": "3fb012f9b74c521bfa27774b31eb7e1a3a34d985252366a1e8df03111582c37b"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_requests instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_requests",
               "generator_name": "nh_pip3_requests",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "requests==2.31.0     --hash=sha256:58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f     --hash=sha256:942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_requests",
                         "generator_name": "nh_pip3_requests",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "requests==2.31.0     --hash=sha256:58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f     --hash=sha256:942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "40479b024d5ace40fe239eef54daacc22514beb7c081594778ac28f0405ab104"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_cncf_xds instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:28:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_cncf_xds",
               "generator_name": "com_github_cncf_xds",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/cncf/xds/archive/3a472e524827f72d1ad621c4983dd5af54c46776.tar.gz"
               ],
               "sha256": "dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927",
               "strip_prefix": "xds-3a472e524827f72d1ad621c4983dd5af54c46776"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/cncf/xds/archive/3a472e524827f72d1ad621c4983dd5af54c46776.tar.gz"
                         ],
                         "sha256": "dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "xds-3a472e524827f72d1ad621c4983dd5af54c46776",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_cncf_xds"
                    },
                    "output_tree_hash": "9993df793faaf87453f1634fc381559f4a1aa02da25e64879e54eded0d52f9c7"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_charset_normalizer instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_charset_normalizer",
               "generator_name": "nh_pip3_charset_normalizer",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "charset-normalizer==3.3.2     --hash=sha256:06435b539f889b1f6f4ac1758871aae42dc3a8c0e24ac9e60c2384973ad73027     --hash=sha256:06a81e93cd441c56a9b65d8e1d043daeb97a3d0856d177d5c90ba85acb3db087     --hash=sha256:0a55554a2fa0d408816b3b5cedf0045f4b8e1a6065aec45849de2d6f3f8e9786     --hash=sha256:0b2b64d2bb6d3fb9112bafa732def486049e63de9618b5843bcdd081d8144cd8     --hash=sha256:10955842570876604d404661fbccbc9c7e684caf432c09c715ec38fbae45ae09     --hash=sha256:122c7fa62b130ed55f8f285bfd56d5f4b4a5b503609d181f9ad85e55c89f4185     --hash=sha256:1ceae2f17a9c33cb48e3263960dc5fc8005351ee19db217e9b1bb15d28c02574     --hash=sha256:1d3193f4a680c64b4b6a9115943538edb896edc190f0b222e73761716519268e     --hash=sha256:1f79682fbe303db92bc2b1136016a38a42e835d932bab5b3b1bfcfbf0640e519     --hash=sha256:2127566c664442652f024c837091890cb1942c30937add288223dc895793f898     --hash=sha256:22afcb9f253dac0696b5a4be4a1c0f8762f8239e21b99680099abd9b2b1b2269     --hash=sha256:25baf083bf6f6b341f4121c2f3c548875ee6f5339300e08be3f2b2ba1721cdd3     --hash=sha256:2e81c7b9c8979ce92ed306c249d46894776a909505d8f5a4ba55b14206e3222f     --hash=sha256:3287761bc4ee9e33561a7e058c72ac0938c4f57fe49a09eae428fd88aafe7bb6     --hash=sha256:34d1c8da1e78d2e001f363791c98a272bb734000fcef47a491c1e3b0505657a8     --hash=sha256:37e55c8e51c236f95b033f6fb391d7d7970ba5fe7ff453dad675e88cf303377a     --hash=sha256:3d47fa203a7bd9c5b6cee4736ee84ca03b8ef23193c0d1ca99b5089f72645c73     --hash=sha256:3e4d1f6587322d2788836a99c69062fbb091331ec940e02d12d179c1d53e25fc     --hash=sha256:42cb296636fcc8b0644486d15c12376cb9fa75443e00fb25de0b8602e64c1714     --hash=sha256:45485e01ff4d3630ec0d9617310448a8702f70e9c01906b0d0118bdf9d124cf2     --hash=sha256:4a78b2b446bd7c934f5dcedc588903fb2f5eec172f3d29e52a9096a43722adfc     --hash=sha256:4ab2fe47fae9e0f9dee8c04187ce5d09f48eabe611be8259444906793ab7cbce     --hash=sha256:4d0d1650369165a14e14e1e47b372cfcb31d6ab44e6e33cb2d4e57265290044d     --hash=sha256:549a3a73da901d5bc3ce8d24e0600d1fa85524c10287f6004fbab87672bf3e1e     --hash=sha256:55086ee1064215781fff39a1af09518bc9255b50d6333f2e4c74ca09fac6a8f6     --hash=sha256:572c3763a264ba47b3cf708a44ce965d98555f618ca42c926a9c1616d8f34269     --hash=sha256:573f6eac48f4769d667c4442081b1794f52919e7edada77495aaed9236d13a96     --hash=sha256:5b4c145409bef602a690e7cfad0a15a55c13320ff7a3ad7ca59c13bb8ba4d45d     --hash=sha256:6463effa3186ea09411d50efc7d85360b38d5f09b870c48e4600f63af490e56a     --hash=sha256:65f6f63034100ead094b8744b3b97965785388f308a64cf8d7c34f2f2e5be0c4     --hash=sha256:663946639d296df6a2bb2aa51b60a2454ca1cb29835324c640dafb5ff2131a77     --hash=sha256:6897af51655e3691ff853668779c7bad41579facacf5fd7253b0133308cf000d     --hash=sha256:68d1f8a9e9e37c1223b656399be5d6b448dea850bed7d0f87a8311f1ff3dabb0     --hash=sha256:6ac7ffc7ad6d040517be39eb591cac5ff87416c2537df6ba3cba3bae290c0fed     --hash=sha256:6b3251890fff30ee142c44144871185dbe13b11bab478a88887a639655be1068     --hash=sha256:6c4caeef8fa63d06bd437cd4bdcf3ffefe6738fb1b25951440d80dc7df8c03ac     --hash=sha256:6ef1d82a3af9d3eecdba2321dc1b3c238245d890843e040e41e470ffa64c3e25     --hash=sha256:753f10e867343b4511128c6ed8c82f7bec3bd026875576dfd88483c5c73b2fd8     --hash=sha256:7cd13a2e3ddeed6913a65e66e94b51d80a041145a026c27e6bb76c31a853c6ab     --hash=sha256:7ed9e526742851e8d5cc9e6cf41427dfc6068d4f5a3bb03659444b4cabf6bc26     --hash=sha256:7f04c839ed0b6b98b1a7501a002144b76c18fb1c1850c8b98d458ac269e26ed2     --hash=sha256:802fe99cca7457642125a8a88a084cef28ff0cf9407060f7b93dca5aa25480db     --hash=sha256:80402cd6ee291dcb72644d6eac93785fe2c8b9cb30893c1af5b8fdd753b9d40f     --hash=sha256:8465322196c8b4d7ab6d1e049e4c5cb460d0394da4a27d23cc242fbf0034b6b5     --hash=sha256:86216b5cee4b06df986d214f664305142d9c76df9b6512be2738aa72a2048f99     --hash=sha256:87d1351268731db79e0f8e745d92493ee2841c974128ef629dc518b937d9194c     --hash=sha256:8bdb58ff7ba23002a4c5808d608e4e6c687175724f54a5dade5fa8c67b604e4d     --hash=sha256:8c622a5fe39a48f78944a87d4fb8a53ee07344641b0562c540d840748571b811     --hash=sha256:8d756e44e94489e49571086ef83b2bb8ce311e730092d2c34ca8f7d925cb20aa     --hash=sha256:8f4a014bc36d3c57402e2977dada34f9c12300af536839dc38c0beab8878f38a     --hash=sha256:9063e24fdb1e498ab71cb7419e24622516c4a04476b17a2dab57e8baa30d6e03     --hash=sha256:90d558489962fd4918143277a773316e56c72da56ec7aa3dc3dbbe20fdfed15b     --hash=sha256:923c0c831b7cfcb071580d3f46c4baf50f174be571576556269530f4bbd79d04     --hash=sha256:95f2a5796329323b8f0512e09dbb7a1860c46a39da62ecb2324f116fa8fdc85c     --hash=sha256:96b02a3dc4381e5494fad39be677abcb5e6634bf7b4fa83a6dd3112607547001     --hash=sha256:9f96df6923e21816da7e0ad3fd47dd8f94b2a5ce594e00677c0013018b813458     --hash=sha256:a10af20b82360ab00827f916a6058451b723b4e65030c5a18577c8b2de5b3389     --hash=sha256:a50aebfa173e157099939b17f18600f72f84eed3049e743b68ad15bd69b6bf99     --hash=sha256:a981a536974bbc7a512cf44ed14938cf01030a99e9b3a06dd59578882f06f985     --hash=sha256:a9a8e9031d613fd2009c182b69c7b2c1ef8239a0efb1df3f7c8da66d5dd3d537     --hash=sha256:ae5f4161f18c61806f411a13b0310bea87f987c7d2ecdbdaad0e94eb2e404238     --hash=sha256:aed38f6e4fb3f5d6bf81bfa990a07806be9d83cf7bacef998ab1a9bd660a581f     --hash=sha256:b01b88d45a6fcb69667cd6d2f7a9aeb4bf53760d7fc536bf679ec94fe9f3ff3d     --hash=sha256:b261ccdec7821281dade748d088bb6e9b69e6d15b30652b74cbbac25e280b796     --hash=sha256:b2b0a0c0517616b6869869f8c581d4eb2dd83a4d79e0ebcb7d373ef9956aeb0a     --hash=sha256:b4a23f61ce87adf89be746c8a8974fe1c823c891d8f86eb218bb957c924bb143     --hash=sha256:bd8f7df7d12c2db9fab40bdd87a7c09b1530128315d047a086fa3ae3435cb3a8     --hash=sha256:beb58fe5cdb101e3a055192ac291b7a21e3b7ef4f67fa1d74e331a7f2124341c     --hash=sha256:c002b4ffc0be611f0d9da932eb0f704fe2602a9a949d1f738e4c34c75b0863d5     --hash=sha256:c083af607d2515612056a31f0a8d9e0fcb5876b7bfc0abad3ecd275bc4ebc2d5     --hash=sha256:c180f51afb394e165eafe4ac2936a14bee3eb10debc9d9e4db8958fe36afe711     --hash=sha256:c235ebd9baae02f1b77bcea61bce332cb4331dc3617d254df3323aa01ab47bd4     --hash=sha256:cd70574b12bb8a4d2aaa0094515df2463cb429d8536cfb6c7ce983246983e5a6     --hash=sha256:d0eccceffcb53201b5bfebb52600a5fb483a20b61da9dbc885f8b103cbe7598c     --hash=sha256:d965bba47ddeec8cd560687584e88cf699fd28f192ceb452d1d7ee807c5597b7     --hash=sha256:db364eca23f876da6f9e16c9da0df51aa4f104a972735574842618b8c6d999d4     --hash=sha256:ddbb2551d7e0102e7252db79ba445cdab71b26640817ab1e3e3648dad515003b     --hash=sha256:deb6be0ac38ece9ba87dea880e438f25ca3eddfac8b002a2ec3d9183a454e8ae     --hash=sha256:e06ed3eb3218bc64786f7db41917d4e686cc4856944f53d5bdf83a6884432e12     --hash=sha256:e27ad930a842b4c5eb8ac0016b0a54f5aebbe679340c26101df33424142c143c     --hash=sha256:e537484df0d8f426ce2afb2d0f8e1c3d0b114b83f8850e5f2fbea0e797bd82ae     --hash=sha256:eb00ed941194665c332bf8e078baf037d6c35d7c4f3102ea2d4f16ca94a26dc8     --hash=sha256:eb6904c354526e758fda7167b33005998fb68c46fbc10e013ca97f21ca5c8887     --hash=sha256:eb8821e09e916165e160797a6c17edda0679379a4be5c716c260e836e122f54b     --hash=sha256:efcb3f6676480691518c177e3b465bcddf57cea040302f9f4e6e191af91174d4     --hash=sha256:f27273b60488abe721a075bcca6d7f3964f9f6f067c8c4c605743023d7d3944f     --hash=sha256:f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5     --hash=sha256:fb69256e180cb6c8a894fee62b3afebae785babc1ee98b81cdf68bbca1987f33     --hash=sha256:fd1abc0d89e30cc4e02e4064dc67fcc51bd941eb395c502aac3ec19fab46b519     --hash=sha256:ff8fa367d09b717b2a17a052544193ad76cd49979c805768879cb63d9ca50561",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_charset_normalizer",
                         "generator_name": "nh_pip3_charset_normalizer",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "charset-normalizer==3.3.2     --hash=sha256:06435b539f889b1f6f4ac1758871aae42dc3a8c0e24ac9e60c2384973ad73027     --hash=sha256:06a81e93cd441c56a9b65d8e1d043daeb97a3d0856d177d5c90ba85acb3db087     --hash=sha256:0a55554a2fa0d408816b3b5cedf0045f4b8e1a6065aec45849de2d6f3f8e9786     --hash=sha256:0b2b64d2bb6d3fb9112bafa732def486049e63de9618b5843bcdd081d8144cd8     --hash=sha256:10955842570876604d404661fbccbc9c7e684caf432c09c715ec38fbae45ae09     --hash=sha256:122c7fa62b130ed55f8f285bfd56d5f4b4a5b503609d181f9ad85e55c89f4185     --hash=sha256:1ceae2f17a9c33cb48e3263960dc5fc8005351ee19db217e9b1bb15d28c02574     --hash=sha256:1d3193f4a680c64b4b6a9115943538edb896edc190f0b222e73761716519268e     --hash=sha256:1f79682fbe303db92bc2b1136016a38a42e835d932bab5b3b1bfcfbf0640e519     --hash=sha256:2127566c664442652f024c837091890cb1942c30937add288223dc895793f898     --hash=sha256:22afcb9f253dac0696b5a4be4a1c0f8762f8239e21b99680099abd9b2b1b2269     --hash=sha256:25baf083bf6f6b341f4121c2f3c548875ee6f5339300e08be3f2b2ba1721cdd3     --hash=sha256:2e81c7b9c8979ce92ed306c249d46894776a909505d8f5a4ba55b14206e3222f     --hash=sha256:3287761bc4ee9e33561a7e058c72ac0938c4f57fe49a09eae428fd88aafe7bb6     --hash=sha256:34d1c8da1e78d2e001f363791c98a272bb734000fcef47a491c1e3b0505657a8     --hash=sha256:37e55c8e51c236f95b033f6fb391d7d7970ba5fe7ff453dad675e88cf303377a     --hash=sha256:3d47fa203a7bd9c5b6cee4736ee84ca03b8ef23193c0d1ca99b5089f72645c73     --hash=sha256:3e4d1f6587322d2788836a99c69062fbb091331ec940e02d12d179c1d53e25fc     --hash=sha256:42cb296636fcc8b0644486d15c12376cb9fa75443e00fb25de0b8602e64c1714     --hash=sha256:45485e01ff4d3630ec0d9617310448a8702f70e9c01906b0d0118bdf9d124cf2     --hash=sha256:4a78b2b446bd7c934f5dcedc588903fb2f5eec172f3d29e52a9096a43722adfc     --hash=sha256:4ab2fe47fae9e0f9dee8c04187ce5d09f48eabe611be8259444906793ab7cbce     --hash=sha256:4d0d1650369165a14e14e1e47b372cfcb31d6ab44e6e33cb2d4e57265290044d     --hash=sha256:549a3a73da901d5bc3ce8d24e0600d1fa85524c10287f6004fbab87672bf3e1e     --hash=sha256:55086ee1064215781fff39a1af09518bc9255b50d6333f2e4c74ca09fac6a8f6     --hash=sha256:572c3763a264ba47b3cf708a44ce965d98555f618ca42c926a9c1616d8f34269     --hash=sha256:573f6eac48f4769d667c4442081b1794f52919e7edada77495aaed9236d13a96     --hash=sha256:5b4c145409bef602a690e7cfad0a15a55c13320ff7a3ad7ca59c13bb8ba4d45d     --hash=sha256:6463effa3186ea09411d50efc7d85360b38d5f09b870c48e4600f63af490e56a     --hash=sha256:65f6f63034100ead094b8744b3b97965785388f308a64cf8d7c34f2f2e5be0c4     --hash=sha256:663946639d296df6a2bb2aa51b60a2454ca1cb29835324c640dafb5ff2131a77     --hash=sha256:6897af51655e3691ff853668779c7bad41579facacf5fd7253b0133308cf000d     --hash=sha256:68d1f8a9e9e37c1223b656399be5d6b448dea850bed7d0f87a8311f1ff3dabb0     --hash=sha256:6ac7ffc7ad6d040517be39eb591cac5ff87416c2537df6ba3cba3bae290c0fed     --hash=sha256:6b3251890fff30ee142c44144871185dbe13b11bab478a88887a639655be1068     --hash=sha256:6c4caeef8fa63d06bd437cd4bdcf3ffefe6738fb1b25951440d80dc7df8c03ac     --hash=sha256:6ef1d82a3af9d3eecdba2321dc1b3c238245d890843e040e41e470ffa64c3e25     --hash=sha256:753f10e867343b4511128c6ed8c82f7bec3bd026875576dfd88483c5c73b2fd8     --hash=sha256:7cd13a2e3ddeed6913a65e66e94b51d80a041145a026c27e6bb76c31a853c6ab     --hash=sha256:7ed9e526742851e8d5cc9e6cf41427dfc6068d4f5a3bb03659444b4cabf6bc26     --hash=sha256:7f04c839ed0b6b98b1a7501a002144b76c18fb1c1850c8b98d458ac269e26ed2     --hash=sha256:802fe99cca7457642125a8a88a084cef28ff0cf9407060f7b93dca5aa25480db     --hash=sha256:80402cd6ee291dcb72644d6eac93785fe2c8b9cb30893c1af5b8fdd753b9d40f     --hash=sha256:8465322196c8b4d7ab6d1e049e4c5cb460d0394da4a27d23cc242fbf0034b6b5     --hash=sha256:86216b5cee4b06df986d214f664305142d9c76df9b6512be2738aa72a2048f99     --hash=sha256:87d1351268731db79e0f8e745d92493ee2841c974128ef629dc518b937d9194c     --hash=sha256:8bdb58ff7ba23002a4c5808d608e4e6c687175724f54a5dade5fa8c67b604e4d     --hash=sha256:8c622a5fe39a48f78944a87d4fb8a53ee07344641b0562c540d840748571b811     --hash=sha256:8d756e44e94489e49571086ef83b2bb8ce311e730092d2c34ca8f7d925cb20aa     --hash=sha256:8f4a014bc36d3c57402e2977dada34f9c12300af536839dc38c0beab8878f38a     --hash=sha256:9063e24fdb1e498ab71cb7419e24622516c4a04476b17a2dab57e8baa30d6e03     --hash=sha256:90d558489962fd4918143277a773316e56c72da56ec7aa3dc3dbbe20fdfed15b     --hash=sha256:923c0c831b7cfcb071580d3f46c4baf50f174be571576556269530f4bbd79d04     --hash=sha256:95f2a5796329323b8f0512e09dbb7a1860c46a39da62ecb2324f116fa8fdc85c     --hash=sha256:96b02a3dc4381e5494fad39be677abcb5e6634bf7b4fa83a6dd3112607547001     --hash=sha256:9f96df6923e21816da7e0ad3fd47dd8f94b2a5ce594e00677c0013018b813458     --hash=sha256:a10af20b82360ab00827f916a6058451b723b4e65030c5a18577c8b2de5b3389     --hash=sha256:a50aebfa173e157099939b17f18600f72f84eed3049e743b68ad15bd69b6bf99     --hash=sha256:a981a536974bbc7a512cf44ed14938cf01030a99e9b3a06dd59578882f06f985     --hash=sha256:a9a8e9031d613fd2009c182b69c7b2c1ef8239a0efb1df3f7c8da66d5dd3d537     --hash=sha256:ae5f4161f18c61806f411a13b0310bea87f987c7d2ecdbdaad0e94eb2e404238     --hash=sha256:aed38f6e4fb3f5d6bf81bfa990a07806be9d83cf7bacef998ab1a9bd660a581f     --hash=sha256:b01b88d45a6fcb69667cd6d2f7a9aeb4bf53760d7fc536bf679ec94fe9f3ff3d     --hash=sha256:b261ccdec7821281dade748d088bb6e9b69e6d15b30652b74cbbac25e280b796     --hash=sha256:b2b0a0c0517616b6869869f8c581d4eb2dd83a4d79e0ebcb7d373ef9956aeb0a     --hash=sha256:b4a23f61ce87adf89be746c8a8974fe1c823c891d8f86eb218bb957c924bb143     --hash=sha256:bd8f7df7d12c2db9fab40bdd87a7c09b1530128315d047a086fa3ae3435cb3a8     --hash=sha256:beb58fe5cdb101e3a055192ac291b7a21e3b7ef4f67fa1d74e331a7f2124341c     --hash=sha256:c002b4ffc0be611f0d9da932eb0f704fe2602a9a949d1f738e4c34c75b0863d5     --hash=sha256:c083af607d2515612056a31f0a8d9e0fcb5876b7bfc0abad3ecd275bc4ebc2d5     --hash=sha256:c180f51afb394e165eafe4ac2936a14bee3eb10debc9d9e4db8958fe36afe711     --hash=sha256:c235ebd9baae02f1b77bcea61bce332cb4331dc3617d254df3323aa01ab47bd4     --hash=sha256:cd70574b12bb8a4d2aaa0094515df2463cb429d8536cfb6c7ce983246983e5a6     --hash=sha256:d0eccceffcb53201b5bfebb52600a5fb483a20b61da9dbc885f8b103cbe7598c     --hash=sha256:d965bba47ddeec8cd560687584e88cf699fd28f192ceb452d1d7ee807c5597b7     --hash=sha256:db364eca23f876da6f9e16c9da0df51aa4f104a972735574842618b8c6d999d4     --hash=sha256:ddbb2551d7e0102e7252db79ba445cdab71b26640817ab1e3e3648dad515003b     --hash=sha256:deb6be0ac38ece9ba87dea880e438f25ca3eddfac8b002a2ec3d9183a454e8ae     --hash=sha256:e06ed3eb3218bc64786f7db41917d4e686cc4856944f53d5bdf83a6884432e12     --hash=sha256:e27ad930a842b4c5eb8ac0016b0a54f5aebbe679340c26101df33424142c143c     --hash=sha256:e537484df0d8f426ce2afb2d0f8e1c3d0b114b83f8850e5f2fbea0e797bd82ae     --hash=sha256:eb00ed941194665c332bf8e078baf037d6c35d7c4f3102ea2d4f16ca94a26dc8     --hash=sha256:eb6904c354526e758fda7167b33005998fb68c46fbc10e013ca97f21ca5c8887     --hash=sha256:eb8821e09e916165e160797a6c17edda0679379a4be5c716c260e836e122f54b     --hash=sha256:efcb3f6676480691518c177e3b465bcddf57cea040302f9f4e6e191af91174d4     --hash=sha256:f27273b60488abe721a075bcca6d7f3964f9f6f067c8c4c605743023d7d3944f     --hash=sha256:f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5     --hash=sha256:fb69256e180cb6c8a894fee62b3afebae785babc1ee98b81cdf68bbca1987f33     --hash=sha256:fd1abc0d89e30cc4e02e4064dc67fcc51bd941eb395c502aac3ec19fab46b519     --hash=sha256:ff8fa367d09b717b2a17a052544193ad76cd49979c805768879cb63d9ca50561",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "e26e09a829c0249bc977fe2624e14902856a24974a2640c15fcf3a3c895fc435"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository opencensus_proto instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:43:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "opencensus_proto",
               "generator_name": "opencensus_proto",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/census-instrumentation/opencensus-proto/archive/v0.4.1.tar.gz"
               ],
               "sha256": "e3d89f7f9ed84c9b6eee818c2e9306950519402bf803698b15c310b77ca2f0f3",
               "strip_prefix": "opencensus-proto-0.4.1/src"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/census-instrumentation/opencensus-proto/archive/v0.4.1.tar.gz"
                         ],
                         "sha256": "e3d89f7f9ed84c9b6eee818c2e9306950519402bf803698b15c310b77ca2f0f3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "opencensus-proto-0.4.1/src",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "opencensus_proto"
                    },
                    "output_tree_hash": "31d4990c83e743d2182b0bbabb8738c9eb45ad87f14477c438c328f097797444"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_setuptools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_setuptools",
               "generator_name": "nh_pip3_setuptools",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "setuptools==69.0.3     --hash=sha256:385eb4edd9c9d5c17540511303e39a147ce2fc04bc55289c322b9e5904fe2c05     --hash=sha256:be1af57fc409f93647f2e8e4573a142ed38724b8cdd389706a867bb4efcf1e78",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_setuptools",
                         "generator_name": "nh_pip3_setuptools",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "setuptools==69.0.3     --hash=sha256:385eb4edd9c9d5c17540511303e39a147ce2fc04bc55289c322b9e5904fe2c05     --hash=sha256:be1af57fc409f93647f2e8e4573a142ed38724b8cdd389706a867bb4efcf1e78",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "8ec6e10e96cbde99d0973574ae7aed99fd3c4da5a18a464152f2875b99dc14e5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:520:13: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/cpp/cc_configure.bzl:184:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/cpp/cc_configure.bzl:143:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "c64edfaec9508ef5f862f41ec781693de88772303a621f25067de03ecc002537"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_absl instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:327:21: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:845:26: in _com_google_absl\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_absl",
               "generator_name": "com_google_absl",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/abseil/abseil-cpp/archive/20230802.1.tar.gz"
               ],
               "sha256": "987ce98f02eefbaf930d6e38ab16aa05737234d7afbab2d5c4ea7adbe50c28ed",
               "strip_prefix": "abseil-cpp-20230802.1",
               "patches": [
                    "@envoy//bazel:abseil.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/abseil/abseil-cpp/archive/20230802.1.tar.gz"
                         ],
                         "sha256": "987ce98f02eefbaf930d6e38ab16aa05737234d7afbab2d5c4ea7adbe50c28ed",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "abseil-cpp-20230802.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:abseil.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_absl"
                    },
                    "output_tree_hash": "6997225e01d733c6f33280b91f4c8ec038388548accb15b16a5791882b755abf"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_yapf instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_yapf",
               "generator_name": "nh_pip3_yapf",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "yapf==0.40.2     --hash=sha256:4dab8a5ed7134e26d57c1647c7483afb3f136878b579062b786c9ba16b94637b     --hash=sha256:adc8b5dd02c0143108878c499284205adb258aad6db6634e5b869e7ee2bd548b",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_yapf",
                         "generator_name": "nh_pip3_yapf",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "yapf==0.40.2     --hash=sha256:4dab8a5ed7134e26d57c1647c7483afb3f136878b579062b786c9ba16b94637b     --hash=sha256:adc8b5dd02c0143108878c499284205adb258aad6db6634e5b869e7ee2bd548b",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "22270c914beb6e402fe056315ad9aef9a14b2db628fb63c035325613ac7a202b"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_flake8_docstrings instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_flake8_docstrings",
               "generator_name": "nh_pip3_flake8_docstrings",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "flake8-docstrings==1.7.0     --hash=sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af     --hash=sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_flake8_docstrings",
                         "generator_name": "nh_pip3_flake8_docstrings",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "flake8-docstrings==1.7.0     --hash=sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af     --hash=sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "3176416a55af0b6c17b1831904b7bd1f01f6fa3dc562136f81c9e9ec6e33b070"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_flake8 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_flake8",
               "generator_name": "nh_pip3_flake8",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "flake8==7.0.0     --hash=sha256:33f96621059e65eec474169085dc92bf26e7b2d47366b70be2f67ab80dc25132     --hash=sha256:a6dfbb75e03252917f2473ea9653f7cd799c3064e54d4c8140044c5c065f53c3",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_flake8",
                         "generator_name": "nh_pip3_flake8",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "flake8==7.0.0     --hash=sha256:33f96621059e65eec474169085dc92bf26e7b2d47366b70be2f67ab80dc25132     --hash=sha256:a6dfbb75e03252917f2473ea9653f7cd799c3064e54d4c8140044c5c065f53c3",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "5554223ff62703e9791ef356c7d8624cec2bbe1ff8673d57e193edc9fb150ef2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_fmtlib_fmt instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:301:27: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:485:26: in _com_github_fmtlib_fmt\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_fmtlib_fmt",
               "generator_name": "com_github_fmtlib_fmt",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/fmtlib/fmt/releases/download/9.1.0/fmt-9.1.0.zip"
               ],
               "sha256": "cceb4cb9366e18a5742128cb3524ce5f50e88b476f1e54737a47ffdf4df4c996",
               "strip_prefix": "fmt-9.1.0",
               "build_file": "@envoy//bazel/external:fmtlib.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/fmtlib/fmt/releases/download/9.1.0/fmt-9.1.0.zip"
                         ],
                         "sha256": "cceb4cb9366e18a5742128cb3524ce5f50e88b476f1e54737a47ffdf4df4c996",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "fmt-9.1.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:fmtlib.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_fmtlib_fmt"
                    },
                    "output_tree_hash": "21c1e191742df55cbf10d5df45ecb340696ba46b142f4fe44221e04151d0d696"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_gabime_spdlog instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:302:30: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:495:26: in _com_github_gabime_spdlog\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_gabime_spdlog",
               "generator_name": "com_github_gabime_spdlog",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/gabime/spdlog/archive/v1.13.0.tar.gz"
               ],
               "sha256": "534f2ee1a4dcbeb22249856edfb2be76a1cf4f708a20b0ac2ed090ee24cfdbc9",
               "strip_prefix": "spdlog-1.13.0",
               "build_file": "@envoy//bazel/external:spdlog.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/gabime/spdlog/archive/v1.13.0.tar.gz"
                         ],
                         "sha256": "534f2ee1a4dcbeb22249856edfb2be76a1cf4f708a20b0ac2ed090ee24cfdbc9",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "spdlog-1.13.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:spdlog.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_gabime_spdlog"
                    },
                    "output_tree_hash": "59e04f732a02513ae518bccf07efca195ac28147096403fcb92c26cd6ae779dd"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_google_tcmalloc instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:307:32: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1304:26: in _com_github_google_tcmalloc\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_google_tcmalloc",
               "generator_name": "com_github_google_tcmalloc",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/tcmalloc/archive/e33c7bc60415127c104006d3301c96902f98d42a.tar.gz"
               ],
               "sha256": "14a2c91b71d6719558768a79671408c9acd8284b418e80386c5888047e2c15aa",
               "strip_prefix": "tcmalloc-e33c7bc60415127c104006d3301c96902f98d42a"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/tcmalloc/archive/e33c7bc60415127c104006d3301c96902f98d42a.tar.gz"
                         ],
                         "sha256": "14a2c91b71d6719558768a79671408c9acd8284b418e80386c5888047e2c15aa",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "tcmalloc-e33c7bc60415127c104006d3301c96902f98d42a",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_google_tcmalloc"
                    },
                    "output_tree_hash": "43705cef8b3b82c723bb219004c2eec1a5fde3e5ab1f0beb941e9ca997d873ba"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_google_googletest instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:328:27: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:830:26: in _com_google_googletest\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_googletest",
               "generator_name": "com_google_googletest",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/googletest/archive/a4ab0abb93620ce26efad9de9296b73b16e88588.tar.gz"
               ],
               "sha256": "7897bfaa5ad39a479177cfb5c3ce010184dbaee22a7c3727b212282871918751",
               "strip_prefix": "googletest-a4ab0abb93620ce26efad9de9296b73b16e88588",
               "patches": [
                    "@envoy//bazel:googletest.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/googletest/archive/a4ab0abb93620ce26efad9de9296b73b16e88588.tar.gz"
                         ],
                         "sha256": "7897bfaa5ad39a479177cfb5c3ce010184dbaee22a7c3727b212282871918751",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "googletest-a4ab0abb93620ce26efad9de9296b73b16e88588",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:googletest.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_google_googletest"
                    },
                    "output_tree_hash": "49ce420303f28335a6fc07da73899392c6443d5dbd50b6ada308ad43671ed9bf"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_download_sdk_rule",
          "definition_information": "Repository go_sdk instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:29:27: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:662:28: in go_register_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:303:25: in go_download_sdk\nRepository rule go_download_sdk_rule defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/sdk.bzl:133:39: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk",
               "generator_name": "go_sdk",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "version": "1.20"
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%go_download_sdk_rule",
                    "attributes": {
                         "name": "go_sdk",
                         "generator_name": "go_sdk",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "version": "1.20"
                    },
                    "output_tree_hash": "2c0a1a009a9fc6280dec49136dfd9be738cb4566b19a5459a40c089a14a9158d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository utf8_range instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:357:16: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1468:26: in _utf8_range\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "utf8_range",
               "generator_name": "utf8_range",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/protocolbuffers/utf8_range/archive/d863bc33e15cba6d873c878dcca9e6fe52b2f8cb.tar.gz"
               ],
               "sha256": "c56f0a8c562050e6523a3095cf5610d19c190cd99bac622cc3e5754be51aaa7b",
               "strip_prefix": "utf8_range-d863bc33e15cba6d873c878dcca9e6fe52b2f8cb"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/protocolbuffers/utf8_range/archive/d863bc33e15cba6d873c878dcca9e6fe52b2f8cb.tar.gz"
                         ],
                         "sha256": "c56f0a8c562050e6523a3095cf5610d19c190cd99bac622cc3e5754be51aaa7b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "utf8_range-d863bc33e15cba6d873c878dcca9e6fe52b2f8cb",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "utf8_range"
                    },
                    "output_tree_hash": "be57997ed15238b802df7beb5bdd049a78fc7d6455fbff14429ab5bfd87a55ec"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_cyan4973_xxhash instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:297:32: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:454:26: in _com_github_cyan4973_xxhash\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_cyan4973_xxhash",
               "generator_name": "com_github_cyan4973_xxhash",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/Cyan4973/xxHash/archive/v0.8.2.tar.gz"
               ],
               "sha256": "baee0c6afd4f03165de7a4e67988d16f0f2b257b51d0e3cb91909302a26a79c4",
               "strip_prefix": "xxHash-0.8.2",
               "build_file": "@envoy//bazel/external:xxhash.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/Cyan4973/xxHash/archive/v0.8.2.tar.gz"
                         ],
                         "sha256": "baee0c6afd4f03165de7a4e67988d16f0f2b257b51d0e3cb91909302a26a79c4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "xxHash-0.8.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:xxhash.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_cyan4973_xxhash"
                    },
                    "output_tree_hash": "a04eb72708c292cff3d76335f061e7dccd969adb4100891eed46381123c75092"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_openhistogram_libcircllhist instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:296:44: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:417:26: in _com_github_openhistogram_libcircllhist\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_openhistogram_libcircllhist",
               "generator_name": "com_github_openhistogram_libcircllhist",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/openhistogram/libcircllhist/archive/39f9db724a81ba78f5d037f1cae79c5a07107c8e.tar.gz"
               ],
               "sha256": "fd2492f6cc1f8734f8f57be8c2e7f2907e94ee2a4c02445ce59c4241fece144b",
               "strip_prefix": "libcircllhist-39f9db724a81ba78f5d037f1cae79c5a07107c8e",
               "build_file": "@envoy//bazel/external:libcircllhist.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/openhistogram/libcircllhist/archive/39f9db724a81ba78f5d037f1cae79c5a07107c8e.tar.gz"
                         ],
                         "sha256": "fd2492f6cc1f8734f8f57be8c2e7f2907e94ee2a4c02445ce59c4241fece144b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "libcircllhist-39f9db724a81ba78f5d037f1cae79c5a07107c8e",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:libcircllhist.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_openhistogram_libcircllhist"
                    },
                    "output_tree_hash": "956538dbf982d92d08b6a02224bfdca8fedb9f5760bbfff55dc41226bf53d799"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_google_quiche instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:335:30: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:1097:26: in _com_github_google_quiche\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_google_quiche",
               "generator_name": "com_github_google_quiche",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/quiche/archive/2c1f10f46ce16d42fcf692d324799d859e8478cc.tar.gz"
               ],
               "sha256": "8754391ff9d75aa1ff3dddbb57c73830c63932f01cfb30d4ca158720b2eadeba",
               "strip_prefix": "quiche-2c1f10f46ce16d42fcf692d324799d859e8478cc",
               "patch_cmds": [
                    "find quiche/ -type f -name \"*.bazel\" -delete"
               ],
               "build_file": "@envoy//bazel/external:quiche.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/quiche/archive/2c1f10f46ce16d42fcf692d324799d859e8478cc.tar.gz"
                         ],
                         "sha256": "8754391ff9d75aa1ff3dddbb57c73830c63932f01cfb30d4ca158720b2eadeba",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "quiche-2c1f10f46ce16d42fcf692d324799d859e8478cc",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [
                              "find quiche/ -type f -name \"*.bazel\" -delete"
                         ],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:quiche.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_google_quiche"
                    },
                    "output_tree_hash": "df4419c4dbe6b5abb384ce84d77ad1a7c588616fd86a3726cd7c8fc300eba11e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository boringssl instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:279:15: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:402:26: in _boringssl\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "boringssl",
               "generator_name": "boringssl",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/boringssl/archive/45cf810dbdbd767f09f8cb0b0fcccd342c39041f.tar.gz"
               ],
               "sha256": "f1f421738e9ba39dd88daf8cf3096ddba9c53e2b6b41b32fff5a3ff82f4cd162",
               "strip_prefix": "boringssl-45cf810dbdbd767f09f8cb0b0fcccd342c39041f",
               "patches": [
                    "@envoy//bazel:boringssl_static.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/boringssl/archive/45cf810dbdbd767f09f8cb0b0fcccd342c39041f.tar.gz"
                         ],
                         "sha256": "f1f421738e9ba39dd88daf8cf3096ddba9c53e2b6b41b32fff5a3ff82f4cd162",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "boringssl-45cf810dbdbd767f09f8cb0b0fcccd342c39041f",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel:boringssl_static.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "boringssl"
                    },
                    "output_tree_hash": "594ff8d8ea3e2db0f0b47856eb59330d57748d53960fa6261b0f90331c50ecff"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository dep_hdrhistogram_c instantiated at:\n  /workspaces/nighthawk/WORKSPACE:5:23: in <toplevel>\n  /workspaces/nighthawk/bazel/repositories.bzl:18:17: in nighthawk_dependencies\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "dep_hdrhistogram_c",
               "generator_name": "dep_hdrhistogram_c",
               "generator_function": "nighthawk_dependencies",
               "generator_location": None,
               "url": "https://github.com/HdrHistogram/HdrHistogram_c/archive/0.11.2.tar.gz",
               "sha256": "637f28b5f64de2e268131e4e34e6eef0b91cf5ff99167db447d9b2825eae6bad",
               "strip_prefix": "HdrHistogram_c-0.11.2",
               "build_file_content": "\ncc_library(\n    name = \"hdrhistogram_c\",\n    srcs = [\n        \"src/hdr_encoding.c\",\n        \"src/hdr_histogram.c\",\n        \"src/hdr_histogram_log.c\",\n        \"src/hdr_interval_recorder.c\",\n        \"src/hdr_thread.c\",\n        \"src/hdr_time.c\",\n        \"src/hdr_writer_reader_phaser.c\",\n    ],\n    hdrs = [\n        \"src/hdr_atomic.h\",\n        \"src/hdr_encoding.h\",\n        \"src/hdr_endian.h\",\n        \"src/hdr_histogram.h\",\n        \"src/hdr_histogram_log.h\",\n        \"src/hdr_interval_recorder.h\",\n        \"src/hdr_tests.h\",\n        \"src/hdr_thread.h\",\n        \"src/hdr_time.h\",\n        \"src/hdr_writer_reader_phaser.h\",\n    ],\n    copts = [\n        \"-std=gnu99\",\n        \"-Wno-implicit-function-declaration\",\n        \"-Wno-error\",\n    ],\n    deps = [\"//external:zlib\"],\n    visibility = [\"//visibility:public\"],\n)\n  "
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/HdrHistogram/HdrHistogram_c/archive/0.11.2.tar.gz",
                         "urls": [],
                         "sha256": "637f28b5f64de2e268131e4e34e6eef0b91cf5ff99167db447d9b2825eae6bad",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "HdrHistogram_c-0.11.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\ncc_library(\n    name = \"hdrhistogram_c\",\n    srcs = [\n        \"src/hdr_encoding.c\",\n        \"src/hdr_histogram.c\",\n        \"src/hdr_histogram_log.c\",\n        \"src/hdr_interval_recorder.c\",\n        \"src/hdr_thread.c\",\n        \"src/hdr_time.c\",\n        \"src/hdr_writer_reader_phaser.c\",\n    ],\n    hdrs = [\n        \"src/hdr_atomic.h\",\n        \"src/hdr_encoding.h\",\n        \"src/hdr_endian.h\",\n        \"src/hdr_histogram.h\",\n        \"src/hdr_histogram_log.h\",\n        \"src/hdr_interval_recorder.h\",\n        \"src/hdr_tests.h\",\n        \"src/hdr_thread.h\",\n        \"src/hdr_time.h\",\n        \"src/hdr_writer_reader_phaser.h\",\n    ],\n    copts = [\n        \"-std=gnu99\",\n        \"-Wno-implicit-function-declaration\",\n        \"-Wno-error\",\n    ],\n    deps = [\"//external:zlib\"],\n    visibility = [\"//visibility:public\"],\n)\n  ",
                         "workspace_file_content": "",
                         "name": "dep_hdrhistogram_c"
                    },
                    "output_tree_hash": "e8d083d879da83476215ff99d7a46c09b37c818659a1f35ecb7b4082a8074a2e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_openzipkin_zipkinapi instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:49:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_openzipkin_zipkinapi",
               "generator_name": "com_github_openzipkin_zipkinapi",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/openzipkin/zipkin-api/archive/1.0.0.tar.gz"
               ],
               "sha256": "6c8ee2014cf0746ba452e5f2c01f038df60e85eb2d910b226f9aa27ddc0e44cf",
               "strip_prefix": "zipkin-api-1.0.0",
               "build_file_content": "\n\nload(\"@envoy_api//bazel:api_build_system.bzl\", \"api_cc_py_proto_library\")\nload(\"@io_bazel_rules_go//proto:def.bzl\", \"go_proto_library\")\n\napi_cc_py_proto_library(\n    name = \"zipkin\",\n    srcs = [\n        \"zipkin-jsonv2.proto\",\n        \"zipkin.proto\",\n    ],\n    visibility = [\"//visibility:public\"],\n)\n\ngo_proto_library(\n    name = \"zipkin_go_proto\",\n    proto = \":zipkin\",\n    visibility = [\"//visibility:public\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/openzipkin/zipkin-api/archive/1.0.0.tar.gz"
                         ],
                         "sha256": "6c8ee2014cf0746ba452e5f2c01f038df60e85eb2d910b226f9aa27ddc0e44cf",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zipkin-api-1.0.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\n\nload(\"@envoy_api//bazel:api_build_system.bzl\", \"api_cc_py_proto_library\")\nload(\"@io_bazel_rules_go//proto:def.bzl\", \"go_proto_library\")\n\napi_cc_py_proto_library(\n    name = \"zipkin\",\n    srcs = [\n        \"zipkin-jsonv2.proto\",\n        \"zipkin.proto\",\n    ],\n    visibility = [\"//visibility:public\"],\n)\n\ngo_proto_library(\n    name = \"zipkin_go_proto\",\n    proto = \":zipkin\",\n    visibility = [\"//visibility:public\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "com_github_openzipkin_zipkinapi"
                    },
                    "output_tree_hash": "b6c02135caaf6163f842fe6c4b1d310debb903dde104cfffca7da54ad257d01e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_mccabe instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_mccabe",
               "generator_name": "nh_pip3_mccabe",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "mccabe==0.7.0     --hash=sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325     --hash=sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_mccabe",
                         "generator_name": "nh_pip3_mccabe",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "mccabe==0.7.0     --hash=sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325     --hash=sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "b92e08b59882a47162924ef6e81610fc3283b04b0273e4f8e95e25ff4ac0c674"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pyflakes instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pyflakes",
               "generator_name": "nh_pip3_pyflakes",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pyflakes==3.2.0     --hash=sha256:1c61603ff154621fb2a9172037d84dca3500def8c8b630657d1701f026f8af3f     --hash=sha256:84b5be138a2dfbb40689ca07e2152deb896a65c3a3e24c251c5c62489568074a",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pyflakes",
                         "generator_name": "nh_pip3_pyflakes",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pyflakes==3.2.0     --hash=sha256:1c61603ff154621fb2a9172037d84dca3500def8c8b630657d1701f026f8af3f     --hash=sha256:84b5be138a2dfbb40689ca07e2152deb896a65c3a3e24c251c5c62489568074a",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "d2addc5466451eb894d0ddb863ddf82bdc4bfabebb3d002c05a7523cdffb415b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_cncf_udpa instantiated at:\n  /workspaces/nighthawk/WORKSPACE:18:23: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/api_repositories.bzl:4:21: in envoy_api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:34:26: in api_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/repositories.bzl:9:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_cncf_udpa",
               "generator_name": "com_github_cncf_udpa",
               "generator_function": "envoy_api_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/cncf/xds/archive/3a472e524827f72d1ad621c4983dd5af54c46776.tar.gz"
               ],
               "sha256": "dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927",
               "strip_prefix": "xds-3a472e524827f72d1ad621c4983dd5af54c46776"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/cncf/xds/archive/3a472e524827f72d1ad621c4983dd5af54c46776.tar.gz"
                         ],
                         "sha256": "dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "xds-3a472e524827f72d1ad621c4983dd5af54c46776",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_cncf_udpa"
                    },
                    "output_tree_hash": "29a41286c93e5a634adc38d98e377c6209985895b24f4075fa401b7cd5aa1f67"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pycodestyle instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pycodestyle",
               "generator_name": "nh_pip3_pycodestyle",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pycodestyle==2.11.1     --hash=sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f     --hash=sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pycodestyle",
                         "generator_name": "nh_pip3_pycodestyle",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pycodestyle==2.11.1     --hash=sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f     --hash=sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "1934bd50f2455cb3699d0e1be465883c51805bb4a59ee9415e1b8aca8feb8e84"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_tomli instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_tomli",
               "generator_name": "nh_pip3_tomli",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "tomli==2.0.1     --hash=sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc     --hash=sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_tomli",
                         "generator_name": "nh_pip3_tomli",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "tomli==2.0.1     --hash=sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc     --hash=sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "7e6af822feb89736cc329dc3461cc148c78fc88c52da70c43d3cbb0bfe36dae0"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_platformdirs instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_platformdirs",
               "generator_name": "nh_pip3_platformdirs",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "platformdirs==4.2.0     --hash=sha256:0614df2a2f37e1a662acbd8e2b25b92ccf8632929bc6d43467e17fe89c75e068     --hash=sha256:ef0cc731df711022c174543cb70a9b5bd22e5a9337c8624ef2c2ceb8ddad8768",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_platformdirs",
                         "generator_name": "nh_pip3_platformdirs",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "platformdirs==4.2.0     --hash=sha256:0614df2a2f37e1a662acbd8e2b25b92ccf8632929bc6d43467e17fe89c75e068     --hash=sha256:ef0cc731df711022c174543cb70a9b5bd22e5a9337c8624ef2c2ceb8ddad8768",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "ef9f095b88a4c571ac1a290043e0ef124a36cd3eb5ba90244eeffc538a9eb09e"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_pydocstyle instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_pydocstyle",
               "generator_name": "nh_pip3_pydocstyle",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "pydocstyle==6.3.0     --hash=sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019     --hash=sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_pydocstyle",
                         "generator_name": "nh_pip3_pydocstyle",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "pydocstyle==6.3.0     --hash=sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019     --hash=sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "e76209c18bbb2b9a5b1fe5dd9bbd80b76495d67fdb96001c0684ebd6f3a0f69e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_mirror_tclap instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:299:29: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:474:26: in _com_github_mirror_tclap\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_mirror_tclap",
               "generator_name": "com_github_mirror_tclap",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/mirror/tclap/archive/v1.2.5.tar.gz"
               ],
               "sha256": "7e87d13734076fa4f626f6144ce9a02717198b3f054341a6886e2107b048b235",
               "strip_prefix": "tclap-1.2.5",
               "patch_args": [
                    "-p1"
               ],
               "build_file": "@envoy//bazel/external:tclap.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/mirror/tclap/archive/v1.2.5.tar.gz"
                         ],
                         "sha256": "7e87d13734076fa4f626f6144ce9a02717198b3f054341a6886e2107b048b235",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "tclap-1.2.5",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:tclap.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_mirror_tclap"
                    },
                    "output_tree_hash": "5fd75e377a9d58842551ec2c51cb1576cec38fc5ec80a67be89deed1831b2ebe"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_nlohmann_json instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:325:30: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:793:26: in _com_github_nlohmann_json\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_nlohmann_json",
               "generator_name": "com_github_nlohmann_json",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/nlohmann/json/archive/v3.11.3.tar.gz"
               ],
               "sha256": "0d8ef5af7f9794e3263480193c491549b2ba6cc74bb018906202ada498a79406",
               "strip_prefix": "json-3.11.3",
               "build_file": "@envoy//bazel/external:json.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/nlohmann/json/archive/v3.11.3.tar.gz"
                         ],
                         "sha256": "0d8ef5af7f9794e3263480193c491549b2ba6cc74bb018906202ada498a79406",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "json-3.11.3",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@envoy//bazel/external:json.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_nlohmann_json"
                    },
                    "output_tree_hash": "29a95dc4f18f26756e4ee3ae60b6582358bb5880590510adf9c5ecb215f7c77a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_nghttp2_nghttp2 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:320:32: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:724:26: in _com_github_nghttp2_nghttp2\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_nghttp2_nghttp2",
               "generator_name": "com_github_nghttp2_nghttp2",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/nghttp2/nghttp2/releases/download/v1.59.0/nghttp2-1.59.0.tar.gz"
               ],
               "sha256": "90fd27685120404544e96a60ed40398a3457102840c38e7215dc6dec8684470f",
               "strip_prefix": "nghttp2-1.59.0",
               "patches": [
                    "@envoy//bazel/foreign_cc:nghttp2.patch"
               ],
               "patch_args": [
                    "-p1"
               ],
               "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/nghttp2/nghttp2/releases/download/v1.59.0/nghttp2-1.59.0.tar.gz"
                         ],
                         "sha256": "90fd27685120404544e96a60ed40398a3457102840c38e7215dc6dec8684470f",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "nghttp2-1.59.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel/foreign_cc:nghttp2.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "com_github_nghttp2_nghttp2"
                    },
                    "output_tree_hash": "90fe4c27cd7cf710672a9b4aa26834071ca06ebde4a81e68ef5a4104eab3065a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository ninja_1.11.0_linux instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:62:28: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:66:22: in prebuilt_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:4200:14: in _ninja_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "ninja_1.11.0_linux",
               "generator_name": "ninja_1.11.0_linux",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "urls": [
                    "https://github.com/ninja-build/ninja/releases/download/v1.11.0/ninja-linux.zip"
               ],
               "sha256": "9726e730d5b8599f82654dc80265e64a10a8a817552c34153361ed0c017f9f02",
               "strip_prefix": "",
               "build_file_content": "load(\"@rules_foreign_cc//toolchains/native_tools:native_tools_toolchain.bzl\", \"native_tool_toolchain\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nfilegroup(\n    name = \"ninja_bin\",\n    srcs = [\"ninja\"],\n)\n\nnative_tool_toolchain(\n    name = \"ninja_tool\",\n    env = {\"NINJA\": \"$(execpath :ninja_bin)\"},\n    path = \"$(execpath :ninja_bin)\",\n    target = \":ninja_bin\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/ninja-build/ninja/releases/download/v1.11.0/ninja-linux.zip"
                         ],
                         "sha256": "9726e730d5b8599f82654dc80265e64a10a8a817552c34153361ed0c017f9f02",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "load(\"@rules_foreign_cc//toolchains/native_tools:native_tools_toolchain.bzl\", \"native_tool_toolchain\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nfilegroup(\n    name = \"ninja_bin\",\n    srcs = [\"ninja\"],\n)\n\nnative_tool_toolchain(\n    name = \"ninja_tool\",\n    env = {\"NINJA\": \"$(execpath :ninja_bin)\"},\n    path = \"$(execpath :ninja_bin)\",\n    target = \":ninja_bin\",\n)\n",
                         "workspace_file_content": "",
                         "name": "ninja_1.11.0_linux"
                    },
                    "output_tree_hash": "5b91b7b7687050070ed6457451ae6c5afce07e0a3c123546cabc94c45d170f81"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_libevent_libevent instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:318:34: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:602:26: in _com_github_libevent_libevent\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_libevent_libevent",
               "generator_name": "com_github_libevent_libevent",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/libevent/libevent/archive/62c152d9a7cd264b993dad730c4163c6ede2e0a3.tar.gz"
               ],
               "sha256": "4c80e5fe044ce5f8055b20a2f141ee32ec2614000f3e95d2aa81611a4c8f5213",
               "strip_prefix": "libevent-62c152d9a7cd264b993dad730c4163c6ede2e0a3",
               "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/libevent/libevent/archive/62c152d9a7cd264b993dad730c4163c6ede2e0a3.tar.gz"
                         ],
                         "sha256": "4c80e5fe044ce5f8055b20a2f141ee32ec2614000f3e95d2aa81611a4c8f5213",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "libevent-62c152d9a7cd264b993dad730c4163c6ede2e0a3",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "com_github_libevent_libevent"
                    },
                    "output_tree_hash": "834212c0a3b88a765f7ab65d779dfc1a6b89907a944ecfba869ae808bbabe648"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_c_ares_c_ares instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:295:30: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:444:26: in _com_github_c_ares_c_ares\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_c_ares_c_ares",
               "generator_name": "com_github_c_ares_c_ares",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/c-ares/c-ares/releases/download/cares-1_19_1/c-ares-1.19.1.tar.gz"
               ],
               "sha256": "321700399b72ed0e037d0074c629e7741f6b2ec2dda92956abe3e9671d3e268e",
               "strip_prefix": "c-ares-1.19.1",
               "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/c-ares/c-ares/releases/download/cares-1_19_1/c-ares-1.19.1.tar.gz"
                         ],
                         "sha256": "321700399b72ed0e037d0074c629e7741f6b2ec2dda92956abe3e9671d3e268e",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "c-ares-1.19.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "com_github_c_ares_c_ares"
                    },
                    "output_tree_hash": "e284adab7fe5beebdda48d972feeefd5118c05a0580be26cb7c06702120400eb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository net_zlib instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:342:14: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:632:26: in _net_zlib\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "net_zlib",
               "generator_name": "net_zlib",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/madler/zlib/archive/v1.2.13.tar.gz"
               ],
               "sha256": "1525952a0a567581792613a9723333d7f8cc20b87a81f920fb8bc7e3f2251428",
               "strip_prefix": "zlib-1.2.13",
               "patches": [
                    "@envoy//bazel/foreign_cc:zlib.patch"
               ],
               "patch_args": [
                    "-p1"
               ],
               "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/madler/zlib/archive/v1.2.13.tar.gz"
                         ],
                         "sha256": "1525952a0a567581792613a9723333d7f8cc20b87a81f920fb8bc7e3f2251428",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zlib-1.2.13",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@envoy//bazel/foreign_cc:zlib.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(name = \"all\", srcs = glob([\"**\"], exclude=[]), visibility = [\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "net_zlib"
                    },
                    "output_tree_hash": "ab66a84be07ae78f2a170cdb81fe81747ec608760000da6adf8dbabd060510c3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_jbeder_yaml_cpp instantiated at:\n  /workspaces/nighthawk/WORKSPACE:22:19: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:317:32: in envoy_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:593:26: in _com_github_jbeder_yaml_cpp\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/repositories.bzl:55:23: in external_http_archive\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy_api/bazel/envoy_http_archive.bzl:16:17: in envoy_http_archive\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_jbeder_yaml_cpp",
               "generator_name": "com_github_jbeder_yaml_cpp",
               "generator_function": "envoy_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/jbeder/yaml-cpp/archive/0.8.0.tar.gz"
               ],
               "sha256": "fbe74bbdcee21d656715688706da3c8becfd946d92cd44705cc6098bb23b3a16",
               "strip_prefix": "yaml-cpp-0.8.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/jbeder/yaml-cpp/archive/0.8.0.tar.gz"
                         ],
                         "sha256": "fbe74bbdcee21d656715688706da3c8becfd946d92cd44705cc6098bb23b3a16",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "yaml-cpp-0.8.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_jbeder_yaml_cpp"
                    },
                    "output_tree_hash": "1648db38f3b3805c59ed3fe1cbb3e8a45d0e35f028978b37a9ad5da60902b683"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository cmake-3.23.2-linux-x86_64 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:62:28: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:65:22: in prebuilt_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/prebuilt_toolchains.bzl:85:14: in _cmake_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "cmake-3.23.2-linux-x86_64",
               "generator_name": "cmake-3.23.2-linux-x86_64",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "urls": [
                    "https://github.com/Kitware/CMake/releases/download/v3.23.2/cmake-3.23.2-linux-x86_64.tar.gz"
               ],
               "sha256": "aaced6f745b86ce853661a595bdac6c5314a60f8181b6912a0a4920acfa32708",
               "strip_prefix": "cmake-3.23.2-linux-x86_64",
               "build_file_content": "load(\"@rules_foreign_cc//toolchains/native_tools:native_tools_toolchain.bzl\", \"native_tool_toolchain\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nfilegroup(\n    name = \"cmake_data\",\n    srcs = glob(\n        [\n            \"**\",\n        ],\n        exclude = [\n            \"WORKSPACE\",\n            \"WORKSPACE.bazel\",\n            \"BUILD\",\n            \"BUILD.bazel\",\n        ],\n    ),\n)\n\nnative_tool_toolchain(\n    name = \"cmake_tool\",\n    path = \"bin/cmake\",\n    target = \":cmake_data\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/Kitware/CMake/releases/download/v3.23.2/cmake-3.23.2-linux-x86_64.tar.gz"
                         ],
                         "sha256": "aaced6f745b86ce853661a595bdac6c5314a60f8181b6912a0a4920acfa32708",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "cmake-3.23.2-linux-x86_64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "load(\"@rules_foreign_cc//toolchains/native_tools:native_tools_toolchain.bzl\", \"native_tool_toolchain\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nfilegroup(\n    name = \"cmake_data\",\n    srcs = glob(\n        [\n            \"**\",\n        ],\n        exclude = [\n            \"WORKSPACE\",\n            \"WORKSPACE.bazel\",\n            \"BUILD\",\n            \"BUILD.bazel\",\n        ],\n    ),\n)\n\nnative_tool_toolchain(\n    name = \"cmake_tool\",\n    path = \"bin/cmake\",\n    target = \":cmake_data\",\n)\n",
                         "workspace_file_content": "",
                         "name": "cmake-3.23.2-linux-x86_64"
                    },
                    "output_tree_hash": "4ed246ef01393a3748ee63d873fb4c0488b432fe51d5fccc4a57a0e862fd76dc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository_cache.bzl%go_repository_cache",
          "definition_information": "Repository bazel_gazelle_go_repository_cache instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:32:25: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/deps.bzl:54:28: in gazelle_dependencies\nRepository rule go_repository_cache defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository_cache.bzl:71:38: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_cache",
               "generator_name": "bazel_gazelle_go_repository_cache",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "go_sdk_name": "go_sdk",
               "go_env": {}
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository_cache.bzl%go_repository_cache",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_cache",
                         "generator_name": "bazel_gazelle_go_repository_cache",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "go_sdk_name": "go_sdk",
                         "go_env": {}
                    },
                    "output_tree_hash": "23f20eb10b83fc688303b22d55e118e2d12aa8bee3e255ebce10114efe3b5b46"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository nh_pip3_snowballstemmer instantiated at:\n  /workspaces/nighthawk/WORKSPACE:42:8: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/nh_pip3/requirements.bzl:77:20: in install_deps\nRepository rule whl_library defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_python/python/pip_install/pip_repository.bzl:932:30: in <toplevel>\n",
          "original_attributes": {
               "name": "nh_pip3_snowballstemmer",
               "generator_name": "nh_pip3_snowballstemmer",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "nh_pip3",
               "requirement": "snowballstemmer==2.2.0     --hash=sha256:09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1     --hash=sha256:c8e1716e83cc398ae16824e5572ae04e0d9fc2c6b985fb0f900f5f0c96ecba1a",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [
                    "--require-hashes"
               ],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "nh_pip3_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "nh_pip3_snowballstemmer",
                         "generator_name": "nh_pip3_snowballstemmer",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "nh_pip3",
                         "requirement": "snowballstemmer==2.2.0     --hash=sha256:09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1     --hash=sha256:c8e1716e83cc398ae16824e5572ae04e0d9fc2c6b985fb0f900f5f0c96ecba1a",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [
                              "--require-hashes"
                         ],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_11_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "nh_pip3_",
                         "timeout": 600
                    },
                    "output_tree_hash": "8ab31db260d753bc2ea29be12b3b730b36db55d175eadbf3c688dfea470f305c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository gnumake_src instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:27:34: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/foreign_cc/repositories.bzl:65:25: in rules_foreign_cc_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/built_toolchains.bzl:37:20: in built_toolchains\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/rules_foreign_cc/toolchains/built_toolchains.bzl:420:14: in _make_toolchain\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "gnumake_src",
               "generator_name": "gnumake_src",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/ftpmirror.gnu.org/gnu/make/make-4.3.tar.gz",
                    "http://ftpmirror.gnu.org/gnu/make/make-4.3.tar.gz"
               ],
               "sha256": "e05fdde47c5f7ca45cb697e973894ff4f5d79e13b750ed57d7b66d8defc78e19",
               "strip_prefix": "make-4.3",
               "patches": [
                    "@rules_foreign_cc//toolchains:make-reproducible-bootstrap.patch"
               ],
               "build_file_content": "filegroup(\n    name = \"all_srcs\",\n    srcs = glob([\"**\"]),\n    visibility = [\"//visibility:public\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/ftpmirror.gnu.org/gnu/make/make-4.3.tar.gz",
                              "http://ftpmirror.gnu.org/gnu/make/make-4.3.tar.gz"
                         ],
                         "sha256": "e05fdde47c5f7ca45cb697e973894ff4f5d79e13b750ed57d7b66d8defc78e19",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "make-4.3",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "@rules_foreign_cc//toolchains:make-reproducible-bootstrap.patch"
                         ],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(\n    name = \"all_srcs\",\n    srcs = glob([\"**\"]),\n    visibility = [\"//visibility:public\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "gnumake_src"
                    },
                    "output_tree_hash": "b1fc7f8339e2054f088bccb46015c241e18c05c7b5a4d1e03d15c47d2e2c4960"
               }
          ]
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:nogo.bzl%go_register_nogo",
          "definition_information": "Repository io_bazel_rules_nogo instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:28:26: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/repositories.bzl:289:12: in go_rules_dependencies\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/repositories.bzl:297:18: in _maybe\nRepository rule go_register_nogo defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/io_bazel_rules_go/go/private/nogo.bzl:31:35: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_nogo",
               "generator_name": "io_bazel_rules_nogo",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "nogo": "@io_bazel_rules_go//:default_nogo"
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:nogo.bzl%go_register_nogo",
                    "attributes": {
                         "name": "io_bazel_rules_nogo",
                         "generator_name": "io_bazel_rules_nogo",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "nogo": "@io_bazel_rules_go//:default_nogo"
                    },
                    "output_tree_hash": "e4772e86da6e3bc0887a236dc36324e6b44be0e0315adf28750fcb363acae413"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
          "definition_information": "Repository local_config_xcode instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:523:16: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/osx/xcode_configure.bzl:312:19: in xcode_configure\nRepository rule xcode_autoconf defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_tools/tools/osx/xcode_configure.bzl:297:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_xcode",
               "generator_name": "local_config_xcode",
               "generator_function": "xcode_configure",
               "generator_location": None,
               "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
                    "attributes": {
                         "name": "local_config_xcode",
                         "generator_name": "local_config_xcode",
                         "generator_function": "xcode_configure",
                         "generator_location": None,
                         "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
                    },
                    "output_tree_hash": "ec026961157bb71cf68d1b568815ad68147ed16f318161bc0da40f6f3d7d79fd"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository_tools.bzl%go_repository_tools",
          "definition_information": "Repository bazel_gazelle_go_repository_tools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:32:25: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/deps.bzl:78:24: in gazelle_dependencies\nRepository rule go_repository_tools defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository_tools.bzl:117:38: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_tools",
               "generator_name": "bazel_gazelle_go_repository_tools",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "go_cache": "@bazel_gazelle_go_repository_cache//:go.env"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository_tools.bzl%go_repository_tools",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_tools",
                         "generator_name": "bazel_gazelle_go_repository_tools",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "go_cache": "@bazel_gazelle_go_repository_cache//:go.env"
                    },
                    "output_tree_hash": "3c326c60bf1b10bbe2ba9e93d1cd4f7d1a4194b01b37a6d5fabcfedab912cf62"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository_config.bzl%go_repository_config",
          "definition_information": "Repository bazel_gazelle_go_repository_config instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:32:25: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/deps.bzl:83:25: in gazelle_dependencies\nRepository rule go_repository_config defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository_config.bzl:69:39: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_gazelle_go_repository_config",
               "generator_name": "bazel_gazelle_go_repository_config",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "config": "//:WORKSPACE"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository_config.bzl%go_repository_config",
                    "attributes": {
                         "name": "bazel_gazelle_go_repository_config",
                         "generator_name": "bazel_gazelle_go_repository_config",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "config": "//:WORKSPACE"
                    },
                    "output_tree_hash": "664adbb8669fce99cfafbf1ac2cd68d8bac2439a39a2623d4fe553a83e4161a6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository com_github_lyft_protoc_gen_star_v2 instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:81:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_lyft_protoc_gen_star_v2",
               "generator_name": "com_github_lyft_protoc_gen_star_v2",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "github.com/lyft/protoc-gen-star/v2",
               "version": "v2.0.1",
               "sum": "h1:keaAo8hRuAT0O3DfJ/wM3rufbAjGeJ1lAtWZHDjKGB0="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "com_github_lyft_protoc_gen_star_v2",
                         "generator_name": "com_github_lyft_protoc_gen_star_v2",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "github.com/lyft/protoc-gen-star/v2",
                         "version": "v2.0.1",
                         "sum": "h1:keaAo8hRuAT0O3DfJ/wM3rufbAjGeJ1lAtWZHDjKGB0="
                    },
                    "output_tree_hash": "16a219f8d88f8b707917244dcbc56454bc744abf96dc38aab04a61ccedc03d1a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_google_protobuf instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:152:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_google_protobuf",
               "generator_name": "org_golang_google_protobuf",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "google.golang.org/protobuf",
               "version": "v1.30.0",
               "sum": "h1:kPPoIgf3TsEvrm0PFe15JQ+570QVxYzEvvHqChK+cng="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_google_protobuf",
                         "generator_name": "org_golang_google_protobuf",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "google.golang.org/protobuf",
                         "version": "v1.30.0",
                         "sum": "h1:kPPoIgf3TsEvrm0PFe15JQ+570QVxYzEvvHqChK+cng="
                    },
                    "output_tree_hash": "ec05854670ffba3d0e3bb7d3a71778b7f592861b0690caf81f86476f4833f627"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository com_github_spf13_afero instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:100:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_spf13_afero",
               "generator_name": "com_github_spf13_afero",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "github.com/spf13/afero",
               "version": "v1.3.3",
               "sum": "h1:p5gZEKLYoL7wh8VrJesMaYeNxdEd1v3cb4irOk9zB54="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "com_github_spf13_afero",
                         "generator_name": "com_github_spf13_afero",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "github.com/spf13/afero",
                         "version": "v1.3.3",
                         "sum": "h1:p5gZEKLYoL7wh8VrJesMaYeNxdEd1v3cb4irOk9zB54="
                    },
                    "output_tree_hash": "5a8b791f84c66ffab5aea57d38dc803c1ed19a1382315dbe9a4e8071ea91b2e8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository com_github_iancoleman_strcase instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:50:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_iancoleman_strcase",
               "generator_name": "com_github_iancoleman_strcase",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "github.com/iancoleman/strcase",
               "version": "v0.2.0",
               "sum": "h1:05I4QRnGpI0m37iZQRuskXh+w77mr6Z41lwQzuHLwW0="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "com_github_iancoleman_strcase",
                         "generator_name": "com_github_iancoleman_strcase",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "github.com/iancoleman/strcase",
                         "version": "v0.2.0",
                         "sum": "h1:05I4QRnGpI0m37iZQRuskXh+w77mr6Z41lwQzuHLwW0="
                    },
                    "output_tree_hash": "9ce9acf16f014988c9968e5b78a13387007896bf1ee682f78d2a122d8e4764b2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository com_github_golang_protobuf instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:32:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_golang_protobuf",
               "generator_name": "com_github_golang_protobuf",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "github.com/golang/protobuf",
               "version": "v1.5.0",
               "sum": "h1:LUVKkCeviFUMKqHa4tXIIij/lbhnMbP7Fn5wKdKkRh4="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "com_github_golang_protobuf",
                         "generator_name": "com_github_golang_protobuf",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "github.com/golang/protobuf",
                         "version": "v1.5.0",
                         "sum": "h1:LUVKkCeviFUMKqHa4tXIIij/lbhnMbP7Fn5wKdKkRh4="
                    },
                    "output_tree_hash": "8c7340bb7720779a078f32095c0e79d0a13e98671970788cd9a2b1084296e881"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_x_tools instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:189:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_x_tools",
               "generator_name": "org_golang_x_tools",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "golang.org/x/tools",
               "version": "v0.7.0",
               "sum": "h1:W4OVu8VVOaIO0yzWMNdepAulS7YfoS3Zabrm8DOXXU4="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_x_tools",
                         "generator_name": "org_golang_x_tools",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "golang.org/x/tools",
                         "version": "v0.7.0",
                         "sum": "h1:W4OVu8VVOaIO0yzWMNdepAulS7YfoS3Zabrm8DOXXU4="
                    },
                    "output_tree_hash": "b5e37697694ba06cb48f074dccb077e161d0b5f651ba385b23e867b5f286efe2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_x_mod instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:164:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_x_mod",
               "generator_name": "org_golang_x_mod",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "golang.org/x/mod",
               "version": "v0.9.0",
               "sum": "h1:KENHtAZL2y3NLMYZeHY9DW8HW8V+kQyJsY/V9JlKvCs="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_x_mod",
                         "generator_name": "org_golang_x_mod",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "golang.org/x/mod",
                         "version": "v0.9.0",
                         "sum": "h1:KENHtAZL2y3NLMYZeHY9DW8HW8V+kQyJsY/V9JlKvCs="
                    },
                    "output_tree_hash": "88b521625d6ad1f11f42d0d7c8322d99ad1bc8994983d0a72b7d62134baaa98f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_x_text instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:183:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_x_text",
               "generator_name": "org_golang_x_text",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "golang.org/x/text",
               "version": "v0.8.0",
               "sum": "h1:57P1ETyNKtuIjB4SRd15iJxuhj8Gc416Y78H3qgMh68="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_x_text",
                         "generator_name": "org_golang_x_text",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "golang.org/x/text",
                         "version": "v0.8.0",
                         "sum": "h1:57P1ETyNKtuIjB4SRd15iJxuhj8Gc416Y78H3qgMh68="
                    },
                    "output_tree_hash": "f3957d60e07f34f85a04a98e1034c1f8aa3a9834b1e746cd487a65306c054148"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
          "definition_information": "Repository org_golang_x_sys instantiated at:\n  /workspaces/nighthawk/WORKSPACE:34:25: in <toplevel>\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/envoy/bazel/dependency_imports.bzl:158:42: in envoy_dependency_imports\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/com_github_chrusty_protoc_gen_jsonschema/deps.bzl:177:18: in go_dependencies\nRepository rule go_repository defined at:\n  /home/vscode/.cache/bazel/_bazel_vscode/569ca105ff1ee29ba68fef891d1fbf6b/external/bazel_gazelle/internal/go_repository.bzl:325:32: in <toplevel>\n",
          "original_attributes": {
               "name": "org_golang_x_sys",
               "generator_name": "org_golang_x_sys",
               "generator_function": "envoy_dependency_imports",
               "generator_location": None,
               "importpath": "golang.org/x/sys",
               "version": "v0.7.0",
               "sum": "h1:3jlCCIQZPdOYu1h8BkNvLz8Kgwtae2cagcG/VamtZRU="
          },
          "repositories": [
               {
                    "rule_class": "@bazel_gazelle//internal:go_repository.bzl%go_repository",
                    "attributes": {
                         "name": "org_golang_x_sys",
                         "generator_name": "org_golang_x_sys",
                         "generator_function": "envoy_dependency_imports",
                         "generator_location": None,
                         "importpath": "golang.org/x/sys",
                         "version": "v0.7.0",
                         "sum": "h1:3jlCCIQZPdOYu1h8BkNvLz8Kgwtae2cagcG/VamtZRU="
                    },
                    "output_tree_hash": "ae36ea74f35920d8e8e3acbefb75aa5f797520e5024e86daa3788feb0c86d42f"
               }
          ]
     }
]