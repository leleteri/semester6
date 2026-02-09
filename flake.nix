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
    packages.${system} = {
      apyori = import ./_nix/apyori.nix;
      # olapy = import ./_nix/olapy.nix;

      default = [
        (python.withPackages (py: with py; [
          numpy
          pandas
          matplotlib
        ]))
      ];

      daming = self.packages.${system}.default ++ [
        (python.withPackages (py: with py; [
          scikit-learn
          seaborn
          plotly
          textblob
          self.packages.${system}.apyori
        ]))
      ];
    };
      
    devShells.${system} = {
      default = pkgs.mkShell {
        packages = self.packages.${system}.default; 
        shellHook = ''zsh'';
      };

      pcd = pkgs.mkShell {
        packages = [
          (python.withPackages (py:[
            py.opencv4Full
          ]))
        ];

        shellHook = ''
          zsh
        '';
      };

      daming = pkgs.mkShell {
        packages = self.packages.${system}.daming;
        shellHook = ''
          zsh
        '';
      };
    };
  };
}

