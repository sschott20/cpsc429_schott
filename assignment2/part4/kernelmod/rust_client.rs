// SPDX-License-Identifier: GPL-2.0

//! Rust minimal sample.
#![allow(missing_docs)]
#![allow(unused_imports)]
#![allow(unused_mut)]
#![allow(unused_variables)]
#![allow(non_camel_case_types)]
#![allow(non_upper_case_globals)]
#![allow(non_snake_case)]

use core::mem::zeroed;
use kernel::bindings::{filp_open, vfs_ioctl};
use kernel::file::SeekFrom;
use kernel::file::{File, Operations};
use kernel::io_buffer::IoBufferReader;
use kernel::io_buffer::IoBufferWriter;
use kernel::net::TcpStream;
use kernel::net::{Ipv4Addr, SocketAddr, SocketAddrV4};
use kernel::prelude::Vec;
use kernel::prelude::*;
use kernel::sync::smutex::Mutex;
use kernel::{miscdev, Module};

mod ionum;
use ionum::*;
mod bindings;
use bindings::*;

module! {
    type: RustClient,
    name: "rust_client",
    author: "Alex Schott",
    license: "GPL",
}

const PAGE_OFFSET: u64 = 0xffff_8000_0000_0000; // example for x86_64, typically high half

fn pfn_to_virt(pfn: u64) -> u64 {
    ((pfn << 12) + PAGE_OFFSET) as u64
}

struct RustClient {
    _dev: Pin<Box<miscdev::Registration<RustClient>>>,
}

impl kernel::Module for RustClient {
    fn init(_name: &'static CStr, _module: &'static ThisModule) -> Result<Self> {
        pr_info!("rust_client init (init)\n");
        let reg = miscdev::Registration::new_pinned(fmt!("rust_client"), ())?;

        
      
        Ok(RustClient { _dev: reg })
    }
}
#[vtable]
impl Operations for RustClient {
    fn open(_context: &(), _file: &File) -> Result {
        pr_info!("RustClient was opened\n");

        // let stream = TcpStream::connect("127.0.0.1:54321").unwrap();
        // ioctl_read!(vidioc_querycap, VIDIOC_MAGIC, 0, v4l2_capability);
        // let _ = unsafe { vfs_ioctl(file, VIDIOC_MAGIC as u32, 0) };

        Ok(())
    }
    fn read(
        _data: (),
        _file: &File,
        writer: &mut impl IoBufferWriter,
        _offset: u64,
    ) -> Result<usize> {
        pr_info!("RustClient Read\n");
        // let mut file = unsafe {
        //     let c_str = CStr::from_bytes_with_nul(b"/dev/video2\0").unwrap();
        //     filp_open(c_str.as_ptr() as *const i8, 0, 0)
        // };
        // // let mut stream = TcpStream::connect()
        // let addr = Ipv4Addr::new(127, 0, 0, 1);
        // let sok: SocketAddr = SocketAddr::V4(SocketAddrV4::new(addr, 54321));
        // let namespace = kernel::net::init_ns();
        // let lo_cstr = CStr::from_bytes_with_nul(b"lo\0").unwrap();
        // namespace.dev_get_by_name(lo_cstr).unwrap();
        // let listener = kernel::net::TcpListener::try_new(&namespace, &sok).unwrap();
        // let mut stream = listener.accept(true).unwrap();

        Ok(10)
    }
    fn write(
        _data: (),
        _file: &File,
        reader: &mut impl IoBufferReader,
        _offset: u64,
    ) -> Result<usize> {
        pr_info!("RustClient Write\n");

        let mut info_capability: v4l2_capability = unsafe { zeroed() };

        let mut filp = unsafe {
            let c_str = CStr::from_bytes_with_nul(b"/dev/video0\0").unwrap();
            filp_open(c_str.as_ptr() as *const i8, 2, 0)
        };

        let _ = unsafe { vfs_ioctl(filp, VIDIOC_QUERYCAP, &mut info_capability as *mut _ as u64) };

        pr_info!(
            "driver: {:?}\n",
            core::str::from_utf8(&info_capability.driver)
        );

        Ok(1)
    }

    // will be used to pass data / addr from user to kernel space
    // seekfrom start means we are sending the physical address of the mmap buffer
    fn seek(_data: (), _file: &File, offset: SeekFrom) -> Result<u64> {
        pr_info!("Rust Client Seek\n");
        let _len = match offset {
            SeekFrom::Start(pfn) => {
                pr_info!("Incoming pfn: {}\n", pfn);
                let kern_addr = pfn_to_virt(pfn);
                pr_info!("Kernel virtual addr: {:x}\n", kern_addr);

                let mut buffer = Vec::new();
                let _ = buffer.try_push(69);
                let buffer_addr = buffer.as_ptr() as usize;
                pr_info!("Buffer virtual addr: {:x}\n", buffer_addr);
                unsafe { pr_info!("Buffer value: {}\n", *(buffer_addr as *const u8)) };

                let byte = unsafe { *(kern_addr as *const u8) };
                pr_info!("First byte at that address: {}\n", byte);
            }
            _ => {
                return Err(EINVAL);
            }
        };

        Ok(10)
    }
}
impl Drop for RustClient {
    fn drop(&mut self) {
        pr_info!("RustClient (exit)\n");
    }
}
