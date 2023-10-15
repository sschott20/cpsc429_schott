#![allow(unused_imports)]

use opencv::core::{flip, Mat, Vec3b, Vector};
use opencv::videoio::*;
use opencv::{highgui::*, imgcodecs, prelude::*, videoio};

mod utils;
use tflitec::interpreter::{Interpreter, Options};
use tflitec::model::Model;
use utils::*;

use std::io::prelude::*;
use std::io::{Read, Write};
use std::net::TcpStream;

fn main() {
    println!("Client started");
    // load model and create interpreter
    let mut stream = TcpStream::connect("127.0.0.1:54321").expect("Connection failed");

    // open camera
    let mut cam = videoio::VideoCapture::new(0, videoio::CAP_ANY).unwrap(); // 0 is the default camera
    videoio::VideoCapture::is_opened(&cam).expect("Open camera [FAILED]");
    cam.set(CAP_PROP_FPS, 30.0)
        .expect("Set camera FPS [FAILED]");

    loop {
        let mut frame = Mat::default();
        cam.read(&mut frame).expect("VideoCapture: read [FAILED]");

        if frame.size().unwrap().width > 0 {
            {
                let mut buffer: Vector<u8> = Vec::new().into();
                buffer.clear();
                let _ = opencv::imgcodecs::imencode(".jpg", &frame, &mut buffer, &Vector::new());

                let buffer: Vec<u8> = buffer.to_vec();
                let mut stream = TcpStream::connect("127.0.0.1:54321").unwrap();
                stream.write_all(&buffer).unwrap();
                println!("image sent to server");
            }

            let mut response_buffer = Vec::new();
            let mut response = [0u8; 1024];
            match stream.read(&mut response) {
                Ok(n) if n > 0 => {
                    response_buffer.extend_from_slice(&response[0..n]);
                    println!("Received response from server: {:?}", response_buffer);
                }
                Ok(_) => {
                    // No data received, continue the loop
                }
                Err(err) => {
                    eprintln!("Error reading from server: {:?}", err);
                    break; // Break the loop on error
                }
            }

            // imshow("MoveNet", &flipped).expect("imshow [ERROR]");
            // print out response
        }

        // keypress check
        let key = wait_key(1).unwrap();
        if key > 0 && key != 255 {
            break;
        }
    }
}
