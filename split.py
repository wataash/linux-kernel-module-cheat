import io
import os

meta = '''
:description: The perfect emulation setup to study and develop the <<linux-kernel>> v5.2.1, kernel modules, <<qemu-buildroot-setup,QEMU>>, <<gem5-buildroot-setup,gem5>> and x86_64, ARMv7 and ARMv8 <<userland-assembly,userland>> and <<baremetal-setup,baremetal>> assembly, <<c,ANSI C>>, <<cpp,C++>> and <<posix,POSIX>>. <<gdb>> and <<kgdb>> just work. Powered by <<about-the-qemu-buildroot-setup,Buildroot>> and <<about-the-baremetal-setup,crosstool-NG>>.  Highly automated. Thoroughly documented. Automated <<test-this-repo,tests>>. "Tested" in an Ubuntu 18.04 host.
:idprefix:
:idseparator: -
:nofooter:
:sectanchors:
:sectlinks:
:sectnumlevels: 6
:sectnums:
:toc-title:
:toc: macro
:toclevels: 6

'''

with open('README.adoc') as f:
    try:
        os.mkdir('splitted/')
    except FileExistsError as e:
        pass
    num_chapter = 0
    chapter = ''
    f2: io.TextIOWrapper = None

    for line in f:
        if line.startswith('== '):
            if f2 is not None:
                f2.close()
            num_chapter += 1
            fname = 'splitted/' + str(num_chapter).zfill(2) + ' ' + line[3:].rstrip() + '.adoc'
            f2 = open(fname, 'w')
            f2.write(meta)

        if num_chapter == 0:
            continue

        f2.write(line)

    f2.close()

exit(0)
