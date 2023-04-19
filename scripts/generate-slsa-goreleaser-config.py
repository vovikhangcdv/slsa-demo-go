import os

matrix = {
    "os": ["linux", "windows", "darwin"],
    "arch": ["amd64", "arm64"]
}

template = """# Filename: ${{{{matrix.os}}}}-${{{{matrix.arch}}}}.yml
# Version for this file.
version: 1

# (Optional) List of env variables used during compilation.
env:
    - GO111MODULE=on
    - CGO_ENABLED=0

# (Optional) Flags for the compiler.
flags:
    - -trimpath
    - -tags=netgo

# The OS to compile for. `GOOS` env variable will be set to this value.
goos: {os}

# The architecture to compile for. `GOARCH` env variable will be set to this value.
goarch: {arch}

# (Optional) Entrypoint to compile.
# main: ./path/to/main.go

# (Optional) Working directory. (default: root of the project)
# dir: ./relative/path/to/dir

# Binary output name.
# {{{{ .Os }}}} will be replaced by goos field in the config file.
# {{{{ .Arch }}}} will be replaced by goarch field in the config file.
binary: binary-guess-number-game-{{{{ .Os }}}}-{{{{ .Arch }}}}

# (Optional) ldflags generated dynamically in the workflow, and set as the `evaluated-envs` input variables in the workflow.
# ldflags:
#     - "-X main.Version={{{{ .Env.VERSION }}}}"
#     - "-X main.Commit={{{{ .Env.COMMIT }}}}"
#     - "-X main.CommitDate={{{{ .Env.COMMIT_DATE }}}}"
#     - "-X main.TreeState={{{{ .Env.TREE_STATE }}}}" 
"""

output_directory = ".github/slsa-goreleaser-configs"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for os_value in matrix["os"]:
    for arch_value in matrix["arch"]:
        config_content = template.format(os=os_value, arch=arch_value)
        filename = f"{output_directory}/{os_value}-{arch_value}.yml"
        with open(filename, "w") as f:
            f.write(config_content)
