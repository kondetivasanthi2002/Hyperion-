// Hyperion RPG Game Logic - Action RPG Engine, Wave Combat, Skills, Shop & Minimap

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('game-canvas');
    const ctx = canvas.getContext('2d');
    const miniCanvas = document.getElementById('minimap-canvas');
    const miniCtx = miniCanvas ? miniCanvas.getContext('2d') : null;
    const consoleOutput = document.getElementById('console-output');

    function resizeCanvas() {
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Console Logger
    function log(msg, type = 'info') {
        const entry = document.createElement('div');
        entry.className = `log-entry log-${type}`;
        entry.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
        consoleOutput.appendChild(entry);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }

    // WebAudio Synthesizer Sound Engine & BGM
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;
    let bgmInterval = null;
    let bgmPlaying = false;

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
                gain.gain.setValueAtTime(0.25, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
                osc.start(now); osc.stop(now + 0.15);
            } else if (type === 'nova') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(150, now);
                osc.frequency.exponentialRampToValueAtTime(800, now + 0.3);
                gain.gain.setValueAtTime(0.35, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
                osc.start(now); osc.stop(now + 0.3);
            } else if (type === 'dash') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(400, now);
                osc.frequency.linearRampToValueAtTime(100, now + 0.15);
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
                osc.start(now); osc.stop(now + 0.15);
            } else if (type === 'heal') {
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, now);
                osc.frequency.exponentialRampToValueAtTime(880, now + 0.25);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                osc.start(now); osc.stop(now + 0.25);
            } else if (type === 'levelup') {
                osc.type = 'square';
                osc.frequency.setValueAtTime(523, now);
                osc.frequency.setValueAtTime(659, now + 0.1);
                osc.frequency.setValueAtTime(783, now + 0.2);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
                osc.start(now); osc.stop(now + 0.35);
            }
        } catch (e) {}
    }

    function toggleBGM() {
        if (bgmPlaying) {
            clearInterval(bgmInterval);
            bgmPlaying = false;
            log('[AUDIO] Synthwave Background Music Stopped.', 'info');
        } else {
            bgmPlaying = true;
            let noteIdx = 0;
            const notes = [220, 261.63, 293.66, 329.63, 392, 440];
            bgmInterval = setInterval(() => {
                try {
                    if (!audioCtx) audioCtx = new AudioCtx();
                    const osc = audioCtx.createOscillator();
                    const gain = audioCtx.createGain();
                    osc.connect(gain);
                    gain.connect(audioCtx.destination);
                    osc.type = 'sine';
                    osc.frequency.value = notes[noteIdx % notes.length];
                    gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.18);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.18);
                    noteIdx++;
                } catch(e) {}
            }, 220);
            log('[AUDIO] Started Synthwave BGM Loop 🎵', 'pink');
        }
    }

    // Engine Core State
    const game = {
        wave: 1,
        coins: 120,
        player: {
            x: 200, y: 180,
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
            { id: 2, name: 'Rose Aegis Shield', icon: '🛡️', type: 'Armor', atk: 0, def: 18 },
            { id: 3, name: 'Health Elixir', icon: '🧪', type: 'Potion', heal: 50 },
            { id: 4, name: 'Mana Crystal', icon: '💎', type: 'Potion', mana: 30 },
            { id: 5, name: 'Neon Power Ring', icon: '💍', type: 'Ring', atk: 10, def: 5 }
        ],
        enemies: [],
        particles: [],
        projectiles: [],
        popups: [],
        dungeonRooms: [
            { x: 40, y: 40, w: 260, h: 200 },
            { x: 340, y: 120, w: 300, h: 250 },
            { x: 180, y: 280, w: 220, h: 180 }
        ],
        keys: { w: false, a: false, s: false, d: false },
        fps: 60,
        lastTime: performance.now()
    };

    // Keyboard Listeners
    window.addEventListener('keydown', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') game.keys.w = true;
        if (k === 'a' || k === 'arrowleft') game.keys.a = true;
        if (k === 's' || k === 'arrowdown') game.keys.s = true;
        if (k === 'd' || k === 'arrowright') game.keys.d = true;
        if (e.code === 'Space') { e.preventDefault(); triggerAttack(); }
        if (k === '1') useSkillNova();
        if (k === '2') useSkillDash();
        if (k === '3') useSkillHeal();
    });

    window.addEventListener('keyup', (e) => {
        const k = e.key.toLowerCase();
        if (k === 'w' || k === 'arrowup') game.keys.w = false;
        if (k === 'a' || k === 'arrowleft') game.keys.a = false;
        if (k === 's' || k === 'arrowdown') game.keys.s = false;
        if (k === 'd' || k === 'arrowright') game.keys.d = false;
    });

    // Particle Emissions
    function spawnParticles(x, y, color = '#ff2a85', count = 15) {
        for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 4.5 + 1;
            game.particles.push({
                x, y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                radius: Math.random() * 5 + 2,
                life: 1.0,
                color
            });
        }
    }

    // Floating Text Popups
    function addPopup(text, x, y, color = '#ff2a85') {
        game.popups.push({ text, x, y, vy: -1.2, life: 1.0, color });
    }

    // Spawn Enemy Wave
    function spawnWave(waveNum) {
        game.enemies = [];
        const isBossWave = waveNum % 5 === 0;
        const count = isBossWave ? 1 : waveNum * 2 + 2;

        if (isBossWave) {
            game.enemies.push({
                id: Date.now(), x: 500, y: 250, hp: 400 + waveNum * 100, maxHp: 400 + waveNum * 100,
                speed: 1.2, color: '#ec4899', isBoss: true, name: 'DARK MECHA BOSS'
            });
            log(`[BOSS WAVE ${waveNum}] Dark Mecha Boss Has Awakened!`, 'warn');
        } else {
            for (let i = 0; i < count; i++) {
                const ex = Math.random() * (canvas.width - 200) + 100;
                const ey = Math.random() * (canvas.height - 200) + 100;
                game.enemies.push({
                    id: Date.now() + i, x: ex, y: ey,
                    hp: 50 + waveNum * 15, maxHp: 50 + waveNum * 15,
                    speed: 1.5 + Math.random() * 0.5,
                    color: i % 2 === 0 ? '#ec4899' : '#f43f5e',
                    isBoss: false
                });
            }
            log(`[WAVE ${waveNum}] Spawned ${count} Cyber Fiends! Defeat all to advance.`, 'pink');
        }
        updateStatsUI();
    }

    // Stats & UI Updates
    function updateStatsUI() {
        const p = game.player;
        let bonusAtk = 0, bonusDef = 0;

        Object.values(game.equipment).forEach(eq => {
            if (eq) { bonusAtk += eq.atk || 0; bonusDef += eq.def || 0; }
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
        document.getElementById('wave-val').textContent = game.wave;
        document.getElementById('coin-val').textContent = game.coins;
        document.getElementById('enemy-count').textContent = `${game.enemies.length} Alive`;

        // Update Equipment Slots UI
        ['Weapon', 'Armor', 'Ring'].forEach(slot => {
            const el = document.getElementById(`eq-${slot.toLowerCase()}`);
            const eq = game.equipment[slot];
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

    // Render Inventory
    function renderInventoryUI() {
        const container = document.getElementById('inventory-container');
        container.innerHTML = '';
        for (let i = 0; i < 8; i++) {
            const slot = document.createElement('div');
            const item = game.inventory[i];
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

    // Handle Item Usage
    function handleItemClick(item, index) {
        if (item.type === 'Potion') {
            if (item.heal) {
                game.player.hp = Math.min(game.player.maxHp, game.player.hp + item.heal);
                log(`[POTION] Used ${item.name}! Restored +${item.heal} HP.`, 'success');
            } else if (item.mana) {
                game.player.mp = Math.min(game.player.maxMp, game.player.mp + item.mana);
                log(`[POTION] Used ${item.name}! Restored +${item.mana} MP.`, 'info');
            }
            playSynthSFX('heal');
            game.inventory.splice(index, 1);
        } else if (['Weapon', 'Armor', 'Ring'].includes(item.type)) {
            const currentEq = game.equipment[item.type];
            game.equipment[item.type] = item;
            game.inventory.splice(index, 1);
            if (currentEq) game.inventory.push(currentEq);
            playSynthSFX('heal');
            spawnParticles(game.player.x, game.player.y, '#ff2a85', 12);
            log(`[EQUIP] Equipped ${item.name} into ${item.type} slot!`, 'pink');
        }
        updateStatsUI();
    }

    // Unequip Listeners
    ['Weapon', 'Armor', 'Ring'].forEach(slot => {
        const el = document.getElementById(`eq-${slot.toLowerCase()}`);
        el.onclick = () => {
            const eq = game.equipment[slot];
            if (eq && game.inventory.length < 8) {
                game.inventory.push(eq);
                game.equipment[slot] = null;
                playSynthSFX('heal');
                log(`[UNEQUIP] Returned ${eq.name} to inventory.`, 'info');
                updateStatsUI();
            }
        };
    });

    // Skill 1: Pink Nova Shockwave
    function useSkillNova() {
        const p = game.player;
        if (p.mp >= 15) {
            p.mp -= 15;
            spawnParticles(p.x, p.y, '#ff2a85', 40);
            playSynthSFX('nova');
            let hits = 0;
            game.enemies.forEach(e => {
                const dist = Math.hypot(e.x - p.x, e.y - p.y);
                if (dist < 180) {
                    e.hp -= 45;
                    addPopup('-45 NOVA!', e.x, e.y - 15, '#ff2a85');
                    hits++;
                }
            });
            log(`[SKILL] Pink Nova Shockwave executed! Hit ${hits} enemies.`, 'pink');
            checkEnemyDeaths();
            updateStatsUI();
        } else {
            log('[SKILL] Not enough MP for Nova!', 'warn');
        }
    }

    // Skill 2: Cyber Dash
    function useSkillDash() {
        const p = game.player;
        p.x += (game.keys.d ? 120 : (game.keys.a ? -120 : 0));
        p.y += (game.keys.s ? 120 : (game.keys.w ? -120 : 0));
        spawnParticles(p.x, p.y, '#22d3ee', 20);
        playSynthSFX('dash');
        log('[SKILL] Executed Cyber Dash!', 'info');
    }

    // Skill 3: Heal Surge
    function useSkillHeal() {
        const p = game.player;
        if (p.mp >= 20) {
            p.mp -= 20;
            p.hp = Math.min(p.maxHp, p.hp + 40);
            spawnParticles(p.x, p.y, '#10b981', 25);
            addPopup('+40 HP', p.x, p.y - 20, '#10b981');
            playSynthSFX('heal');
            log('[SKILL] Healed +40 HP using Mana Surge.', 'success');
            updateStatsUI();
        } else {
            log('[SKILL] Not enough MP to Heal!', 'warn');
        }
    }

    // Basic Attack
    function triggerAttack() {
        const p = game.player;
        let target = null; let minDist = 9999;
        game.enemies.forEach(e => {
            const dist = Math.hypot(e.x - p.x, e.y - p.y);
            if (dist < minDist) { minDist = dist; target = e; }
        });

        const targetX = target ? target.x : p.x + 120;
        const targetY = target ? target.y : p.y;
        const angle = Math.atan2(targetY - p.y, targetX - p.x);

        game.projectiles.push({
            x: p.x, y: p.y,
            vx: Math.cos(angle) * 12, vy: Math.sin(angle) * 12,
            life: 1.0, color: '#ff2a85'
        });

        playSynthSFX('attack');
        spawnParticles(p.x, p.y, '#ff2a85', 6);

        if (target && minDist < 250) {
            let bonusAtk = 0;
            Object.values(game.equipment).forEach(eq => { if (eq) bonusAtk += eq.atk || 0; });
            const totalDmg = p.baseAtk + bonusAtk;
            
            target.hp -= totalDmg;
            addPopup(`-${totalDmg}`, target.x, target.y - 15, '#ff2a85');
            spawnParticles(target.x, target.y, '#ec4899', 12);
            checkEnemyDeaths();
        }
    }

    function checkEnemyDeaths() {
        game.enemies.forEach(e => {
            if (e.hp <= 0) {
                const coinEarned = e.isBoss ? 150 : 25;
                game.coins += coinEarned;
                addPopup(`+${coinEarned} COINS!`, e.x, e.y - 30, '#fbbf24');
                gainExp(e.isBoss ? 150 : 35);
                log(`[VICTORY] Defeated enemy! Earned +${coinEarned} Coins.`, 'gold');
            }
        });
        game.enemies = game.enemies.filter(e => e.hp > 0);
        if (game.enemies.length === 0) {
            log(`[WAVE CLEARED] Wave ${game.wave} completed! Click 'Next Wave' to proceed.`, 'success');
        }
        updateStatsUI();
    }

    function gainExp(amount) {
        const p = game.player;
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
            log(`[LEVEL UP] Advanced to Cyber Level ${p.level}! stats boosted.`, 'success');
        }
        updateStatsUI();
    }

    // Main Engine Render Loop
    function render(time) {
        const dt = (time - game.lastTime) / 1000;
        game.lastTime = time;
        game.fps = Math.round(1 / (dt || 0.016));
        document.getElementById('fps-counter').textContent = game.fps;

        // Player WASD Movement
        const p = game.player;
        if (game.keys.w) p.y -= p.speed;
        if (game.keys.s) p.y += p.speed;
        if (game.keys.a) p.x -= p.speed;
        if (game.keys.d) p.x += p.speed;
        p.x = Math.max(20, Math.min(canvas.width - 20, p.x));
        p.y = Math.max(20, Math.min(canvas.height - 20, p.y));

        // Clear Canvas
        ctx.fillStyle = '#080310';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 1. Neon Grid & Dungeon Rooms
        ctx.strokeStyle = 'rgba(255, 42, 133, 0.08)';
        ctx.lineWidth = 1;
        for (let x = 0; x < canvas.width; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        game.dungeonRooms.forEach(r => {
            ctx.fillStyle = 'rgba(21, 9, 38, 0.75)';
            ctx.strokeStyle = '#ff2a85';
            ctx.lineWidth = 2;
            ctx.shadowColor = '#ff2a85'; ctx.shadowBlur = 8;
            ctx.fillRect(r.x, r.y, r.w, r.h);
            ctx.strokeRect(r.x, r.y, r.w, r.h);
            ctx.shadowBlur = 0;
        });

        // 2. Render Player
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = '#ff2a85';
        ctx.shadowColor = '#ff2a85'; ctx.shadowBlur = 20;
        ctx.fill(); ctx.shadowBlur = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff'; ctx.fill();

        // 3. Render Enemies & Boss
        game.enemies.forEach(e => {
            const dx = p.x - e.x; const dy = p.y - e.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 30) { e.x += (dx / dist) * e.speed; e.y += (dy / dist) * e.speed; }

            // Path Line
            ctx.beginPath();
            ctx.moveTo(e.x, e.y); ctx.lineTo(p.x, p.y);
            ctx.strokeStyle = e.isBoss ? 'rgba(251, 191, 36, 0.5)' : 'rgba(236, 72, 153, 0.3)';
            ctx.setLineDash([4, 4]); ctx.stroke(); ctx.setLineDash([]);

            // Enemy Shape
            const radius = e.isBoss ? 28 : 14;
            ctx.beginPath();
            ctx.arc(e.x, e.y, radius, 0, Math.PI * 2);
            ctx.fillStyle = e.isBoss ? '#fbbf24' : e.color;
            ctx.shadowColor = e.isBoss ? '#fbbf24' : e.color; ctx.shadowBlur = 15;
            ctx.fill(); ctx.shadowBlur = 0;

            // HP Bar
            ctx.fillStyle = 'rgba(0,0,0,0.7)';
            ctx.fillRect(e.x - 20, e.y - radius - 10, 40, 6);
            ctx.fillStyle = '#ff2a85';
            ctx.fillRect(e.x - 20, e.y - radius - 10, (e.hp / e.maxHp) * 40, 6);
        });

        // 4. Projectiles
        for (let i = game.projectiles.length - 1; i >= 0; i--) {
            const pr = game.projectiles[i];
            pr.x += pr.vx; pr.y += pr.vy; pr.life -= 0.03;
            if (pr.life <= 0) { game.projectiles.splice(i, 1); continue; }
            ctx.beginPath();
            ctx.arc(pr.x, pr.y, 8, 0, Math.PI * 2);
            ctx.fillStyle = pr.color; ctx.shadowColor = pr.color; ctx.shadowBlur = 12;
            ctx.fill(); ctx.shadowBlur = 0;
        }

        // 5. Particles
        for (let i = game.particles.length - 1; i >= 0; i--) {
            const part = game.particles[i];
            part.x += part.vx; part.y += part.vy; part.life -= 0.03;
            if (part.life <= 0) { game.particles.splice(i, 1); continue; }
            ctx.beginPath();
            ctx.arc(part.x, part.y, part.radius * part.life, 0, Math.PI * 2);
            ctx.fillStyle = part.color; ctx.globalAlpha = part.life;
            ctx.fill(); ctx.globalAlpha = 1.0;
        }

        // 6. Floating Text Popups
        for (let i = game.popups.length - 1; i >= 0; i--) {
            const pop = game.popups[i];
            pop.y += pop.vy; pop.life -= 0.02;
            if (pop.life <= 0) { game.popups.splice(i, 1); continue; }
            ctx.font = 'bold 13px "JetBrains Mono"';
            ctx.fillStyle = pop.color; ctx.globalAlpha = pop.life;
            ctx.fillText(pop.text, pop.x - 15, pop.y);
            ctx.globalAlpha = 1.0;
        }

        // Render Minimap Radar
        renderMinimap();

        requestAnimationFrame(render);
    }

    function renderMinimap() {
        if (!miniCtx) return;
        miniCtx.fillStyle = '#040108';
        miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);

        const scaleX = miniCanvas.width / canvas.width;
        const scaleY = miniCanvas.height / canvas.height;

        // Player Dot
        miniCtx.fillStyle = '#ff2a85';
        miniCtx.beginPath();
        miniCtx.arc(game.player.x * scaleX, game.player.y * scaleY, 3, 0, Math.PI * 2);
        miniCtx.fill();

        // Enemy Dots
        miniCtx.fillStyle = '#f43f5e';
        game.enemies.forEach(e => {
            miniCtx.beginPath();
            miniCtx.arc(e.x * scaleX, e.y * scaleY, e.isBoss ? 4 : 2, 0, Math.PI * 2);
            miniCtx.fill();
        });
    }

    spawnWave(1);
    requestAnimationFrame(render);

    // Button Event Handlers
    document.getElementById('skill-1').onclick = useSkillNova;
    document.getElementById('skill-2').onclick = useSkillDash;
    document.getElementById('skill-3').onclick = useSkillHeal;
    document.getElementById('btn-audio').onclick = toggleBGM;

    document.getElementById('btn-next-wave').onclick = () => {
        game.wave++;
        spawnWave(game.wave);
    };

    document.getElementById('btn-shop').onclick = () => {
        if (game.coins >= 50 && game.inventory.length < 8) {
            game.coins -= 50;
            const items = [
                { id: Date.now(), name: 'Mythic Cyber Sword', icon: '⚔️', type: 'Weapon', atk: 35, def: 5 },
                { id: Date.now(), name: 'Aegis Dragon Plate', icon: '🛡️', type: 'Armor', atk: 0, def: 30 },
                { id: Date.now(), name: 'Grand Elixir', icon: '🧪', type: 'Potion', heal: 100 }
            ];
            const bought = items[Math.floor(Math.random() * items.length)];
            game.inventory.push(bought);
            log(`[MERCHANT] Purchased ${bought.name} for 50 Coins!`, 'gold');
            playSynthSFX('levelup');
            updateStatsUI();
        } else if (game.coins < 50) {
            log('[MERCHANT] Need at least 50 Coins to buy shop items!', 'warn');
        }
    };
});
