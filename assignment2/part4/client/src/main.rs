#![allow(unused_mut)]
#![allow(unused_imports)]
#![allow(unused_variables)]
use std::{thread, time};
mod utils;

use nix;
use nix::ioctl_write_ptr;
mod bindings;
use bindings::*;
use opencv::core::{flip, Mat, Vec3b};
use opencv::videoio::*;
use opencv::{highgui::*, prelude::*, videoio};
use std::net::TcpStream;

use memmap::Mmap;
use memmap::MmapOptions;
mod server;
mod setup;
use nix::sys::ioctl;
use nix::sys::select;
use nix::sys::select::FdSet;
use server::*;
use setup::*;
mod app;
use app::*;
use std::{fs::File, os::unix::prelude::AsRawFd, str};
use std::{
    fs::OpenOptions,
    io::{self, prelude::*, Seek, SeekFrom, Write},
};
use utils::*;

fn get_pfn(virtual_address: usize) -> io::Result<u64> {
    println!("Virtual address: {}", virtual_address);
    let page_size = 4096; // Obtain this from sysconf(_SC_PAGESIZE) or page_size::get()
    let pagemap_entry_size = std::mem::size_of::<u64>();

    // Calculate the offset in the pagemap file for the corresponding virtual address
    let pagemap_offset = virtual_address / page_size * pagemap_entry_size;
    println!("Vaddr: {}, Offset: {}", virtual_address, pagemap_offset);

    // Open the pagemap file for the current process
    let mut pagemap_file = File::open("/proc/self/pagemap")?;

    // Seek to the corresponding entry in the pagemap file
    pagemap_file.seek(SeekFrom::Start(pagemap_offset as u64))?;

    // Read the pagemap entry
    let mut entry = [0; 8];
    pagemap_file.read_exact(&mut entry)?;

    // Convert to u64 and check if the page is present
    let entry_val = u64::from_ne_bytes(entry);
    println!("Entry: {:#066b}", entry_val);
    let is_present = (entry_val >> 63) & 1 == 1;

    // Mask out the flags and shift to get the PFN if present
    let pfn = if is_present {
        entry_val & ((1 << 55) - 1)
    } else {
        println!("Page not present");
        -1
    };

    Ok(pfn)
}

fn main() -> io::Result<()> {
    let mut f = File::options().write(true).read(true).open("/dev/video0")?;

    let mut fd = f.as_raw_fd();

    // im sorry for this one and I hate borrow rules so much
    let mut ftmp = File::options()
        .write(true)
        .read(true)
        .create(true)
        .open("tmp")?;

    let mut client: App = App {
        buffer: unsafe { memmap::MmapOptions::new().len(1).map_mut(&ftmp)? },
        file: f,
        buf: unsafe { std::mem::zeroed() },
        media_fd: fd,
    };
    client.start_device(3);

    client.buffer = unsafe {
        memmap::MmapOptions::new()
            .len(client.buf.length as usize)
            .map_mut(&client.file)?
    };

    // let buffer_addr = client.buffer.as_ptr() as usize;

    let mut buffer: Vec<u8> = vec![0; 4096]; // This is your buffer
    let buffer_ptr = buffer.as_ptr() as usize;
    buffer[0] = 1;
    let pfn = get_pfn(buffer_ptr)?;
    println!("PFN: {}", pfn);

    Ok(())
    // find physical pages for the buffer
}
