{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};

    python = pkgs.python312;
  in
  {
    devShells.${system} = {
      default = pkgs.mkShell {
        packages = [ 
          (python.withPackages(py: [
            py.numpy
            py.pandas
            py.matplotlib
          ]))
        ];
        shellHook = ''zsh'';
      };

      daming = pkgs.mkShell {
        packages = [
          (python.withPackages (py:[
            py.numpy
            py.pandas
            py.matplotlib
            py.scikit-learn
            py.seaborn
            py.plotly
            py.textblob

            # Manual Derivation
            # py.pycaret
            # py.apyori
            # py.olapy
          ]))
        ];

        shellHook = ''
          mkdir -p daming
          cd ./daming
          zsh
        '';
      };

      pcd = pkgs.mkShell {
        packages = [
          (python.withPackages (py:[
            py.numpy
            py.opencv4Full
          ]))
        ];

        shellHook = ''
          mkdir -p pcd
          cd ./pcd
          zsh
        '';
      };
    };
  };
}

