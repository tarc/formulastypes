import os
import ycm_core
import platform

flags = [
'-Wall',
'-Wextra',
'-Werror',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
'-std=c++11',
'-x', 'c++',
'-isystem', 'C:\\MinGW\\lib\\gcc\\i686-w64-mingw32\\4.8.1\\include\\c++',
#'-I', './src',
#'-isystem', '/usr/include',         # Boost and OpenSSL are here
#'-isystem', '/usr/local/include',   # CppCMS is here

# Without the two below, nothing works
#'-isystem', '/usr/lib/llvm-3.4/include',
#'-isystem', 'C:\\ProgramData\\LLVM\\lib\\clang\\3.6.0\\include'
#'-fms-extensions',
#'-isystem', '/usr/lib/clang/3.4/include'
]

if platform.system() == "Windows":
  flags.append('-isystem')
  flags.append('C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\VC\\include')

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )

def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def FlagsForFile( filename, **kwargs ):
  relative_to = DirectoryOfThisScript()
  final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
