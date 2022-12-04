{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, utils, ... }@inputs:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import inputs.nixpkgs { inherit system; };
        runTests = pkgs.writeShellApplication {
          name = "run-tests";
          text = ./run-tests.sh;
        };
      in rec {
        # `nix develop`
        devShell = pkgs.mkShell {
          # supply the specific rust version
          nativeBuildInputs = [
            runTests
          ];
        };
      });
}
