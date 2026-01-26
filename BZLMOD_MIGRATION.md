# Bzlmod Migration Status

This repository has been partially migrated to use Bazel's bzlmod (Bazel Module) system for dependency management.

## What is Bzlmod?

Bzlmod is Bazel's modern dependency management system that replaces the legacy WORKSPACE-based approach. It provides:
- Better dependency resolution
- Version conflict detection
- Transitive dependency management
- Module registry support

## Current Migration Status

### ✅ Successfully Migrated

1. **Bzlmod Enabled**: The `.bazelrc` file has `--enable_bzlmod` enabled
2. **MODULE.bazel Created**: Core module definition with Python dependencies
3. **Python Dependencies**: Fully migrated to bzlmod using rules_python extensions
   - Python 3.12 toolchain configured via bzlmod
   - pip dependencies managed through MODULE.bazel
   - `nh_pip3` repository created from `tools/base/requirements.txt`

### ⚠️ Partial Migration (Hybrid Approach)

**Envoy and Related Dependencies**: Still loaded via WORKSPACE due to:
- Envoy itself isn't fully bzlmod-compatible for external consumption
- Complex dependency chain with specific version requirements
- HDR Histogram C library not available in Bazel Central Registry

**Why Hybrid?**
The project uses a hybrid approach where:
- Bzlmod manages what it can (Python deps, core build tools)
- WORKSPACE handles Envoy and its ecosystem
- This is a recommended transitional approach per Bazel documentation

### 🔧 Known Issues

1. **Protobuf Version Conflicts**: When building with GCC, there are compilation errors related to protobuf version mismatches between WORKSPACE (older version) and bzlmod dependencies (newer versions)

2. **LLVM Toolchain**: The pre-built LLVM toolchain requires `libtinfo.so.5` which isn't available in modern Ubuntu

3. **rules_foreign_cc Compatibility**: Version conflicts when bzlmod and WORKSPACE both try to manage this dependency

## Files Modified

- `MODULE.bazel`: New file defining the Bazel module with Python dependencies
- `.bazelrc`: Updated to enable bzlmod (`--enable_bzlmod`)
- `WORKSPACE`: Commented out Python dependency loading (now handled by bzlmod)
- `MODULE.bazel.lock`: Auto-generated lock file for bzlmod dependencies

## How to Build

### Standard Build (with known issues)
```bash
CARGO_BAZEL_REPIN=true bazel build //source/exe:nighthawk_client_entry_lib
```

The `CARGO_BAZEL_REPIN=true` environment variable is needed due to Rust dependency lockfile updates when using bzlmod.

### Alternative: Use GCC Toolchain
```bash
CARGO_BAZEL_REPIN=true bazel build --config=gcc //source/exe:nighthawk_client_entry_lib
```

## Future Work

To complete the bzlmod migration:

1. **Wait for Envoy bzlmod Support**: Monitor Envoy project's bzlmod migration
2. **Migrate HDR Histogram**: Either:
   - Publish to Bazel Central Registry
   - Use bzlmod extensions for http_archive
3. **Resolve Version Conflicts**: Once Envoy is bzlmod-compatible, remove WORKSPACE entirely
4. **Test Full Build**: Ensure all targets build and tests pass

## Benefits Achieved

Even with the partial migration:
- ✅ Modern dependency management for new dependencies
- ✅ Better Python toolchain management
- ✅ Clearer separation between bzlmod and legacy WORKSPACE deps
- ✅ Foundation for future full migration
- ✅ Alignment with Bazel's recommended practices

## References

- [Bazel bzlmod Documentation](https://bazel.build/docs/bzlmod)
- [bzlmod Migration Guide](https://bazel.build/migrate/bzlmod)
- [Bazel Central Registry](https://registry.bazel.build/)
- [rules_python bzlmod Support](https://github.com/bazelbuild/rules_python)
