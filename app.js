// Hyperion Game Engine Interactive Canvas App Logic
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('game-canvas');
    const ctx = canvas.getContext('2d');
    const consoleOutput = document.getElementById('console-output');

    function resizeCanvas() {
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Game Engine State
    const state = {
        player: { x: 100, y: 100, vx: 2, vy: 1, radius: 14, color: '#3b82f6' },
        enemies: [
            { x: 300, y: 200, color: '#ef4444', targetX: 100, targetY: 100 },
            { x: 450, y: 320, color: '#f59e0b', targetX: 100, targetY: 100 }
        ],
        particles: [],
        dungeonRooms: [
            { x: 40, y: 40, w: 220, h: 180 },
            { x: 300, y: 120, w: 260, h: 220 },
            { x: 150, y: 280, w: 200, h: 160 }
        ],
        fps: 60,
        lastTime: performance.now()
    };

    function log(msg, type = 'info') {
        const entry = document.createElement('div');
        entry.className = `log-entry log-${type}`;
        entry.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
        consoleOutput.appendChild(entry);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }

    // WebAudio Sound Effects Synthesizer
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function playSynthSFX(type = 'laser') {
        if (!audioCtx) audioCtx = new AudioCtx();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);

        const now = audioCtx.currentTime;
        if (type === 'laser') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(880, now);
            osc.frequency.exponentialRampToValueAtTime(110, now + 0.2);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
            osc.start(now);
            osc.stop(now + 0.2);
            log('[AUDIO] Played Laser Synthesizer SFX', 'info');
        } else if (type === 'explosion') {
            osc.type = 'square';
            osc.frequency.setValueAtTime(150, now);
            osc.frequency.exponentialRampToValueAtTime(40, now + 0.4);
            gain.gain.setValueAtTime(0.4, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
            osc.start(now);
            osc.stop(now + 0.4);
            log('[AUDIO] Played Explosion Synthesizer SFX', 'warn');
        }
    }

    // Particle Emission
    function spawnParticles(x, y, color = '#3b82f6', count = 12) {
        for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 4 + 1;
            state.particles.push({
                x, y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                radius: Math.random() * 4 + 2,
                life: 1.0,
                color
            });
        }
    }

    // Render Engine Loop
    function render(time) {
        const dt = (time - state.lastTime) / 1000;
        state.lastTime = time;
        state.fps = Math.round(1 / (dt || 0.016));
        document.getElementById('fps-counter').textContent = state.fps;

        // Clear Canvas
        ctx.fillStyle = '#070a13';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 1. Draw Procedural Dungeon Rooms & Grid
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.15)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath();
            ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height);
            ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath();
            ctx.moveTo(0, y); ctx.lineTo(canvas.width, y);
            ctx.stroke();
        }

        // Draw Dungeon Rooms
        state.dungeonRooms.forEach(r => {
            ctx.fillStyle = 'rgba(21, 28, 46, 0.7)';
            ctx.strokeStyle = '#3b82f6';
            ctx.lineWidth = 2;
            ctx.fillRect(r.x, r.y, r.w, r.h);
            ctx.strokeRect(r.x, r.y, r.w, r.h);
        });

        // 2. Physics & Player Update
        state.player.x += state.player.vx;
        state.player.y += state.player.vy;
        if (state.player.x < 20 || state.player.x > canvas.width - 20) state.player.vx *= -1;
        if (state.player.y < 20 || state.player.y > canvas.height - 20) state.player.vy *= -1;

        // Draw Player
        ctx.beginPath();
        ctx.arc(state.player.x, state.player.y, state.player.radius, 0, Math.PI * 2);
        ctx.fillStyle = state.player.color;
        ctx.shadowColor = state.player.color;
        ctx.shadowBlur = 15;
        ctx.fill();
        ctx.shadowBlur = 0;

        // 3. Enemies & AI Path lines
        state.enemies.forEach(e => {
            e.x += (state.player.x - e.x) * 0.01;
            e.y += (state.player.y - e.y) * 0.01;

            // Draw A* Path Line to player
            ctx.beginPath();
            ctx.moveTo(e.x, e.y);
            ctx.lineTo(state.player.x, state.player.y);
            ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
            ctx.setLineDash([4, 4]);
            ctx.stroke();
            ctx.setLineDash([]);

            // Draw Enemy
            ctx.beginPath();
            ctx.arc(e.x, e.y, 10, 0, Math.PI * 2);
            ctx.fillStyle = e.color;
            ctx.fill();
        });

        // 4. Update & Draw Particles
        for (let i = state.particles.length - 1; i >= 0; i--) {
            const p = state.particles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.life -= 0.02;
            if (p.life <= 0) {
                state.particles.splice(i, 1);
                continue;
            }
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius * p.life, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.life;
            ctx.fill();
            ctx.globalAlpha = 1.0;
        }

        requestAnimationFrame(render);
    }

    requestAnimationFrame(render);

    // Button Interactivity
    document.getElementById('btn-regen').addEventListener('click', () => {
        state.dungeonRooms = [
            { x: Math.random() * 100 + 20, y: Math.random() * 100 + 20, w: 200, h: 160 },
            { x: Math.random() * 200 + 200, y: Math.random() * 150 + 100, w: 240, h: 180 }
        ];
        spawnParticles(canvas.width / 2, canvas.height / 2, '#06b6d4', 30);
        log('[WORLD] Regenerated Procedural Dungeon Level Architecture', 'success');
    });

    document.getElementById('btn-spawn').addEventListener('click', () => {
        const ex = Math.random() * (canvas.width - 100) + 50;
        const ey = Math.random() * (canvas.height - 100) + 50;
        state.enemies.push({ x: ex, y: ey, color: '#ef4444', targetX: state.player.x, targetY: state.player.y });
        spawnParticles(ex, ey, '#ef4444', 20);
        playSynthSFX('laser');
        log(`[ECS] Spawned Enemy Unit at (${Math.round(ex)}, ${Math.round(ey)})`, 'warn');
    });

    document.getElementById('btn-sfx').addEventListener('click', () => {
        playSynthSFX('explosion');
        spawnParticles(state.player.x, state.player.y, '#f59e0b', 25);
    });
});
