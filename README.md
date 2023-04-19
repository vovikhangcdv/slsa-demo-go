# slsa-demo-go

This is a demo app that applying the [SLSA framework](https://github.com/slsa-framework/slsa) and [Scorecard](https://github.com/ossf/scorecard) - Guess Number Game

## Setup

Setup `slsa-goreleaser` configs for multi-platform builds

    ```bash
    python3 scripts/setup.py
    ```

## Release

Trigger a release then trigger slsa-goreleaser to build and upload the release artifacts.
