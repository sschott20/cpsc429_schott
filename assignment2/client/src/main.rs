#![allow(unused_imports)]

use opencv::core::{flip, Vec3b};
use opencv::videoio::*;
use opencv::{highgui::*, prelude::*, videoio};

mod utils;
use tflitec::interpreter::{Interpreter, Options};
use tflitec::model::Model;
use utils::*;

use std::io::prelude::*;
use std::io::{Read, Write};
use std::net::TcpStream;

fn main() -> opencv::Result<()> {
    // load model and create interpreter
    let mut stream = TcpStream::connect("127.0.0.1:54321")?;

    // let mut stream = TcpStream::connect("
    // let options = Options::default();
    // let path = format!("resource/lite-model_movenet_singlepose_lightning_tflite_int8_4.tflite");
    // let model = Model::new(&path).expect("Load model [FAILED]");
    // let interpreter = Interpreter::new(&model, Some(options)).expect("Create interpreter [FAILED]");
    // interpreter
    //     .allocate_tensors()
    //     .expect("Allocate tensors [FAILED]");
    // Resize input

    // open camera
    let mut cam = videoio::VideoCapture::new(0, videoio::CAP_ANY)?; // 0 is the default camera
    videoio::VideoCapture::is_opened(&cam).expect("Open camera [FAILED]");
    cam.set(CAP_PROP_FPS, 30.0)
        .expect("Set camera FPS [FAILED]");

    loop {
        let mut frame = Mat::default();
        cam.read(&mut frame).expect("VideoCapture: read [FAILED]");

        if frame.size()?.width > 0 {
            let mut buffer = Vec::new();
            opencv::imgcodecs::imencode_def(".png", &frame, &mut buffer)?;

            let mut stream = TcpStream::connect("127.0.0.1:54321")?;
            stream.write_all(&serialized)?;
            
            // imshow("MoveNet", &flipped).expect("imshow [ERROR]");
        }
        // keypress check
        let key = wait_key(1)?;
        if key > 0 && key != 255 {
            break;
        }
    }
}
