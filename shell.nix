{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    python313
    python313Packages.python-lsp-server
  ];
}
