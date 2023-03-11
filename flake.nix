{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {self, nixpkgs, utils}:
  let out = system:
  let pkgs = nixpkgs.legacyPackages."${system}";
  in {

    devShell = pkgs.mkShell {
      buildInputs = with pkgs; [
        python3Packages.django
      ];

      shellHook = ''
      source venv/bin/activate            
      '';
    };

    defaultApp = utils.lib.mkApp {
      drv = self.defaultPackage."${system}";
    };

    run = {
      script = ''
        #!/usr/bin/env bash
        source env/bin/activate
        python3 manage.py runserver
      '';
    };

  }; in with utils.lib; eachSystem defaultSystems out;


}
