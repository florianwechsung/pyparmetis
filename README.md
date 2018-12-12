pyparmetis
==========

Python bindings to ParMETIS

## Instructions 

	export C_INCLUDE_PATH=/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.parmetis/include:$C_INCLUDE_PATH
	export C_INCLUDE_PATH=/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.metis/petsc-build/include:$C_INCLUDE_PATH
	export LD_LIBRARY_PATH=/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.parmetis/petsc-build/libparmetis/
	export LIBRARY_PATH=/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.parmetis/petsc-build/libparmetis/

and change the paths in `setup.py`
