#!/usr/bin/env python

import os
from distutils.core import setup, Extension

import mpi4py

def include_flags(dirs):
    return ['-I' + d for d in dirs]

mpi4py_inc = mpi4py.get_include()

mpi_bin_dir = os.path.dirname( mpi4py.get_config()['mpicc'] )
mpi_dir = os.path.realpath( os.path.join(mpi_bin_dir,'..') )
mpi_dir = '/home/wechsung/bin/openmpi-2.1.1/build/'
mpi_inc_dir = os.path.join(mpi_dir, 'include')
mpi_lib_dir = os.path.join(mpi_dir, 'lib')

#TODO
parmetis_dir = '/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.parmetis/'
parmetis_inc_dir = os.path.join(parmetis_dir,'include')
parmetis_lib_dir = os.path.join(parmetis_dir,'petsc-build/libparmetis')

metis_dir = '/home/wechsung/bin/firedrake-dev-20181123-mkl/src/petsc/linux-gnu-c-opt/externalpackages/git.metis/petsc-build/'
metis_inc_dir = os.path.join(metis_dir,'include')

pyparmetis = Extension('_pyparmetis',
   sources = ['pyparmetis.i', ],
   libraries = ['parmetis','mpich','opa','mpl','rt','pthread'], #TODO
   include_dirs = [parmetis_inc_dir, metis_inc_dir, mpi_inc_dir, mpi4py_inc],
   library_dirs = [parmetis_lib_dir, mpi_lib_dir],
   runtime_library_dirs = [parmetis_lib_dir, mpi_lib_dir],
   swig_opts = include_flags([parmetis_inc_dir, metis_inc_dir, mpi4py_inc])
       + ['-DIDXTYPEWIDTH=64','-DREALTYPEWIDTH=64']
   )

setup (name = 'pyparmetis',
       version = '0.1',
       ext_modules = [pyparmetis],
       py_modules = ["pyparmetis"],
       )

