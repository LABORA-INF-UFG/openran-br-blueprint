# OpenRAN@Brasil Blueprint

## Requirements

- virt-manager 
- qemu-kvm 
- libvirt-daemon-system 
- libvirt-clients 
- bridge-utils

## Deploying VM

### 1st Step - Download the VM Image
Download the [Virtual Machine image](https://drive.google.com/file/d/1yfi_3ZF0s9fDrRXnX73U2WOef0D8573p/view?usp=drive_link) and unzip it.

``` bash
unzip v0_Virt-manager.zip
```

### 2nd Step - Create the virtual machine

Start the `virt-Manager` with sudo privileges.

Select the option `New Virtual Machine` under the `File` menu.

Mark the option `Import existing disk image` before forwarding.

![new vm](docs/figs/0-vm-install.jpg)

Then, browse and select the downloaded image `v0_original.qcow2`

![choose image](docs/figs/1-vm-install.jpg)

You may need to add a new `Pool` by clicking in the `+` button marked with 0 in the image above.

Next, set the operating system as `Ubuntu 20.04`, and advance.

![choose os](docs/figs/2-vm-install.jpg)


In the next screen choose the amount of memory and CPUs for the VM and go forward.

Finally, name your VM and select `Finish`. The VM will be created and initialize.

### 3rd Step - Accessing the virtual machine

In order to access the VM, use the default user.
``` bash
username: openran-br
password: openran-br
```

## Next Steps

Test the deploy of an xApp [(Deploying xApps)](docs/xapp.md).