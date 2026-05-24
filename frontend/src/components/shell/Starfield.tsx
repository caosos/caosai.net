import React, { useEffect, useRef } from 'react';

export default function Starfield() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animId: number;
    const stars: { x: number; y: number; z: number; pz: number }[] = [];
    const NUM = 280;

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener('resize', resize);

    for (let i = 0; i < NUM; i++) {
      stars.push({
        x: Math.random() * canvas.width - canvas.width / 2,
        y: Math.random() * canvas.height - canvas.height / 2,
        z: Math.random() * canvas.width,
        pz: 0,
      });
    }

    const draw = () => {
      ctx.fillStyle = 'rgba(6, 6, 15, 0.18)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      stars.forEach((s) => {
        s.pz = s.z;
        s.z -= 0.6;
        if (s.z <= 0) {
          s.x = Math.random() * canvas.width - cx;
          s.y = Math.random() * canvas.height - cy;
          s.z = canvas.width;
          s.pz = s.z;
        }

        const sx = (s.x / s.z) * canvas.width + cx;
        const sy = (s.y / s.z) * canvas.height + cy;
        const px = (s.x / s.pz) * canvas.width + cx;
        const py = (s.y / s.pz) * canvas.height + cy;

        const size = Math.max(0.3, (1 - s.z / canvas.width) * 2.2);
        const alpha = Math.min(1, (1 - s.z / canvas.width) * 1.4);

        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(sx, sy);
        ctx.strokeStyle = `rgba(180, 160, 255, ${alpha * 0.8})`;
        ctx.lineWidth = size;
        ctx.stroke();
      });

      animId = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener('resize', resize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 0,
        pointerEvents: 'none',
      }}
    />
  );
}
