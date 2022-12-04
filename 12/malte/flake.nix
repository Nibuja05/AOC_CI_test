{
  inputs = {
    nixCargoIntegration.url = "github:yusdacra/nix-cargo-integration";
  };

  outputs = inputs:
    inputs.nixCargoIntegration.lib.makeOutputs {
      root = ./.;
      config = common: {
        shell = {
          packages = with common.pkgs; [
            rust-analyzer
            lldb
            treefmt
            cargo-watch
            cargo-flamegraph
            pkg-config
            hyperfine
          ];
        };
      };
    };
}
