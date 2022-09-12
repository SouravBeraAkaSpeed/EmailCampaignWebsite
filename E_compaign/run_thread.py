from subprocess import call


def open_py_file(args):
    call(args)
open_py_file(args=['python','-c',f"import os; print(os.getcwd())"] )
# open_py_file(args=['python','-c',f"import instance1.main; main(2)"] )