import os
import re
import shutil

# If you need to update boost
# 1. Put boost subfolder from source archive in include directory
# 2. Compile pcsx2.vcxproj and boost.vcxproj with /showIncludes
# 3. Process build log with this script (log file must be called includes.txt)
# 4. Used boost includes will be copied to '_boost' subdirectory. Replace include/boost with its contents.


boost_root_re = re.compile(r'(?i).+ ([^ ]+pcsx2\\3rdparty\\boost-[\d\.]+\\include\\boost/[^ /]+\.[^ /]+$)')
boost_subdir_re = re.compile(r'(?i).+ ([^ ]+pcsx2\\3rdparty\\boost-[\d\.]+\\include\\boost/[^ /]+)/[^ ]+\.[^ /]+$')


with open('includes.txt') as f:
    files = set()
    dirs = set()
    for line in f:
        m = boost_root_re.match(line)
        if m:
            files.add(m.group(1).strip())
            continue
        m = boost_subdir_re.match(line)
        if m:
            dirs.add(m.group(1).strip())
    os.makedirs('_boost')
    for f in files:
        print(f)
        shutil.copy(f, '_boost')
    for d in dirs:
        print(d)
        name = os.path.basename(d)
        shutil.copytree(d, '_boost/'+name)
