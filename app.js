// Hyperion Cyber-Pink Engine App Logic - Fully Interactive Engine & Equipment Framework

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

    // Logger
    function log(msg, type = 'info') {
        const entry = document.createElement('div');
        entry.className = `log-entry log-${type}`;
        entry.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
        consoleOutput.appendChild(entry);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }

    // WebAudio Synthesizer Sound Effects
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function playSynthSFX(type = 'attack') {
        try {
            if (!audioCtx) audioCtx = new AudioCtx();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            const now = audioCtx.currentTime;

            if (type === 'attack') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(600, now);
                osc.frequency.exponentialRampToValueAtTime(150, now + 0.15);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
                osc.start(now); osc.stop(now + 0.15);
            } else if (type === 'equip') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, now);
                osc.frequency.exponentialRampToValueAtTime(880, now + 0.12);
                gain.gain.setValueAtTime(0.25, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
                osc.start(now); osc.stop(now + 0.12);
            } else if (type === 'potion') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.linearRampToValueAtTime(600, now + 0.25);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                osc.start(now); osc.stop(now + 0.25);
            } else if (type === 'levelup') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(523.25, now);
                osc.frequency.setValueAtTime(659.25, now + 0.1);
                osc.frequency.setValueAtTime(783.99, now + 0.2);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
                osc.start(now); osc.stop(now + 0.35);
            }
        } catch (e) {}
    }

    // Engine Core State
    const engineState = {
        player: {
            x: 200, y: 150,
            vx: 0, vy: 0,
            speed: 4.5,
            radius: 16,
            level: 1,
            exp: 0, expNext: 100,
            hp: 100, maxHp: 100,
            mp: 50, maxMp: 50,
            baseAtk: 25, baseDef: 12
        },
        equipment: {
            Weapon: { name: 'Pink Cyber Blade', icon: '⚔️', atk: 15, def: 0 },
            Armor: null,
            Ring: null
        },
        inventory: [
            { id: 1, name: 'Pink Cyber Blade', icon: '⚔️', type: 'Weapon', atk: 15, def: 0 },
            { id: 2, name: 'Rose Shield', icon: '🛡️', type: 'Armor', atk: 0, def: 18 },
            { id: 3, name: 'Health Elixir', icon: '🧪', type: 'Potion', heal: 50 },
            { id: 4, name: 'Mana Crystal', icon: '💎', type: 'Potion', mana: 30 },
            { id: 5, name: 'Neon Power Ring', icon: '💍', type: 'Ring', atk: 10, def: 5 },
            { id: 6, name: 'Aether Wand', icon: '🪄', type: 'Weapon', atk: 22, def: 2 }
        ],
        enemies: [
            { id: 1, x: 500, y: 220, hp: 60, maxHp: 60, speed: 1.8, color: '#ec4899' },
            { id: 2, x: 650, y: 350, hp: 80, maxHp: 80, speed: 1.4, color: '#f43f5e' }
        ],
        particles: [],
        projectiles: [],
        dungeonRooms: [
            { x: 50, y: 40, w: 260, h: 200 },
            { x: 340, y: 120, w: 300, h: 250 },
            { x: 180, y: 280, w: 220, h: 180 }
        ],
        keys: { w: false, a: false, s: false, d: false },
        fps: 60,
        lastTime: performance.now()
    };

    // Keyboard Input Listeners
    window.addEventListener('keydown', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') engineState.keys.w = true;
        if (k === 'a' || k === 'arrowleft') engineState.keys.a = true;
        if (k === 's' || k === 'arrowdown') engineState.keys.s = true;
        if (k === 'd' || k === 'arrowright') engineState.keys.d = true;
        if (e.code === 'Space') {
            e.preventDefault();
            triggerAttack();
        }
    });

    window.addEventListener('keyup', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') engineState.keys.w = false;
        if (k === 'a' || k === 'arrowleft') engineState.keys.a = false;
        if (k === 's' || k === 'arrowdown') engineState.keys.s = false;
        if (k === 'd' || k === 'arrowright') engineState.keys.d = false;
    });

    // Particle Burst
    function spawnParticles(x, y, color = '#ff2a85', count = 15) {
        for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 4.5 + 1;
            engineState.particles.push({
                x, y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                radius: Math.random() * 5 + 2,
                life: 1.0,
                color
            });
        }
    }

    // Equipment & Stat Calculations
    function updateStatsUI() {
        const p = engineState.player;
        let bonusAtk = 0;
        let bonusDef = 0;

        Object.values(engineState.equipment).forEach(eq => {
            if (eq) {
                bonusAtk += eq.atk || 0;
                bonusDef += eq.def || 0;
            }
        });

        const totalAtk = p.baseAtk + bonusAtk;
        const totalDef = p.baseDef + bonusDef;

        document.getElementById('hp-val').textContent = `${Math.round(p.hp)} / ${p.maxHp}`;
        document.getElementById('hp-bar').style.width = `${(p.hp / p.maxHp) * 100}%`;
        
        document.getElementById('mp-val').textContent = `${Math.round(p.mp)} / ${p.maxMp}`;
        document.getElementById('mp-bar').style.width = `${(p.mp / p.maxMp) * 100}%`;
        
        document.getElementById('atk-def-val').textContent = `${totalAtk} ATK / ${totalDef} DEF`;
        document.getElementById('player-lvl').textContent = p.level;
        document.getElementById('exp-val').textContent = `${p.exp} / ${p.expNext}`;
        
        document.getElementById('entity-count').textContent = `${1 + engineState.enemies.length + engineState.particles.length} Entities`;
        document.getElementById('body-count').textContent = `${1 + engineState.enemies.length} Bodies`;

        // Update Equipment Slots UI
        ['Weapon', 'Armor', 'Ring'].forEach(slot => {
            const el = document.getElementById(`eq-${slot.toLowerCase()}`);
            const eq = engineState.equipment[slot];
            if (eq) {
                el.classList.add('active');
                el.querySelector('.eq-icon').textContent = eq.icon;
                el.querySelector('.eq-label').textContent = eq.name;
            } else {
                el.classList.remove('active');
                el.querySelector('.eq-icon').textContent = slot === 'Weapon' ? '⚔️' : (slot === 'Armor' ? '🛡️' : '💍');
                el.querySelector('.eq-label').textContent = slot;
            }
        });

        renderInventoryUI();
    }

    // Inventory UI Renderer
    function renderInventoryUI() {
        const container = document.getElementById('inventory-container');
        container.innerHTML = '';

        for (let i = 0; i < 8; i++) {
            const slot = document.createElement('div');
            const item = engineState.inventory[i];

            if (item) {
                slot.className = 'inv-slot';
                slot.textContent = item.icon;
                slot.title = `${item.name} (${item.type})`;
                slot.onclick = () => handleItemClick(item, i);
            } else {
                slot.className = 'inv-slot empty';
            }
            container.appendChild(slot);
        }
    }

    // Item Action (Equip / Consume)
    function handleItemClick(item, index) {
        if (item.type === 'Potion') {
            if (item.heal) {
                engineState.player.hp = Math.min(engineState.player.maxHp, engineState.player.hp + item.heal);
                log(`[POTION] Drank ${item.name}! Restored ${item.heal} HP.`, 'success');
            } else if (item.mana) {
                engineState.player.mp = Math.min(engineState.player.maxMp, engineState.player.mp + item.mana);
                log(`[POTION] Consumed ${item.name}! Restored ${item.mana} MP.`, 'info');
            }
            playSynthSFX('potion');
            engineState.inventory.splice(index, 1);
        } else if (['Weapon', 'Armor', 'Ring'].includes(item.type)) {
            const currentEq = engineState.equipment[item.type];
            engineState.equipment[item.type] = item;
            engineState.inventory.splice(index, 1);
            if (currentEq) {
                engineState.inventory.push(currentEq);
            }
            playSynthSFX('equip');
            spawnParticles(engineState.player.x, engineState.player.y, '#ff2a85', 12);
            log(`[EQUIP] Equipped ${item.name} into ${item.type} slot!`, 'pink');
        }
        updateStatsUI();
    }

    // Unequip Listener
    ['Weapon', 'Armor', 'Ring'].forEach(slot => {
        const el = document.getElementById(`eq-${slot.toLowerCase()}`);
        el.onclick = () => {
            const eq = engineState.equipment[slot];
            if (eq && engineState.inventory.length < 8) {
                engineState.inventory.push(eq);
                engineState.equipment[slot] = null;
                playSynthSFX('equip');
                log(`[UNEQUIP] Removed ${eq.name} back to inventory.`, 'info');
                updateStatsUI();
            }
        };
    });

    // Trigger Pink Slash Attack
    function triggerAttack() {
        const p = engineState.player;
        let target = null;
        let minDist = 9999;

        engineState.enemies.forEach(e => {
            const dist = Math.hypot(e.x - p.x, e.y - p.y);
            if (dist < minDist) {
                minDist = dist;
                target = e;
            }
        });

        const targetX = target ? target.x : p.x + 120;
        const targetY = target ? target.y : p.y;
        const angle = Math.atan2(targetY - p.y, targetX - p.x);

        engineState.projectiles.push({
            x: p.x, y: p.y,
            vx: Math.cos(angle) * 12,
            vy: Math.sin(angle) * 12,
            life: 1.0,
            color: '#ff2a85'
        });

        playSynthSFX('attack');
        spawnParticles(p.x, p.y, '#ff2a85', 8);

        if (target && minDist < 250) {
            target.hp -= 25;
            spawnParticles(target.x, target.y, '#ec4899', 16);
            log(`[COMBAT] Pink Energy Slash hit ${target.color === '#ec4899' ? 'Cyber Fiend' : 'Stalker'} for 25 DMG!`, 'pink');
            if (target.hp <= 0) {
                engineState.enemies = engineState.enemies.filter(e => e !== target);
                gainExp(45);
                log(`[VICTORY] Enemy defeated! Gained +45 EXP.`, 'success');
            }
        }
    }

    function gainExp(amount) {
        const p = engineState.player;
        p.exp += amount;
        if (p.exp >= p.expNext) {
            p.exp -= p.expNext;
            p.level += 1;
            p.expNext = Math.round(p.expNext * 1.5);
            p.maxHp += 25; p.hp = p.maxHp;
            p.maxMp += 15; p.mp = p.maxMp;
            p.baseAtk += 5;
            playSynthSFX('levelup');
            spawnParticles(p.x, p.y, '#fbbf24', 30);
            log(`[LEVEL UP] Reached Cyber Level ${p.level}! HP & MP fully restored.`, 'success');
        }
        updateStatsUI();
    }

    // Render Engine Loop
    function render(time) {
        const dt = (time - engineState.lastTime) / 1000;
        engineState.lastTime = time;
        engineState.fps = Math.round(1 / (dt || 0.016));
        document.getElementById('fps-counter').textContent = engineState.fps;

        // Player WASD Movement
        const p = engineState.player;
        if (engineState.keys.w) p.y -= p.speed;
        if (engineState.keys.s) p.y += p.speed;
        if (engineState.keys.a) p.x -= p.speed;
        if (engineState.keys.d) p.x += p.speed;

        p.x = Math.max(20, Math.min(canvas.width - 20, p.x));
        p.y = Math.max(20, Math.min(canvas.height - 20, p.y));

        // Clear Canvas
        ctx.fillStyle = '#090312';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 1. Pink Neon Grid
        ctx.strokeStyle = 'rgba(255, 42, 133, 0.1)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        // 2. Dungeon Rooms with Neon Pink Borders
        engineState.dungeonRooms.forEach(r => {
            ctx.fillStyle = 'rgba(23, 10, 40, 0.75)';
            ctx.strokeStyle = '#ff2a85';
            ctx.lineWidth = 2;
            ctx.shadowColor = '#ff2a85';
            ctx.shadowBlur = 10;
            ctx.fillRect(r.x, r.y, r.w, r.h);
            ctx.strokeRect(r.x, r.y, r.w, r.h);
            ctx.shadowBlur = 0;
        });

        // 3. Player Character Rendering (Neon Pink Glow Circle)
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = '#ff2a85';
        ctx.shadowColor = '#ff2a85';
        ctx.shadowBlur = 20;
        ctx.fill();
        ctx.shadowBlur = 0;

        // Player Core Eye
        ctx.beginPath();
        ctx.arc(p.x, p.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.fill();

        // 4. Enemy Movement & Rendering
        engineState.enemies.forEach(e => {
            const dx = p.x - e.x;
            const dy = p.y - e.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 30) {
                e.x += (dx / dist) * e.speed;
                e.y += (dy / dist) * e.speed;
            }

            // Path Line
            ctx.beginPath();
            ctx.moveTo(e.x, e.y); ctx.lineTo(p.x, p.y);
            ctx.strokeStyle = 'rgba(236, 72, 153, 0.3)';
            ctx.setLineDash([4, 4]); ctx.stroke(); ctx.setLineDash([]);

            // Enemy Body
            ctx.beginPath();
            ctx.arc(e.x, e.y, 14, 0, Math.PI * 2);
            ctx.fillStyle = e.color;
            ctx.shadowColor = e.color;
            ctx.shadowBlur = 12;
            ctx.fill();
            ctx.shadowBlur = 0;

            // Enemy HP Bar
            ctx.fillStyle = 'rgba(0,0,0,0.6)';
            ctx.fillRect(e.x - 16, e.y - 22, 32, 5);
            ctx.fillStyle = '#ff2a85';
            ctx.fillRect(e.x - 16, e.y - 22, (e.hp / e.maxHp) * 32, 5);
        });

        // 5. Projectiles
        for (let i = engineState.projectiles.length - 1; i >= 0; i--) {
            const pr = engineState.projectiles[i];
            pr.x += pr.vx; pr.y += pr.vy; pr.life -= 0.03;
            if (pr.life <= 0) {
                engineState.projectiles.splice(i, 1);
                continue;
            }
            ctx.beginPath();
            ctx.arc(pr.x, pr.y, 8, 0, Math.PI * 2);
            ctx.fillStyle = pr.color;
            ctx.shadowColor = pr.color;
            ctx.shadowBlur = 15;
            ctx.fill();
            ctx.shadowBlur = 0;
        }

        // 6. Particles
        for (let i = engineState.particles.length - 1; i >= 0; i--) {
            const part = engineState.particles[i];
            part.x += part.vx; part.y += part.vy; part.life -= 0.03;
            if (part.life <= 0) {
                engineState.particles.splice(i, 1);
                continue;
            }
            ctx.beginPath();
            ctx.arc(part.x, part.y, part.radius * part.life, 0, Math.PI * 2);
            ctx.fillStyle = part.color;
            ctx.globalAlpha = part.life;
            ctx.fill();
            ctx.globalAlpha = 1.0;
        }

        requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
    updateStatsUI();

    // Button Bindings
    document.getElementById('btn-attack').addEventListener('click', triggerAttack);

    document.getElementById('btn-regen').addEventListener('click', () => {
        engineState.dungeonRooms = [
            { x: Math.random() * 100 + 30, y: Math.random() * 100 + 30, w: 220, h: 180 },
            { x: Math.random() * 200 + 250, y: Math.random() * 150 + 100, w: 260, h: 200 }
        ];
        spawnParticles(canvas.width / 2, canvas.height / 2, '#ff2a85', 30);
        log('[WORLD] Regenerated Cyber-Pink Dungeon Level Architecture', 'pink');
    });

    document.getElementById('btn-spawn').addEventListener('click', () => {
        const ex = Math.random() * (canvas.width - 150) + 75;
        const ey = Math.random() * (canvas.height - 150) + 75;
        engineState.enemies.push({
            id: Date.now(), x: ex, y: ey, hp: 70, maxHp: 70, speed: 1.6, color: '#f43f5e'
        });
        spawnParticles(ex, ey, '#f43f5e', 20);
        log(`[ECS] Spawned Cyber Enemy at (${Math.round(ex)}, ${Math.round(ey)})`, 'warn');
        updateStatsUI();
    });

    document.getElementById('btn-loot').addEventListener('click', () => {
        if (engineState.inventory.length < 8) {
            const loots = [
                { id: Date.now(), name: 'Pink Rose Blade', icon: '⚔️', type: 'Weapon', atk: 28, def: 4 },
                { id: Date.now(), name: 'Cyber Amulet', icon: '📿', type: 'Ring', atk: 8, def: 12 },
                { id: Date.now(), name: 'Health Elixir', icon: '🧪', type: 'Potion', heal: 50 },
                { id: Date.now(), name: 'Neon Chestplate', icon: '🛡️', type: 'Armor', atk: 2, def: 24 }
            ];
            const item = loots[Math.floor(Math.random() * loots.length)];
            engineState.inventory.push(item);
            spawnParticles(engineState.player.x, engineState.player.y, '#fbbf24', 15);
            log(`[LOOT] Found rare artifact: ${item.name}!`, 'success');
            updateStatsUI();
        } else {
            log('[LOOT] Inventory bag is full!', 'warn');
        }
    });
});
