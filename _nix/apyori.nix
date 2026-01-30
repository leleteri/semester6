{ lib
, buildPythonPackage
, fetchPypi
, setuptools
}:

buildPythonPackage rec {
  pname = "apyori";
  version = "1.1.2";

  src = fetchPypi {
    inherit pname version;
    sha256 = "sha256-mhp7cwh3wa1mgbpvnmd2my5jpq29d3lk";
  };
  
  doCheck = false;

  pyproject = true;
  build-system = [
    setuptools
  ];
}
