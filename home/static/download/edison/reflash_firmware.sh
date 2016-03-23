#!/bin/sh

error(){
  echo "Something broke. Exiting." 1>&2
  exit 1
}

echo "Running: mkdir /update" 1>&2
mkdir /update || error

echo "Running: /sbin/losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update" 1>&2
/sbin/losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update || error

echo "Running: mount /dev/loop0 /update" 1>&2
mount /dev/loop0 /update || error

echo "Running: rm -rf /update/*" 1>&2
rm -rf /update/* || error

echo "Running: wget --no-check-certificate http://neil-lakin.com/download/edison/firmware_reflash_file_list.sh -P /tmp" 1>&2
wget --no-check-certificate http://neil-lakin.com/download/edison/firmware_reflash_file_list.sh -P /tmp || error

echo "Running: chmod +x /tmp/firmware_update_file_list.sh" 1>&2
chmod +x /tmp/firmware_reflash_file_list.sh || error

echo "Running: /tmp/firmware_reflash_file_list.sh" 1>&2
/tmp/firmware_reflash_file_list.sh || error

echo "Running: reboot ota" 1>&2
reboot ota

echo "Running: umount /update" 1>&2
umount /update || error

echo "Running: rmdir /update" 1>&2
rmdir /update || error

# SEE COMMENT ABOVE
#echo "Running: modprobe g_multi" 1>&2
#/sbin/modprobe g_multi || error

echo "DONE!" 1>&2
