import React, { useRef, useEffect } from "react";
import './styles/style.css';

function Board() {
    const canvasRef = useRef(null);
    const colorsRef = useRef(null);
    const socketRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        const context = canvas.getContext('2d');
        const colors = document.getElementsByClassName('color');
        const current = {
            color: 'black'
        };
        let dataURL = '';
        let drawing = false;

        const onColorUpdate = (e) => {
            current.color = e.target.className.split(' ')[1];
        };

        const drawline = (x0, y0, x1, y1, color) => {
            if (!drawing) return;
            context.beginPath();
            context.moveTo(x0, y0);
            context.lineTo(x1, y1);
            context.strokeStyle = color;
            context.lineWidth = 2;
            context.stroke();
            context.closePath();
        };

        const onmousedown = (e) => {
            drawing = true;
            current.x = e.clientX || e.touches[0].clientX;
            current.y = e.clientY || e.touches[0].clientY;
        };

        const onmousemove = (e) => {
            if (!drawing) return;
            drawline(current.x, current.y, e.clientX || e.touches[0].clientX, e.clientY || e.touches[0].clientY, current.color);
            current.x = e.clientX || e.touches[0].clientX;
            current.y = e.clientY || e.touches[0].clientY;
        };

        const onmouseup = (e) => {
            if (!drawing) return;
            drawing = false;
            drawline(current.x, current.y, e.clientX || e.touches[0].clientX, e.clientY || e.touches[0].clientY, current.color);
        };

        const onmouseout = (e) => {
            drawing = false;
        };

        const throttle = (callback, delay) => {
            let previousCall = new Date().getTime();
            return function() {
                let time = new Date().getTime();
                if ((time - previousCall) >= delay) {
                    previousCall = time;
                    callback.apply(null, arguments);
                }
            };
        };

        const touch = (e) => {
            const touch = e.touches[0];
            const mouseEvent = new MouseEvent(e.type, {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            canvas.dispatchEvent(mouseEvent);
        };

        canvas.addEventListener('mousedown', onmousedown, false);
        canvas.addEventListener('mouseup', onmouseup, false);
        canvas.addEventListener('mouseout', onmouseout, false);
        canvas.addEventListener('mousemove', throttle(onmousemove, 10), false);

        canvas.addEventListener('touchstart', touch, false);
        canvas.addEventListener('touchend', touch, false);
        canvas.addEventListener('touchcancel', touch, false);
        canvas.addEventListener('touchmove', throttle(onmousemove, 10), false);

        for (let i = 0; i < colors.length; i++) {
            colors[i].addEventListener('click', onColorUpdate, false);
        }

        const onresize = () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            let img = new Image();
            img.src = dataURL;
            img.onload = () => {
                context.drawImage(img, 0, 0);
            };
        };

        window.addEventListener('resize', onresize, false);
        onresize();
        socketRef.current = new WebSocket('ws://127.0.0.1:8000/ws/board/')

        socketRef.current.onopen = () => {
            console.log('connected')
        }
        socketRef.current.onerror = e=>{
            console.log(e)
        };

        return () => {
            window.removeEventListener('resize', onresize);
            canvas.removeEventListener('mousedown', onmousedown);
            canvas.removeEventListener('mouseup', onmouseup);
            canvas.removeEventListener('mouseout', onmouseout);
            canvas.removeEventListener('mousemove', throttle(onmousemove, 10));
            canvas.removeEventListener('touchstart', touch);
            canvas.removeEventListener('touchend', touch);
            canvas.removeEventListener('touchcancel', touch);
            canvas.removeEventListener('touchmove', throttle(onmousemove, 10));
            for (let i = 0; i < colors.length; i++) {
                colors[i].removeEventListener('click', onColorUpdate);
            }
        };
    }, []);

    return (
        <>
            <canvas ref={canvasRef} className="whiteboard"/>
            <div ref={colorsRef} className="colors">
                <div className="color black"></div>
                <div className="color red"></div>
                <div className="color yellow"></div>
                <div className="color blue"></div>
                <div className="color green"></div>
            </div>
            Board
        </>
    );
}

export default Board;
